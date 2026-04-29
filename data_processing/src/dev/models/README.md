# Models package

This folder contains the Pydantic models and lightweight helper classes used by the `data_processing` service.

Two model families coexist here:

1. CRUD models for DCAT, FOAF, ODRL, Participants, and controlled vocabularies
2. Legacy or internal models used by ingestion and integration pipelines

Most CRUD models follow the pattern `*Base`, `*Create`, `*Update`, `*Response`, and `*ListResponse`.

## CRUD models

### DCAT models

- `dcat_catalog.py`
  - `CatalogBase`, `CatalogCreate`, `CatalogUpdate`, `CatalogResponse`, `CatalogListResponse`

- `dcat_dataset.py`
  - `DatasetBase`, `DatasetCreate`, `DatasetUpdate`, `DatasetResponse`, `DatasetListResponse`

- `dcat_distribution.py`
  - `DistributionBase`, `DistributionCreate`, `DistributionUpdate`, `DistributionResponse`, `DistributionListResponse`
  - includes controlled vocabulary-backed fields such as `format`, `rights`, and `status`

- `dcat_dataservice.py`
  - `DataServiceBase`, `DataServiceCreate`, `DataServiceUpdate`, `DataServiceResponse`, `DataServiceListResponse`

- `dcat_dataset_offer.py`
  - `DatasetOfferBase`, `DatasetOfferCreate`, `DatasetOfferUpdate`, `DatasetOfferResponse`, `DatasetOfferListResponse`

### FOAF, Participants, and ODRL models

- `foaf_agent.py`
  - `AgentBase`, `AgentCreate`, `AgentUpdate`, `AgentResponse`, `AgentListResponse`

- `participant.py`
  - `ParticipantStatus`
  - `ParticipantIdentifier`
  - `ParticipantAddress`
  - `ParticipantContactPoint`
  - `ParticipantConnectorRef`
  - `ParticipantCreate`, `ParticipantUpdate`, `ParticipantResponse`, `ParticipantListResponse`

  Participant-specific notes:

  - `preferredLabel` is required and multilingual
  - `classification`, `purpose`, and selected address fields are validated against controlled vocabularies
  - reads can be localized through the `lang` query parameter in the API layer

- `odrl_policy.py`
  - `OdrlConstraint`, `OdrlRule`, `OdrlOfferBase`, `OdrlOfferCreate`, `OdrlOfferUpdate`, `OdrlOfferResponse`, `OdrlOfferListResponse`

- `odrl_policy_template.py`
  - policy template CRUD models for reusable ODRL offers

- `odrl.py`
  - legacy or simplified ODRL representations used by orchestration flows

### Controlled vocabulary models

- `controlled_vocabulary.py`
  - `ControlledVocabularyCreate`
  - `ControlledVocabularyResponse`
  - `ControlledVocabularyListItemResponse`
  - `ControlledVocabularyListResponse`
  - concept CRUD models such as `ConceptCreate`, `ConceptUpdate`, `ConceptResponse`, `ConceptListResponse`

- `controlled_vocabulary_entries.py`
  - `VocabularyEntry`
  - `VocabularyEntryListResponse`

These models are used by the controlled vocabulary API to expose vocabulary metadata and localized entry lists.

### Common helpers

- `localized_string.py`
  - `LocalizedString` represents a language-tagged value
  - used heavily by CRUD models and localized responses

- `delete_result.py`
  - common DELETE response body used by CRUD endpoints

### Pipeline and orchestration models

- `resource.py`
  - internal object used by ingestion and integration pipelines

- `resource_type.py`
  - enum describing supported semantic resource types

- `extractor_type.py`
  - enum used by metadata extraction logic

- `phase.py`, `stage.py`, `status.py`
  - enums modeling pipeline execution state

- `custom_metadata.py`, `dcat_metadata.py`
  - helper models used by metadata-oriented flows

## Validation and localization impact on models

The active controlled vocabulary profile maps selected model fields to vocabularies.

Examples:

- Participant
  - `classification`
  - `purpose`
  - `address.adminUnit1`
  - `address.adminUnit2`
  - `address.postCode`

- Semantic resources
  - `type`
  - `resource_extension`
  - `spatial`
  - `language`
  - `theme`
  - `frequency`
  - `status`

When GET endpoints receive `lang`, `LocalizedResponseService` can filter multilingual model fields and replace configured controlled vocabulary values with localized labels.
