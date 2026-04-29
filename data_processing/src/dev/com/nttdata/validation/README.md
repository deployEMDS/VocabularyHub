# Validation package

This package contains helpers used by `data_processing` to integrate with the external validation microservice.

Its main responsibility is to build minimal RDF graphs from incoming CRUD payloads, serialize them as Turtle, and validate them against SHACL shapes before persistence.

## Main module

### `shacl_validator.py`

This module defines graph builder functions. Each function:

- accepts a CRUD payload, usually a Pydantic model
- creates an `rdflib.Graph`
- inserts the triples required by the corresponding SHACL shape
- returns the graph so the caller can serialize it and send it to the validation microservice

Namespaces used include DCAT, DCT, DCAT-AP, FOAF, ADMS, RDF, and XSD.

## Graph builders currently relevant to CRUD

- `build_catalog_graph(...)`
  - builds a minimal `dcat:Catalog` graph

- `build_dataset_graph(...)`
  - builds a minimal `dcat:Dataset` graph

- `build_distribution_graph(...)`
  - builds a minimal `dcat:Distribution` graph

- `build_dataservice_graph(...)`
  - builds a minimal `dcat:DataService` graph

- `build_agent_graph(...)`
  - builds a minimal `foaf:Agent` graph

- `build_participant_graph(...)`
  - builds a minimal participant graph used by `ParticipantService`
  - includes participant-specific fields such as identifiers, multilingual labels and descriptions, classification, purpose, address, contact point, and connector relations as required by the participant shape

## Where it is used

These graph builders are called by CRUD services before writing to the triplestore:

- build graph
- serialize to Turtle
- send to validation microservice
- accept or reject the payload based on the SHACL result

For participants, this happens inside `ParticipantService` before create and update operations.

## SHACL shape locations

CRUD-related SHACL shapes live under:

- `src/dev/resources/shacl/dcatap_crud/`

Current files include:

- `agent_shape.ttl`
- `catalog_shape.ttl`
- `dataset_shape.ttl`
- `distribution_shape.ttl`
- `dataservice_shape.ttl`
- `dataset_offer_shape.ttl`
- `odrl_policy_template_shape.ttl`
- `participant_shape.ttl`

## Relationship with controlled vocabulary validation

This package is focused on SHACL graph generation and validation.

It complements, but does not replace:

- `FieldVocabularyValidationService`, which validates profile-configured controlled vocabulary fields and normalizes codes into IRIs
- `VocabularyHubValidationService`, which applies the same vocabulary rules to ingestion and metadata update flows

Together, these layers ensure that payloads are both structurally valid and semantically aligned with the configured vocabularies.
