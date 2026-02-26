#!/usr/bin/python3
import os
import subprocess
import sys
import time
import socket

# Importar OpenAI si está disponible
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

def install_dependencies():
    """Instala dependencias necesarias automáticamente"""
    print("Verificando e instalando dependencias...")
    dependencies = ["xterm", "apache2"]
    python_packages = ["openai"]
    
    for dep in dependencies:
        try:
            result = subprocess.run(f"which {dep}", shell=True, capture_output=True)
            if result.returncode != 0:
                print(f"  Instalando {dep}...")
                subprocess.run(f"sudo apt install -y {dep}", shell=True)
        except Exception as e:
            print(f"  No se pudo instalar {dep}: {e}")
    
    # Instalar paquetes Python
    for pkg in python_packages:
        try:
            __import__(pkg)
        except ImportError:
            print(f"  Instalando paquete Python: {pkg}...")
            subprocess.run(f"pip install -q {pkg}", shell=True)
    
    print("  Dependencias listas!\n")

def loading_screen():
    print("Cargando LUCASMAN...")
    for i in range(20):
        bar = "█" * (i + 1) + "░" * (19 - i)
        print(f"\r[{bar}] {i*5 + 5}%", end="")
        time.sleep(0.05)
    print("\n¡LUCASMAN cargado exitosamente!")

def show_logo():
    print("""
    ██╗     ██╗   ██╗ ██████╗ █████╗ ███████╗███╗   ███╗ █████╗ ███╗   ██╗
    ██║     ██║   ██║██╔════╝██╔══██╗██╔════╝████╗ ████║██╔══██╗████╗  ██║
    ██║     ██║   ██║██║     ███████║███████╗██╔████╔██║███████║██╔██╗ ██║
    ██║     ██║   ██║██║     ██╔══██║╚════██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ███████╗╚██████╔╝╚██████╗██║  ██║███████║██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    """)

def execute_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"Error ejecutando comando: {e}")

def get_my_ip():
    """Obtiene la IP local de la máquina"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "IP no disponible"

def get_api_key():
    """Obtiene la API key de ChatGPT desde el archivo o la solicita al usuario"""
    config_file = os.path.expanduser("~/.lucasman_openai_key")
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            return f.read().strip()
    return None

def save_api_key(api_key):
    """Guarda la API key de ChatGPT en un archivo"""
    config_file = os.path.expanduser("~/.lucasman_openai_key")
    with open(config_file, "w") as f:
        f.write(api_key)
    os.chmod(config_file, 0o600)  # Permisos de solo lectura para el usuario
    print("✅ API key guardada correctamente.")

def chat_gpt(message, api_key):
    """Envía un mensaje a ChatGPT y obtiene la respuesta"""
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def run_program():
    install_dependencies()
    loading_screen()
    show_logo()
    
    apache_running = False
    
    while True:
        try:
            cmd = input("LUCASMAN> ").strip()
            if not cmd:
                continue
            if cmd.lower() == 'exit':
                print("Saliendo de LUCASMAN...")
                break
            elif cmd.lower() == 'shutdown':
                print("Ejecutando shutdown...")
                execute_command("sudo shutdown -h now")
            elif cmd.lower() == 'windows':
                print("Abriendo nueva ventana de terminal...")
                try:
                    subprocess.Popen(["xterm", "-title", "LUCASMAN Terminal"])
                except FileNotFoundError:
                    print("xterm no encontrado.")
            elif cmd.lower() == 'closew':
                print("Cerrando todas las ventanas xterm...")
                execute_command("pkill xterm")
            elif cmd.lower() == 'apache':
                if not apache_running:
                    print("Iniciando Apache2 en http://localhost:80...")
                    execute_command("sudo systemctl start apache2")
                    apache_running = True
                    print("Apache iniciado. Abre http://localhost en tu navegador.")
                else:
                    print("Apache ya está corriendo. Para detenerlo usa 'apache stop'")
            elif cmd.lower() == 'apache stop':
                if apache_running:
                    print("Deteniendo Apache2...")
                    execute_command("sudo systemctl stop apache2")
                    apache_running = False
                else:
                    print("Apache no está corriendo.")
            elif cmd.lower() == 'myip':
                my_ip = get_my_ip()
                print(f"Tu IP local: {my_ip}")
            elif cmd.lower() == 'netinfo':
                print("\n=== Información de Red ===")
                print(f"IP Local: {get_my_ip()}")
                print("\n=== Interfaces de Red ===")
                execute_command("ip addr")
            elif cmd.lower() == 'netstat':
                print("=== Conexiones de Red ===")
                execute_command("netstat -tuln")
            elif cmd.lower() == 'help':
                print("""
╔═══════════════════════════════════════════════════════════════╗
║              LUCASMAN - Comandos Disponibles                  ║
╚═══════════════════════════════════════════════════════════════╝

📁 ARCHIVOS Y DIRECTORIOS:
  • ls              - Listar archivos
  • cd <dir>        - Cambiar directorio
  • pwd             - Mostrar directorio actual
  • clear           - Limpiar pantalla

🔧 SISTEMA:
  • shutdown        - Apagar sistema (requiere sudo)
  • windows         - Abrir nueva ventana de terminal
  • closew          - Cerrar todas las ventanas xterm

🌐 RED E IP:
  • myip            - Ver tu IP local
  • netinfo         - Ver información completa de red
  • netstat         - Ver conexiones de red activas

🌐 WEB (APACHE):
  • apache          - Iniciar servidor Apache2
  • apache stop     - Detener servidor Apache2

🤖 CHAT GPT (IA):
  • gpt <pregunta>  - Hacer una pregunta a ChatGPT
  • gptkey <key>    - Configurar tu API key de OpenAI
  • chat            - Modo chat interactivo con GPT

ℹ️  AYUDA:
  • help            - Mostrar esta ayuda
  • exit            - Salir del programa

💡 COMANDOS DEL SISTEMA:
  • Puedes ejecutar cualquier comando del sistema (ej: mkdir, rm, etc.)
                """)
            elif cmd.lower().startswith('gpt '):
                if not HAS_OPENAI:
                    print("❌ OpenAI no está instalado. Instálalo con: pip install openai")
                else:
                    api_key = get_api_key()
                    if not api_key:
                        print("⚠️  API key no configurada. Usa 'gptkey <tu_api_key>' para configurarla.")
                    else:
                        question = cmd[4:].strip()
                        print("🤖 Esperando respuesta de ChatGPT...")
                        response = chat_gpt(question, api_key)
                        print(f"\n💬 ChatGPT:\n{response}\n")
            elif cmd.lower().startswith('gptkey '):
                api_key = cmd[7:].strip()
                save_api_key(api_key)
            elif cmd.lower() == 'chat':
                if not HAS_OPENAI:
                    print("❌ OpenAI no está instalado. Instálalo con: pip install openai")
                else:
                    api_key = get_api_key()
                    if not api_key:
                        print("⚠️  API key no configurada. Usa 'gptkey <tu_api_key>' para configurarla.")
                    else:
                        print("🤖 Modo Chat GPT activado. Escribe 'exit_chat' para salir.\n")
                        while True:
                            user_input = input("Tú: ").strip()
                            if user_input.lower() == 'exit_chat':
                                print("Saliendo del chat...")
                                break
                            if user_input:
                                print("🤖 Esperando respuesta...")
                                response = chat_gpt(user_input, api_key)
                                print(f"ChatGPT: {response}\n")
            elif cmd.lower() == 'clear':
                os.system('clear')
            elif cmd.startswith('cd '):
                path = cmd[3:].strip()
                try:
                    os.chdir(path)
                    print(f"Directorio cambiado a: {os.getcwd()}")
                except FileNotFoundError:
                    print("Directorio no encontrado.")
                except Exception as e:
                    print(f"Error: {e}")
            elif cmd == 'pwd':
                print(os.getcwd())
            else:
                execute_command(cmd)
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo...")
            break
        except EOFError:
            print("\nFin de entrada. Saliendo...")
            break

def main():
    run_program()

if __name__ == "__main__":
    main()