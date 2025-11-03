# NPI LIST API DOCUMENTATION

# Important notice

PulsePoint API documentation has a new home! [Link](https://pulsepoint-platform.readme.io/docs/getting-started#/) 

This platform provides guides explaining how each endpoint works as well as the different fields supported. The API Reference tab can be used to test each endpoint right in the app. You can authenticate using your UN/PW and Key and Secret provided by your account manager.

We will be deprecating these Github docs by the end of the year (December 31, 2025).

Please reach out with any questions!


## INTRODUCTION

PulsePoint's clients use NPI lists for campaign targeting. These lists can change often and are customizable by each client. Clients now have direct access and complete control of their standard NPI lists and NPI lists with attributes via the NPI List API.

This document describes the functionality supported by the NPI List API. PulsePoint provides a REST API to access and manage the following actions for two different types of NPI lists:

### NPI LISTS

1. [Get an NPIs lists](#1-get-an-npi-list)
2. [Get all NPI list](#2-get-all-npi-lists)
3. [Create an NPI list](#3-create-an-npi-list)
4. [Replace NPIs in a list](#4-replace-npis-in-a-list)
5. [Add NPIs into a list](#5-add-npis-to-a-list)
6. [Delete NPIs from a list](#6-delete-npis-from-a-list)

### NPI lists with attributes

1. [Create an NPI list with attributes](#1-create-npi-list-with-attributes)
2. [Replace an NPI list with attributes](#2-replace-npi-list-with-attributes)
3. [View an NPI list with attributes](#3-view-npi-list-with-attributes)

---

All examples in this documentation use the `curl` command line tool: `http://curl.haxx.se/` Note that for all statements including `<username>:<password>` and `<client_secret>` you will need to replace with your Life username and password and client_secret respectively.

## Potential Error codes

| Code                                                                                      | Description           |
| ----------------------------------------------------------------------------------------- | --------------------- |
| ![400 BAD_REQUEST](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)           | BAD_REQUEST           |
| ![401 UNAUTHORIZED](https://img.shields.io/badge/401-f93e3e?style=for-the-badge)          | UNAUTHORIZED          |
| ![403 FORBIDDEN](https://img.shields.io/badge/403-f93e3e?style=for-the-badge)             | FORBIDDEN             |
| ![405 METHOD_NOT_ALLOWED](https://img.shields.io/badge/405-f93e3e?style=for-the-badge)    | METHOD_NOT_ALLOWED    |
| ![408 REQUEST_TIMEOUT](https://img.shields.io/badge/408-f93e3e?style=for-the-badge)       | REQUEST_TIMEOUT       |
| ![429 TOO_MANY_REQUESTS](https://img.shields.io/badge/429-f93e3e?style=for-the-badge)     | TOO_MANY_REQUESTS     |
| ![500 INTERNAL_SERVER_ERROR](https://img.shields.io/badge/500-f93e3e?style=for-the-badge) | INTERNAL_SERVER_ERROR |

## NPI API ENDPOINTS, NPI ONLY LISTS

### 1. Get an NPI list

This endpoint allows clients to retrieve a list of all NPI's that are in a single NPI list.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/{listID}
```

#### SAMPLE RESPONSE

```json
{
  "id": 4210,
  "npis": [
    "1234567891",
    "1234567892",
    "1234567893",
    "1234567894",
    "1234567895",
    "123 4567896",
    "1234567897"
  ],
  "name": "NPI_4210",
  "advertisers": ["Demo"],
  "isSmartList": false
}
```

We also offer Lite version of the above endpoint that allows the user to pull infomation about the list, minus the NPI array.

#### ENDPOINT

```txt
/v1/npi/npi-list/{listID}/lite
```

#### SAMPLE RESPONSE

```json
{
  "id": 4210,
  "name": "NPI_4210",
  "advertisers": ["Demo"],
  "isSmartList": false
}
```

If successful in your request the response will be similar to above with a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                                  |
| ------------------------------------------------------------------------------------- | -------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | You do not have access to view this NPI List |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Unknown NPI list ID                          |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests        |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388' \
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388"

headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388")
  .method("GET", body)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Authorization', 'Bearer <token>')

const requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 2. Get all NPI lists

This endpoint allows clients to get a list of all NPI lists associated with an account.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/account/{accountID}
```

#### SAMPLE RESPONSE

```json
[
  {"id": 30, "advertisers": ["Demo"], "name": "NPI_Oncologist"},
  {"id": 38, "advertisers": ["Demo"], "name": "NPI_Cardiology"},
  {"id": 39, "advertisers": ["Demo"], "name": "NPI_Dermatology"}
]
```

If successful in your request the response will be similar to above with a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                                  |
| ------------------------------------------------------------------------------------- | -------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | You do not have access to view this NPI List |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Unknown NPI list ID                          |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests        |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939' \
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939"

headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder().build();
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939")
  .method("GET")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Authorization', 'Bearer <token>')

const requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 3. Create an NPI list

This endpoint allows clients to create a new NPI list and add NPIs to the new list.

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/account/{accountid}
```

#### SAMPLE REQUEST

```json
{
  "name": "Endocrinologist_2022_1",
  "npis": ["3137933127", "3134730121"],
  "advertisers": ["Demo"],
  "applications": ["LIFE"]
}
```

![PLEASE_NOTE](https://img.shields.io/badge/PLEASE_NOTE-661DE1?style=for-the-badge)

The `applications` field accepts either `[“LIFE”]`, `[“SIGNAL”]` or `[‘SOCIAL”]`. These are products used within Pulsepoint.

- `LIFE`: Pulsepoints Buying platform
- `SIGNAL`: HCP365
- `SOCIAL`: ...

If successful in your request the response will return a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                              |
| ------------------------------------------------------------------------------------- | ---------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid property name for post operation |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid value(s) for `"applications""`   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not be empty                  |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid NPI ID                           |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not exceed 10 characters      |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | `"advertisers"` is required              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | 1Mn NPIs have been exceeded              |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests    |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request POST 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>' \
--data '{
  "name": "Endocrinologist_2023_1",
  "npis": ["3137933127", "3134730121"],
  "advertisers": ["Demo"],
  "applications"": ["LIFE"]
}'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939"

payload = json.dumps({
  "name": "Endocrinologist_2023_1",
  "npis": [
    "3137933127",
    "3134730121"
  ],
  "advertisers": [
    "Demo"
  ],
  "applications"": [
    "LIFE"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"Endocrinologist_2023_1\",\n  \"npis\": [\"3137933127\", \"3134730121\"],\n  \"advertisers\": [\"Demo\"],\n  \"applications"\": [\"LIFE\"]\n}");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', 'Bearer <token>')

const raw = JSON.stringify({
  name: 'Endocrinologist_2023_1',
  npis: ['3137933127', '3134730121'],
  advertisers: ['Demo'],
  applications: ['LIFE'],
})

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/561939',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 4. Replace NPIs in a list

This endpoint allows clients to get a list of all NPI lists associated with an account.

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/{listID}
```

#### SAMPLE REQUEST

```json
{
  "npis": ["3137933120", "3134730121"]
}
```

If successful in your request the response will be similar to above with a returned a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                                                                   |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid property name for post operation                                      |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid value(s) for `"applications""`                                        |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not be empty                                                       |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid NPI ID                                                                |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not exceed 10 characters                                           |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | `"advertisers"` is required                                                   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | 1Mn NPIs have been exceeded                                                   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Smart lists cannot be updated or deleted using the NPI List API.              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | PulsePoint provided lists cannot be updated or deleted using the NPI List API |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | List is archived and needs to be un-archived in order to be updated.          |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests                                         |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>' \
--data '{
  "npis": ["3137933120", "3134730121"]
}'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388"

payload = json.dumps({
  "npis": [
    "3137933120",
    "3134730121"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"npis\": [\"3137933120\", \"3134730121\"]\n}");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', 'Bearer <token>')

const raw = JSON.stringify({
  npis: ['3137933120', '3134730121'],
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 5. Add NPIs to a list

This endpoint allows clients to add NPIs to an existing NPI list.

![PATCH](https://img.shields.io/badge/HTTP%20Method-PATCH-50e3c2?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/{listID}
```

#### SAMPLE REQUEST

```json
{
  "operation": "add",
  "npis": ["3137933122", "3134730123"]
}
```

![PLEASE_NOTE](https://img.shields.io/badge/PLEASE_NOTE-661DE1?style=for-the-badge)

This endpoint does allow for duplicated NPIs to be added. To prevent this, we would suggest that you pull NPIs from the list using the [get an npi list](#1-get-an-npi-list) endpoint and comparing agaisnt the NPIs you plan on sending.

If successful in your request will return a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                                                                   |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid property name for post operation                                      |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid value(s) for `"applications"`                                         |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not be empty                                                       |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid NPI ID                                                                |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not exceed 10 characters                                           |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | `"advertisers"` is required                                                   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | 1Mn NPIs have been exceeded                                                   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Unknown `"operation"` type                                                    |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Cannot delete all NPIs from List                                              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Smart lists cannot be updated or deleted using the NPI List API.              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | PulsePoint provided lists cannot be updated or deleted using the NPI List API |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | List is archived and needs to be un-archived in order to be updated.          |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests                                         |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PATCH 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>' \
--data '{
  "operation": "add",
  "npis": ["3137933122", "3134730123"]
}'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388"

payload = json.dumps({
  "operation": "add",
  "npis": [
    "3137933122",
    "3134730123"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"operation\": \"add\",\n  \"npis\": [\"3137933122\", \"3134730123\"]\n}");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388")
  .method("PATCH", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', 'Bearer <token>')

const raw = JSON.stringify({
  operation: 'add',
  npis: ['3137933122', '3134730123'],
})

const requestOptions = {
  method: 'PATCH',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 6. Delete NPIs from a list

This endpoint allows clients to delete NPIs from one list.

![PATCH](https://img.shields.io/badge/HTTP%20Method-PATCH-50e3c2?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/{listID}
```

#### SAMPLE REQUEST

```json
{
  "operation": "remove",
  "npis": ["3137933122", "3134730123"]
}
```

If successful in your request the response will return a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                                                                   |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid property name for post operation                                      |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid value(s) for `"applications"`                                         |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not be empty                                                       |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid NPI ID                                                                |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not exceed 10 characters                                           |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | `"advertisers"` is required                                                   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | 1Mn NPIs have been exceeded                                                   |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Unknown `"operation"` type                                                    |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Cannot delete all NPIs from List                                              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Smart lists cannot be updated or deleted using the NPI List API.              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | PulsePoint provided lists cannot be updated or deleted using the NPI List API |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | List is archived and needs to be un-archived in order to be updated.          |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests                                         |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PATCH 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>' \
--data '{
  "operation": "remove",
  "npis": ["3137933122", "3134730123"]
}'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388"

payload = json.dumps({
  "operation": "remove",
  "npis": [
    "3137933122",
    "3134730123"
  ]
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)


```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"operation\": \"remove\",\n  \"npis\": [\"3137933122\", \"3134730123\"]\n}");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388")
  .method("PATCH", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', 'Bearer <token>')

const raw = JSON.stringify({
  operation: 'remove',
  npis: ['3137933122', '3134730123'],
})

const requestOptions = {
  method: 'PATCH',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/33388',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

## NPI API ENDPOINTS - NPI LISTS WITH ATTRIBUTES

An NPI list with attributes is an NPI list that appends a client's metadata to their list of NPIs. This endpoint allows users to create an NPI list with attributes, replace an NPI list with attributes and view an NPI list with attributes.

Definitions:

- `Attribute` = column headers
- `AttributeValues` = value for corresponding attribute header per NPI
- `Name` = NPI list name (upon creation)
- `NpiColumnIndex` = which column contains NPIs (Starts with first column = 0)
- `NPIListId` = the Pulsepoint numeric identifier for the NPI list.

### 1. Create NPI list with attributes

Create new NPI lists with client’s own attributes.

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)
<br><br>

#### ENDPOINT

```txt
/v1/npi/npi-list/account/{accountId}/attributes
```

#### SAMPLE REQUEST

```json
{
  "attributeValues": [
    ["1639137706", "yes", "NPI Targeted Banners", "PulsePoint Inc.", "123456"]
  ],
  "attributes": ["NPI_ID", "Active", "CampaignName", "CompanyName", "CustomID"],
  "name": "NPI_with_Attr",
  "npiColumnIndex": 0,
  "applications": ["LIFE"],
  "advertisers": ["Demo"]
}
```

![PLEASE_NOTE](https://img.shields.io/badge/PLEASE_NOTE-661DE1?style=for-the-badge)

The `applications` field accepts either `[“LIFE”]`, `[“SIGNAL”]` or `[‘SOCIAL”]`. These are products used within Pulsepoint.

- `LIFE`: Pulsepoints Buying platform
- `SIGNAL`: HCP365
- `SOCIAL`: ...

If successful in your request the response will return a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                              |
| ------------------------------------------------------------------------------------- | ---------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid property name for post operation |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid value(s) for `"applications"`    |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not be empty                  |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Invalid NPI ID                           |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI ID can not exceed 10 characters      |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | `"advertisers"` is required              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | 1Mn NPIs have been exceeded              |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests    |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --globoff '{{base_url}}/123456/attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization', 'Bearer <token>' \
--data '{
  "attributeValues": [
    ["1639137706", "yes", "NPI Targeted Banners", "PulsePoint Inc.", "123456"]
  ],
  "attributes": ["NPI_ID", "Active", "CampaignName", "CompanyName", "CustomID"],
  "npiColumnIndex": 0
}'
```

#### PYTHON

```python
import requests
import json

url = "{{base_url}}/123456/attributes"

payload = json.dumps({
  "attributeValues": [
    [
      "1639137706",
      "yes",
      "NPI Targeted Banners",
      "PulsePoint Inc.",
      "123456"
    ]
  ],
  "attributes": [
    "NPI_ID",
    "Active",
    "CampaignName",
    "CompanyName",
    "CustomID"
  ],
  "npiColumnIndex": 0
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"attributeValues\": [\n    [\"1639137706\", \"yes\", \"NPI Targeted Banners\", \"PulsePoint Inc.\", \"123456\"]\n  ],\n  \"attributes\": [\"NPI_ID\", \"Active\", \"CampaignName\", \"CompanyName\", \"CustomID\"],\n  \"npiColumnIndex\": 0\n}");
Request request = new Request.Builder()
  .url("{{base_url}}/123456/attributes")
  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', 'Bearer <token>')

const raw = JSON.stringify({
  attributeValues: [
    ['1639137706', 'yes', 'NPI Targeted Banners', 'PulsePoint Inc.', '123456'],
  ],
  attributes: ['NPI_ID', 'Active', 'CampaignName', 'CompanyName', 'CustomID'],
  npiColumnIndex: 0,
})

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch('{{base_url}}/123456/attributes', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 2. Replace NPI list with attributes

Replace the entire NPI list with the new set of NPIs with corresponding attributes.

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/{NPIListId}/attributes
```

#### SAMPLE REQUEST

```json
{
  "attributeValues": [
    ["1639137706", "yes", "NPI Targeted Banners", "PulsePoint Inc.", "123456"]
  ],
  "attributes": ["NPI_ID", "Active", "CampaignName", "CompanyName", "CustomID"],
  "npiColumnIndex": 0
}
```

If successful in your request the response will return a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                      | Description                                                          |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | Invalid property name for post operation                             |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | Invalid value(s) for `"applications"`                                |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | NPI ID can not be empty                                              |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | Invalid NPI ID                                                       |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | NPI ID can not exceed 10 characters                                  |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | `"advertisers"` is required                                          |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | 1Mn NPIs have been exceeded                                          |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | Cannot change application property during update                     |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge) | List is archived and needs to be un-archived in order to be updated. |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --globoff --request PUT '{{base_url}}/123456/attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization', 'Bearer <token>' \
--data '{
  "attributeValues": [
    ["1639137706", "yes", "NPI Targeted Banners", "PulsePoint Inc.", "123456"]
  ],
  "attributes": ["NPI_ID", "Active", "CampaignName", "CompanyName", "CustomID"],
  "npiColumnIndex": 0
}'
```

#### PYTHON

```python
import requests
import json

url = "{{base_url}}/123456/attributes"

payload = json.dumps({
  "attributeValues": [
    [
      "1639137706",
      "yes",
      "NPI Targeted Banners",
      "PulsePoint Inc.",
      "123456"
    ]
  ],
  "attributes": [
    "NPI_ID",
    "Active",
    "CampaignName",
    "CompanyName",
    "CustomID"
  ],
  "npiColumnIndex": 0
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <token>'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\n  \"attributeValues\": [\n    [\"1639137706\", \"yes\", \"NPI Targeted Banners\", \"PulsePoint Inc.\", \"123456\"]\n  ],\n  \"attributes\": [\"NPI_ID\", \"Active\", \"CampaignName\", \"CompanyName\", \"CustomID\"],\n  \"npiColumnIndex\": 0\n}");
Request request = new Request.Builder()
  .url("{{base_url}}/123456/attributes")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', 'Bearer <token>')

const raw = JSON.stringify({
  attributeValues: [
    ['1639137706', 'yes', 'NPI Targeted Banners', 'PulsePoint Inc.', '123456'],
  ],
  attributes: ['NPI_ID', 'Active', 'CampaignName', 'CompanyName', 'CustomID'],
  npiColumnIndex: 0,
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch('{{base_url}}/123456/attributes', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### 3. View NPI list with attributes

Show the current NPI list with corresponding attributes.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

#### ENDPOINT

```txt
/v1/npi/npi-list/{NPIListId}/attributes
```

#### SAMPLE RESPONSE

```json
{
  "attributeValues": [
    ["1639137706", "yes", "NPI Targeted Banners", "PulsePoint Inc.", "123456"]
  ],
  "attributes": ["NPI_ID", "Active", "CampaignName", "CompanyName", "CustomID"],
  "name": "NPI_with_Attr",
  "advertisers": ["Demo"]
}
```

If successful in your request the response will return a `200`. If your request fails it will return one of the following errors:

| Error Code                                                                            | Description                               |
| ------------------------------------------------------------------------------------- | ----------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | NPI provided is not a NPI Attribute List. |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | Unknown NPI list ID                       |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests     |

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/123456/attributes' \
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/123456/attributes"

payload = {}
headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/123456/attributes")
  .method("GET", body)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Authorization', 'Bearer <token>')

const requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/123456/attributes',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>
