# Microservice DATA PROCESSING

This repository provides the main process endpoint of Knowledge Factory. It is accessible through `http://127.0.0.1:5000/data-processing/v1/` by default, although host and port are configurable through environment variables.

## What this service does

This microservice orchestrates ingestion and integration flows and exposes CRUD APIs for DCAT, FOAF, ODRL, Participants, and controlled vocabularies.

### Orchestration capabilities

- Vocabularies ingestion and integration
- DCAT and ODRL ingestion and integration
- Metadata update flows
- DCAT and ODRL update flows
- VocabularyHub metadata retrieval and deletion

### CRUD capabilities

All CRUD endpoints below are exposed under `/data-processing/v1/CatalogDatasets` unless noted otherwise.

- Catalogs
- Datasets
- Distributions
- Dataset Offers
- Agents
- Participants
- Data Services
- Policies
- Policy Templates

### Controlled vocabulary capabilities

Controlled vocabulary APIs are exposed under `/data-processing/v1/ControlledVocabularies`.

Supported operations:

- import a vocabulary from a URL or uploaded file
- trigger controlled vocabularies auto-import on demand
- list vocabularies with pagination
- list localized vocabulary entries with pagination
- delete a vocabulary graph
- bootstrap vocabularies automatically at startup when enabled

## Main endpoints

Base path: `http://localhost:5000/data-processing/v1`

### Orchestration endpoints

- `POST {API_BASE}/VocabularyHub/create_resource` - ingestion and integration for vocabularies
- `PUT {API_BASE}/VocabularyHub/update_resource` - update metadata for vocabularies
- `GET {API_BASE}/VocabularyHub` - list all vocabulary resources with pagination
- `GET {API_BASE}/VocabularyHub/{resource_id}` - get a vocabulary resource by ID
- `DELETE {API_BASE}/VocabularyHub/{resource_id}` - delete a vocabulary resource by ID
- `POST {API_BASE}/CatalogDatasets/dcat_odrl_integration` - ingest and integrate DCAT and ODRL resources
- `PUT {API_BASE}/CatalogDatasets/update_dcat_odrl` - update DCAT and ODRL resources

### CRUD endpoints

- Catalogs
  - `POST {API_BASE}/CatalogDatasets/catalogs`
  - `GET {API_BASE}/CatalogDatasets/catalogs/{catalog_id}`
  - `PUT {API_BASE}/CatalogDatasets/catalogs/{catalog_id}`
  - `DELETE {API_BASE}/CatalogDatasets/catalogs/{catalog_id}`
  - `GET {API_BASE}/CatalogDatasets/catalogs`

- Datasets
  - `POST {API_BASE}/CatalogDatasets/datasets`
  - `GET {API_BASE}/CatalogDatasets/datasets/{dataset_id}`
  - `PUT {API_BASE}/CatalogDatasets/datasets/{dataset_id}`
  - `DELETE {API_BASE}/CatalogDatasets/datasets/{dataset_id}`
  - `GET {API_BASE}/CatalogDatasets/datasets`

- Distributions
  - `POST {API_BASE}/CatalogDatasets/distributions`
  - `GET {API_BASE}/CatalogDatasets/distributions/{distribution_id}`
  - `PUT {API_BASE}/CatalogDatasets/distributions/{distribution_id}`
  - `DELETE {API_BASE}/CatalogDatasets/distributions/{distribution_id}`
  - `GET {API_BASE}/CatalogDatasets/distributions`

- Dataset Offers
  - `POST {API_BASE}/CatalogDatasets/datasetoffers`
  - `GET {API_BASE}/CatalogDatasets/datasetoffers/{dataset_offer_id}`
  - `PUT {API_BASE}/CatalogDatasets/datasetoffers/{dataset_offer_id}`
  - `DELETE {API_BASE}/CatalogDatasets/datasetoffers/{dataset_offer_id}`
  - `GET {API_BASE}/CatalogDatasets/datasetoffers`

- Agents
  - `POST {API_BASE}/CatalogDatasets/agents`
  - `GET {API_BASE}/CatalogDatasets/agents/{agent_id}`
  - `PUT {API_BASE}/CatalogDatasets/agents/{agent_id}`
  - `DELETE {API_BASE}/CatalogDatasets/agents/{agent_id}`
  - `GET {API_BASE}/CatalogDatasets/agents`

- Participants
  - `POST {API_BASE}/CatalogDatasets/participants`
  - `GET {API_BASE}/CatalogDatasets/participants/{participant_id}`
  - `PUT {API_BASE}/CatalogDatasets/participants/{participant_id}`
  - `DELETE {API_BASE}/CatalogDatasets/participants/{participant_id}`
  - `GET {API_BASE}/CatalogDatasets/participants`

- Data Services
  - `POST {API_BASE}/CatalogDatasets/dataservices`
  - `GET {API_BASE}/CatalogDatasets/dataservices/{dataservice_id}`
  - `PUT {API_BASE}/CatalogDatasets/dataservices/{dataservice_id}`
  - `DELETE {API_BASE}/CatalogDatasets/dataservices/{dataservice_id}`
  - `GET {API_BASE}/CatalogDatasets/dataservices`

- Policies
  - `POST {API_BASE}/CatalogDatasets/policies`
  - `GET {API_BASE}/CatalogDatasets/policies/{policy_id}`
  - `PUT {API_BASE}/CatalogDatasets/policies/{policy_id}`
  - `DELETE {API_BASE}/CatalogDatasets/policies/{policy_id}`
  - `GET {API_BASE}/CatalogDatasets/policies`

- Policy Templates
  - `POST {API_BASE}/CatalogDatasets/policytemplates`
  - `GET {API_BASE}/CatalogDatasets/policytemplates/{policy_template_id}`
  - `PUT {API_BASE}/CatalogDatasets/policytemplates/{policy_template_id}`
  - `DELETE {API_BASE}/CatalogDatasets/policytemplates/{policy_template_id}`
  - `GET {API_BASE}/CatalogDatasets/policytemplates`

### Controlled vocabularies endpoints

- `POST {API_BASE}/ControlledVocabularies/import`
- `POST {API_BASE}/ControlledVocabularies/auto-import`
- `GET {API_BASE}/ControlledVocabularies`
- `GET {API_BASE}/ControlledVocabularies/{vocab_name}`
- `DELETE {API_BASE}/ControlledVocabularies/{vocab_name}`

Compatibility route:

- `/VocabularyHub/ControlledVocabularies`

## Validation and localization highlights

### Controlled vocabulary validation

`FieldVocabularyValidationService` validates profile-configured fields before persistence.

- input may be either a code or an IRI
- valid codes are normalized to canonical IRIs
- invalid values fail the request with validation errors
- the same profile-based rules are reused by CRUD and VocabularyHub flows

### Participant validation

`ParticipantService` adds three validation layers before create or update:

- duplicate detection by identifier notation and optional identifier scheme
- profile-driven controlled vocabulary validation
- SHACL validation using the participant shapes file and the validator service

Deletion is blocked when the participant is still referenced by catalogs, datasets, dataset offers, policies, or policy templates.

### VocabularyHub validation

`VocabularyHubValidationService` validates semantic resource fields used by ingestion and metadata update flows:

- `type`
- `resource_extension`
- `spatial` or `geographical_coverage`
- `language`
- `theme`
- `frequency`
- `status`

### Localized GET responses

When a CRUD endpoint supports the `lang` query parameter, `LocalizedResponseService` can:

- filter multilingual fields such as `preferredLabel` and `description`
- translate configured controlled vocabulary values from codes or IRIs into localized labels

This behavior is currently relevant for participant reads and can be extended to other entities defined in the active controlled vocabulary profile.

### Controlled vocabulary bootstrap

`controlled_vocabularies_bootstrap.py` can auto-import vocabularies from the resources folder at startup.

Key behaviors:

- supports explicit selection or profile-based selection
- skips vocabularies that already exist in the target graph
- routes vocabularies to custom, EU, IANA, or W3 graphs
- materializes `odrl22.rdf` into `rule_actions`, `constraint_left_operand`, and `constraint_operator`
- the same flow can be executed on demand through `POST /ControlledVocabularies/auto-import`

## Technologies

The following technologies are used in this project:

- FastAPI
- OpenAPI, available at `/docs` and `/redoc`
- Pybuilder for tests and packaging tasks
- Docker for local execution and deployment

## See docs

Check the [docs](docs/README.md) folder for more information about functionalities, architecture, design patterns, and configuration.

## Environment documentation

Environment variables are defined in the [.env](./.env) file. You can modify them according to your environment setup.
Examples: [Environment configuration](docs/environment_config.md)

## Getting Started

These instructions provide a complete local environment for the project. You can adapt them to your operating system and deployment needs.

### Pydoc

Consult the Pydoc documentation about the project's modules, classes, functions, and methods saved to HTML files.

#### Generate Pydoc

##### Generate HTML files

- `python -m pydoc -w <file_name_or_project_path>`

##### Serve the documentation browser

- `python -m pydoc -b`

Terminate the service by pressing `q`.

### Prerequisites

Docker execution:

- Docker Engine v20.10.17
- Docker Compose v2.6.1

Manual execution:

- Python 3.12.3
- Pip 25.1.1
- Install dependencies with `pip install -r .\requirements.txt`

### Dependencies to other resources

- File Manager and Validator microservices must be available
- Elasticsearch or OpenSearch must be available
- GraphDB, Fuseki, or Neptune must be available depending on `TRIPLESTORE_BACKEND`

### Start microservice

Option A: run `src\dev\wsgi.py` from the IDE.

Option B: run from a terminal:

```shell
python src\dev\wsgi.py
```

### Docker execution

#### Prerequisites

- Check the [.env](./.env) file and make sure the configured folders exist.
- Ensure `CONTAINER_ENV_PATH` points to the correct environment file.
- Check that `ELASTIC_OPENSEARCH_DATABASE` is set to either `elasticsearch` or `opensearch`.
- Create the `kf-net` network if needed with `docker network create -d bridge kf-net`.

#### Run

```shell
docker compose up --build -d
```

#### Additional information

- `docker ps`
- `docker logs --since=1h CONTAINER_NAME`

## Running the tests

All project functions have associated unit tests to verify behavior.

### Configuration files

- JSON schema files can be adjusted to generate models dynamically.
- Template-driven SPARQL queries can be adjusted depending on the schema files.
- Elastic mapping, RML mapping, and SHACL validation files can be adapted to field changes.

### Information about CI/CD pipelines

All developers should review:
`https://umane.emeal.nttdata.com/git/KFSEMBU/dsb/pipeline_modules/-/blob/main/README.md?ref_type=heads`
