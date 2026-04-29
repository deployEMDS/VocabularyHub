# Documentation Overview

This folder holds additional project notes for the `data_processing` microservice.

## Microservice purpose

The current documentation covers the backend implemented in `data_processing`, including:

- ingestion and integration flows for vocabularies and DCAT plus ODRL resources
- CRUD APIs for DCAT, FOAF, ODRL, and Participants
- controlled vocabulary import and startup bootstrap
- field-level validation against controlled vocabularies
- language-aware GET responses that translate controlled values into localized labels

## Main documented topics

### Participants CRUD

Participants are exposed under `/data-processing/v1/CatalogDatasets/participants`.

Documented behavior includes:

- create, read, update, delete, and list operations
- duplicate detection by identifier notation and optional scheme
- SHACL validation on create and update
- controlled vocabulary validation for participant-specific fields
- localized GET responses through `lang`
- delete protection when participants are still referenced

### Controlled vocabularies

Controlled vocabularies are exposed under `/data-processing/v1/ControlledVocabularies`.

Documented behavior includes:

- import from `download_url` or uploaded `file`
- support for RDF and supported XML formats
- semantic origin routing to custom, EU, IANA, or W3 graphs
- localized entry listing through `lang`
- special ODRL materialization from `odrl22.rdf`
- optional startup auto-import through the bootstrap service

### Validation services

- `FieldVocabularyValidationService`
  - validates profile-configured entity fields against one or more vocabularies
  - accepts codes or IRIs
  - normalizes codes into IRIs before persistence
- `VocabularyHubValidationService`
  - applies the same validation rules to ingestion and metadata update flows
  - validates `type`, `resource_extension`, `spatial`, `language`, `theme`, `frequency`, and `status`
- `LocalizedResponseService`
  - filters multilingual values to the requested language
  - translates configured controlled vocabulary fields to localized labels

## Folder structure

This repository follows the structure below, simplified to the main folders and files:

```text
data_processing/
|-- build.py
|-- docker-compose.yml
|-- Dockerfile
|-- README.md
|-- requirements.txt
|-- corpus/
|-- docs/
|-- img/
`-- src/
    `-- dev/
        |-- apis/
        |-- app/
        |-- com/
        |-- config/
        |-- models/
        |-- repositories/
        |-- resources/
        |-- services/
        |-- test/
        |-- main.py
        `-- wsgi.py
```

## Related components

- Validation Microservice
- File Manager Microservice
- OpenSearch or Elasticsearch
- GraphDB, Fuseki, or Neptune

## Additional notes

- `architecture.md` describes the internal and external architecture.
- `data_processing_swagger.md` contains an OpenAPI export for the service.
- `environment_config.md` describes runtime configuration.
- `usage_example.md` contains copy-and-paste request examples.
- controlled vocabularies can be bootstrapped according to the active profile defined in `src/dev/config/controlled_vocab_profiles.py`

## See docs

- [architecture.md](./architecture.md) - internal and external architecture
- [environment_config.md](./environment_config.md) - runtime configuration
- [usage_example.md](./usage_example.md) - quick request examples
- [README.md](../README.md) - top-level overview
- [data_processing_swagger.md](./data_processing_swagger.md) - API export
- [API Package README](../src/dev/apis/README.md) - API layer overview
- [Models Package README](../src/dev/models/README.md) - Pydantic models
- [Repositories Package README](../src/dev/repositories/README.md) - persistence layer
- [Repositories Adapters README](../src/dev/repositories/adapters/README.md) - triplestore adapters
- [Services Package README](../src/dev/services/README.md) - business logic layer
- [Validation Package README](../src/dev/com/nttdata/validation/README.md) - SHACL graph builders
- [DGI Package README](../src/dev/com/nttdata/dgi/README.md) - orchestration layer
- [Resources Package README](../src/dev/resources/README.md) - static resources
- [Test Package README](../src/dev/test/README.md) - tests
