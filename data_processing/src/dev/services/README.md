# Services package

This folder contains the service layer for the `data_processing` microservice.

Services encapsulate business logic and orchestrate:

- payload validation before persistence
- controlled vocabulary validation and normalization
- SHACL validation through the validation microservice
- referential integrity checks across graphs
- localized response shaping for supported GET endpoints
- calls to repositories and triplestore adapters

At a high level:

- FastAPI routers call services
- services call repositories
- repositories execute SPARQL through the configured adapter

## Main service groups

### DCAT, FOAF, and Participant CRUD services

- `catalog_service.py`
  - `CatalogService` manages `dcat:Catalog` CRUD
  - validates SHACL constraints and related dataset and publisher references
  - performs best-effort cascade delete for datasets

- `dataset_service.py`
  - `DatasetService` manages `dcat:Dataset` CRUD
  - validates SHACL constraints, duplicate identifiers, publisher and creator references, and distribution references
  - performs best-effort cascade delete for distributions

- `distribution_service.py`
  - `DistributionService` manages `dcat:Distribution` CRUD
  - validates SHACL constraints and optional references to data services and policies
  - performs best-effort cleanup of unreferenced linked resources

- `dataservice_service.py`
  - `DataServiceService` manages `dcat:DataService` CRUD
  - validates SHACL constraints and duplicate endpoint URLs
  - blocks deletion when still referenced by distributions

- `agent_service.py`
  - `AgentService` manages `foaf:Agent` CRUD
  - validates SHACL constraints
  - blocks deletion when still referenced as publisher

- `participant_service.py`
  - `ParticipantService` manages Participant CRUD
  - validates identifier uniqueness by notation and optional scheme URI
  - validates controlled vocabulary-backed participant fields through `FieldVocabularyValidationService`
  - validates the generated participant RDF graph through SHACL before create and update
  - localizes GET and list responses through `LocalizedResponseService` when `lang` is provided
  - blocks deletion when the participant is still referenced by catalogs, datasets, dataset offers, policies, or policy templates

### ODRL services

- `odrl_policy_service.py`
  - `OdrlPolicyService` manages policy CRUD for ODRL offers
  - validates target references and ODRL constraints
  - keeps reverse links in sync with distributions when possible

- `odrl_policy_template_service.py`
  - `OdrlPolicyTemplateService` manages policy template CRUD
  - applies the same controlled vocabulary and referential validation patterns used by policy services

### Controlled vocabulary services

- `controlled_vocabulary_service.py`
  - central business layer for vocabulary metadata and entry retrieval
  - supports vocabulary import, list, delete, entry list, existence checks, label resolution, and code-to-IRI resolution

- `controlled_vocabulary_importer.py`
  - parses RDF and supported XML sources
  - detects RDF/XML versus tabular XML
  - supports special handling for IANA media types XML
  - materializes `odrl22.rdf` into `rule_actions`, `constraint_left_operand`, and `constraint_operator`

- `controlled_vocabularies_bootstrap.py`
  - performs optional startup auto-import of selected vocabularies
  - can derive the selection from the active controlled vocabulary profile
  - skips existing vocabularies and routes imports to the correct target graph

### Validation and localization services

- `field_vocabulary_validation_service.py`
  - validates profile-configured fields against one or more candidate vocabularies
  - accepts either IRIs or codes
  - normalizes valid codes into canonical IRIs before persistence
  - supports nested field paths such as `address.admin_unit1`
  - handles ODRL-specific validation for action, left operand, operator, and dynamically mapped right operand values

- `vocabulary_hub_validation_service.py`
  - applies the same controlled vocabulary validation rules to ingestion and metadata update flows
  - validates `type`, `resource_extension`, `spatial`, `language`, `theme`, `frequency`, and `status`
  - normalizes resource extensions before validation

- `localized_response_service.py`
  - filters multilingual fields to the requested language with fallback
  - resolves configured controlled vocabulary fields from codes or IRIs to localized labels
  - is used by participant reads and can be reused by other CRUD services supported by the active profile

- `controlled_vocab_profile_utils.py`
  - helper utilities related to active profile vocabulary selection and bootstrap logic

- `i18n_utils.py`
  - language normalization and localized field filtering helpers used by response localization

## Active profile behavior

Controlled vocabulary validation and localization are driven by the active profile defined in `src/dev/config/controlled_vocab_profiles.py`.

Important mappings include:

- Participant
  - `classification`
  - `purpose`
  - `address.admin_unit1`
  - `address.admin_unit2`
  - `address.post_code`

- SemanticResource
  - `type`
  - `resource_extension`
  - `spatial`
  - `language`
  - `theme`
  - `frequency`
  - `status`

- ODRL
  - `action`
  - `left_operand`
  - `operator`
  - dynamically mapped `right_operand`

## Package init

- `__init__.py`
  - package marker
