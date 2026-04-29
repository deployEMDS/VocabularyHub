# Configuration package

This folder contains runtime configuration, constants, messages, query templates, profile mappings, and connection settings used across the `data_processing` project.

Its purpose is to centralize:

- environment-driven configuration
- API metadata and route prefixes
- paths to resources, mappings, and SHACL shapes
- triplestore and search backend connection details
- CRUD query templates
- controlled vocabulary profile mappings
- user-facing messages

## Main files

### `constants.py`

Primary runtime configuration module.

Responsibilities include:

- loading environment variables from `.env`
- defining API metadata and global project settings
- defining filesystem paths to resources, RML files, SHACL shapes, and schemas
- defining service endpoint URLs for File Manager, Validator, Extractor, and related services
- exposing constants used by orchestration and CRUD flows

Relevant entries for the current documentation scope include:

- `PARTICIPANT_SHACL_SHAPE_PATH`
- `PARTICIPANT_TEMP_DIR`
- `PARTICIPANT_TEMP_TTL_PREFIX`
- `PARTICIPANT_TEMP_TTL_SUFFIX`
- `CONTROLLED_VOCAB_PROFILE`
- `AUTO_IMPORT_CONTROLLED_VOCABS_ENABLED`
- `AUTO_IMPORT_CONTROLLED_VOCABS_LIST`
- `I18N_FALLBACK_LANG`

### `constants_examples.py`

Example payloads and values used by OpenAPI examples and tests.

### `constants_test.py`

Test-only constants used to keep tests independent from runtime configuration.

### `messages.py`

Centralized user-facing and log messages used by API routers and services.

### `crud.py`

Connection and graph configuration for persistence layers.

Important entries include:

- `TRIPLESTORE_BACKEND`
- GraphDB, Fuseki, and Neptune connection settings
- `GRAPHDB_CATALOG_REPOSITORY_NAME`
- `GRAPHDB_CONTROLLED_VOCABS_REPOSITORY_NAME`
- `BASE_GRAPH_PARTICIPANTS`
- `DSB_GRAPH_VOCABS_OP_EU`
- `DSB_GRAPH_VOCABS_EXTENSIONS`
- `DSB_GRAPH_VOCABS_W3`
- `DSB_GRAPH_VOCABS_IANA`

These values are used by participant repositories, controlled vocabulary repositories, and startup bootstrap logic.

### `controlled_vocab_profiles.py`

Defines the active controlled vocabulary mappings used by validation and localization.

Current profiles include at least:

- `default`
- `eu`

The profile controls which vocabularies are used for:

- Participant fields such as `classification`, `purpose`, and address fields
- semantic resource fields such as `type`, `resource_extension`, `spatial`, `language`, `theme`, `frequency`, and `status`
- ODRL fields such as `action`, `left_operand`, `operator`, and dynamically mapped `right_operand`

### `queries/`

SPARQL query templates used by the CRUD repositories.

Modules include:

- `agents_queries.py`
- `catalogs_queries.py`
- `datasets_queries.py`
- `distributions_queries.py`
- `data_services_queries.py`
- `dataset_offers_queries.py`
- `participants_queries.py`
- `policies_queries.py`
- `policy_templates_queries.py`
- `controlled_vocabularies_queries.py`

These templates power entity CRUD operations, referential integrity checks, duplicate detection, vocabulary retrieval, and localized entry resolution.

## Configuration areas to review when enabling the new features

### Participants

Review:

- `BASE_GRAPH_PARTICIPANTS`
- `PARTICIPANT_SHACL_SHAPE_PATH`
- validator endpoint configuration in `constants.py`

### Controlled vocabularies

Review:

- `GRAPHDB_CONTROLLED_VOCABS_REPOSITORY_NAME`
- `DSB_GRAPH_VOCABS_OP_EU`
- `DSB_GRAPH_VOCABS_EXTENSIONS`
- `DSB_GRAPH_VOCABS_W3`
- `DSB_GRAPH_VOCABS_IANA`
- `CONTROLLED_VOCAB_PROFILE`
- `AUTO_IMPORT_CONTROLLED_VOCABS_ENABLED`
- `AUTO_IMPORT_CONTROLLED_VOCABS_LIST`

### Localized GET responses

Review:

- `CONTROLLED_VOCAB_PROFILE`
- `I18N_FALLBACK_LANG`

These settings determine which fields are translated and which fallback language is used when the requested language is not present.
