from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import HTTPException

from app.api.deps import get_current_user

from app.workers.log_processor import (
    process_log_file
)

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


@router.post("/upload")
async def upload_logs(
    file: UploadFile = File(...),
    current_user=Depends(get_current_user)
):
    if not file.filename.endswith(".log"):
        raise HTTPException(
            status_code=400,
            detail="Only .log files allowed"
        )

    content = await file.read()

    process_log_file.delay(
        content.decode("utf-8")
    )

    return {
        "message": "Log file uploaded",
        "filename": file.filename
    }