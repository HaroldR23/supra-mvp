# Workshop Management - Frontend

Interfaz de usuario para el sistema de gestión de órdenes de taller. Desarrollado con Next.js (App Router), React, TypeScript y TailwindCSS.

## Requisitos

- Node.js 18+

## Instalación

### 1. Instalar dependencias

```bash
npm install
```

### 2. Configurar variables de entorno

```bash
cp .env.example .env.local
# Editar .env.local:
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3. Iniciar en desarrollo

```bash
npm run dev
```

Aplicación disponible en: http://localhost:3000

## Docker

```bash
docker build -t workshop-frontend .
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=http://backend:8000 workshop-frontend
```

## Estructura

```
frontend/src/
├── app/           # Páginas (App Router)
├── components/    # Componentes UI y layout
├── features/      # Módulos por funcionalidad
├── services/      # Servicios API
├── hooks/         # Hooks personalizados
└── types/         # Tipos TypeScript
```

## Funcionalidades

- **Dashboard**: Lista de órdenes con filtros por estado y fecha
- **Crear orden**: Formulario de alta con validación de garantía/costo
- **Detalle/Edición**: Actualizar estado, diagnóstico y costo estimado
- **Autenticación**: Login JWT
- **Roles**: Admin (acceso total), Técnico (órdenes únicamente)

Todo el contenido de la interfaz está en español.
