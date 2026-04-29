# Resources package

This folder contains static runtime assets used by the `data_processing` microservice.

The resources in this package support:

- ingestion and integration pipelines
- CRUD payload validation through SHACL
- RML-based RDF generation
- search index mappings
- dynamic schema generation
- controlled vocabulary bootstrap and import

## Main folders

### `elasticsearch/`

Index mapping templates used for OpenSearch or Elasticsearch.

Key files:

- `dcat_mapping.json`
- `rsc_mapping.json`

These mappings are consumed by the persistence helpers when creating or validating indices.

### `entity_matching/`

Configuration files for entity matching and record linkage scenarios.

Key file:

- `entity_attributes.json`

### `integration/`

Assets used by integration flows, including per-flow RML artifacts.

### `metadata/`

Schema and extraction assets used by ingestion and metadata update flows.

Key files:

- `dcat_fields.json`
- `metadata_fields.json`
- `extract_metadata.yaml`

These files drive dynamic model generation and metadata extraction behavior.

### `queries/`

Template files used by metadata update and SPARQL generation helpers.

Key file:

- `queries_template.json`

### `rml/`

RML mapping templates and helper assets used to transform JSON payloads into RDF.

Key files include:

- `bregdcat_rml.ttl`
- `bregdcat_rml_v2.ttl`
- `dcatap_rml_v1.ttl`
- `dcat_odrl_rml_v1.ttl`
- `rml_rules_eurio_KF_version.ttl`
- `lib/`

These mappings are used by the converter layer during ingestion and integration.

### `shacl/`

SHACL shapes used by both orchestration and CRUD validation flows.

Key folders:

- `bregdcat/`
- `dcatap/`
- `dcatap_crud/`
- `generic/`
- `odrl/`

#### `shacl/dcatap_crud/`

This folder contains the shapes used by CRUD services before data is written to the triplestore.

Current shapes include:

- `agent_shape.ttl`
- `catalog_shape.ttl`
- `dataset_shape.ttl`
- `distribution_shape.ttl`
- `dataservice_shape.ttl`
- `dataset_offer_shape.ttl`
- `odrl_policy_template_shape.ttl`
- `participant_shape.ttl`

These files are referenced from `config/constants.py` and used by the CRUD service layer through the validation microservice.

## Controlled vocabulary resources

Controlled vocabularies used by validation and localization are stored under the resources root and can be auto-imported by `controlled_vocabularies_bootstrap.py`.

Relevant conventions:

- `custom_vocabs/` for custom XML vocabularies
- `eu_vocabs/` for RDF vocabularies from EU sources
- `iana-vocabs/` for IANA XML vocabularies
- `w3.org-vocabs/` or `w3-vocabs/` for W3 vocabularies

Special case:

- `odrl22.rdf` is materialized into `rule_actions`, `constraint_left_operand`, and `constraint_operator`

## How these resources are used

- CRUD services serialize payloads into RDF and validate them against SHACL shapes from `shacl/dcatap_crud/`
- ingestion and integration flows use schemas from `metadata/` and mappings from `rml/`
- repositories and update services use templates from `queries/`
- controlled vocabulary services and bootstrap use the controlled vocabulary resource folders during import and startup
