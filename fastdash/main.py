# -*- coding: utf-8 -*-

"""Main module."""
# -*- coding: utf-8 -*-

"""Main module."""

from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from fastdash.api.errors.http_error import http_error_handler
from fastdash.core.events import create_start_app_handler, create_stop_app_handler
from fastdash.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from fastdash.api.routes.api import router as api_router


def create_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    application.add_exception_handler(HTTPException, http_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = create_application()
