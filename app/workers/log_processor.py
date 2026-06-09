from app.core.celery_app import celery

from app.utils.parser import parse_log_line

from app.models.log import Log

from app.core.database import SessionLocal


@celery.task
def process_log_file(content: str):
    db = SessionLocal()

    try:
        logs_to_insert = []

        for line in content.splitlines():
            parsed = parse_log_line(line)

            if parsed:
                logs_to_insert.append(
                    Log(**parsed)
                )

        db.bulk_save_objects(logs_to_insert)

        db.commit()

        return {
            "processed": len(logs_to_insert)
        }

    except Exception as error:
        db.rollback()

        return {
            "error": str(error)
        }

    finally:
        db.close()