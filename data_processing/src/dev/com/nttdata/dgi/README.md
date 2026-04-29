# DGI (Data Governance & Integration) package

This README documents the `src/dev/com/nttdata/dgi` package. It summarizes the purpose of the package, the main subpackages and modules, the public classes and methods you will interact with, and implementation/usage notes.

Summary
- Purpose: provide the data ingestion, conversion, validation, integration and persistence glue for resources (DCAT, metadata, vocabularies, structured and unstructured resources). The package exposes factories, managers and updaters that are consumed by the REST API layer.

## Modules

- `data_processing.py`
  - Entry-level helper class `DataProcessing` (implements `IDataProcessing` and composes `SearchEngineManager`).
  - Methods:
    - `ingest(...)` (stub in this module; concrete logic in specific ingestion classes)
    - `integrate(...)` (stub)
  - Utilities:
    - `__process_mapping_response__` — helper to process persistence mapping responses (returns tuple with success and message).

- `idata_processing.py`
  - `IDataProcessing` interface defining the contract for processing classes:
    - `ingest(self, *args, **kwargs)`
    - `integrate(self, *args, **kwargs)`
  - Implementors include classes in `ingestion` and `integration` subpackages.


- `ingestion/`
  - Contains ingestion classes and a factory used to create the correct ingestion implementation based on resource type.
  - Key modules:
    - `data_ingestion_factory.py` — factory: `DataIngestionFactory.new(apis_details, resource_type)` returns an instance of the correct ingestion class:
      - `VocabularyIngestion` for ONTOLOGY/THESAURUS/TAXONOMY
      - `StructuredIngestion` for STRUCTURED
      - `UnstructuredIngestion` for UNSTRUCTURED
    - `data_ingestion.py` — base `DataIngestion` class (shared logic, abstract/parent methods)
    - `structured_ingestion.py`, `unstructured_ingestion.py`, `vocabulary_ingestion.py` — concrete ingestion implementations that implement `ingest(...)` and expose behavior used by the API layer.
  - Typical behavior: download or ingest a resource (possibly via `FileManagerRequest`), compute a resource hash, persist resource metadata to search index and/or pass resource to integration pipeline.

- `integration/`
  - Contains integration classes and `DataIntegrationFactory`.
  - Key modules:
    - `data_integration_factory.py` — factory: `DataIntegrationFactory.new(apis_details, resource_type)` returns integration class (`StructuredIntegration`, `VocabularyIntegration`, etc.).
    - `data_integration.py` — base `DataIntegration` class and concrete implementations (e.g., `StructuredIntegration`, `VocabularyIntegration`).
  - Typical behavior: run semantic transformations, apply SHACL, push to GraphDB and search index; returns status/message pairs.

- `persistence/`
  - Contains persistence helpers that encapsulate calls to the persistor API or OpenSearch.
  - Key modules:
    - `isearch_engine_manager.py` — interface `ISearchEngineManager` (defines skeleton methods for mapping and insert behaviors).
    - `search_engine_manager.py` — `SearchEngineManager` implementation used across updaters and integrators:
      - `__call_persistence__(rsql_query, request_url=None)` — send RSQL query to persistor API and return JSON.
      - `__prepare_elastic_resource__(resource)` — convert `Resource` object to JSON suitable for persistence.
      - `__insert_elastic_resource__(resource, elastic_details=None, index=None)` — insert resource into persistence using RSQL queries.
      - `__create_mapping_persistence__(elastic_details, index, mapping)` — create index mapping using the persistor.
      - `update_opensearch_resource(resource_hash, index)` — update existing resource in OpenSearch via opensearch-py.
  - These helpers centralize error handling and response processing for search/index persistence.

- `dcat_odrl_ingestion_integration/`
  - Contains the logic to integrate DCAT metadata together with ODRL rules and produce semantic artifacts.
  - Key module:
    - `dcat_integration.py` (class `DcatIntegration`) — orchestrates the integration flow:
      - Generates a DCAT resource id (file hash), creates index mappings, validates controlled vocabulary codes, checks existing DCAT, generates intermediate JSON, converts JSON->RML (via `RML` mapper), edits RML, validates SHACL, and persists results to search index and GraphDB.
      - `integrate(...) -> tuple[str, str, str]` returns `(status_name, message, file_hash)` where `status_name` follows `Status` enum (e.g., VALID/INVALID/ERROR).
    - `dcat_odrl_ingestion_integration.py` — base class that `DcatIntegration` extends; it holds shared helpers used across DCAT+ODRL flows.

- `update_dcat_odrl/`
  - Key module:
    - `dcat_odrl_updater.py` (class `DcatOdrlUpdater`) — extends `MetadataUpdater` and `SearchEngineManager`.
      - Responsibility: update DCAT metadata and ODRL policies for an existing resource.
      - Public methods:
        - `update(self, *args, **kwargs) -> tuple[str, str]` — main entry point, returns `(status, message)`.
        - `get_odrl_rule(resource_id, policy_id)` — helper to read an existing ODRL rule type from GraphDB via the persistor.
      - Internals: builds SPARQL DELETE/INSERT queries for DCAT/ODRL and delegates execution to `__execute_update_process__` in `MetadataUpdater` / persistence layer.

- `update_metadata/`
  - Key module:
    - `metadata_updater.py` (class `MetadataUpdater`) — performs metadata update operations in GraphDB:
      - Validates input codes using `ValidationRequest`.
      - Validates the resource exists in GraphDB.
      - Builds SPARQL templates for fields to DELETE/INSERT and executes them via persistor.
      - Public method: `updating(self, *args, **kwargs) -> tuple[str, str]` returns `(status, message)`.

- `request/`
  - Utilities to call external services (uploader, validator, SHACL validator, etc.).
  - Key modules:
    - `file_manager_request.py` — `FileManagerRequest` helpers to upload/download encoded resources to the uploader service (`__upload__(req_url, resource_encode, resource_type, resource_extension)`), returns path list or error message.
    - `validation_request.py` — `ValidationRequest` helpers to call remote validation APIs:
      - `__validation__(request_url, resource_dcat_content_hash)` — checks whether a DCAT content hash already exists.
      - `__validation_shacl__(data_graph_path, shacl_shapes_path, request_url)` — validates RDF graphs against SHACL shapes.
      - `validate_input_code(request_url, controlled_vocabulary, metadata_fields_in)` — validates controlled vocabulary codes via code validator and returns `(bool_or_none, message)`.
      - `quality_service_request.py(__call_quality_service__, generate_quality_report)` — helpers to call asynchronous Quality Service microservice to generate the metadata quality report.

- `converter/`
  - Contains conversion helpers used to transform JSON->RML->TTL or similar conversions.
  - Key modules:
    - `iconverter.py` — `IConverter` interface.
    - `converter.py` — concrete `Converter` stub/placeholder.
    - `rml_mapper.py` — `Mapper` class that executes an external RML mapper Java JAR to convert JSON+RML mapping into RDF (TTL). Main method: `execute_converter(output_converted_path) -> tuple[bool, str]`.

Data types and cross-cutting classes
- `Resource`, `Status`, `Stage`, `Phase`, `ResourceType`, `Odrl` and other domain classes are defined elsewhere (`com.nttdata.data_types.*`) and used across this package.
- `SchemeModelGenerator` is used extensively to generate runtime data classes and to extract controlled vocabulary and URI fields based on the JSON scheme files (DCAT, METADATA).
