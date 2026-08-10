from sqlalchemy.orm import Session
from sqlalchemy import select
from app.model.user import User 

class UserRepository:
    def __init__(self, session : Session):
        self.session = session 

    def get_by_id(self,user:int) ->User | None:
        statement = select(User).where(User.id == user)
        result = self.session.execute(statement)
        return result.scalar_one_or_none()
   
