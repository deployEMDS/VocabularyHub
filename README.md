# VocabularyHub Component (data_processing)

This document describes the current VocabularyHub APIs exposed by the `data_processing` microservice and its integration with the other platform microservices:

- `Validation`
- `file_manager`

## Scope

VocabularyHub in this service includes:

- resource ingestion and integration flows
- metadata update and versioned metadata edit
- resource retrieval and deletion
- controlled vocabularies import, listing, retrieval, deletion, and auto-import

Base URL (default local):

- `http://127.0.0.1:5000/data-processing/v1`

## API groups

### 1) VocabularyHub resource APIs

Prefix:

- `/data-processing/v1/VocabularyHub`

| Method | Path | Purpose |
|---|---|---|
| POST | `/VocabularyHub/create_resource` | Ingest and integrate a semantic resource |
| PUT | `/VocabularyHub/update_resource` | Update metadata of an existing resource |
| POST | `/VocabularyHub/edit_metadata` | Create a new version by applying a metadata patch |
| GET | `/VocabularyHub` | List resources (paginated, with optional filters) |
| GET | `/VocabularyHub/{resource_id}` | Get one resource by UUID |
| GET | `/VocabularyHub/versions/by-name?resource_name=...` | List all versions for a resource name |
| DELETE | `/VocabularyHub/{resource_id}` | Delete resource metadata by id |

Notes:

- `POST /edit_metadata` is copy-on-write versioning: the original resource is preserved and a new version is created.
- `DELETE /{resource_id}` can return conflict when referential integrity rules are violated.

### 2) Controlled vocabularies APIs

Primary prefix:

- `/data-processing/v1/ControlledVocabularies`

Compatibility prefix:

- `/data-processing/v1/VocabularyHub/ControlledVocabularies`

| Method | Path | Purpose |
|---|---|---|
| POST | `/ControlledVocabularies/import` | Import a vocabulary from `download_url` or uploaded `file` |
| POST | `/ControlledVocabularies/auto-import` | Run on-demand auto-import from configured resources |
| GET | `/ControlledVocabularies` | List vocabularies (paginated) |
| GET | `/ControlledVocabularies/{vocab_name}` | List vocabulary entries (paginated, localized with `lang`) |
| DELETE | `/ControlledVocabularies/{vocab_name}` | Delete a vocabulary graph |

### 3) Health-check API

| Method | Path | Purpose |
|---|---|---|
| GET | `/health-check` | Service health endpoint |

## Dependency with the other microservices

VocabularyHub orchestration in `data_processing` relies on the two related microservices below.

### Validation microservice

Default host:

- `http://127.0.0.1:5200/validator/v1`

Used endpoints:

- `/FileValidation/file_validation`
- `/CodeValidation/code_validation`
- `/SHACLValidation/SHACL_validation`
- `/DataIngestionValidation/data_ingestion_validation`
- `/DataIntegrationValidation/data_integration_validation`

Usage highlights:

- validates files and metadata before integration
- validates controlled vocabulary codes and SHACL constraints
- checks duplicate/existing resources before persistence

### file_manager microservice

Default host:

- `http://127.0.0.1:5100/file-manager/v1`

Used endpoints:

- `/Downloader/download`
- `/Uploader/upload`

Usage highlights:

- uploads resource files used by ingestion flows
- downloads remote files required for processing

## OpenAPI and interactive docs

When running `data_processing`, API docs are available at:

- `/docs`
- `/redoc`

## Related docs in this repository

- `README.md`
- `docs/README.md`
- `docs/architecture.md`
- `docs/data_processing_swagger.md`


