# LUCASMAN - Gestor de Archivos y Sistema

Un programa simple escrito en Python para gestionar archivos y ejecutar comandos del sistema en Kali Linux.

## Características

- **Pantalla de carga**: Animación cool al iniciar.
- **Logo personalizado**: Muestra "LUCASMAN" en arte ASCII.
- **Instalación automática de dependencias**: Al iniciar, instala xterm y apache2 automáticamente.
- **Gestión de archivos**: Comandos como `ls`, `cd`, `pwd`.
- **Comandos del sistema**: Ejecuta cualquier comando.
- **Servidor Apache**: Inicia/detiene Apache2 con un solo comando.
- **Información de red**: Ver IP, interfaces de red y conexiones.
- **Gestión de ventanas**: Abre y cierra ventanas de terminal.

## Comandos Personalizados

### 📁 Archivos y Directorios
- `ls`: Listar archivos.
- `cd <directorio>`: Cambiar directorio.
- `pwd`: Mostrar directorio actual.
- `clear`: Limpiar pantalla.

### 🔧 Sistema
- `shutdown`: Apagar el sistema (requiere sudo).
- `windows`: Abrir nueva ventana de terminal xterm.
- `closew`: Cerrar todas las ventanas xterm.

### 🌐 Red e IP
- `myip`: Ver tu IP local.
- `netinfo`: Ver información completa de red e interfaces.
- `netstat`: Ver conexiones de red activas.

### 🌐 Servidor Web (Apache)
- `apache`: Iniciar servidor Apache2 en http://localhost.
- `apache stop`: Detener servidor Apache2.

### ℹ️ Ayuda
- `help`: Mostrar help completo con todos los comandos.
- `exit`: Salir del programa.

### 💡 Comandos del Sistema
- Puedes ejecutar cualquier comando del sistema (ej: mkdir, rm, ps, etc.).

## Requisitos

- Python 3
- Kali Linux (o cualquier distribución Linux)
- Permisos de sudo para comandos administrativos

## Ejemplos de Uso

```
LUCASMAN> ls
LUCASMAN> cd /home
LUCASMAN> pwd
LUCASMAN> shutdown
LUCASMAN> exit
```

¡Disfruta gestionando tu sistema con LUCASMAN!



## INSTALACION

Pon en tu terminal:

```
sudo apt install gnome-terminal
```

Pega el codigo de main.py
y presiona CTRL X luego Y y luego ENTER y lo has guardado, luego escribe

```
chmod +x LUCASMAN.py
./LUCASMAN.py
```

¡Y LISTO!

disfrutalo