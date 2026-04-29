---
title: DataProcessing.API v1
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---


<h1 id="dataprocessing-api">DataProcessing.API v1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

This service is responsible for orchestrating the core backend processes within the dataspace environment. Its main functions include the ingestion, validation, metadata extraction, and persistence of resources, ensuring that datasets and vocabularies are properly processed and made available for discovery and consumption.

<h1 id="dataprocessing-api-vocabularyhub">VocabularyHub</h1>

This API manages the creation and maintenance of semantic resources.

## ingestion_integration_data_processing_v1_VocabularyHub_create_resource_post

<a id="opIdingestion_integration_data_processing_v1_VocabularyHub_create_resource_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/VocabularyHub/create_resource \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/VocabularyHub/create_resource HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "type": "ONTOLOGY",
  "resource_url": "http://publications.europa.eu/resource/distribution/eurio/20260204-0/ttl/owl/EURIO.ttl",
  "resource_file": "",
  "title": [
    {
      "language": "en",
      "value": "EURIO"
    }
  ],
  "version_info": "1.0.0",
  "resource_extension": "TTL",
  "metadata": {
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      }
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      }
    ],
    "author": [
      "European Commission"
    ],
    "publisher": "European Commission",
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "spatial": [
      "EUR"
    ],
    "theme": [
      "GOVE"
    ],
    "frequency": "NEVER",
    "language": [
      "ENG"
    ],
    "status": "COMPLETED",
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ]
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/VocabularyHub/create_resource',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/VocabularyHub/create_resource',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/VocabularyHub/create_resource', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/VocabularyHub/create_resource', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/VocabularyHub/create_resource");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/VocabularyHub/create_resource", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/VocabularyHub/create_resource`

*Class to execute data ingestion_integration process.*

> Body parameter

```json
{
  "type": "ONTOLOGY",
  "resource_url": "http://publications.europa.eu/resource/distribution/eurio/20260204-0/ttl/owl/EURIO.ttl",
  "resource_file": "",
  "title": [
    {
      "language": "en",
      "value": "EURIO"
    }
  ],
  "version_info": "1.0.0",
  "resource_extension": "TTL",
  "metadata": {
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      }
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      }
    ],
    "author": [
      "European Commission"
    ],
    "publisher": "European Commission",
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "spatial": [
      "EUR"
    ],
    "theme": [
      "GOVE"
    ],
    "frequency": "NEVER",
    "language": [
      "ENG"
    ],
    "status": "COMPLETED",
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ]
  }
}
```

<h3 id="ingestion_integration_data_processing_v1_vocabularyhub_create_resource_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[IngestionIntegrationInput](#schemaingestionintegrationinput)|true|none|

> Example responses

> 200 Response

```json
{
  "status": "VALID",
  "message": "Ingestion_integration successful. All resources were ingested and integrated.",
  "resource_hash": "string"
}
```

<h3 id="ingestion_integration_data_processing_v1_vocabularyhub_create_resource_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[IngestionIntegrationOutput](#schemaingestionintegrationoutput)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_metadata_data_processing_v1_VocabularyHub_update_resource_put

<a id="opIdupdate_metadata_data_processing_v1_VocabularyHub_update_resource_put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/VocabularyHub/update_resource \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/VocabularyHub/update_resource HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "resource_id": "26c9c211-d693-434f-9155-27689becc8c8",
  "metadata": {
    "title": [
      {
        "language": "en",
        "value": "Core Assessment Vocabulary (CAV)."
      },
      {
        "language": "eu",
        "value": "Oinarrizko ebaluazio hiztegia (CAV)."
      },
      {
        "language": "es",
        "value": "Vocabulario básico de evaluación (CAV)."
      }
    ],
    "version_info": "6.2.0",
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      }
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      }
    ],
    "author": [
      "European Commission"
    ],
    "publisher": "European Commission",
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "spatial": [
      "EUR"
    ],
    "theme": [
      "GOVE"
    ],
    "frequency": "NEVER",
    "language": [
      "ENG"
    ],
    "status": "COMPLETED",
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ]
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/VocabularyHub/update_resource',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/VocabularyHub/update_resource',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/VocabularyHub/update_resource', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/VocabularyHub/update_resource', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/VocabularyHub/update_resource");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/VocabularyHub/update_resource", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/VocabularyHub/update_resource`

*Class to execute metadata updating process.*

> Body parameter

```json
{
  "resource_id": "26c9c211-d693-434f-9155-27689becc8c8",
  "metadata": {
    "title": [
      {
        "language": "en",
        "value": "Core Assessment Vocabulary (CAV)."
      },
      {
        "language": "eu",
        "value": "Oinarrizko ebaluazio hiztegia (CAV)."
      },
      {
        "language": "es",
        "value": "Vocabulario básico de evaluación (CAV)."
      }
    ],
    "version_info": "6.2.0",
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      }
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      }
    ],
    "author": [
      "European Commission"
    ],
    "publisher": "European Commission",
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "spatial": [
      "EUR"
    ],
    "theme": [
      "GOVE"
    ],
    "frequency": "NEVER",
    "language": [
      "ENG"
    ],
    "status": "COMPLETED",
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ]
  }
}
```

<h3 id="update_metadata_data_processing_v1_vocabularyhub_update_resource_put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MetadataUpdateInput](#schemametadataupdateinput)|true|none|

> Example responses

> 200 Response

```json
{
  "status": "VALID",
  "message": "Metadata updated successfully."
}
```

<h3 id="update_metadata_data_processing_v1_vocabularyhub_update_resource_put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[MetadataUpdateResponse](#schemametadataupdateresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_metadata_data_processing_v1_VocabularyHub_get

<a id="opIdlist_metadata_data_processing_v1_VocabularyHub_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/VocabularyHub \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/VocabularyHub HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/VocabularyHub',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/VocabularyHub',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/VocabularyHub', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/VocabularyHub', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/VocabularyHub");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/VocabularyHub", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/VocabularyHub`

*List all Resources*

Retrieve a paginated list of all Resources stored in the triplestore.

<h3 id="list_metadata_data_processing_v1_vocabularyhub_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number|
|size|query|integer|false|Page size|
|lang|query|any|false|Filter by language code (e.g., 'en', 'es')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "identifier": "550e8400-e29b-41d4-a716-446655440000",
      "metadata": {
        "access_url": "http://data.dsb.com/ontology/DSD_1.0.0",
        "author": [
          "European Commission"
        ],
        "description": [
          {
            "language": "en",
            "value": "This module provides the definitions for the Core Assessment Vocabulary."
          },
          {
            "language": "es",
            "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
          },
          {
            "language": "eu",
            "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
          }
        ],
        "documentation": [
          "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
        ],
        "download_url": "https://ibestat.es/edatos/apis/structural-resources/v1.0/datastructures/IBESTAT/DSD_000001A_00001/01.000.xml",
        "frequency": "http://publications.europa.eu/resource/authority/frequency/NEVER",
        "language": [
          "http://publications.europa.eu/resource/authority/language/ENG"
        ],
        "license": "http://creativecommons.org/licenses/by-sa/4.0/",
        "modified": "2026-02-23",
        "publisher": "European Commission",
        "spatial": [
          "http://publications.europa.eu/resource/authority/country/EUR"
        ],
        "status": "http://publications.europa.eu/resource/authority/distribution-status/COMPLETED",
        "theme": [
          "http://publications.europa.eu/resource/authority/data-theme/GOVE"
        ],
        "version_notes": [
          {
            "language": "en",
            "value": "Version notes test."
          },
          {
            "language": "es",
            "value": "Prueba de notas de versión."
          },
          {
            "language": "eu",
            "value": "Proba-oharrak."
          }
        ]
      },
      "resource_extension": "https://www.iana.org/assignments/media-types/application/xml",
      "title": [
        {
          "language": "en",
          "value": "DSD"
        }
      ],
      "version_info": "1.0.0"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_metadata_data_processing_v1_vocabularyhub_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[CustomMetadataListResponse](#schemacustommetadatalistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_metadata_data_processing_v1_VocabularyHub__resource_id__get

<a id="opIdget_metadata_data_processing_v1_VocabularyHub__resource_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/VocabularyHub/{resource_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/VocabularyHub/{resource_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/VocabularyHub/{resource_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/VocabularyHub/{resource_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/VocabularyHub/{resource_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/VocabularyHub/{resource_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/VocabularyHub/{resource_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/VocabularyHub/{resource_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/VocabularyHub/{resource_id}`

*Get Resource by ID*

<h3 id="get_metadata_data_processing_v1_vocabularyhub__resource_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|resource_id|path|string(uuid)|true|none|
|lang|query|any|false|Filter by language code (e.g., 'en', 'es')|

> Example responses

> 200 Response

```json
{
  "identifier": "550e8400-e29b-41d4-a716-446655440000",
  "metadata": {
    "access_url": "http://data.dsb.com/ontology/DSD_1.0.0",
    "author": [
      "European Commission"
    ],
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      }
    ],
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ],
    "download_url": "https://ibestat.es/edatos/apis/structural-resources/v1.0/datastructures/IBESTAT/DSD_000001A_00001/01.000.xml",
    "frequency": "http://publications.europa.eu/resource/authority/frequency/NEVER",
    "language": [
      "http://publications.europa.eu/resource/authority/language/ENG"
    ],
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "modified": "2026-02-23",
    "publisher": "European Commission",
    "spatial": [
      "http://publications.europa.eu/resource/authority/country/EUR"
    ],
    "status": "http://publications.europa.eu/resource/authority/distribution-status/COMPLETED",
    "theme": [
      "http://publications.europa.eu/resource/authority/data-theme/GOVE"
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      }
    ]
  },
  "resource_extension": "https://www.iana.org/assignments/media-types/application/xml",
  "title": [
    {
      "language": "en",
      "value": "DSD"
    }
  ],
  "version_info": "1.0.0"
}
```

<h3 id="get_metadata_data_processing_v1_vocabularyhub__resource_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[CustomMetadataResponse](#schemacustommetadataresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_metadata_data_processing_v1_VocabularyHub__resource_id__delete

<a id="opIddelete_metadata_data_processing_v1_VocabularyHub__resource_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/VocabularyHub/{resource_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/VocabularyHub/{resource_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/VocabularyHub/{resource_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/VocabularyHub/{resource_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/VocabularyHub/{resource_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/VocabularyHub/{resource_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/VocabularyHub/{resource_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/VocabularyHub/{resource_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/VocabularyHub/{resource_id}`

*Delete metadata by resource id*

<h3 id="delete_metadata_data_processing_v1_vocabularyhub__resource_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|resource_id|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete_metadata_data_processing_v1_vocabularyhub__resource_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="delete_metadata_data_processing_v1_vocabularyhub__resource_id__delete-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-dataservices">DataServices</h1>

CRUD operations for DCAT DataServices.

## create_dataservice_data_processing_v1_CatalogDatasets_dataservices_post

<a id="opIdcreate_dataservice_data_processing_v1_CatalogDatasets_dataservices_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/dataservices \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/dataservices HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataservices',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/dataservices',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/dataservices', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/dataservices', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataservices");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/dataservices", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/dataservices`

*Create a new DataService*

Create a new DataService.

**Required fields:**
- title: Title of the service
- endpoint_url: URL of the service endpoint

**Optional fields:**
- applicable_legislation: List of applicable legislation URIs
- endpoint_description: URL to endpoint description (e.g., OpenAPI spec)
- documentation: URL to documentation
- description: Text description of the service
- serves_dataset: List of dataset URIs that this service provides access to

**Returns:**
- Created DataService with generated URI and timestamps

> Body parameter

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ]
}
```

<h3 id="create_dataservice_data_processing_v1_catalogdatasets_dataservices_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DataServiceCreate](#schemadataservicecreate)|true|none|

> Example responses

> 201 Response

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-15T10:30:00Z",
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "id": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ],
  "updated_at": "2025-01-15T10:30:00Z"
}
```

<h3 id="create_dataservice_data_processing_v1_catalogdatasets_dataservices_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|DataService created successfully|[DataServiceResponse](#schemadataserviceresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate DataService)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_dataservices_data_processing_v1_CatalogDatasets_dataservices_get

<a id="opIdlist_dataservices_data_processing_v1_CatalogDatasets_dataservices_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/dataservices \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/dataservices HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataservices',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/dataservices',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/dataservices', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/dataservices', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataservices");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/dataservices", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/dataservices`

*List all DataServices*

List all DataServices with pagination.

**Query Parameters:**
- page: Page number (default: 1, minimum: 1)
- size: Number of items per page (default: 10, minimum: 1, maximum: 100)

**Returns:**
- Paginated list of DataServices with metadata (total count, page info)

<h3 id="list_dataservices_data_processing_v1_catalogdatasets_dataservices_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number (1-based)|
|size|query|integer|false|Page size (max 100)|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "applicable_legislation": [
        "http://data.europa.eu/eli/reg/2016/679/oj"
      ],
      "created_at": "2025-01-15T10:30:00Z",
      "endpoint_url": "https://api.data.gov/sparql",
      "id": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
      "title": [
        {
          "language": "en",
          "value": "SPARQL Endpoint"
        }
      ],
      "updated_at": "2025-01-15T10:30:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_dataservices_data_processing_v1_catalogdatasets_dataservices_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DataServiceListResponse](#schemadataservicelistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_dataservice_data_processing_v1_CatalogDatasets_dataservices__dataservice_id__get

<a id="opIdget_dataservice_data_processing_v1_CatalogDatasets_dataservices__dataservice_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}`

*Get DataService by ID*

Retrieve a DataService by its URI.

**Parameters:**
- dataservice_id: The URI of the DataService (URL-encoded)

**Returns:**
- DataService details if found
- 404 error if not found

<h3 id="get_dataservice_data_processing_v1_catalogdatasets_dataservices__dataservice_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataservice_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-15T10:30:00Z",
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "id": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ],
  "updated_at": "2025-01-15T10:30:00Z"
}
```

<h3 id="get_dataservice_data_processing_v1_catalogdatasets_dataservices__dataservice_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DataServiceResponse](#schemadataserviceresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_dataservice_data_processing_v1_CatalogDatasets_dataservices__dataservice_id__put

<a id="opIdupdate_dataservice_data_processing_v1_CatalogDatasets_dataservices__dataservice_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying datasets"
    }
  ],
  "documentation": "https://example.com/docs",
  "endpoint_description": "https://example.com/openapi.json",
  "endpoint_url": "https://example.com/sparql",
  "serves_dataset": [
    "http://example.org/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}`

*Update a DataService*

Update an existing DataService.

**Parameters:**
- dataservice_id: The URI of the DataService to update (URL-encoded)
- payload: DataService update payload (all fields are optional)

**Returns:**
- Updated DataService details
- 404 error if DataService not found

> Body parameter

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying datasets"
    }
  ],
  "documentation": "https://example.com/docs",
  "endpoint_description": "https://example.com/openapi.json",
  "endpoint_url": "https://example.com/sparql",
  "serves_dataset": [
    "http://example.org/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ]
}
```

<h3 id="update_dataservice_data_processing_v1_catalogdatasets_dataservices__dataservice_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataservice_id|path|string|true|none|
|body|body|[DataServiceUpdate](#schemadataserviceupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-15T10:30:00Z",
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "id": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ],
  "updated_at": "2025-01-15T10:30:00Z"
}
```

<h3 id="update_dataservice_data_processing_v1_catalogdatasets_dataservices__dataservice_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DataServiceResponse](#schemadataserviceresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_dataservice_data_processing_v1_CatalogDatasets_dataservices__dataservice_id__delete

<a id="opIddelete_dataservice_data_processing_v1_CatalogDatasets_dataservices__dataservice_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/dataservices/{dataservice_id}`

*Delete a DataService*

Delete a DataService.

**Referential integrity rule :**
- A `dcat:DataService` may be referenced by one or more `dcat:Distribution` resources via `dcat:accessService`.
- If the DataService is referenced by at least one Distribution, deletion is **blocked** and the API returns
  **409 Conflict**.

<h3 id="delete_dataservice_data_processing_v1_catalogdatasets_dataservices__dataservice_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataservice_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_dataservice_data_processing_v1_catalogdatasets_dataservices__dataservice_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|DataService deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (DataService is referenced by Distributions)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-participants">Participants</h1>

CRUD operations for Participants.

## create_participant_data_processing_v1_CatalogDatasets_participants_post

<a id="opIdcreate_participant_data_processing_v1_CatalogDatasets_participants_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/participants \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/participants HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/participants',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/participants',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/participants', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/participants', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/participants");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/participants", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/participants`

*Create a new Participant*

> Body parameter

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE"
}
```

<h3 id="create_participant_data_processing_v1_catalogdatasets_participants_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ParticipantCreate](#schemaparticipantcreate)|true|none|

> Example responses

> 201 Response

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "created_at": "2026-03-10T00:00:00Z",
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "id": "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000",
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE",
  "updated_at": "2026-03-10T00:00:00Z"
}
```

<h3 id="create_participant_data_processing_v1_catalogdatasets_participants_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Participant created successfully|[ParticipantResponse](#schemaparticipantresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Participant)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_participants_data_processing_v1_CatalogDatasets_participants_get

<a id="opIdlist_participants_data_processing_v1_CatalogDatasets_participants_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/participants \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/participants HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/participants',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/participants',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/participants', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/participants', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/participants");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/participants", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/participants`

*List all Participants*

<h3 id="list_participants_data_processing_v1_catalogdatasets_participants_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number|
|size|query|integer|false|Page size|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "address": {
        "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
        "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
        "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
        "postCode": "28021",
        "postName": "Madrid"
      },
      "classification": [
        "http://publications.europa.eu/resource/authority/organization-type/MIN"
      ],
      "connector": [
        {
          "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
          "status": "ACTIVE"
        }
      ],
      "contactPoint": {
        "email": "atencionalaciudadania@digital.gob.es",
        "openingHours": "Mo-Fr 09:00-14:00",
        "telephone": "+34911596128"
      },
      "created_at": "2026-03-10T00:00:00Z",
      "description": [
        {
          "language": "es",
          "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
        }
      ],
      "id": "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000",
      "identifier": [
        {
          "notation": "E05068901",
          "schemeName": {
            "language": "es",
            "value": "Identificación de los organismos públicos"
          },
          "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
        }
      ],
      "preferredLabel": [
        {
          "language": "es",
          "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
        }
      ],
      "purpose": [
        "http://data.europa.eu/7yx/cofog/01.1.1"
      ],
      "status": "ACTIVE",
      "updated_at": "2026-03-10T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_participants_data_processing_v1_catalogdatasets_participants_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[ParticipantListResponse](#schemaparticipantlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_participant_data_processing_v1_CatalogDatasets_participants__participant_id__get

<a id="opIdget_participant_data_processing_v1_CatalogDatasets_participants__participant_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/participants/{participant_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/participants/{participant_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/participants/{participant_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/participants/{participant_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/participants/{participant_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/participants/{participant_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/participants/{participant_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/participants/{participant_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/participants/{participant_id}`

*Get Participant by ID*

<h3 id="get_participant_data_processing_v1_catalogdatasets_participants__participant_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|participant_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "created_at": "2026-03-10T00:00:00Z",
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "id": "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000",
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE",
  "updated_at": "2026-03-10T00:00:00Z"
}
```

<h3 id="get_participant_data_processing_v1_catalogdatasets_participants__participant_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[ParticipantResponse](#schemaparticipantresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_participant_data_processing_v1_CatalogDatasets_participants__participant_id__put

<a id="opIdupdate_participant_data_processing_v1_CatalogDatasets_participants__participant_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/participants/{participant_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/participants/{participant_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/participants/{participant_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/participants/{participant_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/participants/{participant_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/participants/{participant_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/participants/{participant_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/participants/{participant_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/participants/{participant_id}`

*Update a Participant*

> Body parameter

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE"
}
```

<h3 id="update_participant_data_processing_v1_catalogdatasets_participants__participant_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|participant_id|path|string|true|none|
|body|body|[ParticipantUpdate](#schemaparticipantupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "created_at": "2026-03-10T00:00:00Z",
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "id": "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000",
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE",
  "updated_at": "2026-03-10T00:00:00Z"
}
```

<h3 id="update_participant_data_processing_v1_catalogdatasets_participants__participant_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[ParticipantResponse](#schemaparticipantresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Participant)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_participant_data_processing_v1_CatalogDatasets_participants__participant_id__delete

<a id="opIddelete_participant_data_processing_v1_CatalogDatasets_participants__participant_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/participants/{participant_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/participants/{participant_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/participants/{participant_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/participants/{participant_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/participants/{participant_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/participants/{participant_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/participants/{participant_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/participants/{participant_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/participants/{participant_id}`

*Delete a Participant*

<h3 id="delete_participant_data_processing_v1_catalogdatasets_participants__participant_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|participant_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_participant_data_processing_v1_catalogdatasets_participants__participant_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Participant deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (in-use Participant)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-agents">Agents</h1>

CRUD operations for FOAF Agents.

## create_agent_data_processing_v1_CatalogDatasets_agents_post

<a id="opIdcreate_agent_data_processing_v1_CatalogDatasets_agents_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/agents \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/agents HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "homepage": "http://example.org/organizations/example",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/agents',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/agents',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/agents', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/agents', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/agents");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/agents", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/agents`

*Create a new Agent*

> Body parameter

```json
{
  "homepage": "http://example.org/organizations/example",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT"
}
```

<h3 id="create_agent_data_processing_v1_catalogdatasets_agents_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AgentCreate](#schemaagentcreate)|true|none|

> Example responses

> 201 Response

```json
{
  "created_at": "2025-01-01T00:00:00Z",
  "homepage": "http://example.org/organizations/example",
  "id": "http://data.dsb.com/agent/550e8400-e29b-41d4-a716-446655440000",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="create_agent_data_processing_v1_catalogdatasets_agents_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Agent created successfully|[AgentResponse](#schemaagentresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Agent)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_agents_data_processing_v1_CatalogDatasets_agents_get

<a id="opIdlist_agents_data_processing_v1_CatalogDatasets_agents_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/agents \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/agents HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/agents',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/agents',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/agents', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/agents', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/agents");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/agents", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/agents`

*List all Agents*

<h3 id="list_agents_data_processing_v1_catalogdatasets_agents_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number|
|size|query|integer|false|Page size|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "created_at": "2025-01-01T00:00:00Z",
      "homepage": "http://example.org/organizations/example",
      "id": "http://data.dsb.com/agent/550e8400-e29b-41d4-a716-446655440000",
      "name": "Example Organization",
      "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_agents_data_processing_v1_catalogdatasets_agents_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[AgentListResponse](#schemaagentlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_agent_data_processing_v1_CatalogDatasets_agents__agent_id__get

<a id="opIdget_agent_data_processing_v1_CatalogDatasets_agents__agent_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/agents/{agent_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/agents/{agent_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/agents/{agent_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/agents/{agent_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/agents/{agent_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/agents/{agent_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/agents/{agent_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/agents/{agent_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/agents/{agent_id}`

*Get Agent by ID*

<h3 id="get_agent_data_processing_v1_catalogdatasets_agents__agent_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|agent_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "created_at": "2025-01-01T00:00:00Z",
  "homepage": "http://example.org/organizations/example",
  "id": "http://data.dsb.com/agent/550e8400-e29b-41d4-a716-446655440000",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="get_agent_data_processing_v1_catalogdatasets_agents__agent_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[AgentResponse](#schemaagentresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_agent_data_processing_v1_CatalogDatasets_agents__agent_id__put

<a id="opIdupdate_agent_data_processing_v1_CatalogDatasets_agents__agent_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/agents/{agent_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/agents/{agent_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "homepage": "http://example.org/organizations/example",
  "name": "Example Organization (updated)",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/agents/{agent_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/agents/{agent_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/agents/{agent_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/agents/{agent_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/agents/{agent_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/agents/{agent_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/agents/{agent_id}`

*Update an Agent*

> Body parameter

```json
{
  "homepage": "http://example.org/organizations/example",
  "name": "Example Organization (updated)",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT"
}
```

<h3 id="update_agent_data_processing_v1_catalogdatasets_agents__agent_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|agent_id|path|string|true|none|
|body|body|[AgentUpdate](#schemaagentupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "created_at": "2025-01-01T00:00:00Z",
  "homepage": "http://example.org/organizations/example",
  "id": "http://data.dsb.com/agent/550e8400-e29b-41d4-a716-446655440000",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="update_agent_data_processing_v1_catalogdatasets_agents__agent_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[AgentResponse](#schemaagentresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Agent)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_agent_data_processing_v1_CatalogDatasets_agents__agent_id__delete

<a id="opIddelete_agent_data_processing_v1_CatalogDatasets_agents__agent_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/agents/{agent_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/agents/{agent_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/agents/{agent_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/agents/{agent_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/agents/{agent_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/agents/{agent_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/agents/{agent_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/agents/{agent_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/agents/{agent_id}`

*Delete an Agent*

Delete an Agent.
**Referential integrity rules (enforced):**
- Deletion is **blocked** (409 Conflict) if the Agent is referenced as `dct:publisher` by any `dcat:Catalog`.
- Deletion is **blocked** (409 Conflict) if the Agent is referenced as `dct:publisher` by any `dcat:Dataset`.
- Deletion is **blocked** (409 Conflict) if the Agent is referenced as `dct:creator` by any `dcat:Dataset`.
- Deletion is **blocked** (409 Conflict) if the Agent is referenced as `dct:publisher` by any `dcat:Resource` in the dataset offers graph.
- Deletion is **blocked** (409 Conflict) if the Agent is referenced as `odrl:assigner` by any `odrl:Policy` in the policies graph.
- Deletion is **blocked** (409 Conflict) if the Agent is referenced as `odrl:assigner` by any `odrl:Policy` in the policy templates graph.
If none of the above references exist, the Agent entity is deleted from the agents graph.

<h3 id="delete_agent_data_processing_v1_catalogdatasets_agents__agent_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|agent_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_agent_data_processing_v1_catalogdatasets_agents__agent_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Agent deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (in-use Agent)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-policytemplates">PolicyTemplates</h1>

CRUD operations for ODRL access control policy templates (odrl:Offer).

## create_template_data_processing_v1_CatalogDatasets_policy_templates_post

<a id="opIdcreate_template_data_processing_v1_CatalogDatasets_policy_templates_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/policy-templates \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/policy-templates HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "description": [
    {
      "language": "en",
      "value": "Allow use of CSV dataset"
    }
  ],
  "obligations": [
    {
      "action": "http://www.w3.org/ns/odrl/2/attribute",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/delayPeriod",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "Required"
        }
      ]
    }
  ],
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "prohibitions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/commercialize",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "commercial"
        }
      ]
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "Policy for Distribution CSV"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policy-templates',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/policy-templates',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/policy-templates', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/policy-templates', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policy-templates");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/policy-templates", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/policy-templates`

*Create a new ODRL Policy Template (Offer)*

> Body parameter

```json
{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "description": [
    {
      "language": "en",
      "value": "Allow use of CSV dataset"
    }
  ],
  "obligations": [
    {
      "action": "http://www.w3.org/ns/odrl/2/attribute",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/delayPeriod",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "Required"
        }
      ]
    }
  ],
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "prohibitions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/commercialize",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "commercial"
        }
      ]
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "Policy for Distribution CSV"
    }
  ]
}
```

<h3 id="create_template_data_processing_v1_catalogdatasets_policy_templates_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[OdrlPolicyTemplateCreate](#schemaodrlpolicytemplatecreate)|true|none|

> Example responses

> 201 Response

```json
{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "created_at": "2026-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "updated_at": "2026-01-01T00:00:00Z"
}
```

<h3 id="create_template_data_processing_v1_catalogdatasets_policy_templates_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Policy template created successfully|[OdrlPolicyTemplateResponse](#schemaodrlpolicytemplateresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_templates_data_processing_v1_CatalogDatasets_policy_templates_get

<a id="opIdlist_templates_data_processing_v1_CatalogDatasets_policy_templates_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/policy-templates \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/policy-templates HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policy-templates',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/policy-templates',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/policy-templates', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/policy-templates', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policy-templates");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/policy-templates", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/policy-templates`

*List ODRL Policy Templates (Offers)*

<h3 id="list_templates_data_processing_v1_catalogdatasets_policy_templates_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number (1-based)|
|size|query|integer|false|Page size (max 100)|
|include_details|query|boolean|false|Include nested rules/constraints in the response|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
      "created_at": "2026-01-01T00:00:00Z",
      "id": "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000",
      "obligations": [],
      "permissions": [],
      "prohibitions": [],
      "updated_at": "2026-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_templates_data_processing_v1_catalogdatasets_policy_templates_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OdrlPolicyTemplateListResponse](#schemaodrlpolicytemplatelistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_template_data_processing_v1_CatalogDatasets_policy_templates__template_id__get

<a id="opIdget_template_data_processing_v1_CatalogDatasets_policy_templates__template_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/policy-templates/{template_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/policy-templates/{template_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policy-templates/{template_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/policy-templates/{template_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/policy-templates/{template_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/policy-templates/{template_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policy-templates/{template_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/policy-templates/{template_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/policy-templates/{template_id}`

*Get ODRL Policy Template by ID*

<h3 id="get_template_data_processing_v1_catalogdatasets_policy_templates__template_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|template_id|path|string|true|none|
|include_details|query|boolean|false|Include nested rules/constraints in the response|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "created_at": "2026-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "updated_at": "2026-01-01T00:00:00Z"
}
```

<h3 id="get_template_data_processing_v1_catalogdatasets_policy_templates__template_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OdrlPolicyTemplateResponse](#schemaodrlpolicytemplateresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_template_data_processing_v1_CatalogDatasets_policy_templates__template_id__put

<a id="opIdupdate_template_data_processing_v1_CatalogDatasets_policy_templates__template_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/policy-templates/{template_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/policy-templates/{template_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/spatial",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "ES"
        }
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policy-templates/{template_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/policy-templates/{template_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/policy-templates/{template_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/policy-templates/{template_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policy-templates/{template_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/policy-templates/{template_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/policy-templates/{template_id}`

*Update an ODRL Policy Template (Offer)*

> Body parameter

```json
{
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/spatial",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "ES"
        }
      ]
    }
  ]
}
```

<h3 id="update_template_data_processing_v1_catalogdatasets_policy_templates__template_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|template_id|path|string|true|none|
|body|body|[OdrlPolicyTemplateUpdate](#schemaodrlpolicytemplateupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "created_at": "2026-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "updated_at": "2026-01-01T00:00:00Z"
}
```

<h3 id="update_template_data_processing_v1_catalogdatasets_policy_templates__template_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OdrlPolicyTemplateResponse](#schemaodrlpolicytemplateresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_template_data_processing_v1_CatalogDatasets_policy_templates__template_id__delete

<a id="opIddelete_template_data_processing_v1_CatalogDatasets_policy_templates__template_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/policy-templates/{template_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/policy-templates/{template_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policy-templates/{template_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/policy-templates/{template_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/policy-templates/{template_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/policy-templates/{template_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policy-templates/{template_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/policy-templates/{template_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/policy-templates/{template_id}`

*Delete an ODRL Policy Template (Offer)*

Delete an ODRL Policy Template (Offer).

**Referential integrity rules (enforced):**
- Deletion is **blocked** (409 Conflict) if the template is referenced by one or more `dcat:Distribution`
  resources via `odrl:hasPolicy`.

If no references exist, the template subgraph is deleted from the policy templates graph.

<h3 id="delete_template_data_processing_v1_catalogdatasets_policy_templates__template_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|template_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_template_data_processing_v1_catalogdatasets_policy_templates__template_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Policy template deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (template is referenced by one or more Distributions)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-distributions">Distributions</h1>

CRUD operations for DCAT Distributions.

## create_distribution_data_processing_v1_CatalogDatasets_distributions_post

<a id="opIdcreate_distribution_data_processing_v1_CatalogDatasets_distributions_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/distributions \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/distributions HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000"
  ],
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/distributions',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/distributions',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/distributions', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/distributions', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/distributions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/distributions", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/distributions`

*Create a new Distribution*

Create a new Distribution.

**Referential integrity rules (important):**
- If `access_service` is provided, it must point to an existing `dcat:DataService` (a URI stored in the DataServices graph).
- If `has_policies` is provided, every policy IRI must exist in the policies graph.

**Duplicate rule (summary):**
- Unique by `(dataset, access_url)` when `dataset` is provided; otherwise unique by `access_url`.

> Body parameter

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000"
  ],
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ]
}
```

<h3 id="create_distribution_data_processing_v1_catalogdatasets_distributions_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DistributionCreate](#schemadistributioncreate)|true|none|

> Example responses

> 201 Response

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "created_at": "2025-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "id": "http://data.dsb.com/distribution/550e8400-e29b-41d4-a716-446655440000",
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="create_distribution_data_processing_v1_catalogdatasets_distributions_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Distribution created successfully|[DistributionResponse](#schemadistributionresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Distribution)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_distributions_data_processing_v1_CatalogDatasets_distributions_get

<a id="opIdlist_distributions_data_processing_v1_CatalogDatasets_distributions_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/distributions \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/distributions HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/distributions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/distributions',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/distributions', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/distributions', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/distributions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/distributions", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/distributions`

*List all Distributions*

<h3 id="list_distributions_data_processing_v1_catalogdatasets_distributions_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number|
|size|query|integer|false|Page size|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "access_url": "https://data.example.org/files/dataset.csv",
      "created_at": "2025-01-01T00:00:00Z",
      "description": [
        {
          "language": "en",
          "value": "CSV export of the dataset"
        }
      ],
      "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
      "id": "http://data.dsb.com/distribution/550e8400-e29b-41d4-a716-446655440000",
      "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_distributions_data_processing_v1_catalogdatasets_distributions_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DistributionListResponse](#schemadistributionlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_distribution_data_processing_v1_CatalogDatasets_distributions__distribution_id__get

<a id="opIdget_distribution_data_processing_v1_CatalogDatasets_distributions__distribution_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/distributions/{distribution_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/distributions/{distribution_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/distributions/{distribution_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/distributions/{distribution_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/distributions/{distribution_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/distributions/{distribution_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/distributions/{distribution_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/distributions/{distribution_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/distributions/{distribution_id}`

*Get Distribution by ID*

<h3 id="get_distribution_data_processing_v1_catalogdatasets_distributions__distribution_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|distribution_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "created_at": "2025-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "id": "http://data.dsb.com/distribution/550e8400-e29b-41d4-a716-446655440000",
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="get_distribution_data_processing_v1_catalogdatasets_distributions__distribution_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DistributionResponse](#schemadistributionresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_distribution_data_processing_v1_CatalogDatasets_distributions__distribution_id__put

<a id="opIdupdate_distribution_data_processing_v1_CatalogDatasets_distributions__distribution_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/distributions/{distribution_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/distributions/{distribution_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "description": [
    {
      "language": "en",
      "value": "Updated CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV (v2)"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/distributions/{distribution_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/distributions/{distribution_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/distributions/{distribution_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/distributions/{distribution_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/distributions/{distribution_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/distributions/{distribution_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/distributions/{distribution_id}`

*Update a Distribution*

Update an existing Distribution.

**Referential integrity rules (important):**
- When `access_service` is included in the update payload, it must point to an existing `dcat:DataService`.
- When `has_policies` is included in the update payload, every policy IRI must exist in the policies graph.

Notes:
- If `access_service` is omitted from the payload, the existing value is kept.
- If `has_policies` is omitted from the payload, the existing list is kept.

> Body parameter

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "description": [
    {
      "language": "en",
      "value": "Updated CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV (v2)"
    }
  ]
}
```

<h3 id="update_distribution_data_processing_v1_catalogdatasets_distributions__distribution_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|distribution_id|path|string|true|none|
|body|body|[DistributionUpdate](#schemadistributionupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "created_at": "2025-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "id": "http://data.dsb.com/distribution/550e8400-e29b-41d4-a716-446655440000",
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="update_distribution_data_processing_v1_catalogdatasets_distributions__distribution_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DistributionResponse](#schemadistributionresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_distribution_data_processing_v1_CatalogDatasets_distributions__distribution_id__delete

<a id="opIddelete_distribution_data_processing_v1_CatalogDatasets_distributions__distribution_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/distributions/{distribution_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/distributions/{distribution_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/distributions/{distribution_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/distributions/{distribution_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/distributions/{distribution_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/distributions/{distribution_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/distributions/{distribution_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/distributions/{distribution_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/distributions/{distribution_id}`

*Delete a Distribution*

Delete a Distribution.

**Referential integrity / cascade rules (enforced):**
- Deletion is **blocked** (409 Conflict) if the Distribution is referenced by one or more Datasets
  via `dcat:distribution`.

- If the Distribution has one or more `odrl:hasPolicy` references:
  - the service deletes only the referenced IRIs that exist in the active policies graph, and
  - policy templates are never deleted by this operation.

- Finally, the Distribution entity is deleted from the distributions graph.

<h3 id="delete_distribution_data_processing_v1_catalogdatasets_distributions__distribution_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|distribution_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_distribution_data_processing_v1_catalogdatasets_distributions__distribution_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Distribution deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (referential integrity)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-policies">Policies</h1>

CRUD operations for ODRL access control policies (odrl:Offer) linked to DCAT Dataset Offers.

## create_policy_data_processing_v1_CatalogDatasets_policies_post

<a id="opIdcreate_policy_data_processing_v1_CatalogDatasets_policies_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/policies \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/policies HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "description": [
    {
      "language": "en",
      "value": "Allow use of CSV dataset"
    }
  ],
  "obligations": [
    {
      "action": "http://www.w3.org/ns/odrl/2/attribute",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "prohibitions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/distribute",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "commercial"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "title": [
    {
      "language": "en",
      "value": "Policy for Distribution CSV"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policies',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/policies',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/policies', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/policies', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policies");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/policies", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/policies`

*Create a new ODRL Policy (Offer) for a Distribution*

Create a new ODRL Policy (odrl:Offer) for a Distribution.

**Referential integrity rules (important):**
- `target` must point to an existing `dcat:Distribution`.

**Validation:**
- Payload is validated with ODRL SHACL shapes (best-effort via validation microservice).

Notes:
- After creating/updating a policy, the service synchronizes the reverse link by adding the policy IRI
  to `Distribution.has_policies` (best-effort).

> Body parameter

```json
{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "description": [
    {
      "language": "en",
      "value": "Allow use of CSV dataset"
    }
  ],
  "obligations": [
    {
      "action": "http://www.w3.org/ns/odrl/2/attribute",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "prohibitions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/distribute",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "commercial"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "title": [
    {
      "language": "en",
      "value": "Policy for Distribution CSV"
    }
  ]
}
```

<h3 id="create_policy_data_processing_v1_catalogdatasets_policies_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[OdrlOfferCreate](#schemaodrloffercreate)|true|none|

> Example responses

> 201 Response

```json
{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "created_at": "2025-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="create_policy_data_processing_v1_catalogdatasets_policies_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Policy created successfully|[OdrlOfferResponse](#schemaodrlofferresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (policy already exists for the target Distribution)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_policies_data_processing_v1_CatalogDatasets_policies_get

<a id="opIdlist_policies_data_processing_v1_CatalogDatasets_policies_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/policies \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/policies HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policies',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/policies',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/policies', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/policies', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policies");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/policies", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/policies`

*List ODRL Policies (Offers)*

<h3 id="list_policies_data_processing_v1_catalogdatasets_policies_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number (1-based)|
|size|query|integer|false|Page size (max 100)|
|include_details|query|boolean|false|Include nested rules/constraints in the response|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "assigner": "http://data.dsb.com/participant/AG-001",
      "created_at": "2025-01-01T00:00:00Z",
      "id": "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000",
      "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_policies_data_processing_v1_catalogdatasets_policies_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OdrlOfferListResponse](#schemaodrlofferlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_policy_data_processing_v1_CatalogDatasets_policies__policy_id__get

<a id="opIdget_policy_data_processing_v1_CatalogDatasets_policies__policy_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/policies/{policy_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/policies/{policy_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policies/{policy_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/policies/{policy_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/policies/{policy_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/policies/{policy_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policies/{policy_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/policies/{policy_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/policies/{policy_id}`

*Get ODRL Policy (Offer) by ID*

<h3 id="get_policy_data_processing_v1_catalogdatasets_policies__policy_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|policy_id|path|string|true|none|
|include_details|query|boolean|false|Include nested rules/constraints in the response|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "created_at": "2025-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="get_policy_data_processing_v1_catalogdatasets_policies__policy_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OdrlOfferResponse](#schemaodrlofferresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_policy_data_processing_v1_CatalogDatasets_policies__policy_id__put

<a id="opIdupdate_policy_data_processing_v1_CatalogDatasets_policies__policy_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/policies/{policy_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/policies/{policy_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/spatial",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "ES"
        }
      ]
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policies/{policy_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/policies/{policy_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/policies/{policy_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/policies/{policy_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policies/{policy_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/policies/{policy_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/policies/{policy_id}`

*Update an ODRL Policy (Offer)*

Update an existing ODRL Policy.

Semantics:
- Omitted fields are preserved (they are NOT deleted).
- To explicitly clear an optional field (e.g. a rule `assignee`), send it as `null`.

> Body parameter

```json
{
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/spatial",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "ES"
        }
      ]
    }
  ]
}
```

<h3 id="update_policy_data_processing_v1_catalogdatasets_policies__policy_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|policy_id|path|string|true|none|
|body|body|[OdrlOfferUpdate](#schemaodrlofferupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "created_at": "2025-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="update_policy_data_processing_v1_catalogdatasets_policies__policy_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[OdrlOfferResponse](#schemaodrlofferresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_policy_data_processing_v1_CatalogDatasets_policies__policy_id__delete

<a id="opIddelete_policy_data_processing_v1_CatalogDatasets_policies__policy_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/policies/{policy_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/policies/{policy_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/policies/{policy_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/policies/{policy_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/policies/{policy_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/policies/{policy_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/policies/{policy_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/policies/{policy_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/policies/{policy_id}`

*Delete an ODRL Policy (Offer)*

Delete an ODRL Policy (Offer).

**Referential integrity / cascade (enforced):**
- Remove `odrl:hasPolicy` references from any `dcat:Distribution` that links to this policy.
- Delete the Policy subgraph from the policies graph.

Notes:
- This endpoint deletes active policies only; policy templates are managed separately.

<h3 id="delete_policy_data_processing_v1_catalogdatasets_policies__policy_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|policy_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_policy_data_processing_v1_catalogdatasets_policies__policy_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Policy deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (policy is referenced by one or more Distributions)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-datasets">Datasets</h1>

CRUD operations for DCAT Datasets.

## create_dataset_data_processing_v1_CatalogDatasets_datasets_post

<a id="opIdcreate_dataset_data_processing_v1_CatalogDatasets_datasets_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/datasets \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/datasets HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    },
    {
      "language": "en",
      "value": "Minor fix in metadata"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/datasets',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/datasets',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/datasets', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/datasets', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/datasets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/datasets", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/datasets`

*Create a new Dataset*

Create a new Dataset.

Required fields :
- `identifier`, `title`, `description`, `theme`, `access_rights`, `publisher`, `modified`

Business rules enforced by this service:
- `identifier` (dct:identifier) is mandatory and must be unique.
- `distributions` (dcat:distribution) must contain at least one IRI.

> Body parameter

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    },
    {
      "language": "en",
      "value": "Minor fix in metadata"
    }
  ]
}
```

<h3 id="create_dataset_data_processing_v1_catalogdatasets_datasets_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DatasetCreate](#schemadatasetcreate)|true|none|

> Example responses

> 201 Response

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "id": "http://data.dsb.com/dataset/550e8400-e29b-41d4-a716-446655440000",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "quality_score": 145,
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "updated_at": "2025-01-01T00:00:00Z",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    }
  ]
}
```

<h3 id="create_dataset_data_processing_v1_catalogdatasets_datasets_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Dataset created successfully|[DatasetResponse](#schemadatasetresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Dataset)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_datasets_data_processing_v1_CatalogDatasets_datasets_get

<a id="opIdlist_datasets_data_processing_v1_CatalogDatasets_datasets_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/datasets \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/datasets HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/datasets',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/datasets',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/datasets', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/datasets', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/datasets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/datasets", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/datasets`

*List all Datasets*

<h3 id="list_datasets_data_processing_v1_catalogdatasets_datasets_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number|
|size|query|integer|false|Page size|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
      "created_at": "2025-01-01T00:00:00Z",
      "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
      "description": [
        {
          "language": "en",
          "value": "Dataset example description"
        }
      ],
      "distributions": [
        "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
      ],
      "id": "http://data.dsb.com/dataset/550e8400-e29b-41d4-a716-446655440000",
      "identifier": "DS-001",
      "modified": "2025-01-01T00:00:00Z",
      "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
      "theme": [
        "http://data.dsb.com/vocab/concept/data-theme/ECON"
      ],
      "title": [
        {
          "language": "en",
          "value": "Dataset example"
        }
      ],
      "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_datasets_data_processing_v1_catalogdatasets_datasets_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DatasetListResponse](#schemadatasetlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_dataset_data_processing_v1_CatalogDatasets_datasets__dataset_id__get

<a id="opIdget_dataset_data_processing_v1_CatalogDatasets_datasets__dataset_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/datasets/{dataset_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/datasets/{dataset_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/datasets/{dataset_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/datasets/{dataset_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/datasets/{dataset_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/datasets/{dataset_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/datasets/{dataset_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/datasets/{dataset_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/datasets/{dataset_id}`

*Get Dataset by ID*

<h3 id="get_dataset_data_processing_v1_catalogdatasets_datasets__dataset_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataset_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "id": "http://data.dsb.com/dataset/550e8400-e29b-41d4-a716-446655440000",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "quality_score": 145,
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "updated_at": "2025-01-01T00:00:00Z",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    }
  ]
}
```

<h3 id="get_dataset_data_processing_v1_catalogdatasets_datasets__dataset_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DatasetResponse](#schemadatasetresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_dataset_data_processing_v1_CatalogDatasets_datasets__dataset_id__put

<a id="opIdupdate_dataset_data_processing_v1_CatalogDatasets_datasets__dataset_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/datasets/{dataset_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/datasets/{dataset_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Updated dataset description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "keywords": [
    "economy",
    "update"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-02T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example (updated)"
    }
  ],
  "version_info": "1.0.1",
  "version_notes": [
    {
      "language": "en",
      "value": "Updated metadata"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/datasets/{dataset_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/datasets/{dataset_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/datasets/{dataset_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/datasets/{dataset_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/datasets/{dataset_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/datasets/{dataset_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/datasets/{dataset_id}`

*Update a Dataset*

> Body parameter

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Updated dataset description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "keywords": [
    "economy",
    "update"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-02T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example (updated)"
    }
  ],
  "version_info": "1.0.1",
  "version_notes": [
    {
      "language": "en",
      "value": "Updated metadata"
    }
  ]
}
```

<h3 id="update_dataset_data_processing_v1_catalogdatasets_datasets__dataset_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataset_id|path|string|true|none|
|body|body|[DatasetUpdate](#schemadatasetupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "id": "http://data.dsb.com/dataset/550e8400-e29b-41d4-a716-446655440000",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "quality_score": 145,
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "updated_at": "2025-01-01T00:00:00Z",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    }
  ]
}
```

<h3 id="update_dataset_data_processing_v1_catalogdatasets_datasets__dataset_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DatasetResponse](#schemadatasetresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_dataset_data_processing_v1_CatalogDatasets_datasets__dataset_id__delete

<a id="opIddelete_dataset_data_processing_v1_CatalogDatasets_datasets__dataset_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/datasets/{dataset_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/datasets/{dataset_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/datasets/{dataset_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/datasets/{dataset_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/datasets/{dataset_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/datasets/{dataset_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/datasets/{dataset_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/datasets/{dataset_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/datasets/{dataset_id}`

*Delete a Dataset*

Delete a Dataset.

**Referential integrity / cascade :**
- Deletion is **blocked** (409 Conflict) if the Dataset is referenced by one or more DatasetOffers
  via `dcat:relatedResource`.

- The Dataset is deleted from the datasets graph.
- Before deleting the Dataset, the service performs a **best-effort cascade** delete of its child
  `dcat:Distribution` IRIs listed in `Dataset.distributions`.

**Important interactions / blocking rules:**
- `DistributionService.delete_distribution()` can **block** deletion (raises `ValueError` -> 409 here) when:
  - the Distribution is still referenced by any Dataset (including this one) via `dcat:distribution`, or
  - the Distribution still has one or more `odrl:hasPolicy` references.

The response includes the list of Distribution IDs that were intended to be cascaded.

<h3 id="delete_dataset_data_processing_v1_catalogdatasets_datasets__dataset_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|dataset_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_dataset_data_processing_v1_catalogdatasets_datasets__dataset_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Dataset deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (in-use Dataset)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-datasetoffers">DatasetOffers</h1>

CRUD operations for DCAT Dataset Offers.

## create_offer_data_processing_v1_CatalogDatasets_dataset_offers_post

<a id="opIdcreate_offer_data_processing_v1_CatalogDatasets_dataset_offers_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/dataset-offers \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/dataset-offers HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataset-offers',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/dataset-offers',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/dataset-offers', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/dataset-offers', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataset-offers");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/dataset-offers", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/dataset-offers`

*Create a new Dataset Offer*

> Body parameter

```json
{
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ]
}
```

<h3 id="create_offer_data_processing_v1_catalogdatasets_dataset_offers_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DatasetOfferCreate](#schemadatasetoffercreate)|true|none|

> Example responses

> 201 Response

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "id": "http://data.dsb.com/dataset_offer/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ],
  "type": "OFFER",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

<h3 id="create_offer_data_processing_v1_catalogdatasets_dataset_offers_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Dataset offer created successfully|[DatasetOfferResponse](#schemadatasetofferresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_offers_data_processing_v1_CatalogDatasets_dataset_offers_get

<a id="opIdlist_offers_data_processing_v1_CatalogDatasets_dataset_offers_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/dataset-offers \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/dataset-offers HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataset-offers',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/dataset-offers',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/dataset-offers', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/dataset-offers', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataset-offers");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/dataset-offers", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/dataset-offers`

*List Dataset Offers*

<h3 id="list_offers_data_processing_v1_catalogdatasets_dataset_offers_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number (1-based)|
|size|query|integer|false|Page size (max 100)|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "created_at": "2026-01-01T00:00:00Z",
      "description": [
        {
          "language": "en",
          "value": "Offer for non-commercial research usage"
        }
      ],
      "id": "http://data.dsb.com/dataset_offer/550e8400-e29b-41d4-a716-446655440000",
      "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
      "related_resource": [
        "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
      ],
      "title": [
        {
          "language": "en",
          "value": "Research access offer"
        }
      ],
      "type": "OFFER",
      "updated_at": "2026-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_offers_data_processing_v1_catalogdatasets_dataset_offers_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DatasetOfferListResponse](#schemadatasetofferlistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_offer_data_processing_v1_CatalogDatasets_dataset_offers__offer_id__get

<a id="opIdget_offer_data_processing_v1_CatalogDatasets_dataset_offers__offer_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}`

*Get Dataset Offer by ID*

<h3 id="get_offer_data_processing_v1_catalogdatasets_dataset_offers__offer_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offer_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "id": "http://data.dsb.com/dataset_offer/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ],
  "type": "OFFER",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

<h3 id="get_offer_data_processing_v1_catalogdatasets_dataset_offers__offer_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DatasetOfferResponse](#schemadatasetofferresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_offer_data_processing_v1_CatalogDatasets_dataset_offers__offer_id__put

<a id="opIdupdate_offer_data_processing_v1_CatalogDatasets_dataset_offers__offer_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "description": [
    {
      "language": "en",
      "value": "Updated offer description"
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "Updated offer title"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}`

*Update a Dataset Offer*

> Body parameter

```json
{
  "description": [
    {
      "language": "en",
      "value": "Updated offer description"
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "Updated offer title"
    }
  ]
}
```

<h3 id="update_offer_data_processing_v1_catalogdatasets_dataset_offers__offer_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offer_id|path|string|true|none|
|body|body|[DatasetOfferUpdate](#schemadatasetofferupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "id": "http://data.dsb.com/dataset_offer/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ],
  "type": "OFFER",
  "updated_at": "2026-01-01T00:00:00Z"
}
```

<h3 id="update_offer_data_processing_v1_catalogdatasets_dataset_offers__offer_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[DatasetOfferResponse](#schemadatasetofferresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_offer_data_processing_v1_CatalogDatasets_dataset_offers__offer_id__delete

<a id="opIddelete_offer_data_processing_v1_CatalogDatasets_dataset_offers__offer_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/dataset-offers/{offer_id}`

*Delete a Dataset Offer*

Delete a Dataset Offer.

**Cascade rules (best-effort):**
- Resolve all `dcat:Distribution` resources belonging to the datasets listed in `related_resource`.
- Resolve all active ODRL Policies where `odrl:target` equals this offer.
- For each Distribution that references one of those Policies via `odrl:hasPolicy`:
  - if the policy has a `dct:source` pointing to an existing policy template, replace the policy IRI with the template IRI,
  - otherwise remove the policy reference from the Distribution.
- Delete the active Policy subgraphs from the policies graph.
- Finally, delete the Dataset Offer entity from the dataset offers graph.

Notes:
- Policy templates are never deleted by this operation.

<h3 id="delete_offer_data_processing_v1_catalogdatasets_dataset_offers__offer_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offer_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_offer_data_processing_v1_catalogdatasets_dataset_offers__offer_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Dataset offer deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-catalogs">Catalogs</h1>

CRUD operations for DCAT Catalogs.

## create_catalog_data_processing_v1_CatalogDatasets_catalogs_post

<a id="opIdcreate_catalog_data_processing_v1_CatalogDatasets_catalogs_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/CatalogDatasets/catalogs \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/CatalogDatasets/catalogs HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/catalogs',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/CatalogDatasets/catalogs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/CatalogDatasets/catalogs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/CatalogDatasets/catalogs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/catalogs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/CatalogDatasets/catalogs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/CatalogDatasets/catalogs`

*Create a new Catalog*

Create a new Catalog.

Required fields :
- `title`, `description`, `publisher`

Business rules enforced by this service:
- `publisher` (dct:publisher) must reference an existing foaf:Agent.
- `datasets` (dcat:dataset), if provided, must reference existing dcat:Dataset entities.

> Body parameter

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ]
}
```

<h3 id="create_catalog_data_processing_v1_catalogdatasets_catalogs_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CatalogCreate](#schemacatalogcreate)|true|none|

> Example responses

> 201 Response

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "id": "http://data.dsb.com/catalog/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="create_catalog_data_processing_v1_catalogdatasets_catalogs_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Catalog created successfully|[CatalogResponse](#schemacatalogresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict (duplicate Catalog)|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## list_catalogs_data_processing_v1_CatalogDatasets_catalogs_get

<a id="opIdlist_catalogs_data_processing_v1_CatalogDatasets_catalogs_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/catalogs \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/catalogs HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/catalogs',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/catalogs',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/catalogs', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/catalogs', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/catalogs");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/catalogs", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/catalogs`

*List all Catalogs*

<h3 id="list_catalogs_data_processing_v1_catalogdatasets_catalogs_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|Page number|
|size|query|integer|false|Page size|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "applicable_legislation": [
        "http://data.europa.eu/eli/reg/2016/679/oj"
      ],
      "created_at": "2025-01-01T00:00:00Z",
      "datasets": [
        "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
      ],
      "description": [
        {
          "language": "en",
          "value": "Official catalog of public sector datasets"
        }
      ],
      "id": "http://data.dsb.com/catalog/550e8400-e29b-41d4-a716-446655440000",
      "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
      "title": [
        {
          "language": "en",
          "value": "National Open Data Catalog"
        }
      ],
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}
```

<h3 id="list_catalogs_data_processing_v1_catalogdatasets_catalogs_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[CatalogListResponse](#schemacataloglistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## get_catalog_data_processing_v1_CatalogDatasets_catalogs__catalog_id__get

<a id="opIdget_catalog_data_processing_v1_CatalogDatasets_catalogs__catalog_id__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/CatalogDatasets/catalogs/{catalog_id} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/CatalogDatasets/catalogs/{catalog_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/CatalogDatasets/catalogs/{catalog_id}`

*Get Catalog by ID*

Retrieve a Catalog by ID.

The catalog_id can be:
- Full URI: http://catalog/catalog/uuid
- UUID only: uuid
- Path-like: /catalog/uuid

<h3 id="get_catalog_data_processing_v1_catalogdatasets_catalogs__catalog_id__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|catalog_id|path|string|true|none|
|lang|query|any|false|Language filter (e.g. 'en', 'es', 'eng')|

> Example responses

> 200 Response

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "id": "http://data.dsb.com/catalog/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="get_catalog_data_processing_v1_catalogdatasets_catalogs__catalog_id__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[CatalogResponse](#schemacatalogresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## update_catalog_data_processing_v1_CatalogDatasets_catalogs__catalog_id__put

<a id="opIdupdate_catalog_data_processing_v1_CatalogDatasets_catalogs__catalog_id__put"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /data-processing/v1/CatalogDatasets/catalogs/{catalog_id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```http
PUT /data-processing/v1/CatalogDatasets/catalogs/{catalog_id} HTTP/1.1

Content-Type: application/json
Accept: application/json

```

```javascript
const inputBody = '{
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "description": [
    {
      "language": "en",
      "value": "Updated catalog description"
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog (Updated)"
    }
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}',
{
  method: 'PUT',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.put '/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('PUT','/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"application/json"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("PUT", "/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`PUT /data-processing/v1/CatalogDatasets/catalogs/{catalog_id}`

*Update a Catalog*

Update an existing Catalog.

This is a partial update - only the fields provided in the payload will be updated.

Validations:
- If `publisher` is updated, the new publisher must exist
- If `datasets` are updated, all referenced datasets must exist

> Body parameter

```json
{
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "description": [
    {
      "language": "en",
      "value": "Updated catalog description"
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog (Updated)"
    }
  ]
}
```

<h3 id="update_catalog_data_processing_v1_catalogdatasets_catalogs__catalog_id__put-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|catalog_id|path|string|true|none|
|body|body|[CatalogUpdate](#schemacatalogupdate)|true|none|

> Example responses

> 200 Response

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "id": "http://data.dsb.com/catalog/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}
```

<h3 id="update_catalog_data_processing_v1_catalogdatasets_catalogs__catalog_id__put-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[CatalogResponse](#schemacatalogresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_catalog_data_processing_v1_CatalogDatasets_catalogs__catalog_id__delete

<a id="opIddelete_catalog_data_processing_v1_CatalogDatasets_catalogs__catalog_id__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/CatalogDatasets/catalogs/{catalog_id} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/CatalogDatasets/catalogs/{catalog_id} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/CatalogDatasets/catalogs/{catalog_id}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/CatalogDatasets/catalogs/{catalog_id}`

*Delete a Catalog*

Delete a Catalog.

**Referential integrity rules:**
- No explicit inbound reference checks are enforced by the service for Catalog deletion.

If the Catalog exists, it is deleted from the catalogs graph.

<h3 id="delete_catalog_data_processing_v1_catalogdatasets_catalogs__catalog_id__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|catalog_id|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}
```

<h3 id="delete_catalog_data_processing_v1_catalogdatasets_catalogs__catalog_id__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Catalog deleted successfully|[DeleteResult](#schemadeleteresult)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-controlledvocabularies">ControlledVocabularies</h1>

CRUD operations for controlled vocabularies.

## trigger_controlled_vocabularies_auto_import_data_processing_v1_ControlledVocabularies_auto_import_post

<a id="opIdtrigger_controlled_vocabularies_auto_import_data_processing_v1_ControlledVocabularies_auto_import_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/ControlledVocabularies/auto-import \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/ControlledVocabularies/auto-import HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/ControlledVocabularies/auto-import',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/ControlledVocabularies/auto-import',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/ControlledVocabularies/auto-import', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/ControlledVocabularies/auto-import', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/ControlledVocabularies/auto-import");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/ControlledVocabularies/auto-import", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/ControlledVocabularies/auto-import`

*Run controlled vocabularies auto-import on demand*

> Example responses

> 200 Response

```json
null
```

<h3 id="trigger_controlled_vocabularies_auto_import_data_processing_v1_controlledvocabularies_auto_import_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Controlled vocabularies auto-import completed|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="trigger_controlled_vocabularies_auto_import_data_processing_v1_controlledvocabularies_auto_import_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## import_vocabulary_data_processing_v1_ControlledVocabularies_import_post

<a id="opIdimport_vocabulary_data_processing_v1_ControlledVocabularies_import_post"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /data-processing/v1/ControlledVocabularies/import \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'

```

```http
POST /data-processing/v1/ControlledVocabularies/import HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json

```

```javascript
const inputBody = '{
  "vocab_name": "string",
  "source_url": "string",
  "download_url": "string",
  "source": "custom",
  "graph_iri": "string",
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/data-processing/v1/ControlledVocabularies/import',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/data-processing/v1/ControlledVocabularies/import',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/data-processing/v1/ControlledVocabularies/import', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/data-processing/v1/ControlledVocabularies/import', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/ControlledVocabularies/import");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/data-processing/v1/ControlledVocabularies/import", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /data-processing/v1/ControlledVocabularies/import`

*Import a controlled vocabulary from URL or uploaded RDF/XML file*

Import a controlled vocabulary.

Notes:
- Provide exactly one of: download_url | file.
- `graph_iri` overrides `source`. If neither is provided, a heuristic selects the target graph.

> Body parameter

```yaml
vocab_name: string
source_url: string
download_url: string
source: custom
graph_iri: string
file: string

```

<h3 id="import_vocabulary_data_processing_v1_controlledvocabularies_import_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_import_vocabulary_data_processing_v1_ControlledVocabularies_import_post](#schemabody_import_vocabulary_data_processing_v1_controlledvocabularies_import_post)|true|none|

> Example responses

> 201 Response

```json
{
  "vocab_name": "string",
  "source_url": "string",
  "code_predicate": "skos:notation",
  "terminology_notation_datatype": "string",
  "vocab_id": "string",
  "scheme_iri": "string",
  "graph_iri": "string"
}
```

<h3 id="import_vocabulary_data_processing_v1_controlledvocabularies_import_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Vocabulary imported successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Vocabulary already exists|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="import_vocabulary_data_processing_v1_controlledvocabularies_import_post-responseschema">Response Schema</h3>

Status Code **201**

*Response Import Vocabulary Data Processing V1 Controlledvocabularies Import Post*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|Response Import Vocabulary Data Processing V1 Controlledvocabularies Import Post|any|false|none|none|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ControlledVocabularyResponse](#schemacontrolledvocabularyresponse)|false|none|Response shape for a vocabulary.|
|»» vocab_name|string|true|none|Vocabulary name (public identifier, e.g. 'language', 'country')|
|»» source_url|any|false|none|Source URL used for syncing/importing|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» code_predicate|string|false|none|Predicate used as code field (default: skos:notation). Allowed: skos:notation | dct:identifier|
|»» terminology_notation_datatype|any|false|none|Optional datatype IRI to filter skos:notation when multiple typed notations exist|

*anyOf*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|string|false|none|none|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»»» *anonymous*|null|false|none|none|

*continued*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» vocab_id|string|true|none|Internal UUID for this vocabulary (generated by the service)|
|»» scheme_iri|string|true|none|IRI of the skos:ConceptScheme|
|»» graph_iri|string|true|none|Named graph IRI where this vocabulary is stored|

*or*

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ControlledVocabularyResponse](#schemacontrolledvocabularyresponse)]|false|none|[Response shape for a vocabulary.]|
|»» ControlledVocabularyResponse|[ControlledVocabularyResponse](#schemacontrolledvocabularyresponse)|false|none|Response shape for a vocabulary.|

<aside class="success">
This operation does not require authentication
</aside>

## list_vocabularies_data_processing_v1_ControlledVocabularies_get

<a id="opIdlist_vocabularies_data_processing_v1_ControlledVocabularies_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/ControlledVocabularies \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/ControlledVocabularies HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/ControlledVocabularies',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/ControlledVocabularies',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/ControlledVocabularies', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/ControlledVocabularies', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/ControlledVocabularies");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/ControlledVocabularies", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/ControlledVocabularies`

*Get all vocabularies (paginated)*

<h3 id="list_vocabularies_data_processing_v1_controlledvocabularies_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|page|query|integer|false|none|
|size|query|integer|false|none|
|filter|query|any|false|Free text filter (matches scheme IRI)|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "vocab_id": "string",
      "vocab_name": "string",
      "source_url": "string",
      "code_predicate": "skos:notation",
      "scheme_iri": "string",
      "graph_iri": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "size": 0,
  "pages": 0
}
```

<h3 id="list_vocabularies_data_processing_v1_controlledvocabularies_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[ControlledVocabularyListResponse](#schemacontrolledvocabularylistresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## get_vocabulary_data_processing_v1_ControlledVocabularies__vocab_name__get

<a id="opIdget_vocabulary_data_processing_v1_ControlledVocabularies__vocab_name__get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/ControlledVocabularies/{vocab_name} \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/ControlledVocabularies/{vocab_name} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/ControlledVocabularies/{vocab_name}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/ControlledVocabularies/{vocab_name}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/ControlledVocabularies/{vocab_name}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/ControlledVocabularies/{vocab_name}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/ControlledVocabularies/{vocab_name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/ControlledVocabularies/{vocab_name}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/ControlledVocabularies/{vocab_name}`

*Get vocabulary entries by vocab_name (paginated)*

<h3 id="get_vocabulary_data_processing_v1_controlledvocabularies__vocab_name__get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|vocab_name|path|string|true|none|
|lang|query|string|false|Entries language (default: en)|
|page|query|integer|false|Entries page|
|size|query|integer|false|Entries page size|

> Example responses

> 200 Response

```json
{
  "items": [
    {
      "code": "string",
      "label": "string",
      "concept_iri": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "size": 0,
  "pages": 0
}
```

<h3 id="get_vocabulary_data_processing_v1_controlledvocabularies__vocab_name__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[VocabularyEntryListResponse](#schemavocabularyentrylistresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

## delete_vocabulary_data_processing_v1_ControlledVocabularies__vocab_name__delete

<a id="opIddelete_vocabulary_data_processing_v1_ControlledVocabularies__vocab_name__delete"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /data-processing/v1/ControlledVocabularies/{vocab_name} \
  -H 'Accept: application/json'

```

```http
DELETE /data-processing/v1/ControlledVocabularies/{vocab_name} HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/ControlledVocabularies/{vocab_name}',
{
  method: 'DELETE',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.delete '/data-processing/v1/ControlledVocabularies/{vocab_name}',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/data-processing/v1/ControlledVocabularies/{vocab_name}', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DELETE','/data-processing/v1/ControlledVocabularies/{vocab_name}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/ControlledVocabularies/{vocab_name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DELETE", "/data-processing/v1/ControlledVocabularies/{vocab_name}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`DELETE /data-processing/v1/ControlledVocabularies/{vocab_name}`

*Delete a vocabulary (clears its named graph)*

<h3 id="delete_vocabulary_data_processing_v1_controlledvocabularies__vocab_name__delete-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|vocab_name|path|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete_vocabulary_data_processing_v1_controlledvocabularies__vocab_name__delete-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete_vocabulary_data_processing_v1_controlledvocabularies__vocab_name__delete-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="dataprocessing-api-health-check">Health-Check</h1>

## health_check_data_processing_v1_health_check_get

<a id="opIdhealth_check_data_processing_v1_health_check_get"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /data-processing/v1/health-check \
  -H 'Accept: application/json'

```

```http
GET /data-processing/v1/health-check HTTP/1.1

Accept: application/json

```

```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/data-processing/v1/health-check',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});

```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/data-processing/v1/health-check',
  params: {
  }, headers: headers

p JSON.parse(result)

```

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/data-processing/v1/health-check', headers = headers)

print(r.json())

```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/data-processing/v1/health-check', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

```

```java
URL obj = new URL("/data-processing/v1/health-check");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/data-processing/v1/health-check", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /data-processing/v1/health-check`

*Class to execute healthcheck process.*

> Example responses

> 200 Response

```json
{
  "message": "Health check successful.",
  "status": true
}
```

<h3 id="health_check_data_processing_v1_health_check_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|[HealthcheckOutput](#schemahealthcheckoutput)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AgentCreate">AgentCreate</h2>
<!-- backwards compatibility -->
<a id="schemaagentcreate"></a>
<a id="schema_AgentCreate"></a>
<a id="tocSagentcreate"></a>
<a id="tocsagentcreate"></a>

```json
{
  "homepage": "http://example.org/organizations/example",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT"
}

```

AgentCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|Agent name (foaf:name)|
|type|any|false|none|Agent type IRI (dct:type)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|homepage|any|false|none|Agent homepage IRI (foaf:homepage)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_AgentListResponse">AgentListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaagentlistresponse"></a>
<a id="schema_AgentListResponse"></a>
<a id="tocSagentlistresponse"></a>
<a id="tocsagentlistresponse"></a>

```json
{
  "items": [
    {
      "created_at": "2025-01-01T00:00:00Z",
      "homepage": "http://example.org/organizations/example",
      "id": "http://data.dsb.com/agent/550e8400-e29b-41d4-a716-446655440000",
      "name": "Example Organization",
      "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

AgentListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[AgentResponse](#schemaagentresponse)]|true|none|List of agents|
|total|integer|true|none|Total number of agents|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_AgentResponse">AgentResponse</h2>
<!-- backwards compatibility -->
<a id="schemaagentresponse"></a>
<a id="schema_AgentResponse"></a>
<a id="tocSagentresponse"></a>
<a id="tocsagentresponse"></a>

```json
{
  "created_at": "2025-01-01T00:00:00Z",
  "homepage": "http://example.org/organizations/example",
  "id": "http://data.dsb.com/agent/550e8400-e29b-41d4-a716-446655440000",
  "name": "Example Organization",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT",
  "updated_at": "2025-01-01T00:00:00Z"
}

```

AgentResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|Agent name (foaf:name)|
|type|any|false|none|Agent type IRI (dct:type)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|homepage|any|false|none|Agent homepage IRI (foaf:homepage)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (URI) of the Agent|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_AgentUpdate">AgentUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaagentupdate"></a>
<a id="schema_AgentUpdate"></a>
<a id="tocSagentupdate"></a>
<a id="tocsagentupdate"></a>

```json
{
  "homepage": "http://example.org/organizations/example",
  "name": "Example Organization (updated)",
  "type": "http://publications.europa.eu/resource/authority/organization-type/INSTIT"
}

```

AgentUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|any|false|none|Agent name (foaf:name)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|any|false|none|Agent type IRI (dct:type)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|homepage|any|false|none|Agent homepage IRI (foaf:homepage)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_Body_import_vocabulary_data_processing_v1_ControlledVocabularies_import_post">Body_import_vocabulary_data_processing_v1_ControlledVocabularies_import_post</h2>
<!-- backwards compatibility -->
<a id="schemabody_import_vocabulary_data_processing_v1_controlledvocabularies_import_post"></a>
<a id="schema_Body_import_vocabulary_data_processing_v1_ControlledVocabularies_import_post"></a>
<a id="tocSbody_import_vocabulary_data_processing_v1_controlledvocabularies_import_post"></a>
<a id="tocsbody_import_vocabulary_data_processing_v1_controlledvocabularies_import_post"></a>

```json
{
  "vocab_name": "string",
  "source_url": "string",
  "download_url": "string",
  "source": "custom",
  "graph_iri": "string",
  "file": "string"
}

```

Body_import_vocabulary_data_processing_v1_ControlledVocabularies_import_post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|vocab_name|string|true|none|Public vocabulary name (one graph per vocab_name)|
|source_url|any|false|none|Optional source URL (metadata)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|download_url|any|false|none|If provided, RDF/XML or XML will be downloaded from this URL|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|source|any|false|none|Optional vocabulary origin selector. Overrides heuristic when provided.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ControlledVocabSource](#schemacontrolledvocabsource)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|graph_iri|any|false|none|Optional target named graph IRI. If provided, it overrides `source` and heuristic.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|file|any|false|none|Upload RDF/XML or supported XML|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(binary)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_CatalogCreate">CatalogCreate</h2>
<!-- backwards compatibility -->
<a id="schemacatalogcreate"></a>
<a id="schema_CatalogCreate"></a>
<a id="tocScatalogcreate"></a>
<a id="tocscatalogcreate"></a>

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ]
}

```

CatalogCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|[[LocalizedString](#schemalocalizedstring)]|true|none|Title(s) of the catalog (dct:title)|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Description(s) of the catalog (dct:description)|
|publisher|string|true|none|Publisher IRI (dct:publisher)|
|datasets|any|false|none|Dataset IRIs (dcat:dataset)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_CatalogListResponse">CatalogListResponse</h2>
<!-- backwards compatibility -->
<a id="schemacataloglistresponse"></a>
<a id="schema_CatalogListResponse"></a>
<a id="tocScataloglistresponse"></a>
<a id="tocscataloglistresponse"></a>

```json
{
  "items": [
    {
      "applicable_legislation": [
        "http://data.europa.eu/eli/reg/2016/679/oj"
      ],
      "created_at": "2025-01-01T00:00:00Z",
      "datasets": [
        "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
      ],
      "description": [
        {
          "language": "en",
          "value": "Official catalog of public sector datasets"
        }
      ],
      "id": "http://data.dsb.com/catalog/550e8400-e29b-41d4-a716-446655440000",
      "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
      "title": [
        {
          "language": "en",
          "value": "National Open Data Catalog"
        }
      ],
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

CatalogListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[CatalogResponse](#schemacatalogresponse)]|true|none|List of catalogs|
|total|integer|true|none|Total number of catalogs|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_CatalogResponse">CatalogResponse</h2>
<!-- backwards compatibility -->
<a id="schemacatalogresponse"></a>
<a id="schema_CatalogResponse"></a>
<a id="tocScatalogresponse"></a>
<a id="tocscatalogresponse"></a>

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
  ],
  "description": [
    {
      "language": "en",
      "value": "Official catalog of public sector datasets"
    }
  ],
  "id": "http://data.dsb.com/catalog/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}

```

CatalogResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|[[LocalizedString](#schemalocalizedstring)]|true|none|Title(s) of the catalog (dct:title)|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Description(s) of the catalog (dct:description)|
|publisher|string|true|none|Publisher IRI (dct:publisher)|
|datasets|any|false|none|Dataset IRIs (dcat:dataset)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (URI) of the Catalog|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_CatalogUpdate">CatalogUpdate</h2>
<!-- backwards compatibility -->
<a id="schemacatalogupdate"></a>
<a id="schema_CatalogUpdate"></a>
<a id="tocScatalogupdate"></a>
<a id="tocscatalogupdate"></a>

```json
{
  "datasets": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "description": [
    {
      "language": "en",
      "value": "Updated catalog description"
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "National Open Data Catalog (Updated)"
    }
  ]
}

```

CatalogUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Title(s) of the catalog (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s) of the catalog (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|any|false|none|Publisher IRI (dct:publisher)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|datasets|any|false|none|Dataset IRIs (dcat:dataset)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ControlledVocabSource">ControlledVocabSource</h2>
<!-- backwards compatibility -->
<a id="schemacontrolledvocabsource"></a>
<a id="schema_ControlledVocabSource"></a>
<a id="tocScontrolledvocabsource"></a>
<a id="tocscontrolledvocabsource"></a>

```json
"custom"

```

ControlledVocabSource

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ControlledVocabSource|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|ControlledVocabSource|custom|
|ControlledVocabSource|eu|
|ControlledVocabSource|iana|

<h2 id="tocS_ControlledVocabularyListItemResponse">ControlledVocabularyListItemResponse</h2>
<!-- backwards compatibility -->
<a id="schemacontrolledvocabularylistitemresponse"></a>
<a id="schema_ControlledVocabularyListItemResponse"></a>
<a id="tocScontrolledvocabularylistitemresponse"></a>
<a id="tocscontrolledvocabularylistitemresponse"></a>

```json
{
  "vocab_id": "string",
  "vocab_name": "string",
  "source_url": "string",
  "code_predicate": "skos:notation",
  "scheme_iri": "string",
  "graph_iri": "string"
}

```

ControlledVocabularyListItemResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|vocab_id|string|true|none|none|
|vocab_name|string|true|none|none|
|source_url|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code_predicate|string|false|none|Predicate used as code field (default: skos:notation). Allowed: skos:notation | dct:identifier|
|scheme_iri|string|true|none|IRI of the skos:ConceptScheme|
|graph_iri|string|true|none|Named graph IRI where this vocabulary is stored|

<h2 id="tocS_ControlledVocabularyListResponse">ControlledVocabularyListResponse</h2>
<!-- backwards compatibility -->
<a id="schemacontrolledvocabularylistresponse"></a>
<a id="schema_ControlledVocabularyListResponse"></a>
<a id="tocScontrolledvocabularylistresponse"></a>
<a id="tocscontrolledvocabularylistresponse"></a>

```json
{
  "items": [
    {
      "vocab_id": "string",
      "vocab_name": "string",
      "source_url": "string",
      "code_predicate": "skos:notation",
      "scheme_iri": "string",
      "graph_iri": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "size": 0,
  "pages": 0
}

```

ControlledVocabularyListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[ControlledVocabularyListItemResponse](#schemacontrolledvocabularylistitemresponse)]|true|none|[Lightweight shape for vocabulary listings.]|
|total|integer|true|none|none|
|page|integer|true|none|none|
|size|integer|true|none|none|
|pages|integer|true|none|none|

<h2 id="tocS_ControlledVocabularyResponse">ControlledVocabularyResponse</h2>
<!-- backwards compatibility -->
<a id="schemacontrolledvocabularyresponse"></a>
<a id="schema_ControlledVocabularyResponse"></a>
<a id="tocScontrolledvocabularyresponse"></a>
<a id="tocscontrolledvocabularyresponse"></a>

```json
{
  "vocab_name": "string",
  "source_url": "string",
  "code_predicate": "skos:notation",
  "terminology_notation_datatype": "string",
  "vocab_id": "string",
  "scheme_iri": "string",
  "graph_iri": "string"
}

```

ControlledVocabularyResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|vocab_name|string|true|none|Vocabulary name (public identifier, e.g. 'language', 'country')|
|source_url|any|false|none|Source URL used for syncing/importing|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code_predicate|string|false|none|Predicate used as code field (default: skos:notation). Allowed: skos:notation | dct:identifier|
|terminology_notation_datatype|any|false|none|Optional datatype IRI to filter skos:notation when multiple typed notations exist|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|vocab_id|string|true|none|Internal UUID for this vocabulary (generated by the service)|
|scheme_iri|string|true|none|IRI of the skos:ConceptScheme|
|graph_iri|string|true|none|Named graph IRI where this vocabulary is stored|

<h2 id="tocS_CustomMetadata">CustomMetadata</h2>
<!-- backwards compatibility -->
<a id="schemacustommetadata"></a>
<a id="schema_CustomMetadata"></a>
<a id="tocScustommetadata"></a>
<a id="tocscustommetadata"></a>

```json
{
  "description": [
    {
      "value": "string",
      "language": "string"
    }
  ],
  "version_notes": [
    {
      "value": "string",
      "language": "string"
    }
  ],
  "author": [
    "string"
  ],
  "publisher": "string",
  "license": "string",
  "spatial": [
    "string"
  ],
  "theme": [
    "string"
  ],
  "frequency": "string",
  "language": [
    "string"
  ],
  "modified": "string",
  "access_url": "string",
  "download_url": "string",
  "status": "string",
  "documentation": [
    "string"
  ]
}

```

CustomMetadata

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_notes|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|license|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|spatial|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|theme|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|frequency|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|language|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modified|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_url|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|download_url|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|documentation|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_CustomMetadataListResponse">CustomMetadataListResponse</h2>
<!-- backwards compatibility -->
<a id="schemacustommetadatalistresponse"></a>
<a id="schema_CustomMetadataListResponse"></a>
<a id="tocScustommetadatalistresponse"></a>
<a id="tocscustommetadatalistresponse"></a>

```json
{
  "items": [
    {
      "identifier": "550e8400-e29b-41d4-a716-446655440000",
      "metadata": {
        "access_url": "http://data.dsb.com/ontology/DSD_1.0.0",
        "author": [
          "European Commission"
        ],
        "description": [
          {
            "language": "en",
            "value": "This module provides the definitions for the Core Assessment Vocabulary."
          },
          {
            "language": "es",
            "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
          },
          {
            "language": "eu",
            "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
          }
        ],
        "documentation": [
          "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
        ],
        "download_url": "https://ibestat.es/edatos/apis/structural-resources/v1.0/datastructures/IBESTAT/DSD_000001A_00001/01.000.xml",
        "frequency": "http://publications.europa.eu/resource/authority/frequency/NEVER",
        "language": [
          "http://publications.europa.eu/resource/authority/language/ENG"
        ],
        "license": "http://creativecommons.org/licenses/by-sa/4.0/",
        "modified": "2026-02-23",
        "publisher": "European Commission",
        "spatial": [
          "http://publications.europa.eu/resource/authority/country/EUR"
        ],
        "status": "http://publications.europa.eu/resource/authority/distribution-status/COMPLETED",
        "theme": [
          "http://publications.europa.eu/resource/authority/data-theme/GOVE"
        ],
        "version_notes": [
          {
            "language": "en",
            "value": "Version notes test."
          },
          {
            "language": "es",
            "value": "Prueba de notas de versión."
          },
          {
            "language": "eu",
            "value": "Proba-oharrak."
          }
        ]
      },
      "resource_extension": "https://www.iana.org/assignments/media-types/application/xml",
      "title": [
        {
          "language": "en",
          "value": "DSD"
        }
      ],
      "version_info": "1.0.0"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

CustomMetadataListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[CustomMetadataResponse](#schemacustommetadataresponse)]|true|none|List of datasets|
|total|integer|true|none|Total number of datasets|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_CustomMetadataResponse">CustomMetadataResponse</h2>
<!-- backwards compatibility -->
<a id="schemacustommetadataresponse"></a>
<a id="schema_CustomMetadataResponse"></a>
<a id="tocScustommetadataresponse"></a>
<a id="tocscustommetadataresponse"></a>

```json
{
  "identifier": "550e8400-e29b-41d4-a716-446655440000",
  "metadata": {
    "access_url": "http://data.dsb.com/ontology/DSD_1.0.0",
    "author": [
      "European Commission"
    ],
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      }
    ],
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ],
    "download_url": "https://ibestat.es/edatos/apis/structural-resources/v1.0/datastructures/IBESTAT/DSD_000001A_00001/01.000.xml",
    "frequency": "http://publications.europa.eu/resource/authority/frequency/NEVER",
    "language": [
      "http://publications.europa.eu/resource/authority/language/ENG"
    ],
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "modified": "2026-02-23",
    "publisher": "European Commission",
    "spatial": [
      "http://publications.europa.eu/resource/authority/country/EUR"
    ],
    "status": "http://publications.europa.eu/resource/authority/distribution-status/COMPLETED",
    "theme": [
      "http://publications.europa.eu/resource/authority/data-theme/GOVE"
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      }
    ]
  },
  "resource_extension": "https://www.iana.org/assignments/media-types/application/xml",
  "title": [
    {
      "language": "en",
      "value": "DSD"
    }
  ],
  "version_info": "1.0.0"
}

```

CustomMetadataResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|any|false|none|Dataset unique identifier (UUID)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_info|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resource_extension|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|metadata|[CustomMetadata](#schemacustommetadata)|true|none|none|

<h2 id="tocS_DataServiceCreate">DataServiceCreate</h2>
<!-- backwards compatibility -->
<a id="schemadataservicecreate"></a>
<a id="schema_DataServiceCreate"></a>
<a id="tocSdataservicecreate"></a>
<a id="tocsdataservicecreate"></a>

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ]
}

```

DataServiceCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|[[LocalizedString](#schemalocalizedstring)]|true|none|Title(s) of the data service (dct:title)|
|endpoint_url|string(uri)|true|none|URL of the service endpoint|
|applicable_legislation|any|false|none|Applicable legislation URIs (e.g., GDPR)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|endpoint_description|any|false|none|URL to endpoint description (e.g., OpenAPI specification)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|documentation|any|false|none|URL to documentation|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s) of the service (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serves_dataset|any|false|none|List of dataset URIs that this service provides access to|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DataServiceListResponse">DataServiceListResponse</h2>
<!-- backwards compatibility -->
<a id="schemadataservicelistresponse"></a>
<a id="schema_DataServiceListResponse"></a>
<a id="tocSdataservicelistresponse"></a>
<a id="tocsdataservicelistresponse"></a>

```json
{
  "items": [
    {
      "applicable_legislation": [
        "http://data.europa.eu/eli/reg/2016/679/oj"
      ],
      "created_at": "2025-01-15T10:30:00Z",
      "endpoint_url": "https://api.data.gov/sparql",
      "id": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
      "title": [
        {
          "language": "en",
          "value": "SPARQL Endpoint"
        }
      ],
      "updated_at": "2025-01-15T10:30:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

DataServiceListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[DataServiceResponse](#schemadataserviceresponse)]|true|none|List of data services|
|total|integer|true|none|Total number of data services|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_DataServiceResponse">DataServiceResponse</h2>
<!-- backwards compatibility -->
<a id="schemadataserviceresponse"></a>
<a id="schema_DataServiceResponse"></a>
<a id="tocSdataserviceresponse"></a>
<a id="tocsdataserviceresponse"></a>

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-15T10:30:00Z",
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying government datasets"
    }
  ],
  "documentation": "https://docs.data.gov/sparql",
  "endpoint_description": "https://api.data.gov/sparql/openapi.json",
  "endpoint_url": "https://api.data.gov/sparql",
  "id": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "serves_dataset": [
    "http://data.gov/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ],
  "updated_at": "2025-01-15T10:30:00Z"
}

```

DataServiceResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|[[LocalizedString](#schemalocalizedstring)]|true|none|Title(s) of the data service (dct:title)|
|endpoint_url|string(uri)|true|none|URL of the service endpoint|
|applicable_legislation|any|false|none|Applicable legislation URIs (e.g., GDPR)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|endpoint_description|any|false|none|URL to endpoint description (e.g., OpenAPI specification)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|documentation|any|false|none|URL to documentation|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s) of the service (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serves_dataset|any|false|none|List of dataset URIs that this service provides access to|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (URI) of the DataService|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DataServiceUpdate">DataServiceUpdate</h2>
<!-- backwards compatibility -->
<a id="schemadataserviceupdate"></a>
<a id="schema_DataServiceUpdate"></a>
<a id="tocSdataserviceupdate"></a>
<a id="tocsdataserviceupdate"></a>

```json
{
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "description": [
    {
      "language": "en",
      "value": "Public SPARQL endpoint for querying datasets"
    }
  ],
  "documentation": "https://example.com/docs",
  "endpoint_description": "https://example.com/openapi.json",
  "endpoint_url": "https://example.com/sparql",
  "serves_dataset": [
    "http://example.org/dataset/census-2024"
  ],
  "title": [
    {
      "language": "en",
      "value": "SPARQL Endpoint for Public Data"
    }
  ]
}

```

DataServiceUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Title(s) of the data service (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|endpoint_url|any|false|none|URL of the service endpoint|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation URIs|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|endpoint_description|any|false|none|URL to endpoint description|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|documentation|any|false|none|URL to documentation|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s) of the service (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serves_dataset|any|false|none|List of dataset URIs|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DatasetCreate">DatasetCreate</h2>
<!-- backwards compatibility -->
<a id="schemadatasetcreate"></a>
<a id="schema_DatasetCreate"></a>
<a id="tocSdatasetcreate"></a>
<a id="tocsdatasetcreate"></a>

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    },
    {
      "language": "en",
      "value": "Minor fix in metadata"
    }
  ]
}

```

DatasetCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|string|true|none|Identifier of the dataset (dct:identifier)|
|title|[[LocalizedString](#schemalocalizedstring)]|true|none|Title(s) of the dataset (dct:title)|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Description(s) of the dataset (dct:description)|
|type|any|false|none|Type IRI (dct:type)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|theme|[string]|true|none|Theme IRIs (dcat:theme)|
|access_rights|string|true|none|Access rights IRI (dcat:accessRights)|
|publisher|string|true|none|Publisher IRI (dct:publisher)|
|creator|any|false|none|Creator IRI (dct:creator)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modified|string(date-time)|true|none|Last modification date (dct:modified)|
|distributions|[string]|true|none|Distribution IRIs (dcat:distribution)|
|keywords|any|false|none|Keywords (dcat:keyword)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_notes|any|false|none|Version notes (adms:versionNotes)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|landing_page|any|false|none|Landing page IRI (dcat:landingPage)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_info|any|false|none|Version info (owl:versionInfo)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|frequency|any|false|none|Update frequency IRI (dct:accrualPeriodicity)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|language|any|false|none|Language IRI (dct:language)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|spatial|any|false|none|Spatial coverage IRIs (dct:spatial)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DatasetListResponse">DatasetListResponse</h2>
<!-- backwards compatibility -->
<a id="schemadatasetlistresponse"></a>
<a id="schema_DatasetListResponse"></a>
<a id="tocSdatasetlistresponse"></a>
<a id="tocsdatasetlistresponse"></a>

```json
{
  "items": [
    {
      "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
      "created_at": "2025-01-01T00:00:00Z",
      "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
      "description": [
        {
          "language": "en",
          "value": "Dataset example description"
        }
      ],
      "distributions": [
        "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
      ],
      "id": "http://data.dsb.com/dataset/550e8400-e29b-41d4-a716-446655440000",
      "identifier": "DS-001",
      "modified": "2025-01-01T00:00:00Z",
      "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
      "theme": [
        "http://data.dsb.com/vocab/concept/data-theme/ECON"
      ],
      "title": [
        {
          "language": "en",
          "value": "Dataset example"
        }
      ],
      "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

DatasetListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[DatasetResponse](#schemadatasetresponse)]|true|none|List of datasets|
|total|integer|true|none|Total number of datasets|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_DatasetOfferCreate">DatasetOfferCreate</h2>
<!-- backwards compatibility -->
<a id="schemadatasetoffercreate"></a>
<a id="schema_DatasetOfferCreate"></a>
<a id="tocSdatasetoffercreate"></a>
<a id="tocsdatasetoffercreate"></a>

```json
{
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ]
}

```

DatasetOfferCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|related_resource|[string]|true|none|IRIs of the datasets associated to the offer (dcat:relatedResource)|
|title|any|false|none|Offer title(s) (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Offer description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|string|true|none|Publisher agent IRI (dct:publisher)|

<h2 id="tocS_DatasetOfferListResponse">DatasetOfferListResponse</h2>
<!-- backwards compatibility -->
<a id="schemadatasetofferlistresponse"></a>
<a id="schema_DatasetOfferListResponse"></a>
<a id="tocSdatasetofferlistresponse"></a>
<a id="tocsdatasetofferlistresponse"></a>

```json
{
  "items": [
    {
      "created_at": "2026-01-01T00:00:00Z",
      "description": [
        {
          "language": "en",
          "value": "Offer for non-commercial research usage"
        }
      ],
      "id": "http://data.dsb.com/dataset_offer/550e8400-e29b-41d4-a716-446655440000",
      "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
      "related_resource": [
        "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111"
      ],
      "title": [
        {
          "language": "en",
          "value": "Research access offer"
        }
      ],
      "type": "OFFER",
      "updated_at": "2026-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

DatasetOfferListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[DatasetOfferResponse](#schemadatasetofferresponse)]|false|none|none|
|total|integer|true|none|none|
|page|integer|true|none|none|
|size|integer|true|none|none|
|pages|integer|true|none|none|

<h2 id="tocS_DatasetOfferResponse">DatasetOfferResponse</h2>
<!-- backwards compatibility -->
<a id="schemadatasetofferresponse"></a>
<a id="schema_DatasetOfferResponse"></a>
<a id="tocSdatasetofferresponse"></a>
<a id="tocsdatasetofferresponse"></a>

```json
{
  "created_at": "2026-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "Offer for non-commercial research usage"
    }
  ],
  "id": "http://data.dsb.com/dataset_offer/550e8400-e29b-41d4-a716-446655440000",
  "publisher": "http://data.dsb.com/participant/AG-PUBLISHER-001",
  "related_resource": [
    "http://data.dsb.com/dataset/11111111-1111-1111-1111-111111111111",
    "http://data.dsb.com/dataset/22222222-2222-2222-2222-222222222222"
  ],
  "title": [
    {
      "language": "en",
      "value": "Research access offer"
    }
  ],
  "type": "OFFER",
  "updated_at": "2026-01-01T00:00:00Z"
}

```

DatasetOfferResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|related_resource|[string]|true|none|IRIs of the datasets associated to the offer (dcat:relatedResource)|
|title|any|false|none|Offer title(s) (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Offer description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|string|true|none|Publisher agent IRI (dct:publisher)|
|id|string|true|none|Unique identifier (IRI) of the dataset offer|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|false|none|Entity type discriminator|

<h2 id="tocS_DatasetOfferUpdate">DatasetOfferUpdate</h2>
<!-- backwards compatibility -->
<a id="schemadatasetofferupdate"></a>
<a id="schema_DatasetOfferUpdate"></a>
<a id="tocSdatasetofferupdate"></a>
<a id="tocsdatasetofferupdate"></a>

```json
{
  "description": [
    {
      "language": "en",
      "value": "Updated offer description"
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "Updated offer title"
    }
  ]
}

```

DatasetOfferUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|related_resource|any|false|none|IRIs of the related datasets (dcat:relatedResource)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Offer title(s) (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Offer description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|any|false|none|Publisher agent IRI (dct:publisher)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DatasetResponse">DatasetResponse</h2>
<!-- backwards compatibility -->
<a id="schemadatasetresponse"></a>
<a id="schema_DatasetResponse"></a>
<a id="tocSdatasetresponse"></a>
<a id="tocsdatasetresponse"></a>

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "created_at": "2025-01-01T00:00:00Z",
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Dataset example description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "id": "http://data.dsb.com/dataset/550e8400-e29b-41d4-a716-446655440000",
  "identifier": "DS-001",
  "keywords": [
    "economy",
    "gdp",
    "open-data"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-01T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "quality_score": 145,
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON",
    "http://data.dsb.com/vocab/concept/data-theme/TECH"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example"
    }
  ],
  "type": "http://data.dsb.com/vocab/concept/resource-types/ONTOLOGY",
  "updated_at": "2025-01-01T00:00:00Z",
  "version_info": "1.0.0",
  "version_notes": [
    {
      "language": "en",
      "value": "Initial release"
    }
  ]
}

```

DatasetResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|string|true|none|Identifier of the dataset (dct:identifier)|
|title|[[LocalizedString](#schemalocalizedstring)]|true|none|Title(s) of the dataset (dct:title)|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Description(s) of the dataset (dct:description)|
|type|any|false|none|Type IRI (dct:type)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|theme|[string]|true|none|Theme IRIs (dcat:theme)|
|access_rights|string|true|none|Access rights IRI (dcat:accessRights)|
|publisher|string|true|none|Publisher IRI (dct:publisher)|
|creator|any|false|none|Creator IRI (dct:creator)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modified|string(date-time)|true|none|Last modification date (dct:modified)|
|distributions|[string]|true|none|Distribution IRIs (dcat:distribution)|
|keywords|any|false|none|Keywords (dcat:keyword)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_notes|any|false|none|Version notes (adms:versionNotes)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|landing_page|any|false|none|Landing page IRI (dcat:landingPage)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_info|any|false|none|Version info (owl:versionInfo)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|frequency|any|false|none|Update frequency IRI (dct:accrualPeriodicity)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|language|any|false|none|Language IRI (dct:language)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|spatial|any|false|none|Spatial coverage IRIs (dct:spatial)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (URI) of the Dataset|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|quality_score|any|false|none|Overall quality score (0-160) calculated by quality service|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DatasetUpdate">DatasetUpdate</h2>
<!-- backwards compatibility -->
<a id="schemadatasetupdate"></a>
<a id="schema_DatasetUpdate"></a>
<a id="tocSdatasetupdate"></a>
<a id="tocsdatasetupdate"></a>

```json
{
  "access_rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "creator": "http://data.dsb.com/agent/00000000-0000-0000-0000-000000000000",
  "description": [
    {
      "language": "en",
      "value": "Updated dataset description"
    }
  ],
  "distributions": [
    "http://data.dsb.com/distribution/00000000-0000-0000-0000-000000000000"
  ],
  "frequency": "http://data.dsb.com/vocab/concept/frequencies/ANNUAL",
  "keywords": [
    "economy",
    "update"
  ],
  "landing_page": "http://example.org/datasets/DS-001",
  "language": "http://data.dsb.com/vocab/concept/languages/ENG",
  "modified": "2025-01-02T00:00:00Z",
  "publisher": "http://data.dsb.com/participant/00000000-0000-0000-0000-000000000000",
  "spatial": [
    "http://data.dsb.com/vocab/concept/countries/EUR"
  ],
  "theme": [
    "http://data.dsb.com/vocab/concept/data-theme/ECON"
  ],
  "title": [
    {
      "language": "en",
      "value": "Dataset example (updated)"
    }
  ],
  "version_info": "1.0.1",
  "version_notes": [
    {
      "language": "en",
      "value": "Updated metadata"
    }
  ]
}

```

DatasetUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|any|false|none|Identifier of the dataset (dct:identifier)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Title(s) (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|any|false|none|Type IRI (dct:type)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|theme|any|false|none|Theme IRIs (dcat:theme)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_rights|any|false|none|Access rights IRI (dcat:accessRights)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|any|false|none|Publisher IRI (dct:publisher)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|creator|any|false|none|Creator IRI (dct:creator)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|modified|any|false|none|Last modification date (dct:modified)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|distributions|any|false|none|Distribution IRIs (dcat:distribution)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|keywords|any|false|none|Keywords (dcat:keyword)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_notes|any|false|none|Version notes (adms:versionNotes)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|landing_page|any|false|none|Landing page IRI (dcat:landingPage)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version_info|any|false|none|Version info (owl:versionInfo)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|frequency|any|false|none|Update frequency IRI (dct:accrualPeriodicity)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|language|any|false|none|Language IRI (dct:language)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|spatial|any|false|none|Spatial coverage IRIs (dct:spatial)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DeleteResult">DeleteResult</h2>
<!-- backwards compatibility -->
<a id="schemadeleteresult"></a>
<a id="schema_DeleteResult"></a>
<a id="tocSdeleteresult"></a>
<a id="tocsdeleteresult"></a>

```json
{
  "id": "string",
  "deleted": true,
  "cascades": [
    {}
  ],
  "message": "string"
}

```

DeleteResult

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|IRI of the entity requested to be deleted|
|deleted|boolean|true|none|True when the entity was deleted|
|cascades|[object]|false|none|List of cascade deletion actions performed by the service|
|message|any|false|none|Optional human-readable message|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DistributionCreate">DistributionCreate</h2>
<!-- backwards compatibility -->
<a id="schemadistributioncreate"></a>
<a id="schema_DistributionCreate"></a>
<a id="tocSdistributioncreate"></a>
<a id="tocsdistributioncreate"></a>

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000"
  ],
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ]
}

```

DistributionCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Title(s) of the distribution (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_url|string(uri)|true|none|Access URL of the distribution (dcat:accessURL)|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Description(s) of the distribution (dct:description)|
|format|string|true|none|Format IRI (dct:format). Typically a controlled vocabulary term.|
|rights|string|true|none|Rights IRI (dct:rights)|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|conforms_to|any|false|none|Standard IRI/URL (dct:conformsTo)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|Status concept IRI (adms:status)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_service|any|false|none|IRI of dcat:DataService used to access the Distribution (dcat:accessService)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|byte_size|any|false|none|Size in bytes (dcat:byteSize)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|has_policies|any|false|none|IRIs of existing ODRL policies (odrl:hasPolicy)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DistributionListResponse">DistributionListResponse</h2>
<!-- backwards compatibility -->
<a id="schemadistributionlistresponse"></a>
<a id="schema_DistributionListResponse"></a>
<a id="tocSdistributionlistresponse"></a>
<a id="tocsdistributionlistresponse"></a>

```json
{
  "items": [
    {
      "access_url": "https://data.example.org/files/dataset.csv",
      "created_at": "2025-01-01T00:00:00Z",
      "description": [
        {
          "language": "en",
          "value": "CSV export of the dataset"
        }
      ],
      "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
      "id": "http://data.dsb.com/distribution/550e8400-e29b-41d4-a716-446655440000",
      "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

DistributionListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[DistributionResponse](#schemadistributionresponse)]|true|none|List of distributions|
|total|integer|true|none|Total number of distributions|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_DistributionResponse">DistributionResponse</h2>
<!-- backwards compatibility -->
<a id="schemadistributionresponse"></a>
<a id="schema_DistributionResponse"></a>
<a id="tocSdistributionresponse"></a>
<a id="tocsdistributionresponse"></a>

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "created_at": "2025-01-01T00:00:00Z",
  "description": [
    {
      "language": "en",
      "value": "CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "id": "http://data.dsb.com/distribution/550e8400-e29b-41d4-a716-446655440000",
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV"
    }
  ],
  "updated_at": "2025-01-01T00:00:00Z"
}

```

DistributionResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Title(s) of the distribution (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_url|string(uri)|true|none|Access URL of the distribution (dcat:accessURL)|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Description(s) of the distribution (dct:description)|
|format|string|true|none|Format IRI (dct:format). Typically a controlled vocabulary term.|
|rights|string|true|none|Rights IRI (dct:rights)|
|applicable_legislation|any|false|none|Applicable legislation IRIs (dcatap:applicableLegislation)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|conforms_to|any|false|none|Standard IRI/URL (dct:conformsTo)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|Status concept IRI (adms:status)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_service|any|false|none|IRI of dcat:DataService used to access the Distribution (dcat:accessService)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|byte_size|any|false|none|Size in bytes (dcat:byteSize)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|has_policies|any|false|none|IRIs of existing ODRL policies (odrl:hasPolicy)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (URI) of the Distribution|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_DistributionUpdate">DistributionUpdate</h2>
<!-- backwards compatibility -->
<a id="schemadistributionupdate"></a>
<a id="schema_DistributionUpdate"></a>
<a id="tocSdistributionupdate"></a>
<a id="tocsdistributionupdate"></a>

```json
{
  "access_service": "http://data.dsb.com/dataservice/550e8400-e29b-41d4-a716-446655440000",
  "access_url": "https://data.example.org/files/dataset.csv",
  "applicable_legislation": [
    "http://data.europa.eu/eli/reg/2016/679/oj"
  ],
  "byte_size": 123456,
  "conforms_to": "https://example.org/standards/openapi",
  "description": [
    {
      "language": "en",
      "value": "Updated CSV export of the dataset"
    }
  ],
  "format": "http://publications.europa.eu/resource/authority/file-type/CSV",
  "has_policies": [
    "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000"
  ],
  "rights": "http://publications.europa.eu/resource/authority/access-right/PUBLIC",
  "status": "http://data.dsb.com/vocab/concept/distribution-status/COMPLETED",
  "title": [
    {
      "language": "en",
      "value": "Distribution CSV (v2)"
    }
  ]
}

```

DistributionUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|Title(s) (dct:title)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_url|any|false|none|Access URL (dcat:accessURL)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(uri)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|format|any|false|none|Format IRI (dct:format)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rights|any|false|none|Rights (dct:rights)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|applicable_legislation|any|false|none|dcatap:applicableLegislation|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|conforms_to|any|false|none|dct:conformsTo|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|adms:status concept IRI|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_service|any|false|none|dcat:accessService IRI|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|byte_size|any|false|none|dcat:byteSize|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|number|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|has_policies|any|false|none|odrl:hasPolicy IRIs|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_HealthcheckOutput">HealthcheckOutput</h2>
<!-- backwards compatibility -->
<a id="schemahealthcheckoutput"></a>
<a id="schema_HealthcheckOutput"></a>
<a id="tocShealthcheckoutput"></a>
<a id="tocshealthcheckoutput"></a>

```json
{
  "message": "Health check successful.",
  "status": true
}

```

HealthcheckOutput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|boolean|true|none|none|
|message|string|true|none|none|

<h2 id="tocS_IngestionIntegrationInput">IngestionIntegrationInput</h2>
<!-- backwards compatibility -->
<a id="schemaingestionintegrationinput"></a>
<a id="schema_IngestionIntegrationInput"></a>
<a id="tocSingestionintegrationinput"></a>
<a id="tocsingestionintegrationinput"></a>

```json
{
  "type": "ONTOLOGY",
  "resource_url": "http://publications.europa.eu/resource/distribution/eurio/20260204-0/ttl/owl/EURIO.ttl",
  "resource_file": "",
  "title": [
    {
      "language": "en",
      "value": "EURIO"
    }
  ],
  "version_info": "1.0.0",
  "resource_extension": "TTL",
  "metadata": {
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      }
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      }
    ],
    "author": [
      "European Commission"
    ],
    "publisher": "European Commission",
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "spatial": [
      "EUR"
    ],
    "theme": [
      "GOVE"
    ],
    "frequency": "NEVER",
    "language": [
      "ENG"
    ],
    "status": "COMPLETED",
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ]
  }
}

```

IngestionIntegrationInput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|type|string|true|none|Resource types. Possible values: {ResourceType.list_no_none()}|
|resource_url|any|false|none|URL of the resource to be downloaded. Mandatory if resource file is empty.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resource_file|any|false|none|File of the resource in base64 to be processed. Mandatory if resource URL is empty.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|[object]|false|none|Resource name to integrate. It is used during the insertion of the resource to semantic database.|
|version_info|string|true|none|Resource version to integrate. It is used during the insertion of the resource to semantic database.|
|resource_extension|string|true|none|Extension of the resource file that will be downloaded.|
|metadata|any|false|none|DCAT metadata applied to the resource.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[MetadataModel](#schemametadatamodel)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_IngestionIntegrationOutput">IngestionIntegrationOutput</h2>
<!-- backwards compatibility -->
<a id="schemaingestionintegrationoutput"></a>
<a id="schema_IngestionIntegrationOutput"></a>
<a id="tocSingestionintegrationoutput"></a>
<a id="tocsingestionintegrationoutput"></a>

```json
{
  "status": "VALID",
  "message": "Ingestion_integration successful. All resources were ingested and integrated.",
  "resource_hash": "string"
}

```

IngestionIntegrationOutput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|true|none|Status of the resource in the data ingestion and integration process.|
|message|string|true|none|Result in text.|
|resource_hash|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_LocalizedString">LocalizedString</h2>
<!-- backwards compatibility -->
<a id="schemalocalizedstring"></a>
<a id="schema_LocalizedString"></a>
<a id="tocSlocalizedstring"></a>
<a id="tocslocalizedstring"></a>

```json
{
  "value": "string",
  "language": "string"
}

```

LocalizedString

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|string|true|none|none|
|language|string|true|none|none|

<h2 id="tocS_MetadataModel">MetadataModel</h2>
<!-- backwards compatibility -->
<a id="schemametadatamodel"></a>
<a id="schema_MetadataModel"></a>
<a id="tocSmetadatamodel"></a>
<a id="tocsmetadatamodel"></a>

```json
{
  "description": [
    {
      "language": "en",
      "value": "This module provides the definitions for the Core Assessment Vocabulary."
    },
    {
      "language": "eu",
      "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
    },
    {
      "language": "es",
      "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
    }
  ],
  "version_notes": [
    {
      "language": "en",
      "value": "Version notes test."
    },
    {
      "language": "eu",
      "value": "Proba-oharrak."
    },
    {
      "language": "es",
      "value": "Prueba de notas de versión."
    }
  ],
  "author": [
    "European Commission"
  ],
  "publisher": "European Commission",
  "license": "http://creativecommons.org/licenses/by-sa/4.0/",
  "spatial": [
    "EUR"
  ],
  "theme": [
    "GOVE"
  ],
  "frequency": "NEVER",
  "language": [
    "ENG"
  ],
  "status": "COMPLETED",
  "documentation": [
    "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
  ]
}

```

MetadataModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|[[LocalizedString](#schemalocalizedstring)]|true|none|Metadata description.|
|version_notes|any|false|none|Possible differences between this version and a previous version.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|any|false|none|Entity responsible for producing the resource.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|publisher|string|true|none|Entity responsible for making the resource available.|
|license|any|false|none|License under the resource is made available.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|spatial|any|false|none|Country covered by the resource.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|theme|any|false|none|Theme of the resource.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|frequency|any|false|none|Frequency the resource is updated.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|language|any|false|none|Language used in the resource.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|Resource status.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|documentation|any|false|none|URL web page that provides access to the resource and give more information.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[any]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_MetadataUpdateInput">MetadataUpdateInput</h2>
<!-- backwards compatibility -->
<a id="schemametadataupdateinput"></a>
<a id="schema_MetadataUpdateInput"></a>
<a id="tocSmetadataupdateinput"></a>
<a id="tocsmetadataupdateinput"></a>

```json
{
  "resource_id": "26c9c211-d693-434f-9155-27689becc8c8",
  "metadata": {
    "title": [
      {
        "language": "en",
        "value": "Core Assessment Vocabulary (CAV)."
      },
      {
        "language": "eu",
        "value": "Oinarrizko ebaluazio hiztegia (CAV)."
      },
      {
        "language": "es",
        "value": "Vocabulario básico de evaluación (CAV)."
      }
    ],
    "version_info": "6.2.0",
    "description": [
      {
        "language": "en",
        "value": "This module provides the definitions for the Core Assessment Vocabulary."
      },
      {
        "language": "eu",
        "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
      },
      {
        "language": "es",
        "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
      }
    ],
    "version_notes": [
      {
        "language": "en",
        "value": "Version notes test."
      },
      {
        "language": "eu",
        "value": "Proba-oharrak."
      },
      {
        "language": "es",
        "value": "Prueba de notas de versión."
      }
    ],
    "author": [
      "European Commission"
    ],
    "publisher": "European Commission",
    "license": "http://creativecommons.org/licenses/by-sa/4.0/",
    "spatial": [
      "EUR"
    ],
    "theme": [
      "GOVE"
    ],
    "frequency": "NEVER",
    "language": [
      "ENG"
    ],
    "status": "COMPLETED",
    "documentation": [
      "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
    ]
  }
}

```

MetadataUpdateInput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|resource_id|string|true|none|Resource identifier whose metadata is to be updated.|
|metadata|any|false|none|The metadata of the resource to be updated.|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[UpdateMetadataInput](#schemaupdatemetadatainput)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_MetadataUpdateResponse">MetadataUpdateResponse</h2>
<!-- backwards compatibility -->
<a id="schemametadataupdateresponse"></a>
<a id="schema_MetadataUpdateResponse"></a>
<a id="tocSmetadataupdateresponse"></a>
<a id="tocsmetadataupdateresponse"></a>

```json
{
  "status": "VALID",
  "message": "Metadata updated successfully."
}

```

MetadataUpdateResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|true|none|Status of the metadata updating process.|
|message|string|true|none|Result in text.|

<h2 id="tocS_OdrlConstraint">OdrlConstraint</h2>
<!-- backwards compatibility -->
<a id="schemaodrlconstraint"></a>
<a id="schema_OdrlConstraint"></a>
<a id="tocSodrlconstraint"></a>
<a id="tocsodrlconstraint"></a>

```json
{
  "left_operand": "string",
  "operator": "string",
  "right_operand": "string"
}

```

OdrlConstraint

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|left_operand|string|true|none|odrl:leftOperand IRI|
|operator|string|true|none|odrl:operator IRI|
|right_operand|string|true|none|odrl:rightOperand literal value (string/date/integer encoded as string)|

<h2 id="tocS_OdrlOfferCreate">OdrlOfferCreate</h2>
<!-- backwards compatibility -->
<a id="schemaodrloffercreate"></a>
<a id="schema_OdrlOfferCreate"></a>
<a id="tocSodrloffercreate"></a>
<a id="tocsodrloffercreate"></a>

```json
{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "description": [
    {
      "language": "en",
      "value": "Allow use of CSV dataset"
    }
  ],
  "obligations": [
    {
      "action": "http://www.w3.org/ns/odrl/2/attribute",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "prohibitions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/distribute",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "commercial"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "title": [
    {
      "language": "en",
      "value": "Policy for Distribution CSV"
    }
  ]
}

```

OdrlOfferCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assigner|string|true|none|odrl:assigner IRI|
|target|string|true|none|odrl:target (DatasetOffer IRI)|
|permissions|any|false|none|odrl:permission rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|obligations|any|false|none|odrl:obligation rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prohibitions|any|false|none|odrl:prohibition rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|dct:title language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|dct:description language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlOfferListResponse">OdrlOfferListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaodrlofferlistresponse"></a>
<a id="schema_OdrlOfferListResponse"></a>
<a id="tocSodrlofferlistresponse"></a>
<a id="tocsodrlofferlistresponse"></a>

```json
{
  "items": [
    {
      "assigner": "http://data.dsb.com/participant/AG-001",
      "created_at": "2025-01-01T00:00:00Z",
      "id": "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000",
      "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
      "updated_at": "2025-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

OdrlOfferListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[OdrlOfferResponse](#schemaodrlofferresponse)]|true|none|none|
|total|integer|true|none|none|
|page|integer|true|none|none|
|size|integer|true|none|none|
|pages|integer|true|none|none|

<h2 id="tocS_OdrlOfferResponse">OdrlOfferResponse</h2>
<!-- backwards compatibility -->
<a id="schemaodrlofferresponse"></a>
<a id="schema_OdrlOfferResponse"></a>
<a id="tocSodrlofferresponse"></a>
<a id="tocsodrlofferresponse"></a>

```json
{
  "assigner": "http://data.dsb.com/participant/AG-001",
  "created_at": "2025-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "assignee": "http://data.dsb.com/agent/USER-123",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/dateTime",
          "operator": "http://www.w3.org/ns/odrl/2/lt",
          "right_operand": "2025-12-31T23:59:59Z"
        }
      ]
    }
  ],
  "target": "http://data.dsb.com/dataset_offer/2b666b7e-709e-4fac-b5a6-9b1041708445",
  "updated_at": "2025-01-01T00:00:00Z"
}

```

OdrlOfferResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assigner|string|true|none|odrl:assigner IRI|
|target|string|true|none|odrl:target (DatasetOffer IRI)|
|permissions|any|false|none|odrl:permission rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|obligations|any|false|none|odrl:obligation rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prohibitions|any|false|none|odrl:prohibition rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|dct:title language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|dct:description language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Policy (Offer) URI|
|created_at|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlOfferUpdate">OdrlOfferUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaodrlofferupdate"></a>
<a id="schema_OdrlOfferUpdate"></a>
<a id="tocSodrlofferupdate"></a>
<a id="tocsodrlofferupdate"></a>

```json
{
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/spatial",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "ES"
        }
      ]
    }
  ]
}

```

OdrlOfferUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assigner|any|false|none|odrl:assigner IRI|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|target|any|false|none|odrl:target (DatasetOffer IRI)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|permissions|any|false|none|odrl:permission rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|obligations|any|false|none|odrl:obligation rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prohibitions|any|false|none|odrl:prohibition rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlRule](#schemaodrlrule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|dct:title language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|dct:description language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlPolicyTemplateCreate">OdrlPolicyTemplateCreate</h2>
<!-- backwards compatibility -->
<a id="schemaodrlpolicytemplatecreate"></a>
<a id="schema_OdrlPolicyTemplateCreate"></a>
<a id="tocSodrlpolicytemplatecreate"></a>
<a id="tocsodrlpolicytemplatecreate"></a>

```json
{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "description": [
    {
      "language": "en",
      "value": "Allow use of CSV dataset"
    }
  ],
  "obligations": [
    {
      "action": "http://www.w3.org/ns/odrl/2/attribute",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/delayPeriod",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "Required"
        }
      ]
    }
  ],
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "prohibitions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/commercialize",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "commercial"
        }
      ]
    }
  ],
  "title": [
    {
      "language": "en",
      "value": "Policy for Distribution CSV"
    }
  ]
}

```

OdrlPolicyTemplateCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assigner|string|true|none|odrl:assigner IRI|
|permissions|any|false|none|odrl:permission rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|obligations|any|false|none|odrl:obligation rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prohibitions|any|false|none|odrl:prohibition rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|dct:title language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|dct:description language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlPolicyTemplateListResponse">OdrlPolicyTemplateListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaodrlpolicytemplatelistresponse"></a>
<a id="schema_OdrlPolicyTemplateListResponse"></a>
<a id="tocSodrlpolicytemplatelistresponse"></a>
<a id="tocsodrlpolicytemplatelistresponse"></a>

```json
{
  "items": [
    {
      "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
      "created_at": "2026-01-01T00:00:00Z",
      "id": "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000",
      "obligations": [],
      "permissions": [],
      "prohibitions": [],
      "updated_at": "2026-01-01T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

OdrlPolicyTemplateListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[OdrlPolicyTemplateResponse](#schemaodrlpolicytemplateresponse)]|true|none|none|
|total|integer|true|none|none|
|page|integer|true|none|none|
|size|integer|true|none|none|
|pages|integer|true|none|none|

<h2 id="tocS_OdrlPolicyTemplateResponse">OdrlPolicyTemplateResponse</h2>
<!-- backwards compatibility -->
<a id="schemaodrlpolicytemplateresponse"></a>
<a id="schema_OdrlPolicyTemplateResponse"></a>
<a id="tocSodrlpolicytemplateresponse"></a>
<a id="tocsodrlpolicytemplateresponse"></a>

```json
{
  "assigner": "http://data.dsb.com/participant/AG-LEGAL-001",
  "created_at": "2026-01-01T00:00:00Z",
  "id": "http://data.dsb.com/policy_template/550e8400-e29b-41d4-a716-446655440000",
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/purpose",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "research"
        }
      ]
    }
  ],
  "updated_at": "2026-01-01T00:00:00Z"
}

```

OdrlPolicyTemplateResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assigner|string|true|none|odrl:assigner IRI|
|permissions|any|false|none|odrl:permission rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|obligations|any|false|none|odrl:obligation rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prohibitions|any|false|none|odrl:prohibition rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|dct:title language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|dct:description language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Policy template URI|
|created_at|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlPolicyTemplateUpdate">OdrlPolicyTemplateUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaodrlpolicytemplateupdate"></a>
<a id="schema_OdrlPolicyTemplateUpdate"></a>
<a id="tocSodrlpolicytemplateupdate"></a>
<a id="tocsodrlpolicytemplateupdate"></a>

```json
{
  "permissions": [
    {
      "action": "http://www.w3.org/ns/odrl/2/read",
      "constraints": [
        {
          "left_operand": "http://www.w3.org/ns/odrl/2/spatial",
          "operator": "http://www.w3.org/ns/odrl/2/eq",
          "right_operand": "ES"
        }
      ]
    }
  ]
}

```

OdrlPolicyTemplateUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assigner|any|false|none|odrl:assigner IRI|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|permissions|any|false|none|odrl:permission rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|obligations|any|false|none|odrl:obligation rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|prohibitions|any|false|none|odrl:prohibition rules|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlTemplateRule](#schemaodrltemplaterule)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|any|false|none|dct:title language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|dct:description language-tagged literals|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlRule">OdrlRule</h2>
<!-- backwards compatibility -->
<a id="schemaodrlrule"></a>
<a id="schema_OdrlRule"></a>
<a id="tocSodrlrule"></a>
<a id="tocsodrlrule"></a>

```json
{
  "action": "string",
  "assignee": "string",
  "constraints": [
    {
      "left_operand": "string",
      "operator": "string",
      "right_operand": "string"
    }
  ]
}

```

OdrlRule

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|action|string|true|none|odrl:action absolute IRI (e.g., http://www.w3.org/ns/odrl/2/read)|
|assignee|any|false|none|odrl:assignee absolute IRI (optional)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|constraints|any|false|none|Optional constraints|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlConstraint](#schemaodrlconstraint)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_OdrlTemplateRule">OdrlTemplateRule</h2>
<!-- backwards compatibility -->
<a id="schemaodrltemplaterule"></a>
<a id="schema_OdrlTemplateRule"></a>
<a id="tocSodrltemplaterule"></a>
<a id="tocsodrltemplaterule"></a>

```json
{
  "action": "string",
  "constraints": [
    {
      "left_operand": "string",
      "operator": "string",
      "right_operand": "string"
    }
  ]
}

```

OdrlTemplateRule

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|action|string|true|none|odrl:action absolute IRI|
|constraints|any|false|none|Optional constraints|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[OdrlConstraint](#schemaodrlconstraint)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantAddress">ParticipantAddress</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantaddress"></a>
<a id="schema_ParticipantAddress"></a>
<a id="tocSparticipantaddress"></a>
<a id="tocsparticipantaddress"></a>

```json
{
  "adminUnit1": "string",
  "adminUnit2": "string",
  "fullAddress": "string",
  "postCode": "string",
  "postName": "string"
}

```

ParticipantAddress

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|adminUnit1|any|false|none|Admin unit L1 (country)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|adminUnit2|any|false|none|Admin unit L2 (region)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fullAddress|any|false|none|Full address|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|postCode|any|false|none|Postal code|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|postName|any|false|none|Post name|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantConnectorRef">ParticipantConnectorRef</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantconnectorref"></a>
<a id="schema_ParticipantConnectorRef"></a>
<a id="tocSparticipantconnectorref"></a>
<a id="tocsparticipantconnectorref"></a>

```json
{
  "identifier": "string",
  "status": "ACTIVE"
}

```

ParticipantConnectorRef

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|string|true|none|Connector identifier|
|status|any|false|none|Connector relation status|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantStatus](#schemaparticipantstatus)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantContactPoint">ParticipantContactPoint</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantcontactpoint"></a>
<a id="schema_ParticipantContactPoint"></a>
<a id="tocSparticipantcontactpoint"></a>
<a id="tocsparticipantcontactpoint"></a>

```json
{
  "email": "string",
  "telephone": "string",
  "openingHours": "string"
}

```

ParticipantContactPoint

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|any|false|none|Contact email|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|telephone|any|false|none|Contact telephone|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|openingHours|any|false|none|Opening hours|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantCreate">ParticipantCreate</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantcreate"></a>
<a id="schema_ParticipantCreate"></a>
<a id="tocSparticipantcreate"></a>
<a id="tocsparticipantcreate"></a>

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE"
}

```

ParticipantCreate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|Participant status|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantStatus](#schemaparticipantstatus)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|any|false|none|External identifiers (adms:Identifier)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ParticipantIdentifier](#schemaparticipantidentifier)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|preferredLabel|[[LocalizedString](#schemalocalizedstring)]|true|none|Preferred label(s) (skos:prefLabel)|
|description|any|false|none|Description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|classification|any|false|none|Classification(s) (org:classification)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|purpose|any|false|none|Purpose(s) (org:purpose)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|any|false|none|Address|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantAddress](#schemaparticipantaddress)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|contactPoint|any|false|none|Contact point|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantContactPoint](#schemaparticipantcontactpoint)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connector|any|false|none|Connector relations|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ParticipantConnectorRef](#schemaparticipantconnectorref)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantIdentifier">ParticipantIdentifier</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantidentifier"></a>
<a id="schema_ParticipantIdentifier"></a>
<a id="tocSparticipantidentifier"></a>
<a id="tocsparticipantidentifier"></a>

```json
{
  "notation": "string",
  "schemeURI": "string",
  "schemeName": {
    "value": "string",
    "language": "string"
  }
}

```

ParticipantIdentifier

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|notation|string|true|none|Identifier notation (skos:notation)|
|schemeURI|any|false|none|Scheme URI (skos:inScheme)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|schemeName|any|false|none|Scheme label (skos:prefLabel)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[LocalizedString](#schemalocalizedstring)|false|none|Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantListResponse">ParticipantListResponse</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantlistresponse"></a>
<a id="schema_ParticipantListResponse"></a>
<a id="tocSparticipantlistresponse"></a>
<a id="tocsparticipantlistresponse"></a>

```json
{
  "items": [
    {
      "address": {
        "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
        "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
        "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
        "postCode": "28021",
        "postName": "Madrid"
      },
      "classification": [
        "http://publications.europa.eu/resource/authority/organization-type/MIN"
      ],
      "connector": [
        {
          "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
          "status": "ACTIVE"
        }
      ],
      "contactPoint": {
        "email": "atencionalaciudadania@digital.gob.es",
        "openingHours": "Mo-Fr 09:00-14:00",
        "telephone": "+34911596128"
      },
      "created_at": "2026-03-10T00:00:00Z",
      "description": [
        {
          "language": "es",
          "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
        }
      ],
      "id": "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000",
      "identifier": [
        {
          "notation": "E05068901",
          "schemeName": {
            "language": "es",
            "value": "Identificación de los organismos públicos"
          },
          "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
        }
      ],
      "preferredLabel": [
        {
          "language": "es",
          "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
        }
      ],
      "purpose": [
        "http://data.europa.eu/7yx/cofog/01.1.1"
      ],
      "status": "ACTIVE",
      "updated_at": "2026-03-10T00:00:00Z"
    }
  ],
  "page": 1,
  "pages": 1,
  "size": 10,
  "total": 1
}

```

ParticipantListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[ParticipantResponse](#schemaparticipantresponse)]|true|none|List of participants|
|total|integer|true|none|Total number of participants|
|page|integer|true|none|Current page number|
|size|integer|true|none|Page size|
|pages|integer|true|none|Total number of pages|

<h2 id="tocS_ParticipantResponse">ParticipantResponse</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantresponse"></a>
<a id="schema_ParticipantResponse"></a>
<a id="tocSparticipantresponse"></a>
<a id="tocsparticipantresponse"></a>

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "created_at": "2026-03-10T00:00:00Z",
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "id": "http://data.dsb.com/participant/550e8400-e29b-41d4-a716-446655440000",
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE",
  "updated_at": "2026-03-10T00:00:00Z"
}

```

ParticipantResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|Participant status|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantStatus](#schemaparticipantstatus)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|any|false|none|External identifiers (adms:Identifier)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ParticipantIdentifier](#schemaparticipantidentifier)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|preferredLabel|[[LocalizedString](#schemalocalizedstring)]|true|none|Preferred label(s) (skos:prefLabel)|
|description|any|false|none|Description(s) (dct:description)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|classification|any|false|none|Classification(s) (org:classification)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|purpose|any|false|none|Purpose(s) (org:purpose)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|any|false|none|Address|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantAddress](#schemaparticipantaddress)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|contactPoint|any|false|none|Contact point|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantContactPoint](#schemaparticipantcontactpoint)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connector|any|false|none|Connector relations|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ParticipantConnectorRef](#schemaparticipantconnectorref)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|true|none|Unique identifier (URI) of the Participant|
|created_at|any|false|none|Creation timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|updated_at|any|false|none|Last update timestamp|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string(date-time)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ParticipantStatus">ParticipantStatus</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantstatus"></a>
<a id="schema_ParticipantStatus"></a>
<a id="tocSparticipantstatus"></a>
<a id="tocsparticipantstatus"></a>

```json
"ACTIVE"

```

ParticipantStatus

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|ParticipantStatus|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|ParticipantStatus|ACTIVE|
|ParticipantStatus|INACTIVE|
|ParticipantStatus|PENDING|
|ParticipantStatus|SUSPENDED|

<h2 id="tocS_ParticipantUpdate">ParticipantUpdate</h2>
<!-- backwards compatibility -->
<a id="schemaparticipantupdate"></a>
<a id="schema_ParticipantUpdate"></a>
<a id="tocSparticipantupdate"></a>
<a id="tocsparticipantupdate"></a>

```json
{
  "address": {
    "adminUnit1": "http://data.dsb.com/vocab/concept/countries/ESP",
    "adminUnit2": "http://data.dsb.com/vocab/concept/provincias/MADRID",
    "fullAddress": "C/ Poeta Joan Maragall nº 41, Madrid 28020",
    "postCode": "28021",
    "postName": "Madrid"
  },
  "classification": [
    "http://publications.europa.eu/resource/authority/organization-type/MIN"
  ],
  "connector": [
    {
      "identifier": "0cc5ffe6-19cd-413d-b1f5-41d9a9528e8f",
      "status": "ACTIVE"
    }
  ],
  "contactPoint": {
    "email": "atencionalaciudadania@digital.gob.es",
    "openingHours": "Mo-Fr 09:00-14:00",
    "telephone": "+34911596128"
  },
  "description": [
    {
      "language": "es",
      "value": "La Secretaría de Estado de Digitalización e Inteligencia Artificial..."
    }
  ],
  "identifier": [
    {
      "notation": "E05068901",
      "schemeName": {
        "language": "es",
        "value": "Identificación de los organismos públicos"
      },
      "schemeURI": "http://datos.gob.es/recurso/sector-publico/org/Organismo"
    }
  ],
  "preferredLabel": [
    {
      "language": "es",
      "value": "Secretaría de Estado de Digitalización e Inteligencia Artificial."
    }
  ],
  "purpose": [
    "http://data.europa.eu/7yx/cofog/01.1.1"
  ],
  "status": "ACTIVE"
}

```

ParticipantUpdate

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|false|none|Participant status|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantStatus](#schemaparticipantstatus)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identifier|any|false|none|External identifiers|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ParticipantIdentifier](#schemaparticipantidentifier)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|preferredLabel|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|any|false|none|Description(s)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[LocalizedString](#schemalocalizedstring)]|false|none|[Represents an RDF language-tagged literal: { value, language }.<br><br>`language` should be a BCP47 language tag (e.g. 'en', 'es', 'es-ES').]|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|classification|any|false|none|Classification(s)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|purpose|any|false|none|Purpose(s)|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|any|false|none|Address|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantAddress](#schemaparticipantaddress)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|contactPoint|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[ParticipantContactPoint](#schemaparticipantcontactpoint)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connector|any|false|none|Connector relations|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[ParticipantConnectorRef](#schemaparticipantconnectorref)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_UpdateMetadataInput">UpdateMetadataInput</h2>
<!-- backwards compatibility -->
<a id="schemaupdatemetadatainput"></a>
<a id="schema_UpdateMetadataInput"></a>
<a id="tocSupdatemetadatainput"></a>
<a id="tocsupdatemetadatainput"></a>

```json
{
  "title": [
    {
      "language": "en",
      "value": "Core Assessment Vocabulary (CAV)."
    },
    {
      "language": "eu",
      "value": "Oinarrizko ebaluazio hiztegia (CAV)."
    },
    {
      "language": "es",
      "value": "Vocabulario básico de evaluación (CAV)."
    }
  ],
  "version_info": "6.2.0",
  "description": [
    {
      "language": "en",
      "value": "This module provides the definitions for the Core Assessment Vocabulary."
    },
    {
      "language": "eu",
      "value": "Modulu honek oinarrizko ebaluazio-hiztegiaren definizioak eskaintzen ditu."
    },
    {
      "language": "es",
      "value": "Este módulo proporciona las definiciones del vocabulario básico de evaluación."
    }
  ],
  "version_notes": [
    {
      "language": "en",
      "value": "Version notes test."
    },
    {
      "language": "eu",
      "value": "Proba-oharrak."
    },
    {
      "language": "es",
      "value": "Prueba de notas de versión."
    }
  ],
  "author": [
    "European Commission"
  ],
  "publisher": "European Commission",
  "license": "http://creativecommons.org/licenses/by-sa/4.0/",
  "spatial": [
    "EUR"
  ],
  "theme": [
    "GOVE"
  ],
  "frequency": "NEVER",
  "language": [
    "ENG"
  ],
  "status": "COMPLETED",
  "documentation": [
    "https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/core-assessment-vocabulary-cav"
  ]
}

```

UpdateMetadataInput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|title|[[LocalizedString](#schemalocalizedstring)]|false|none|String indicating the resource title.|
|version_info|string|false|none|Resource version indicator.|
|description|[[LocalizedString](#schemalocalizedstring)]|false|none|Metadata description.|
|version_notes|[[LocalizedString](#schemalocalizedstring)]|false|none|Possible differences between this version and a previous version.|
|author|[any]|false|none|Entity responsible for producing the resource.|
|publisher|string|false|none|Entity responsible for making the resource available.|
|license|string|false|none|License under the resource is made available.|
|spatial|[any]|false|none|Country covered by the resource.|
|theme|[any]|false|none|Theme of the resource.|
|frequency|string|false|none|Frequency the resource is updated.|
|language|[any]|false|none|Language used in the resource.|
|status|string|false|none|Resource status.|
|documentation|[any]|false|none|URL web page that provides access to the resource and give more information.|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_VocabularyEntry">VocabularyEntry</h2>
<!-- backwards compatibility -->
<a id="schemavocabularyentry"></a>
<a id="schema_VocabularyEntry"></a>
<a id="tocSvocabularyentry"></a>
<a id="tocsvocabularyentry"></a>

```json
{
  "code": "string",
  "label": "string",
  "concept_iri": "string"
}

```

VocabularyEntry

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|string|true|none|Concept code (e.g., ISO-639-3 in 3 letters)|
|label|any|false|none|Preferred label in the requested language|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|concept_iri|any|false|none|Concept IRI|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_VocabularyEntryListResponse">VocabularyEntryListResponse</h2>
<!-- backwards compatibility -->
<a id="schemavocabularyentrylistresponse"></a>
<a id="schema_VocabularyEntryListResponse"></a>
<a id="tocSvocabularyentrylistresponse"></a>
<a id="tocsvocabularyentrylistresponse"></a>

```json
{
  "items": [
    {
      "code": "string",
      "label": "string",
      "concept_iri": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "size": 0,
  "pages": 0
}

```

VocabularyEntryListResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|items|[[VocabularyEntry](#schemavocabularyentry)]|true|none|[A single concept lookup entry.]|
|total|integer|true|none|none|
|page|integer|true|none|none|
|size|integer|true|none|none|
|pages|integer|true|none|none|

