# LUCASMAN - Gestor de Archivos y Sistema

Un programa simple escrito en Python para gestionar archivos y ejecutar comandos del sistema en Kali Linux.

## Características

- **Pantalla de carga**: Animación cool al iniciar.
- **Logo personalizado**: Muestra "LUCASMAN" en arte ASCII.
- **Gestión de archivos**: Comandos como `ls`, `cd`, `pwd`.
- **Comandos del sistema**: Ejecuta cualquier comando, incluyendo `shutdown`.
- **Ejecución directa**: Se ejecuta en la terminal actual sin dependencias externas.

## Instalación con apt

Para instalar LUCASMAN como un paquete Debian:

1. Construye el paquete (si no está): `dpkg-deb --build deb_package lucasman_1.0_all.deb`
2. Instala: `sudo dpkg -i lucasman_1.0_all.deb`
3. Ejecuta: `lucasman`

## Cómo Ejecutar (sin instalar)

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el programa: `python3 main.py`
3. Interactúa con el prompt `LUCASMAN>`.
4. Al hacer `exit`, el programa termina (la terminal queda abierta).

## Comandos Especiales

- `cd <directorio>`: Cambiar directorio.
- `pwd`: Mostrar directorio actual.
- `ls`: Listar archivos.
- `clear`: Limpiar pantalla.
- `help`: Mostrar ayuda.
- `windows`: Abrir nueva ventana de terminal (requiere xterm).
- `shutdown`: Apagar el sistema (requiere permisos de sudo).
- `exit`: Salir del programa.
- Cualquier comando del sistema.

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