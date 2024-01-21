import subprocess
import sys

# Install Flask
subprocess.call([sys.executable, '-m', 'pip', 'install', 'flask'])

subprocess.call([sys.executable, '-m', 'pip', 'install', 'waitress'])