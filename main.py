#!/usr/bin/env python3
import os
import subprocess
import sys
import time

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

def run_program():
    loading_screen()
    show_logo()
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
            elif cmd.startswith('cd '):
                path = cmd[3:].strip()
                try:
                    os.chdir(path)
                    print(f"Directorio cambiado a: {os.getcwd()}")
                except FileNotFoundError:
                    print("Directorio no encontrado.")
                except Exception as e:
                    print(f"Error cambiando directorio: {e}")
            elif cmd == 'pwd':
                print(os.getcwd())
            else:
                # Ejecutar como comando del sistema
                execute_command(cmd)
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo...")
            break
        except EOFError:
            print("\nFin de entrada. Saliendo...")
            break
    # Cerrar el terminal al salir
    os.system("exit")

def main():
    if len(sys.argv) == 1:
        # Modo launcher: abrir nueva terminal
        try:
            subprocess.run([
                "gnome-terminal",
                "--title", "LUCASMAN terminal",
                "--", "python3", __file__, "--run"
            ])
        except FileNotFoundError:
            print("Error: gnome-terminal no encontrado. Instálalo con 'sudo apt install gnome-terminal'")
        except Exception as e:
            print(f"Error al abrir terminal: {e}")
    elif len(sys.argv) == 2 and sys.argv[1] == "--run":
        # Modo programa: ejecutar el gestor
        run_program()
    else:
        print("Uso: python3 main.py")

if __name__ == "__main__":
    main()