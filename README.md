# LUCASMAN - Gestor de Archivos y Sistema

Un programa simple escrito en Python para gestionar archivos y ejecutar comandos del sistema en Kali Linux.

## Características

- **Pantalla de carga**: Animación cool al iniciar.
- **Logo personalizado**: Muestra "LUCASMAN" en arte ASCII.
- **Terminal dedicada**: Se abre en una nueva terminal llamada "LUCASMAN terminal".
- **Gestión de archivos**: Comandos como `ls`, `cd`, `pwd`.
- **Comandos del sistema**: Ejecuta cualquier comando, incluyendo `shutdown`.
- **Cierre automático**: Al salir con `exit`, la terminal se cierra.

## Cómo Ejecutar

1. Asegúrate de tener Python 3 y gnome-terminal instalado.
2. Ejecuta el programa: `python3 main.py`
3. Esto abrirá automáticamente una nueva terminal con el programa ejecutándose.
4. Al hacer `exit`, la terminal se cerrará automáticamente.

## Comandos Especiales

- `cd <directorio>`: Cambiar directorio.
- `pwd`: Mostrar directorio actual.
- `shutdown`: Apagar el sistema (requiere permisos de sudo).
- `exit`: Salir del programa y cerrar la terminal.

## Requisitos

- Python 3
- Kali Linux con entorno gráfico (XFCE/GNOME)
- gnome-terminal
- Permisos de sudo para comandos administrativos

## Ejemplos de Uso

En la terminal LUCASMAN:

```
LUCASMAN> ls
LUCASMAN> cd /home
LUCASMAN> pwd
LUCASMAN> shutdown
LUCASMAN> exit
```

¡Disfruta gestionando tu sistema con LUCASMAN!