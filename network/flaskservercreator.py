import importlib
import subprocess

# Try to import the Flask module
try:
  from flask import Flask
except ImportError:
  # If the import fails, install Flask using pip
  subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
  # Import the Flask module again
  from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
