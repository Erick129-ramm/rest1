import os
import sys

# Agrega el directorio actual a la ruta del sistema para que Python pueda encontrar tus módulos
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from rest import app

# Exporta la aplicación Flask como la aplicación WSGI
application = app