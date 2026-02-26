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

### 🤖 Chat GPT (Inteligencia Artificial)
- `gptkey <tu_api_key>`: Configura tu clave API de OpenAI.
- `gpt <pregunta>`: Haz una pregunta a ChatGPT y obtén respuesta inmediata.
- `chat`: Entra en modo chat interactivo con ChatGPT (escribe `exit_chat` para salir).

**Nota:** Necesitas una API key de OpenAI. Obtén la tuya en https://platform.openai.com/api-keys

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



## Instalación

### 📦 Opción 1: Instalación Global con APT (Recomendado)
Para instalar LUCASMAN globalmente en cualquier máquina Linux (Kali, Ubuntu, Debian):

1. **Agrega el repositorio oficial:**
   ```
   echo "deb [trusted=yes] https://lucasbazuki-web-developer.github.io/LUCASMAN/ ./" | sudo tee /etc/apt/sources.list.d/lucasman.list
   ```

2. **Actualiza la lista de paquetes:**
   ```
   sudo apt update
   ```

3. **Instala LUCASMAN:**
   ```
   sudo apt install lucasman
   ```

4. **Ejecuta el programa:**
   ```
   lucasman
   ```

✅ **Ventaja:** Las dependencias se instalan automáticamente.

### 📥 Opción 2: Instalación Manual (sin repositorio)
Si prefieres instalar sin agregar un repositorio:

1. **Descarga el paquete .deb:**
   ```
   wget https://github.com/lucasbazuki-web-developer/LUCASMAN/raw/main/lucasman_1.0_all.deb
   ```

2. **Instala el paquete:**
   ```
   sudo dpkg -i lucasman_1.0_all.deb
   ```

3. **Ejecuta:**
   ```
   lucasman
   ```

### 🚀 Opción 3: Ejecutar Directamente (sin instalar)
Si solo quieres probar sin instalar nada:

1. **Clona el repositorio:**
   ```
   git clone https://github.com/lucasbazuki-web-developer/LUCASMAN.git
   cd LUCASMAN
   ```

2. **Ejecuta directamente:**
   ```
   python3 main.py
   ```

✅ **Nota:** Al iniciar, LUCASMAN instalará automáticamente las dependencias necesarias (xterm, apache2).

## Primer Uso

Al ejecutar LUCASMAN por primera vez:
1. Verás una pantalla de carga con animación.
2. Se mostrará el logo de LUCASMAN.
3. Se instalarán automáticamente las dependencias si es necesario.
4. ¡Listo para usar! Escribe `help` para ver todos los comandos disponibles.