from fastapi import APIRouter, Depends, UploadFile , status
from fastapi.responses import JSONResponse
from helpers.config import Settings, get_settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile,
    app_settings: Settings = Depends(get_settings)
):
    is_valid, message = DataController().validate_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": message}
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": message}
    )