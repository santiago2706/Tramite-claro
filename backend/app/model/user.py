from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_colum

from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_colum(primary_key = true)
    name: Mapped[str] = mapped_colum(String(100))
    email: Mapped[str] = mapped_colum(String(255), unique = true)

