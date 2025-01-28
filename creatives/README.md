# CREATIVE MANAGEMENT API

## INTRODUCTION

PulsePoint clients seeking enhanced creative management capabilities can now utilize the newly introduced Creative Management API. This API allows clients to effortlessly upload new creatives and modify existing ones directly through an ad server's user interface, eliminating the need to log into the PulsePoint platform.

_This document describes the functionality supported by the Creative Management API, initially built to support Flashtalking. PulsePoint provides a REST API to access and manage the following actions for creative management_:

### CREATIVES

1. [View list of advertisers for a specific account](#view-list-of-advertisers-for-a-specific-account)
2. [Upload new html creatives to an advertiser](#upload-new-html-creatives-to-an-advertiser)
   - 2a [Upload new video creatives to an advertiser](#upload-new-video-creatives-to-an-advertiser)
3. [View existing FT creatives for that advertiser](#view-all-existing-creatives-from-an-ad-server-for-a-given-advertiser)
4. [Update existing html FT creatives](#update-existing-html-creatives-from-a-specific-ad-server)
   - 4a [Update existing video FT creatives](#update-existing-video-creatives-from-a-specific-ad-server)

**Important to Note:**

- Clients may only `PUT` to upload creatives to the PulsePoint creative library for a given advertiser. This API does not support assigning creatives to a specific tactic or creating new line items or tactics.
- The Creative Management API endpoints support 10 calls per minute
- Advertiser ID is required in every call

## CREATIVES API ENDPOINTS

### View list of advertisers for a specific account

This endpoint allows an ad server to get a list of all of the advertisers associated with a specific account, so that they can ensure they are uploading a creative to the correct advertiser.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

#### ENDPOINT

```txt
v1/account/{accountId}/advertisers
```

#### SAMPLE RESPONSE

```json
[
  {"id": 1075, "name": "Bayer"},
  {"id": 5536, "name": "Demo"},
  {"id": 6061, "name": "Jivi"},
  {"id": 6060, "name": "Stivarga"}
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
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers'
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers"

headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```

#### JAVA

```java

OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers")
  .method("GET", body)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const requestOptions = {
  method: 'GET',
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))

const myHeaders = new Headers()
myHeaders.append('Authorization', 'Bearer <token>')
```

</details>

---

### Upload new html creatives to an advertiser

This endpoint allows an ad server to upload new html creatives to the Life platform and associate them with a specific Advertiser. One creative can be uploaded per API call.

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

#### ENDPOINT

```txt
v1/advertiser/{advertiserId}/creatives
```

#### SAMPLE RESPONSE

```json
[
  {
    "id": 173074,
    "advId": 6061,
    "campaignId": 123123,
    "htmlCode": "html code",
    "creativeType": "html",
    "height": 250,
    "width": 300,
    "landingDomain": "test.com",
    "name": "creative_name_300x250_STAND",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
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
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives' \
--header 'Content-Type: application/json'
--header 'Authorization: Bearer <token>'

--data '[
  {
    "name": "creative_name_300x250_STAND",
    "campaignId": 123123,
    "creativeType": "html",
    "height": 250,
    "width": 300,
    "htmlCode": "html code",
    "landingDomain": "test.com",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
  }
]'
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives"

payload = json.dumps([
  {
    "name": "creative_name_300x250_STAND",
    "campaignId": 123123,
    "creativeType": "html",
    "height": 250,
    "width": 300,
    "htmlCode": "html code",
    "landingDomain": "test.com",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java

OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "[\n  {\n    \"name\": \"creative_name_300x250_STAND\",\n    \"campaignId\": 123123,\n    \"creativeType\": \"html\",\n    \"height\": 250,\n    \"width\": 300,\n    \"htmlCode\": \"html code\",\n    \"landingDomain\": \"test.com\",\n    \"notes\": \"creative_name_300x250_STAND - 300x250\",\n    \"adChoiceIcon\": \"TopRight\",\n    \"expandDirection\": \"Down\"\n  }\n]");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives")
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

const raw = JSON.stringify([
  {
    name: 'creative_name_300x250_STAND',
    campaignId: 123123,
    creativeType: 'html',
    height: 250,
    width: 300,
    htmlCode: 'html code',
    landingDomain: 'test.com',
    notes: 'creative_name_300x250_STAND - 300x250',
    adChoiceIcon: 'TopRight',
    expandDirection: 'Down',
  },
])

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### Upload new video creatives to an advertiser

This endpoint allows an ad server to upload new video creatives to the Life platform and associate them with a specific Advertiser. One creative can be uploaded per API call.

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

#### ENDPOINT

```txt
v1/advertiser/{advertiserId}/creatives
```

#### SAMPLE RESPONSE

```json
[
  {
    "id": 173075,
    "advId": 1240,
    "campaignId": 123123,
    "creativeType": "video",
    "clickUrl": "test.com",
    "landingDomain": "test.com",
    "name": "creative_name_VidLnk_60s_X",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down",
    "height": 250,
    "width": 300,
    "videoURL": "video url",
    "bitRate": 3000,
    "duration": 60
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
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives' \
--header 'Content-Type: application/json'
--header 'Authorization: Bearer <token>'

--data '[
  {
   "advId": 1240,
   "campaignId": 123123,
   "creativeType": "video",
   "clickUrl": "test.com",
   "landingDomain": "test.com",
   "name": "creative_name_VidLnk_60s_X",
   "notes": "creative_name_300x250_STAND - 300x250",
   "adChoiceIcon": "TopRight",
   "expandDirection": "Down",
   "height": 250,
   "width": 300,
   "videoURL": "video url",
   "bitRate": 3000,
   "duration": 60
}
]'
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives"

payload = json.dumps([
  {
    "advId": 1240,
    "campaignId": 123123,
    "creativeType": "video",
    "clickUrl": "test.com",
    "landingDomain": "test.com",
    "name": "creative_name_VidLnk_60s_X",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down",
    "height": 250,
    "width": 300,
    "videoURL": "video url",
    "bitRate": 3000,
    "duration": 60
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java

OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "[\n  {\n   \"advId\": 1240,\n \"campaignId\": 123123,\n   \"creativeType\": \"video\",\n   \"clickUrl\": \"test.com\",\n   \"landingDomain\": \"test.com\",\n   \"name\": \"creative_name_VidLnk_60s_X\",\n   \"notes\": \"creative_name_300x250_STAND - 300x250\",\n   \"adChoiceIcon\": \"TopRight\",\n   \"expandDirection\": \"Down\",\n   \"height\": 250,\n   \"width\": 300,\n   \"videoURL\": \"video url\",\n   \"bitRate\": 3000,\n   \"duration\": 60\n}\n\n]");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives")
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

const raw = JSON.stringify([
  {
    advId: 1240,
    campaignId: 123123,
    creativeType: 'video',
    clickUrl: 'test.com',
    landingDomain: 'test.com',
    name: 'creative_name_VidLnk_60s_X',
    notes: 'creative_name_300x250_STAND - 300x250',
    adChoiceIcon: 'TopRight',
    expandDirection: 'Down',
    height: 250,
    width: 300,
    videoURL: 'video url',
    bitRate: 3000,
    duration: 60,
  },
])

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### View all existing creatives from an ad server for a given advertiser

This endpoint allows an ad server to get a list of their creatives that are currently in the Life platform and associated with a specific advertiser. Initial API version will only send back creatives uploaded via the Creative Management API OR Life UI bulk upload. Creatives uploaded via Life UI single creative upload may not be included until a future build.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

#### ENDPOINT

```txt
v1/account/{accountId}/advertisers/creatives
```

#### SAMPLE RESPONSE

```json
[
  {
    "id": 173074,
    "advId": 6061,
    "htmlCode": "html code",
    "creativeType": "html",
    "height": 250,
    "width": 300,
    "landingDomain": "test.com",
    "name": "creative_name_300x250_STAND",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
  },
  {
    "id": 173075,
    "advId": 6061,
    "creativeType": "video",
    "clickUrl": "test.com",
    "landingDomain": "test.com",
    "name": "creative_name_VidLnk_60s_X",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down",
    "height": 250,
    "width": 300,
    "videoURL": "video url",
    "bitRate": 3000,
    "duration": 60
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
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives'
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives"

headers = {
  'Authorization': 'Bearer <token>'
}

response = requests.request("GET", url, headers=headers)

print(response.text)
```

#### JAVA

```java

OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("text/plain");
RequestBody body = RequestBody.create(mediaType, "");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives")
  .method("GET", body)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const requestOptions = {
  method: 'GET',
  redirect: 'follow',
}

fetch(
  'https://lifeapi.pulsepoint.com/RestApi/v1/account/562382/advertisers/creatives',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))

const myHeaders = new Headers()
myHeaders.append('Authorization', 'Bearer <token>')
```

</details>

---

### Update existing html creatives from a specific ad server

This endpoint allows an ad server to make changes to their html creatives that are currently in the Life platform. One creative can be updated per API call. Initial API version will only send back creatives uploaded via Creative Management API OR Life UI bulk upload. Creatives uploaded via Life UI single creative upload may not be included until a future release

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

#### ENDPOINT

```txt
v1/creatives/{creativeId}
```

#### SAMPLE RESPONSE

```json
[
  {
    "id": 173074,
    "advId": 6061,
    "htmlCode": "html code",
    "creativeType": "html",
    "height": 250,
    "width": 300,
    "landingDomain": "test.com",
    "name": "creative_name_300x250_STAND",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
  },
  {
    "id": 173075,
    "advId": 6061,
    "creativeType": "video",
    "clickUrl": "test.com",
    "landingDomain": "test.com",
    "name": "creative_name_VidLnk_60s_X",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down",
    "height": 250,
    "width": 300,
    "videoURL": "video url",
    "bitRate": 3000,
    "duration": 60
  }
]
```

If successful in your request the response will be similar to above with a returned a `200`

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location 'http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
--data '[{
  "htmlCode": "html code",
  "landingDomain": "test.com",
  "campaignId": 123123,
  "name": "creative_name_300x250_STAND",
  "notes": "creative_name_300x250_STAND - 300x250",
  "adChoiceIcon": "TopRight",
  "expandDirection": "Down"
}]'
```

#### PYTHON

```python
import requests
import json

url = "http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074"

payload = json.dumps([
  {
    "htmlCode": "html code",
    "landingDomain": "test.com",
    "campaignId": 123123,
    "name": "creative_name_300x250_STAND",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
  }
])
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
RequestBody body = RequestBody.create(mediaType, "[{\n  \"htmlCode\": \"html code\",\n  \"landingDomain\": \"test.com\",\n  \"campaignId\": 123123,\n  \"name\": \"creative_name_300x250_STAND\",\n  \"notes\": \"creative_name_300x250_STAND - 300x250\",\n  \"adChoiceIcon\": \"TopRight\",\n  \"expandDirection\": \"Down\"\n}]");
Request request = new Request.Builder()
  .url("http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074")
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

const raw = JSON.stringify([
  {
    htmlCode: 'html code',
    landingDomain: 'test.com',
    campaignId: 123123,
    name: 'creative_name_300x250_STAND',
    notes: 'creative_name_300x250_STAND - 300x250',
    adChoiceIcon: 'TopRight',
    expandDirection: 'Down',
  },
])

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---

### Update existing Video creatives from a specific ad server

This endpoint allows an ad server to make changes to their video creatives that are currently in the Life platform. One creative can be updated per API call. Initial API version will only send back creatives uploaded via Creative Management API OR Life UI bulk upload. Creatives uploaded via Life UI single creative upload may not be included until a future release.

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

#### ENDPOINT

```txt
v1/creatives/{creativeId}
```

#### SAMPLE RESPONSE

```json
[
  {
    "id": 173074,
    "advId": 6061,
    "htmlCode": "html code",
    "creativeType": "html",
    "height": 250,
    "width": 300,
    "landingDomain": "test.com",
    "name": "creative_name_300x250_STAND",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down"
  },
  {
    "id": 173075,
    "advId": 6061,
    "creativeType": "video",
    "clickUrl": "test.com",
    "landingDomain": "test.com",
    "name": "creative_name_VidLnk_60s_X",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down",
    "height": 250,
    "width": 300,
    "videoURL": "video url",
    "bitRate": 3000,
    "duration": 60
  }
]
```

If successful in your request the response will be similar to above with a returned a `200`

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location 'http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <token>'
--data '[{
  "clickUrl": "test.com",
  "landingDomain": "test.com",
  "campaignId": 123123,
  "name": "creative_name_VidLnk_60s_X",
  "notes": "creative_name_300x250_STAND - 300x250",
  "adChoiceIcon": "TopRight",
  "expandDirection": "Down",
  "height": 250,
  "width": 300,
  "videoURL": "video url",
  "bitRate": 3000,
  "duration": 60
}]'
```

#### PYTHON

```python
import requests
import json

url = "http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074"

payload = json.dumps([
  {
    "clickUrl": "test.com",
    "landingDomain": "test.com",
    "campaignId": 123123,
    "name": "creative_name_VidLnk_60s_X",
    "notes": "creative_name_300x250_STAND - 300x250",
    "adChoiceIcon": "TopRight",
    "expandDirection": "Down",
    "height": 250,
    "width": 300,
    "videoURL": "video url",
    "bitRate": 3000,
    "duration": 60
  }
])
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
RequestBody body = RequestBody.create(mediaType, "[{\n  \"clickUrl\": \"test.com\",\n  \"landingDomain\": \"test.com\",\n  \"campaignId\": 123123,\n  \"name\": \"creative_name_VidLnk_60s_X\",\n  \"notes\": \"creative_name_300x250_STAND - 300x250\",\n  \"adChoiceIcon\": \"TopRight\",\n  \"expandDirection\": \"Down\",\n  \"height\": 250,\n  \"width\": 300,\n  \"videoURL\": \"video url\",\n  \"bitRate\": 3000,\n  \"duration\": 60\n}]");
Request request = new Request.Builder()
  .url("http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074")
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

const raw = JSON.stringify([
  {
    clickUrl: 'test.com',
    landingDomain: 'test.com',
    campaignId: 123123,
    name: 'creative_name_VidLnk_60s_X',
    notes: 'creative_name_300x250_STAND - 300x250',
    adChoiceIcon: 'TopRight',
    expandDirection: 'Down',
    height: 250,
    width: 300,
    videoURL: 'video url',
    bitRate: 3000,
    duration: 60,
  },
])

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch(
  'http://lifeapi.pulsepoint.com/RestApi/v1/creatives/173074',
  requestOptions,
)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

---
