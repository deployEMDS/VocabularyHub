# Usage examples

This document provides quick copy-and-paste examples for the most common endpoints of the `data_processing` service.

Notes before you start:

- replace `{API_BASE}` with your API base URL, for example `http://localhost:5000/data-processing/v1`
- on Windows, it is usually easier to store request bodies in JSON files and use `-d @payload.json`
- the live OpenAPI docs remain available at `{API_BASE}/docs` and `{API_BASE}/redoc`

## 1. Healthcheck

```bash
curl --location --request GET "{API_BASE}/health-check"
```

## 2. VocabularyHub create_resource

Use this endpoint to ingest and integrate a semantic resource.

```bash
curl --location --request POST "{API_BASE}/VocabularyHub/create_resource" \
  --header "Content-Type: application/json" \
  --data @payload.json
```

Minimal example payload:

```json
{
  "type": "ONTOLOGY",
  "resource_url": "https://raw.githubusercontent.com/isa-camss/CAV/refs/heads/master/ttl/cav_tbox.ttl",
  "resource_name": [
    {
      "text": "CAV",
      "lang": "en"
    }
  ],
  "resource_version": "1.3.0",
  "resource_extension": "ttl",
  "metadata": {
    "language": ["eng"],
    "description": [
      {
        "lang": "en",
        "text": "Core Assessment Vocabulary."
      }
    ]
  }
}
```

`VocabularyHubValidationService` can validate fields such as `type`, `resource_extension`, `language`, `theme`, `frequency`, `status`, and `spatial` during this flow.

## 3. VocabularyHub update_resource

```bash
curl --location --request PUT "{API_BASE}/VocabularyHub/update_resource" \
  --header "Content-Type: application/json" \
  --data @update_metadata.json
```

Example payload:

```json
{
  "resource_id": "<resource-id>",
  "metadata": {
    "language": ["eng"],
    "theme": ["http://publications.europa.eu/resource/authority/data-theme/GOVE"],
    "description": "Updated description"
  }
}
```

## 4. Participants CRUD

### Create participant

```bash
curl --location --request POST "{API_BASE}/CatalogDatasets/participants" \
  --header "Content-Type: application/json" \
  --data @participant_create.json
```

Example payload:

```json
{
  "status": "ACTIVE",
  "identifier": [
    {
      "notation": "E05068901",
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaria de Estado de Digitalizacion e Inteligencia Artificial"
    },
    {
      "language": "en",
      "value": "Secretary of State for Digitalization and Artificial Intelligence"
    }
  ],
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "address": {
    "adminUnit1": "ESP",
    "adminUnit2": "MADRID",
    "postCode": "28021",
    "postName": "Madrid",
    "fullAddress": "C/ Poeta Joan Maragall 41, Madrid"
  },
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "telephone": "+34911596128",
    "openingHours": "Mo-Fr 09:00-14:00"
  }
}
```

Notes:

- controlled vocabulary-backed fields may be provided as codes or IRIs
- valid codes are normalized to IRIs before persistence
- create and update also perform SHACL validation

### Get participant with localization

```bash
curl --location --request GET "{API_BASE}/CatalogDatasets/participants/{participant_id}?lang=en"
```

### List participants with localization

```bash
curl --location --request GET "{API_BASE}/CatalogDatasets/participants?page=1&size=10&lang=es"
```

### Update participant

```bash
curl --location --request PUT "{API_BASE}/CatalogDatasets/participants/{participant_id}" \
  --header "Content-Type: application/json" \
  --data @participant_update.json
```

### Delete participant

```bash
curl --location --request DELETE "{API_BASE}/CatalogDatasets/participants/{participant_id}"
```

Deletion returns `409` if the participant is still referenced by other entities.

## 5. Controlled vocabularies

### Import from URL

```bash
curl --location --request POST "{API_BASE}/ControlledVocabularies/import" \
  --form "vocab_name=languages-eu" \
  --form "download_url=https://publications.europa.eu/resource/authority/language?format=application/rdf+xml" \
  --form "source=eu"
```

### Import from local file

```bash
curl --location --request POST "{API_BASE}/ControlledVocabularies/import" \
  --form "vocab_name=organizationtypes-eu" \
  --form "file=@organizationtypes.xml"
```

### List vocabularies

```bash
curl --location --request GET "{API_BASE}/ControlledVocabularies?page=1&size=10"
```

### Get localized vocabulary entries

```bash
curl --location --request GET "{API_BASE}/ControlledVocabularies/languages-eu?lang=es&page=1&size=20"
```

### Delete a vocabulary

```bash
curl --location --request DELETE "{API_BASE}/ControlledVocabularies/languages-eu"
```

### Trigger on-demand controlled vocabularies auto-import

```bash
curl --location --request POST "{API_BASE}/ControlledVocabularies/auto-import"
```

Notes:

- use either `download_url` or `file`, not both
- `odrl22.rdf` is a special case and materializes three vocabularies
- tabular XML imports are normalized to SKOS concepts using `dct:identifier`

## 6. Dataset CRUD example

```bash
curl --location --request POST "{API_BASE}/CatalogDatasets/datasets" \
  --header "Content-Type: application/json" \
  --data @dataset_create.json
```

```bash
curl --location --request GET "{API_BASE}/CatalogDatasets/datasets/{dataset_id}?lang=en"
```

```bash
curl --location --request GET "{API_BASE}/CatalogDatasets/datasets?page=1&size=10&lang=en"
```

## 7. Policy CRUD example

```bash
curl --location --request POST "{API_BASE}/CatalogDatasets/policies" \
  --header "Content-Type: application/json" \
  --data @policy_create.json
```

```bash
curl --location --request GET "{API_BASE}/CatalogDatasets/policies/{policy_id}?include_details=true&lang=en"
```

## 8. Python example for participant GET

```python
import requests

BASE = "http://localhost:5000/data-processing/v1"
participant_id = "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000"

resp = requests.get(
    f"{BASE}/CatalogDatasets/participants/{participant_id}",
    params={"lang": "en"},
)
print(resp.status_code)
print(resp.json())
```
