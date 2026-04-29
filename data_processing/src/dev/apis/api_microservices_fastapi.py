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
from fastapi import APIRouter

from apis.ingestion_integration.fastapi_data_ingestion_integration import router as data_ingestion_integration_router
from apis.ingestion_integration.fastapi_get_metadata import router as get_metadata_router
from apis.ingestion_integration.fastapi_delete_metadata import router as delete_metadata_router
from apis.update_metadata.fastapi_update_metadata import router as update_metadata_router
from apis.edit_metadata.fastapi_edit_metadata import router as edit_metadata_router
from apis.healthcheck.fastapi_healthcheck import router as healthcheck_router
from apis.controlled_vocabularies.fastapi_controlled_vocabularies import router as controlled_vocabularies_router


# Api Router
router = APIRouter()

# Register sub-APIs as routers
router.include_router(data_ingestion_integration_router, prefix="/VocabularyHub", tags=["VocabularyHub"])
router.include_router(update_metadata_router, prefix="/VocabularyHub", tags=["VocabularyHub"])
router.include_router(edit_metadata_router, prefix="/VocabularyHub", tags=["VocabularyHub"])
router.include_router(get_metadata_router, prefix="/VocabularyHub", tags=["VocabularyHub"])
router.include_router(delete_metadata_router, prefix="/VocabularyHub", tags=["VocabularyHub"])
router.include_router(controlled_vocabularies_router, prefix="", tags=["ControlledVocabularies"])
router.include_router(healthcheck_router, prefix="", tags=["Health-Check"])
