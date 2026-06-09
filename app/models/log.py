# pyrefly: ignore [missing-import]
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.core.database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    ip_address = Column(
        String(50),
        index=True
    )

    method = Column(String(20))

    endpoint = Column(String(255))

    status_code = Column(
        Integer,
        index=True
    )

    response_time = Column(Float)

    user_agent = Column(String(500))

    log_level = Column(
        String(50),
        index=True
    )

    message = Column(String(2000))

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
