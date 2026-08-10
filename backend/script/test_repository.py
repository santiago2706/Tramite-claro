import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.database.session import SessionLocal
from app.repositories.user_repository import UserRepository

def main() -> None:
    session = SessionLocal()
    try: 
        repository = UserRepository(session)
        user = repository.get_by_id(1)
        print("Resultado: ")
        print(user)
    finally: 
        session.close()
if __name__ == "__main__":
    main()

