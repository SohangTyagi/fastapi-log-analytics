# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
# pyrefly: ignore [import-not-found]
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@"
    f"{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()