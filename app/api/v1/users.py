from fastapi import APIRouter
from fastapi import Depends

from app.api.deps import get_current_user
from app.core.permissions import require_role

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def profile(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "role": current_user.role
    }


@router.get("/admin-dashboard")
def admin_dashboard(
    current_user=Depends(get_current_user)
):
    require_role(
        current_user,
        ["admin"]
    )

    return {
        "message": "Welcome Admin"
    }