# 🔄 Sistema de Auto-Update Automático

## ¿Qué se ha añadido?

El `index.html` ahora incluye:

1. **APP_VERSION**: Un identificador que cambia automáticamente cuando hay cambios reales en los datos
2. **Service Worker**: Evita que el navegador cachee el HTML indefinidamente
3. **Verificación automática**: Cada 30 segundos, la app descarga el archivo y comprueba si hay una versión más nueva
4. Si hay versión más nueva → **La página se recarga automáticamente** sin intervención del usuario

## ¿Cómo funciona?

### En los navegadores de tus amigos:
- La app está constantemente "escuchando" si hay cambios
- Cuando subes una nueva versión a GitHub Pages, dentro de máximo 30 segundos todos los usuarios verán la actualización
- **Automático, sin que tengan que hacer nada**

### Tu flujo de trabajo:

**Opción 1: Manual (cada vez que actualices)**
```bash
python3 update_version.py index.html
# Sube el archivo a GitHub
```

**Opción 2: Automático (recomendado)**
Simplemente:
1. Guarda los cambios en el HTML
2. Sube a GitHub
3. ✅ El sistema detecta automáticamente que hay cambios

## Detalles técnicos

- **APP_VERSION**: Es un hash MD5 del contenido de DATA. Cada vez que DATA cambia (nuevos partidos, puntos actualizados), el hash cambia
- **Service Worker**: Fuerza el navegador a descargar siempre la última versión del HTML (no caché)
- **Intervalo de verificación**: 30 segundos (puedes cambiar a `60000` ms para 1 minuto si prefieres menos tráfico)

## Si algo no se actualiza

Pide a tus amigos que:
1. Cierren la app completamente (cerrar pestaña/app)
2. Esperen 30 segundos
3. Abran la URL de nuevo

O si es urgente: Ctrl+Shift+R (borrar caché + recargar)

## Archivo auxiliar

`update_version.py` - Script Python que regenera el APP_VERSION. Úsalo si quieres forzar una actualización manual antes de subir a GitHub.
