#!/usr/bin/python3
import os
import subprocess
import sys
import time
import socket

# Versión y cambios
VERSION = "2.0"
CHANGELOG = """
v2.0 - 26/02/2026:
  ✨ Integración de ChatGPT (gpt, gptkey, chat)
  ✨ Herramientas de pentesting integradas (nmap, aircrack, etc)
  ✨ Instalación automática de herramientas de hacking
  ✨ Bloqueo de programa hasta instalar dependencias
  🔧 Mejora en UI y comandos
  
v1.0 - 25/02/2026:
  ✨ Pantalla de carga
  ✨ Gestión de archivos
  ✨ Control de Apache2
  ✨ Información de red (IP, netinfo, netstat)
  ✨ Manejo de terminal (windows, closew)
"""

# Importar OpenAI si está disponible
try:
    from openai import OpenAI
    HAS_OPENAI = True
except (ImportError, ModuleNotFoundError):
    try:
        import openai
        HAS_OPENAI = True
    except (ImportError, ModuleNotFoundError):
        HAS_OPENAI = False

def check_root():
    """Verifica si se ejecuta como root"""
    return os.geteuid() == 0 if hasattr(os, 'geteuid') else False

def install_dependencies():
    """Instala dependencias necesarias automáticamente de forma bloqueante"""
    print("\n" + "="*70)
    print("🔧 INSTALADOR DE DEPENDENCIAS - LUCASMAN".center(70))
    print("="*70)
    print("\n⚠️  IMPORTANTE: El programa bloqueará hasta que todas las")
    print("   dependencias estén instaladas. Por favor, espera...\n")
    
    # Herramientas del sistema
    system_tools = [
        "xterm",           # Terminal
        "apache2",         # Servidor web
        "nmap",            # Escaneo de puertos
        "aircrack-ng",     # Pentesting WiFi
        "wireshark",       # Análisis de tráfico
        "hashcat",         # Cracking de hashes
        "john",            # John the Ripper
        "metasploit-framework",  # Framework de hacking
        "hydra",           # Fuerza bruta
        "nikto",           # Escáner web
        "sqlmap",          # Inyección SQL
        "netcat",          # Swiss army knife
        "clamav"           # Antivirus
    ]
    
    python_packages = ["openai>=1.0"]
    
    total_tools = len(system_tools) + len(python_packages)
    installed = 0
    
    print(f"📦 Total de paquetes a instalar: {total_tools}\n")
    
    # Instalar herramientas del sistema
    for dep in system_tools:
        try:
            result = subprocess.run(f"which {dep}", shell=True, capture_output=True, timeout=5)
            if result.returncode == 0:
                print(f"✅ {dep:25} - YA INSTALADO")
                installed += 1
            else:
                print(f"⬇️  {dep:25} - Instalando...", end=" ", flush=True)
                cmd = f"sudo apt install -y {dep} > /dev/null 2>&1"
                proc = subprocess.run(cmd, shell=True, timeout=300)
                if proc.returncode == 0:
                    print("✅ Instalado")
                    installed += 1
                else:
                    print("⚠️  Error (continuando...)")
        except subprocess.TimeoutExpired:
            print("⏱️  Timeout (continuando...)")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print()  # Espaciado
    
    # Instalar paquetes Python
    for pkg in python_packages:
        try:
            __import__(pkg)
            print(f"✅ {pkg:25} - YA INSTALADO")
            installed += 1
        except ImportError:
            print(f"⬇️  {pkg:25} - Instalando...", end=" ", flush=True)
            result = subprocess.run(f"pip install -q {pkg}", shell=True, timeout=300)
            if result.returncode == 0:
                print("✅ Instalado")
                installed += 1
            else:
                print("⚠️  Error (continuando...)")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "="*70)
    print(f"✅ INSTALACIÓN COMPLETADA: {installed}/{total_tools} paquetes listos")
    print("="*70 + "\n")
    time.sleep(2)

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
        # Intentar con OpenAI 1.0+ (cliente)
        if HAS_OPENAI:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}],
                    max_tokens=500
                )
                return response.choices[0].message.content
            except (ImportError, AttributeError):
                # Fallback para versiones antiguas de OpenAI
                import openai
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message}],
                    max_tokens=500
                )
                return response.choices[0].message.content
        else:
            return "❌ Error: OpenAI no está instalado"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def show_hacking_tools():
    """Muestra las herramientas de hacking disponibles"""
    tools = {
        "nmap": "Escaneo de puertos y reconocimiento",
        "aircrack-ng": "Pentesting de redes WiFi",
        "wireshark": "Análisis de tráfico de red",
        "hashcat": "Cracking acelerado de hashes",
        "john": "John the Ripper - Cracking de passwords",
        "hydra": "Ataques de fuerza bruta",
        "nikto": "Escáner de vulnerabilidades web",
        "sqlmap": "Detección y explotación de inyección SQL",
        "netcat": "Herramienta de red versátil",
        "metasploit": "Framework de penetración"
    }
    
    print("\n" + "="*70)
    print("🔓 HERRAMIENTAS DE PENTESTING DISPONIBLES".center(70))
    print("="*70)
    for tool, description in tools.items():
        print(f"  • {tool:20} - {description}")
    print("="*70 + "\n")

def scan_file_antivirus(filepath):
    """Escanea un archivo individual con ClamAV"""
    print(f"\n🛡️  Escaneando archivo: {filepath}")
    print("="*70)
    try:
        result = subprocess.run(f"clamscan '{filepath}'", shell=True, capture_output=True, text=True, timeout=60)
        print(result.stdout)
        if result.returncode == 0:
            print("✅ Archivo limpio")
        elif result.returncode == 1:
            print("⚠️  ¡VIRUS DETECTADO!")
        else:
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print("⏱️  El escaneo tardó demasiado")
    except Exception as e:
        print(f"❌ Error: {e}")
    print("="*70 + "\n")

def scan_directory_antivirus(dirpath):
    """Escanea un directorio completo con ClamAV"""
    print(f"\n🛡️  Escaneando directorio: {dirpath}")
    print("="*70)
    try:
        result = subprocess.run(f"clamscan -r '{dirpath}'", shell=True, capture_output=True, text=True, timeout=300)
        print(result.stdout)
        if result.returncode == 0:
            print("✅ Directorio limpio")
        elif result.returncode == 1:
            print("⚠️  ¡AMENAZA DETECTADA!")
        else:
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print("⏱️  El escaneo tardó demasiado")
    except Exception as e:
        print(f"❌ Error: {e}")
    print("="*70 + "\n")

def update_antivirus_db():
    """Actualiza la base de datos de virus de ClamAV"""
    print("\n🔄 Actualizando base de datos de virus...")
    print("="*70)
    try:
        result = subprocess.run("sudo freshclam", shell=True, capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            print("✅ Base de datos actualizada correctamente")
        else:
            print(result.stdout)
            print(result.stderr)
    except subprocess.TimeoutExpired:
        print("⏱️  La actualización tardó demasiado")
    except Exception as e:
        print(f"❌ Error: {e}")
    print("="*70 + "\n")

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
            elif cmd.lower() == 'version':
                print("\n" + "="*70)
                print(f"LUCASMAN v{VERSION}".center(70))
                print("="*70)
                print(CHANGELOG)
                print("="*70 + "\n")
            elif cmd.lower() == 'tools':
                show_hacking_tools()
            elif cmd.lower().startswith('scan '):
                filepath = cmd[5:].strip()
                scan_file_antivirus(filepath)
            elif cmd.lower().startswith('scan-dir '):
                dirpath = cmd[9:].strip()
                scan_directory_antivirus(dirpath)
            elif cmd.lower() == 'update-av':
                update_antivirus_db()
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
║              LUCASMAN v{} - Comandos Disponibles              ║
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

🔓 PENTESTING (HACKING):
  • tools           - Ver herramientas de pentesting disponibles
  • nmap <host>     - Escaneo de puertos
  • aircrack-ng     - WiFi pentesting
  • hydra           - Fuerza bruta

🛡️  ANTIVIRUS (CLAMAV):
  • scan <archivo>  - Escanear archivo individual
  • scan-dir <dir>  - Escanear un directorio completo
  • update-av       - Actualizar base de datos de virus

🤖 CHAT GPT (IA):
  • gpt <pregunta>  - Hacer una pregunta a ChatGPT
  • gptkey <key>    - Configurar tu API key de OpenAI
  • chat            - Modo chat interactivo con GPT

ℹ️  INFO:
  • version         - Ver versión y cambios
  • help            - Mostrar esta ayuda
  • exit            - Salir del programa

💡 COMANDOS DEL SISTEMA:
  • Puedes ejecutar cualquier comando del sistema (ej: mkdir, rm, etc.)
                """.format(VERSION))
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