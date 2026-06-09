from app.core.database import engine
from app.models.user import User
from app.models.log import Log

User.__table__.create(bind=engine, checkfirst=True)
Log.__table__.create(bind=engine, checkfirst=True)

print("Tables created successfully")