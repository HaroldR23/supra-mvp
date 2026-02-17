#!/usr/bin/env bash
set -e

echo "🚀 Starting full stack application"

########################################
# 🐘 Start DB + Backend
########################################
echo "🐘 Starting PostgreSQL and API..."
cd backend
docker compose up -d --build
cd ..

########################################
# ⏳ Wait for API to be ready
########################################
echo "⏳ Waiting for API..."

until curl -s http://localhost:8000 > /dev/null; do
  sleep 1
done

echo "✅ API ready!"


########################################
# 🎨 Start Frontend
########################################
echo "🎨 Starting frontend..."
cd frontend

# clean stale lock
rm -f .next/dev/lock

# install deps if missing
if [ ! -d "node_modules" ]; then
  npm install
fi

# kill stuck next instances
pkill -f "next dev" 2>/dev/null || true

npm run dev &
FRONTEND_PID=$!

cd ..

########################################
# 📜 Backend logs (background)
########################################
echo "📜 Streaming backend logs..."
cd backend
docker compose logs -f api &
LOGS_PID=$!
cd ..

########################################
# 🛑 Graceful shutdown
########################################
cleanup() {
  echo ""
  echo "🛑 Shutting down services..."

  kill $FRONTEND_PID 2>/dev/null || true
  kill $LOGS_PID 2>/dev/null || true

  cd backend
  docker compose down
  cd ..

  echo "✅ Shutdown complete"
}

trap cleanup EXIT INT TERM

########################################
# 🚀 Status
########################################
echo ""
echo "✅ Application running!"
echo "➡ Frontend: http://localhost:3000"
echo "➡ Backend : http://localhost:8000"
echo ""
echo "Press CTRL+C to stop"
echo ""

wait
