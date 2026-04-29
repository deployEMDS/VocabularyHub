# Environment Configuration for Data Processing Microservice

This document lists the most relevant `.env` settings for the current `data_processing` implementation.

## External service endpoints

### Example using a domain

```dotenv
protocol=https
subdomain=test.
domain=nttdata-dataspacebuilder.com
instanceIP=16.171.86.185
URI="${protocol}://${subdomain}${domain}"

FILE_MANAGER_HOST="${URI}/api/file-manager/v1"
VALIDATOR_HOST="${URI}/api/validator/v1"
INFORMATION_EXTRACTION_HOST="${URI}/api/information-extraction/v1"
PERSISTOR_HOST="${URI}/api/persistence/v1/Persistence/persistence"

GRAPHDB_HOST="${URI}/graphdb/repositories/"

ELASTIC_OPENSEARCH_DATABASE="opensearch"
ELASTICSEARCH_HOST="${URI}/elasticsearch/"
OPENSEARCH_HOST="${URI}/opensearch/"

QUALITY_SERVICE_HOST="${URI}/api/v1"
```

### Example using host and port

```dotenv
protocol=http
instanceIP=16.171.86.185
URI="${protocol}://${instanceIP}"

FILE_MANAGER_HOST="${URI}:5100/file-manager/v1"
VALIDATOR_HOST="${URI}:5200/validator/v1"
INFORMATION_EXTRACTION_HOST="${URI}:5300/information-extraction/v1"
PERSISTOR_HOST="${URI}:5400/persistence/v1/Persistence/persistence"

GRAPHDB_HOST="${URI}:7200/repositories/"

ELASTIC_OPENSEARCH_DATABASE="opensearch"
ELASTICSEARCH_HOST="${URI}:9200"
OPENSEARCH_HOST="${URI}:9200"

QUALITY_SERVICE_HOST="${URI}:8000/api/v1"
```

## Triplestore backend for CRUD and controlled vocabularies

The CRUD layer executes SPARQL directly against a triplestore using an adapter.

```dotenv
TRIPLESTORE_BACKEND=graphdb

# GraphDB
GRAPHDB_HOST="http://127.0.0.1:7200/repositories/"
GRAPHDB_CATALOG_REPOSITORY_NAME="catalog"
GRAPHDB_CONTROLLED_VOCABS_REPOSITORY_NAME="controlledVocabularies"

# Apache Jena Fuseki
FUSEKI_BASE_URL="http://127.0.0.1:3030"
FUSEKI_DATASET="catalog"
FUSEKI_USER=""
FUSEKI_PASSWORD=""

# AWS Neptune
NEPTUNE_ENDPOINT="https://<neptune-endpoint>:8182"
NEPTUNE_REGION="<aws-region>"
NEPTUNE_IAM_ROLE_ARN=""
```

## Base graph URIs for CRUD entities

These variables must be absolute IRIs.

```dotenv
BASE_GRAPH_CATALOGS="http://data.dsb.com/catalog/"
BASE_GRAPH_DATASETS="http://data.dsb.com/dataset/"
BASE_GRAPH_DISTRIBUTIONS="http://data.dsb.com/distribution/"
BASE_GRAPH_DATA_SERVICES="http://data.dsb.com/dataservice/"
BASE_GRAPH_AGENTS="http://data.dsb.com/agent/"
BASE_GRAPH_PARTICIPANTS="http://data.dsb.com/participant/"
BASE_GRAPH_DATASET_OFFERS="http://data.dsb.com/dataset_offer/"
BASE_GRAPH_POLICIES="http://data.dsb.com/policy/"
BASE_GRAPH_POLICY_TEMPLATES="http://data.dsb.com/policy_template/"
```

## Controlled vocabulary graphs and profile selection

These settings control where imported vocabularies are stored and which profile drives validation and localization.

```dotenv
CONTROLLED_VOCAB_PROFILE=default
AUTO_IMPORT_CONTROLLED_VOCABS_ENABLED=true
AUTO_IMPORT_CONTROLLED_VOCABS_LIST=profile
I18N_FALLBACK_LANG=en

DSB_GRAPH_VOCABS_OP_EU="http://data.dsb.com/graph/reference/source/op-eu"
DSB_GRAPH_VOCABS_EXTENSIONS="http://data.dsb.com/graph/reference/extensions"
DSB_GRAPH_VOCABS_W3="http://data.dsb.com/graph/reference/source/w3"
DSB_GRAPH_VOCABS_IANA="http://data.dsb.com/graph/reference/source/iana"
```

Notes:

- `CONTROLLED_VOCAB_PROFILE` selects the profile from `controlled_vocab_profiles.py`
- `AUTO_IMPORT_CONTROLLED_VOCABS_LIST` can be an explicit list or `profile`
- `I18N_FALLBACK_LANG` is used by localized GET responses when the requested language is not available

## Participant SHACL validation settings

Participants are validated through SHACL before create and update operations.

Relevant runtime values are derived in `constants.py`, but these are the important concepts to keep aligned:

- validator endpoint configuration must point to a reachable validation microservice
- the participant shape file is resolved from `src/dev/resources/shacl/dcatap_crud/participant_shape.ttl`
- temporary Turtle files are generated during validation and removed afterwards

## Search backend selection

```dotenv
ELASTIC_OPENSEARCH_DATABASE=opensearch
ELASTICSEARCH_HOST="http://127.0.0.1:9200"
OPENSEARCH_HOST="http://127.0.0.1:9200"
```

Choose the backend that matches your deployment and ensure the associated mapping files under `src/dev/resources/elasticsearch/` are available.
