import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database.init_db import init_db

init_db()

print("✅ Tablas creadas correctamente.")