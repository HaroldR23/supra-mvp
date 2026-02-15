# Workshop Management - Backend

API REST para el sistema de gestión de órdenes de taller. Desarrollado con FastAPI, SQLAlchemy y arquitectura hexagonal.

## Requisitos

- Python 3.11+
- PostgreSQL 14+

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o: venv\Scripts\activate  # Windows
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con sus valores:
# DATABASE_URL=postgresql://user:pass@localhost:5432/workshop
# SECRET_KEY=su-clave-secreta-para-jwt
```

### 4. Ejecutar migraciones

```bash
alembic upgrade head
```

### 5. Crear usuario admin inicial (opcional)

```bash
python scripts/seed_admin.py
```

Credenciales por defecto: `admin@workshop.local` / `admin123`

### 6. Iniciar servidor

```bash
uvicorn main:app --reload
```

API disponible en: http://localhost:8000

Documentación Swagger: http://localhost:8000/docs

## Docker

```bash
docker-compose up -d
```

Esto inicia PostgreSQL y la API. Las migraciones deben ejecutarse manualmente la primera vez:

```bash
docker-compose exec api alembic upgrade head
docker-compose exec api python scripts/seed_admin.py
```

## Estructura

```
backend/
├── api/           # Rutas y dependencias
├── domain/        # Modelos de dominio y puertos
├── use_cases/     # Casos de uso
├── adapters/      # Adaptadores (DB, etc.)
├── schemas/       # Esquemas Pydantic
└── alembic/       # Migraciones
```

## Endpoints

| Método | Ruta | Descripción | Roles |
|--------|------|-------------|-------|
| POST | /api/v1/auth/login | Iniciar sesión | Público |
| GET | /api/v1/auth/me | Usuario actual | Autenticado |
| GET | /api/v1/orders | Listar órdenes (filtros) | Admin, Técnico |
| POST | /api/v1/orders | Crear orden | Admin, Técnico |
| GET | /api/v1/orders/{id} | Obtener orden | Admin, Técnico |
| PATCH | /api/v1/orders/{id} | Actualizar orden | Admin, Técnico |
| GET | /api/v1/users | Listar usuarios | Solo Admin |
| POST | /api/v1/users | Crear usuario | Solo Admin |
