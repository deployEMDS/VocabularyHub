# APIs package

This README describes the contents of the `src/dev/apis` package. It summarizes each api of the microservice, their purpose, public objects (routers), and the main REST endpoints exposed by the project.

## Files

### `api_microservices_fastapi.py`
- Purpose: Registers all API routers into a FastAPI `APIRouter` and composes the application router used by the FastAPI app.
- Public objects:
  - `router`: FastAPI `APIRouter` used to include sub-routers and expose endpoints on the main FastAPI application.
- Routers added to `router` (in order) and their path prefixes / OpenAPI tags:
  - `ingestion_integration` — ingests resources and triggers integration flows (registered under `/VocabularyHub` tag)
  - `update_metadata` — updates resource metadata (registered under `/VocabularyHub` tag)
  - `dcat_odrl_integration` — integrates DCAT + ODRL information (registered under `/CatalogDatasets` tag)
  - `update_dcat_odrl` — updates DCAT/ODRL for an existing resource (registered under `/CatalogDatasets` tag)
  - `dcat_dataservices` — CRUD for `dcat:DataService` (prefix `/CatalogDatasets`, tag `DataServices`)
  - `dcat_distributions` — CRUD for `dcat:Distribution` (prefix `/CatalogDatasets`, tag `Distributions`)
  - `dcat_policies` — CRUD for ODRL policies (`odrl:Offer`) (prefix `/CatalogDatasets`, tag `Policies`)
  - `dcat_agents` — CRUD for FOAF agents (prefix `/CatalogDatasets`, tag `Agents`)
  - `dcat_datasets` — CRUD for `dcat:Dataset` (prefix `/CatalogDatasets`, tag `Datasets`)
  - `dcat_catalogs` — CRUD for `dcat:Catalog` (prefix `/CatalogDatasets`, tag `Catalogs`)
  - `healthcheck` — simple health endpoint (root-level route, `Health-Check` tag)

---

## Apis and their responsibilities

### `healthcheck`
- Files: `healthcheck/fastapi_healthcheck.py`
- Purpose: A lightweight health check endpoint to verify the service is running.
- Router: `APIRouter` (path resolved from `constants.END_POINT_HEALTHCHECK`).
- Main resource: `HealthCheck` with method `get`.
- Input: none.
- Output model: `HealthcheckOutput` (Pydantic model) — returns a boolean `status` and a `message` string.

### `ingestion_integration`
- Files: `ingestion_integration/fastapi_data_ingestion_integration.py`
- Purpose: Combined ingestion + integration flow: ingests a resource and then runs the integration pipeline. Uses `DataIngestionFactory` and `DataIntegrationFactory`.
- Router: registered under the `/VocabularyHub` prefix and corresponding tag.
- Main resource: `IngestionIntegration` with method `post`.
- Input model: `ingestion_integration_input` — includes resource `type`, `resourceUrl` (optional), `resourceName`, `resourceVersion`, `fileExtension`, optional `metadata`.
- Output model: `ingestion_integration_output` — returns `status` and `message`.

### `dcat_odrl_ingestion_integration`
- Files: `dcat_odrl_ingestion_integration/fastapi_dcat_odr_integration.py`
- Purpose: Accepts a DCAT model plus a list of ODRL rules and performs an integration.
- Router: registered under the `/CatalogDatasets` prefix and corresponding tag.
- Main resource: `DcatOdrlIntegration` with method `post`.
- Input model: `dcat_odrl_input` — contains `dcat` and `odrl`.
- Output model: `dcat_odrl_output` — returns `status` and `message`.

### `update_dcat_odrl`
- Files: `update_dcat_odrl/fastapi_update_dcat_odrl.py`
- Purpose: Update DCAT data and ODRL rules of an existing resource.
- Router: registered under the `/CatalogDatasets` prefix and tag.
- Main resource: `UpdateDcatOdrl` with method `put`.
- Input model: `update_metadata_input` — includes `resourceId`, `dcat` and `odrl`.
- Output model: `update_dcat_odrl_output` — returns `status` and `message`.

### `update_metadata`
- Files: `update_metadata/fastapi_update_metadata.py`
- Purpose: Update metadata for an existing resource.
- Router: registered under the `/VocabularyHub` prefix and tag.
- Main resource: `UpdateMetadata` with method `put`.
- Input model: `update_metadata_input` — includes `resourceId` and `metadata`.
- Output model: `update_metadata_output` — returns `status` and `message`.

---

## CRUD APIs (DCAT)

All CRUD routers below are registered under the `/CatalogDatasets` prefix.

### `dcat_catalogs`
- Files: `dcat_catalogs/fastapi_catalogs.py`
- Purpose: CRUD for `dcat:Catalog`.
- Endpoints:
  - `POST   /CatalogDatasets/catalogs`
  - `GET    /CatalogDatasets/catalogs/{catalog_id}`
  - `PUT    /CatalogDatasets/catalogs/{catalog_id}`
  - `DELETE /CatalogDatasets/catalogs/{catalog_id}`
  - `GET    /CatalogDatasets/catalogs` (pagination via `page`, `size`)

### `dcat_datasets`
- Files: `dcat_datasets/fastapi_datasets.py`
- Purpose: CRUD for `dcat:Dataset`.
- Endpoints:
  - `POST   /CatalogDatasets/datasets`
  - `GET    /CatalogDatasets/datasets/{dataset_id}`
  - `PUT    /CatalogDatasets/datasets/{dataset_id}`
  - `DELETE /CatalogDatasets/datasets/{dataset_id}`
  - `GET    /CatalogDatasets/datasets` (pagination via `page`, `size`)

### `dcat_distributions`
- Files: `dcat_distributions/fastapi_distributions.py`
- Purpose: CRUD for `dcat:Distribution`.
- Endpoints:
  - `POST   /CatalogDatasets/distributions`
  - `GET    /CatalogDatasets/distributions/{distribution_id}`
  - `PUT    /CatalogDatasets/distributions/{distribution_id}`
  - `DELETE /CatalogDatasets/distributions/{distribution_id}`
  - `GET    /CatalogDatasets/distributions` (pagination via `page`, `size`)

### `dcat_agents`
- Files: `dcat_agents/fastapi_agents.py`
- Purpose: CRUD for FOAF agents.
- Endpoints:
  - `POST   /CatalogDatasets/agents`
  - `GET    /CatalogDatasets/agents/{agent_id}`
  - `PUT    /CatalogDatasets/agents/{agent_id}`
  - `DELETE /CatalogDatasets/agents/{agent_id}`
  - `GET    /CatalogDatasets/agents` (pagination via `page`, `size`)

### `dcat_dataservices`
- Files: `dcat_dataservices/fastapi_dataservices.py`
- Purpose: CRUD for `dcat:DataService`.
- Endpoints:
  - `POST   /CatalogDatasets/dataservices`
  - `GET    /CatalogDatasets/dataservices/{dataservice_id}`
  - `PUT    /CatalogDatasets/dataservices/{dataservice_id}`
  - `DELETE /CatalogDatasets/dataservices/{dataservice_id}`
  - `GET    /CatalogDatasets/dataservices` (pagination via `page`, `size`)

### `dcat_policies`
- Files: `dcat_policies/fastapi_policies.py`
- Purpose: CRUD for ODRL policies (`odrl:Offer`).
- Endpoints:
  - `POST   /CatalogDatasets/policies`
  - `GET    /CatalogDatasets/policies/{policy_id}` (supports `include_details`)
  - `PUT    /CatalogDatasets/policies/{policy_id}`
  - `DELETE /CatalogDatasets/policies/{policy_id}`
  - `GET    /CatalogDatasets/policies` (pagination via `page`, `size`, optional `include_details`)
