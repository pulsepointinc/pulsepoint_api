# CREATIVE MANAGEMENT API

## INTRODUCTION

PulsePoint clients seeking enhanced creative management capabilities can now utilize the newly introduced Creative Management API. This API allows clients to effortlessly upload new creatives and modify existing ones directly through an ad server's user interface, eliminating the need to log into the PulsePoint platform.

![IMPORTANT](https://img.shields.io/badge/IMPORTANT-red?style=for-the-badge)

**Please note this API currently only supports HTML creatives.**

### Actions

1. [Create a creative specific account](#1-create-creative)
2. [Get a creative by its ID](#2-get-a-creative-by-its-id)
3. [Update a creative](#3-update-a-creative)
4. [Assign creatives to a tactic](#4-assign-creatives-to-tactic)
5. [VIDEO: Create Creative](#1-create-video-creative)
6. [VIDEO: Retrieve Creative](#2-retrieve-video-creative)
7. [VIDEO: Update Creative](#3-update-a-creative)

**Important to Note:**

| Field                             | Mandatory | Expected Values                                                 |
| --------------------------------- | --------- | --------------------------------------------------------------- |
| name                              | Y         | String                                                          |
| creativeType                      | Y         | Expandable / Html                                               |
| advertiserName                    | Y         | String                                                          |
| adSizeHeight                      | Y         | Number                                                          |
| adSizeWidth                       | Y         | Number                                                          |
| domainLandingPage                 | Y         | String                                                          |
| adChoicesIcon                     | Y         | TopRight, TopLeft, BottomRight, BottomLeft, None                |
| creativeHtml                      | Y         | String                                                          |
| notes                             |           | String                                                          |
| placementId                       |           | Number                                                          |
| campaignRestrictName              |           | Valid Campaign Name                                             |
| expandDirection (Expandable type) |           | Up, Down, Left, Right, Up Left, Up Right, Down Left, Down Right |
| categoryNames                     |           | Valid Category Name                                             |

- The Creative Management API endpoints support 10 calls per minute

## Endpoints

### 1. Create Creative

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

```
/v1/lifecreative/account/{accountId}
```

#### Example Request Body

```json
{
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": ["Family & Parenting", "Personal Finance"]
}
```

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request POST 'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer LFFqkw8CkqmbhITaS0oP1xDGAfk' \
--header 'Authorization: Bearer <token>' \
--data '{
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": ["Family & Parenting", "Personal Finance"]
}'
```

#### PYTHON

```python
import requests
import json

url = "http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534"

payload = json.dumps({
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": [
    "Family & Parenting",
    "Personal Finance"
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"testApr-10\",\n  \"creativeType\": \"html\",\n  \"advertiserName\": \"01- Advertiser\",\n  \"adSizeHeight\": 576,\n  \"adSizeWidth\": 1024,\n  \"domainLandingPage\": \"https://test.com/\",\n  \"adChoicesIcon\": \"TopRight\",\n  \"creativeHtml\": \"test-html\",\n  \"notes\": \"test-notes\",\n  \"placementId\": 123,\n  \"campaignRestrictName\": \"camp1_drug\",\n  \"categoryNames\": [\"Family & Parenting\", \"Personal Finance\"]\n}");
Request request = new Request.Builder()
  .url("http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534")
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
  name: 'testApr-10',
  creativeType: 'html',
  advertiserName: '01- Advertiser',
  adSizeHeight: 576,
  adSizeWidth: 1024,
  domainLandingPage: 'https://test.com/',
  adChoicesIcon: 'TopRight',
  creativeHtml: 'test-html',
  notes: 'test-notes',
  placementId: 123,
  campaignRestrictName: 'camp1_drug',
  categoryNames: ['Family & Parenting', 'Personal Finance'],
})

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

### 2. Get a creative by it's ID

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

```
/v1/lifecreative/{creativeId}
```

#### SAMPLE RESPONSE

```json
{
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": ["Family & Parenting", "Personal Finance"]
}
```

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location 'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534' \
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534"

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
  .url("http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534")
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
  'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

### 3. Update a Creative

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

```
/v1/lifecreative/{creativeId}
```

#### Example Request Body

```json
{
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": ["Family & Parenting", "Personal Finance"]
}
```

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer LFFqkw8CkqmbhITaS0oP1xDGAfk' \
--header 'Authorization: Bearer <token>' \
--data '{
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": ["Family & Parenting", "Personal Finance"]
}'
```

#### PYTHON

```python
import requests
import json

url = "http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534"

payload = json.dumps({
  "name": "testApr-10",
  "creativeType": "html",
  "advertiserName": "01- Advertiser",
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://test.com/",
  "adChoicesIcon": "TopRight",
  "creativeHtml": "test-html",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "camp1_drug",
  "categoryNames": [
    "Family & Parenting",
    "Personal Finance"
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
RequestBody body = RequestBody.create(mediaType, "{\n  \"name\": \"testApr-10\",\n  \"creativeType\": \"html\",\n  \"advertiserName\": \"01- Advertiser\",\n  \"adSizeHeight\": 576,\n  \"adSizeWidth\": 1024,\n  \"domainLandingPage\": \"https://test.com/\",\n  \"adChoicesIcon\": \"TopRight\",\n  \"creativeHtml\": \"test-html\",\n  \"notes\": \"test-notes\",\n  \"placementId\": 123,\n  \"campaignRestrictName\": \"camp1_drug\",\n  \"categoryNames\": [\"Family & Parenting\", \"Personal Finance\"]\n}");
Request request = new Request.Builder()
  .url("http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534")
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
  name: 'testApr-10',
  creativeType: 'html',
  advertiserName: '01- Advertiser',
  adSizeHeight: 576,
  adSizeWidth: 1024,
  domainLandingPage: 'https://test.com/',
  adChoicesIcon: 'TopRight',
  creativeHtml: 'test-html',
  notes: 'test-notes',
  placementId: 123,
  campaignRestrictName: 'camp1_drug',
  categoryNames: ['Family & Parenting', 'Personal Finance'],
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/5534',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

### 4. Assign Creatives to Tactic

| Field               | Mandatory | Expected Values                        |
| ------------------- | --------- | -------------------------------------- |
| tacticId            | Y         | Number (A Valid Tactic ID)             |
| creativesToAssign   |           | Array of Numbers (A Valid Creative ID) |
|                     |           | Ex: `[205581]`                         |
| creativesToUnAssign |           | Array of Numbers (A Valid Creative ID) |
|                     |           | Ex: `[207561, 213290]`                 |

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

```
/v1/lifecreative/account/{accountId}/creativeassociation
```

#### Example Request Body

```json
[
  {
    "tacticId": 123425,
    "creativesToAssign": [2055812]
  },
  {
    "tacticId": 65465,
    "creativesToUnAssign": [207561, 213290]
  },
  {
    "tacticId": 878545,
    "creativesToAssign": [205581],
    "creativesToUnAssign": [207561, 213290]
  }
]
```

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/account/123456/creativeassociation' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>' \
--data '[{
    "tacticId" : 123425,
    "creativesToAssign" : [2055812]
},
{
    "tacticId" : 65465,
    "creativesToUnAssign" : [207561, 213290]
},
{
    "tacticId" : 878545,
    "creativesToAssign" : [205581],
    "creativesToUnAssign" : [207561, 213290]
}]
'
```

#### PYTHON

```python
import requests
import json

url = "http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/account/123456/creativeassociation"

payload = json.dumps([
  {
    "tacticId": 123425,
    "creativesToAssign": [
      2055812
    ]
  },
  {
    "tacticId": 65465,
    "creativesToUnAssign": [
      207561,
      213290
    ]
  },
  {
    "tacticId": 878545,
    "creativesToAssign": [
      205581
    ],
    "creativesToUnAssign": [
      207561,
      213290
    ]
  }
])
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
RequestBody body = RequestBody.create(mediaType, "[{\n    \"tacticId\" : 123425,\n    \"creativesToAssign\" : [2055812]\n},\n{\n    \"tacticId\" : 65465,\n    \"creativesToUnAssign\" : [207561, 213290]\n},\n{\n    \"tacticId\" : 878545,\n    \"creativesToAssign\" : [205581],\n    \"creativesToUnAssign\" : [207561, 213290]\n}]\n");
Request request = new Request.Builder()
  .url("http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/account/123456/creativeassociation")
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

const raw = JSON.stringify([
  {
    tacticId: 123425,
    creativesToAssign: [2055812],
  },
  {
    tacticId: 65465,
    creativesToUnAssign: [207561, 213290],
  },
  {
    tacticId: 878545,
    creativesToAssign: [205581],
    creativesToUnAssign: [207561, 213290],
  },
])

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'http://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/account/123456/creativeassociation',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

## Video Creatives

### 1. Create Video Creative

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

**Required Path Parameters**

- `accountId`: The ID of the account to own this creative

```
v1/lifecreative/account/{accountId}
```

| Field                | Type          | Required? | Constraints / Notes                                            |
| -------------------- | ------------- | --------- | -------------------------------------------------------------- |
| creativeType         | string        | Yes       | Must be `"video"`<br>— Identifies this as a video creative     |
| name                 | string        | No        | 1–80 chars                                                     |
| source               | string        | Yes       | One of the allowed video source types (see combinations below) |
| type                 | string        | Yes       | One of the allowed video tech types (see combinations below)   |
| videoURL             | string        | No        | URL to the video asset                                         |
| duration             | integer       | Yes       | In seconds                                                     |
| adSizeWidth          | integer       | Yes       |                                                                |
| adSizeHeight         | integer       | Yes       |                                                                |
| domainLandingPage    | string (URL)  | Yes       | Valid URL, max length 1024                                     |
| advertiserName       | string        | Yes       |                                                                |
| clickThroughURL      | string        | Yes       |                                                                |
| bitRate              | integer       | No        | Video bit rate                                                 |
| adChoicesIcon        | string        | Yes       | TopRight, TopLeft, BottomRight, BottomLeft, None               |
| campaignRestrictName | string        | No        | Campaign restriction name                                      |
| notes                | string        | No        | Internal notes                                                 |
| videoSkippingAfter   | integer       | No        | Seconds before skip button appears                             |
| categoryNames        | array[string] | No        | List of category names                                         |

**Allowed Source & Type Combinations**

- source: `VAST_Doc`, type: `HTML5_VPAID`
- source: `VAST_Doc`, type: `MP4_VIDEO`
- source: `VAST_URL`, type: `HTML5_VPAID`
- source: `VAST_URL`, type: `MP4_VIDEO`
- source: `URL`, type: `FLV`
- source: `URL`, type: `MP4_VIDEO`

#### Example Request Body

```json
{
  "creativeType": "video",
  "name": "July3_video_Vasturl",
  "source": "VAST_URL",
  "type": "HTML5_VPAID",
  "videoURL": "https://rtr.innovid.com/r1.656e48c6baa313.39895082;cb=[timestamp]",
  "duration": 9,
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://landing.test.com",
  "advertiserName": "Amgen",
  "clickThroughURL": "https://click.test.com",
  "bitRate": 20,
  "adChoicesIcon": "TopRight",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "TestDAS1221",
  "videoSkippingAfter": null,
  "categoryNames": ["contests & Freebies", "Diabetes"]
}
```

### Responses

| Response                      | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| **201 Created**               | Returns the newly created `VideoCreativeDTO` JSON. |
| **400 Bad Request**           | Validation errors (field-level messages).          |
| **401 Unauthorized**          | Missing or invalid credentials.                    |
| **404 Not Found**             | Account not found.                                 |
| **500 Internal Server Error** |                                                    |

### 2. Retrieve Video Creative

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

**Required Path Parameters**

- `creativeId`: The unique ID of the video creative to retrieve

```bash
v1/lifecreative/{creativeId}
```

#### Sample Request

```bash
GET https://lifeapi.pulsepoint.com/RestApi/v1/lifecreative/311453
Accept: application/json
Authorization: Bearer <token>
```

| Response                      | Description                                 |
| ----------------------------- | ------------------------------------------- |
| **200 OK**                    | Returns the `VideoCreativeDTO` JSON object. |
| **400 Bad Request**           | Invalid `creativeId`.                       |
| **401 Unauthorized**          | Missing or invalid credentials.             |
| **404 Not Found**             | No creative found with the given ID.        |
| **500 Internal Server Error** |                                             |

### 3. Update Video Creative

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

**Required Path Parameters**

- `creativeId`: The unique ID of the video creative to retrieve

```bash
v1/lifecreative/{creativeId}
```

**Request Headers**

- Content-Type: application/json
- Authorization: Bearer `<token>` (if applicable)

**Request Body**

- Content-Type: application/json

### Sample Request

```json
{
  "creativeType": "video",
  "name": "July3_video_Vasturl",
  "source": "VAST_URL",
  "type": "HTML5_VPAID",
  "videoURL": "https://rtr.innovid.com/r1.656e48c6baa313.39895082;cb=[timestamp]",
  "duration": 9,
  "adSizeHeight": 576,
  "adSizeWidth": 1024,
  "domainLandingPage": "https://landing.test.com",
  "advertiserName": "Amgen",
  "clickThroughURL": "https://click.test.com",
  "bitRate": 20,
  "adChoicesIcon": "TopRight",
  "notes": "test-notes",
  "placementId": 123,
  "campaignRestrictName": "TestDAS1221",
  "videoSkippingAfter": null,
  "categoryNames": ["contests & Freebies", "Diabetes"]
}
```
