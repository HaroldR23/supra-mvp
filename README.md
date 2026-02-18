# Supra - MVP

## ⚙️ Requisitos
- Docker
- Poetry
- Node.js 18+

## 🛠️ Configuración de Variables de Entorno (Requerido)

Antes de ejecutar el script de inicio, debes configurar las variables de entorno requeridas.
 
### 🔹 Variables de Entorno del Backend

Crea un archivo llamado .env dentro del directorio backend:
```bash
backend/.env
```

Agrega los siguientes valores:
```bash
POSTGRES_USER=<user_postgres>
POSTGRES_PASSWORD=<password_postgress>
POSTGRES_DB=<nombre_db>
```

Explicación de variables:
- `POSTGRES_USER`: Usuario para la base de datos PostgreSQL
- `POSTGRES_PASSWORD`: Contraseña del usuario PostgreSQL
- `POSTGRES_DB`: Nombre de la base de datos a crear
- `SECRET_KEY`: Clave secreta para firmar y verificar tokens JWT en la aplicación

Notas:
- Las variables `POSTGRES_*` se utilizan automáticamente por la imagen de PostgreSQL en el contenedor
- Estos valores se leen desde el archivo `.env` cuando se ejecuta `docker-compose`

## 🔹 Variables de Entorno del Frontend

Crea un archivo llamado .env dentro del directorio frontend:
```bash
frontend/.env
```

Agrega el siguiente valor:
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Importante:

El prefijo NEXT_PUBLIC_ es requerido para que la variable esté expuesta al navegador en Next.js

## 🐘 Configuración de la Base de Datos

PostgreSQL se aprovisiona automáticamente usando Docker.

La base de datos se crea automáticamente cuando se inicia el contenedor

Las migraciones de Alembic se ejecutan automáticamente durante el inicio de la aplicación

No se requiere configuración manual de la base de datos

## 🚀 Inicia todo con:

```bash
./run.sh
```

## 📝 Usuarios Disponibles (Seed Script)

Los siguientes usuarios se crean automáticamente cuando se inicia la aplicación:

- **Admin User**: `admin@workshop.local` / `admin123`
- **Technician User**: `tech@workshop.local` / `tech123`

Puedes usar estas credenciales para acceder a la aplicación en http://localhost:3000

## 🌐 URLs de la Aplicación:

Frontend	http://localhost:3000

Backend API	http://localhost:8000

PostgreSQL	localhost:5432
