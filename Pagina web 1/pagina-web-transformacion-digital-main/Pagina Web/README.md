# Perfil Académico

Sitio web tipo perfil profesional con estilo académico, listo para ejecutarse con Docker.

## Requisitos

- Docker
- Docker Compose

## Ejecutar

Desde la carpeta del proyecto:

```bash
docker compose up --build
```

Después abre en tu navegador:

```text
http://localhost:8000
```

## Archivos editables

- Datos del perfil: `app/data/perfil.json`
- Diseño visual: `app/static/css/estilos.css`
- Texto y estructura: `app/templates/perfil.html`
- Foto de perfil: `app/static/img/perfil-placeholder.svg`
- Videos locales: `app/static/videos/`
- PDFs: `app/static/documentos/`

## Observaciones

- Los videos y documentos se montan como volúmenes para que puedas añadir o cambiar archivos sin reconstruir la imagen.
- Si quieres cambiar tu información personal, edita `app/data/perfil.json`.
