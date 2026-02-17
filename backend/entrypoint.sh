#!/usr/bin/env bash
set -e

echo "⏳ Waiting for database..."

until pg_isready -h db -p 5432 -U "$POSTGRES_USER"; do
  sleep 1
done

echo "✅ Database ready"

echo "🚀 Running migrations..."
alembic upgrade head

echo "🔥 Starting API..."

exec "$@"
