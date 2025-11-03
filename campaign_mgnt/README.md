# CAMPAIGN MANAGEMENT API

# Important notice

PulsePoint API documentation has a new home! [Link](https://pulsepoint-platform.readme.io/docs/getting-started#/)

This platform provides guides explaining how each endpoint works as well as the different fields supported. The API Reference tab can be used to test each endpoint right in the app. You can authenticate using your UN/PW and Key and Secret provided by your account manager.

We will be deprecating these Github docs by the end of the year (December 31, 2025).

Please reach out with any questions!

## INTRODUCTION

PulsePoint's clients use budgeting to strategically optimize their
campaigns and tactics. Clients may want to change budgeting
and allocations rapidly. Now with access to the new Campaign API,
clients can seamlessly change budgeting options on their tactics
without logging into the platform.

![IMPORTANT](https://img.shields.io/badge/IMPORTANT-red?style=for-the-badge)

- Clients may only PUT to replace
  current budget and allocations.
  This API does not support the
  creation of new line items and
  tactics and their budgeting
- The Campaign API endpoints
  only support 5 calls per minute
  per tactic
- Base bid price and allocation for
  a specific tactic can be combined
  in one `PUT` call
- For allocation replacements, the
  allocation type must be validated
  to the tactic level allocation type
  first before the call is accepted
  and executed.
- Tactic ID is required in every call

---

1. [View current tactic budgeting](#view-current-tactic-budgeting)
2. [Update base bid price](#update-tactic-base-bid)
3. [Update priority allocation](#update-tactic-allocation---priority)
4. [Update dollar allocation](#update-tactic-allocation---dollar-allocation)
5. [Update percent allocation](#update-tactic-allocation---percent-allocation)

## View Current Tactic Budgeting

This endpoint allows clients to view a tactic’s current base bid price, allocation type and allocation
amount for a specific tactic.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

#### ENDPOINT

```txt
/v1/tactic/{tacticid}
```

If successful in your request the response will be similar to above with a `200`.

#### SAMPLE RESPONSE

```json
{
  "tacticId": 228191,
  "name": "API_TEST_PCT",
  "baseBidPrice": 10.0,
  "maxBidPrice": 50.0,
  "percentAllocation": 25.0
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
curl --location 'https://lifeapi.pulsepoint.com/RestApi/v1/tactic/123456' \
--header 'Authorization: Bearer <token>'
```

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/v1/tactic/123456"

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
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/tactic/123456")
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

fetch('https://lifeapi.pulsepoint.com/RestApi/v1/tactic/123456', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

### Update Tactic base bid

This endpoint allows clients to update an amount for a specific tactics base bid.

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

#### ENDPOINT

```txt
/v1/tactic/{tacticid}
```

If successful in your request the response will be similar to above with a `200`.

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191' \
--header 'Content-Type: application/json' \
--header 'Authorization: <token>' \
--data '{    "baseBidPrice": 25 }'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191"

payload = json.dumps({
  "baseBidPrice": 25
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': '<token>'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{    \"baseBidPrice\": 25 }");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "<token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', '<token>')

const raw = JSON.stringify({
  baseBidPrice: 25,
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch('https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

</details>

### Update Tactic Allocation - Priority

This endpoint allows clients to update a priority allocation for a specific tactic. The options here are only
whole numbers. More than one tactic can have the same priority allocation. This can only be used if the
tactic is currently using priority allocation.

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

#### ENDPOINT

```txt
/v1/tactic/{tacticid}
```

If successful in your request the response will be similar to above with a `200`.

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191' \
--header 'Content-Type: application/json' \
--header 'Authorization: <token>' \
--data '{    "priority": 2 }'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191"

payload = json.dumps({
  "priority": 2
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': '<token>'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{    \"priority\":2 }");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "<token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', '<token>')

const raw = JSON.stringify({
  priority: 2,
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch('https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

### Update Tactic Allocation - Dollar Allocation

This endpoint allows clients to update a dollar allocation for a specific tactic. Only whole numbers will
be accepted. E.g. $5 = 5. This can only be used if the tactic is currently using dollar allocation.

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

#### ENDPOINT

```txt
/v1/tacticid/{tacticid}
```

If successful in your request the response will be similar to above with a `200`.

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191' \
--header 'Content-Type: application/json' \
--header 'Authorization: <token>' \
--data '{    "dollarAllocation": 2 }'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191"

payload = json.dumps({
  "dollarAllocation": 2
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': '<token>'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{    \"dollarAllocation\": 2 }");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "<token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', '<token>')

const raw = JSON.stringify({
  dollarAllocation: 2,
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch('https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

### Update Tactic Allocation - Percent Allocation

This endpoint allows clients to update a percent allocation for a specific tactic. Please enter a whole
number as the percent, no decimals. E.g. 32% = 32. This can only be used if the tactic is currently using
dollar allocation.

![PUT](https://img.shields.io/badge/HTTP%20Method-PUT-fca130?style=for-the-badge)

#### ENDPOINT

```txt
/v1/tactic/{tacticid}
```

If successful in your request the response will be similar to above with a `200`.

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### CURL

```bash
curl --location --request PUT 'https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191' \
--header 'Content-Type: application/json' \
--header 'Authorization: <token>' \
--data '{    "percentAllocation": 25 }'
```

#### PYTHON

```python
import requests
import json

url = "https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191"

payload = json.dumps({
  "percentAllocation": 25
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': '<token>'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

```

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{    \"percentAllocation\": 25 }");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191")
  .method("PUT", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Authorization", "<token>")
  .build();
Response response = client.newCall(request).execute();
```

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/json')
myHeaders.append('Authorization', '<token>')

const raw = JSON.stringify({
  percentAllocation: 25,
})

const requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow',
}

fetch('https://lifeapi.pulsepoint.com/RestApi/v1/tactic/228191', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>
