from app.database.base import Base
from app.database.session import engine

from app.model.user import User

def init_db():
    Base.MetaData.create_all(bind= engine)
