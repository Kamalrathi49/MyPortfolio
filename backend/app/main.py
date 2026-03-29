import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.exceptions import AppException
from app.core.middleware import RequestLoggingMiddleware

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")


def create_app() -> FastAPI:
    settings = get_settings()
    application = FastAPI(title="Portfolio API", version="1.0.0")
    application.add_middleware(RequestLoggingMiddleware)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @application.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException) -> JSONResponse:
        rid = getattr(request.state, "request_id", None)
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": exc.code,
                    "message": exc.message,
                    "request_id": rid,
                }
            },
        )

    @application.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request, exc: StarletteHTTPException
    ) -> JSONResponse:
        rid = getattr(request.state, "request_id", None)
        detail = exc.detail
        message = detail if isinstance(detail, str) else "Request failed"
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "code": "HTTP_ERROR",
                    "message": message,
                    "request_id": rid,
                }
            },
        )

    @application.exception_handler(RequestValidationError)
    async def validation_handler(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        rid = getattr(request.state, "request_id", None)
        return JSONResponse(
            status_code=422,
            content={
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": "Invalid request",
                    "request_id": rid,
                    "details": exc.errors(),
                }
            },
        )

    @application.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, _exc: Exception) -> JSONResponse:
        rid = getattr(request.state, "request_id", None)
        logging.getLogger("app.main").exception("unhandled")
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "An unexpected error occurred",
                    "request_id": rid,
                }
            },
        )

    @application.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    application.include_router(api_router, prefix="/api/v1")
    return application


app = create_app()
