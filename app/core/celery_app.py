from celery import Celery

from app.core.config import settings

celery = Celery(
    "log_analytics",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery.conf.task_routes = {
    "app.workers.log_processor.*": {
        "queue": "logs"
    }
}