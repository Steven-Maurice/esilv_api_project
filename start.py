import subprocess
import sys

# Installer les dépendances depuis requirements.txt
def install_requirements():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

# Exécuter server.py
def run_server():
    subprocess.run([sys.executable, 'server.py'])

if __name__ == "__main__":
    install_requirements()
    run_server()
