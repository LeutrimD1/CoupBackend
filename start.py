import subprocess
import sys

# Install Flask
subprocess.call([sys.executable, '-m', 'pip', 'install', 'flask'])

# Execute the main program (program.py)
subprocess.call([sys.executable, 'program.py'])
