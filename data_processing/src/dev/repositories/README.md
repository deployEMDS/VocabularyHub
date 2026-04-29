# Repositories package

This folder contains the persistence layer for the `data_processing` service.

Repositories implement CRUD and lookup operations against a triplestore through a pluggable adapter.

At a high level:

- FastAPI routers call services
- services call repositories
- repositories build and execute SPARQL using the configured adapter

## Core utilities

- `base_repository.py`
  - common helpers for URI generation, timestamp handling, pagination, existence checks, and SPARQL escaping

- `sparql_literals.py`
  - helpers to serialize and parse multilingual RDF literals represented as `LocalizedString`

## CRUD repositories

Each repository targets a named graph and base URI prefix defined in `config.crud`.

### DCAT and FOAF repositories

- `catalog_repository.py`
  - CRUD for `dcat:Catalog`

- `dataset_repository.py`
  - CRUD for `dcat:Dataset`
  - includes duplicate detection by identifier and reference checks for distributions

- `distribution_repository.py`
  - CRUD for `dcat:Distribution`
  - includes integrity helpers for linked data services and policies

- `dataservice_repository.py`
  - CRUD for `dcat:DataService`

- `dataset_offer_repository.py`
  - CRUD for dataset offer entities

- `agent_repository.py`
  - CRUD for `foaf:Agent`

### Participant repository

- `participant_repository.py`
  - CRUD for participant entities
  - supports duplicate lookup by identifier notation and optional scheme URI
  - supports localized retrieval used by `ParticipantService`
  - exposes reference counters used to block deletion when a participant is still in use

The participant repository is used together with `BASE_GRAPH_PARTICIPANTS` and the main catalog repository connection.

### ODRL repositories

- `odrl_policy_repository.py`
  - CRUD for ODRL offers stored in the policies graph
  - handles nested rules and constraints

- `odrl_policy_template_repository.py`
  - CRUD for reusable policy templates

### Controlled vocabulary repository

- `controlled_vocabulary_repository.py`
  - persists imported vocabulary metadata and graph content
  - lists vocabularies and localized entries
  - checks concept existence by IRI or code
  - resolves code to IRI
  - resolves labels by IRI with requested and fallback language support
  - detects duplicates within the correct target graph

This repository is used by:

- `ControlledVocabularyService`
- `FieldVocabularyValidationService`
- `VocabularyHubValidationService`
- `LocalizedResponseService`
- startup bootstrap logic

## Query template dependencies

Most repositories rely on templates under `src/dev/config/queries/`.

Relevant modules for the new documentation scope include:

- `participants_queries.py`
- `controlled_vocabularies_queries.py`

## Adapters

See:

- `repositories/adapters/README.md`

Adapters abstract GraphDB, Fuseki, and Neptune so repositories can stay focused on domain-specific SPARQL behavior.
