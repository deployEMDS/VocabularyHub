# Repositories adapters package

This folder contains **triplestore adapter implementations**.

Adapters are responsible for executing SPARQL operations (SELECT/ASK/CONSTRUCT/UPDATE) against a concrete backend.

In this project they are used mainly by the **DCAT CRUD repositories** (Catalogs/Datasets/Distributions/DataServices/Agents/Policies) to talk directly to:
- **GraphDB** (default)
- **Apache Jena Fuseki** (optional)

The concrete adapter is selected at runtime using environment variables (see `adapter_factory.py`).

## Files and main classes

- `triplestore_adapter.py`
  - `TriplestoreAdapter` (abstract base class): common interface with:
    - `execute_query(...)` (SPARQL SELECT)
    - `execute_update(...)` (SPARQL UPDATE)
    - `execute_construct(...)` (SPARQL CONSTRUCT)
    - `execute_ask(...)` (SPARQL ASK)
    - `check_connection()`

- `graphdb_adapter.py`
  - `GraphDBAdapter`: implementation for GraphDB REST API.
  - Uses:
    - POST `{base}/repositories/{repo}` for SELECT/ASK/CONSTRUCT
    - POST `{base}/repositories/{repo}/statements` for UPDATE
  - Optional basic auth via `GRAPHDB_USER` / `GRAPHDB_PASSWORD` (wired through `config.crud.GRAPHDB_DETAILS`).

- `fuseki_adapter.py`
  - `FusekiAdapter`: implementation for Apache Jena Fuseki.
  - Uses:
    - POST `{base}/{dataset}/query` for SELECT/ASK/CONSTRUCT
    - POST `{base}/{dataset}/update` for UPDATE
  - Optional basic auth via `FUSEKI_USER` / `FUSEKI_PASSWORD`.

- `adapter_factory.py`
  - `get_triplestore_adapter(...)`: selects the adapter based on `TRIPLESTORE_BACKEND`:
    - `graphdb` (default)
    - `fuseki`

  Expected environment variables:
  - `TRIPLESTORE_BACKEND`: `graphdb` | `fuseki`

  GraphDB:
  - `GRAPHDB_HOST` (from `config.crud`) — commonly ends with `/repositories/`
  - `GRAPHDB_CATALOG_REPOSITORY_NAME` (from `config.crud`) or `repository_id` argument
  - Credentials from `crud.GRAPHDB_DETAILS`

  Fuseki:
  - `FUSEKI_BASE_URL` (default: `http://127.0.0.1:3030`)
  - `FUSEKI_DATASET` (default: `catalog`) or `repository_id` argument
  - `FUSEKI_USER`, `FUSEKI_PASSWORD` (optional)

- `__init__.py`
  - Package marker.

## Notes

- These adapters intentionally bypass the persistence microservice and communicate directly with the triplestore.
- Most repository SPARQL templates live in `config/queries/*_queries.py`.

