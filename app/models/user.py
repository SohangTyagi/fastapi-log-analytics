# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String
# pyre-check-ignore [missing-import]
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password = Column(String(255), nullable=False)

    role = Column(String(50), nullable=False)