#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import logging
import secrets
import os
from typing import Annotated
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi

from apis.api_microservices_fastapi import router as api_router
import config.constants as constants
from com.nttdata.utils.loggers import config_logging
from apis.healthcheck.fastapi_healthcheck import router as healthcheck_router


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

# Create FastAPI app
app = FastAPI(
    redirect_slashes=False,
    title="DataProcessing.API",
    description=constants.DESCRIPTION_API,
    version=constants.VERSION,
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    openapi_tags=[
      {
            "name": "VocabularyHub",
            "description": constants.DESCRIPTION_VOCABULARY_HUB,
        },

        {
            "name": "ControlledVocabularies",
            "description": "CRUD operations for controlled vocabularies."
        }
    ],
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security scheme
security = HTTPBasic()

# Import and register routers
app.include_router(api_router, prefix=constants.END_POINT_API)

# Logging
config_logging()
logger = logging.getLogger(__name__)

@app.get("/", include_in_schema=False)
def read_root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Root endpoint for the DSB Data Processing API.
    Provides links to the documentation.
    """
    correct_username = secrets.compare_digest(credentials.username, constants.API_USER)
    correct_password = secrets.compare_digest(credentials.password, constants.API_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return {
        "message": "Welcome to DataProcessing API!",
        "docs_url": f"/{constants.PROJECT_NAME}/{constants.VERSION}/docs",
        "redoc_url": f"/{constants.PROJECT_NAME}/{constants.VERSION}/redoc",
    }

@app.get(f"/{constants.PROJECT_NAME}/{constants.VERSION}/docs", include_in_schema=False)
def swagger_docs(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Endpoint for Swagger UI documentation.
    """
    correct_username = secrets.compare_digest(credentials.username, constants.API_USER)
    correct_password = secrets.compare_digest(credentials.password, constants.API_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return get_swagger_ui_html(
        openapi_url=f"/{constants.PROJECT_NAME}/{constants.VERSION}/openapi.json",
        title="DataProcessing.API - Swagger UI"
    )

@app.get(f"/{constants.PROJECT_NAME}/{constants.VERSION}/redoc", include_in_schema=False)
def get_redoc(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Endpoint for ReDoc documentation.
    """
    correct_username = secrets.compare_digest(credentials.username, constants.API_USER)
    correct_password = secrets.compare_digest(credentials.password, constants.API_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return get_redoc_html(
        openapi_url=f"/{constants.PROJECT_NAME}/{constants.VERSION}/openapi.json",
        title="DataProcessing.API - ReDoc"
    )

@app.get(f"/{constants.PROJECT_NAME}/{constants.VERSION}/openapi.json", include_in_schema=False)
def get_openapi_schema(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    """
    Endpoint for OpenApi Schema.
    """
    correct_username = secrets.compare_digest(credentials.username, constants.API_USER)
    correct_password = secrets.compare_digest(credentials.password, constants.API_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return JSONResponse(app.openapi())
