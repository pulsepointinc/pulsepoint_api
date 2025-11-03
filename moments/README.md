# MOMENTS API DOCUMENTATION

# Important notice

PulsePoint API documentation has a new home! [Link](https://pulsepoint-platform.readme.io/docs/getting-started#/)

This platform provides guides explaining how each endpoint works as well as the different fields supported. The API Reference tab can be used to test each endpoint right in the app. You can authenticate using your UN/PW and Key and Secret provided by your account manager.

We will be deprecating these Github docs by the end of the year (December 31, 2025).

Please reach out with any questions!

## INTRODUCTION

The purpose of this API is to provide the list of NPIs that reach brand moment qualification criteria.

### NPI LISTS

1. [Get Moment NPI's](#1-get-moments-npis)

---

All examples in this documentation use the `curl` command line tool: `http://curl.haxx.se/` Note that for all statements including `<username>:<password>` and `<client_secret>` you will need to replace with your Life username and password and client_secret respectively.

![IMPORTANT](https://img.shields.io/badge/PLEASE_NOTE-661DE1?style=for-the-badge)

The base URL for all API calls is the following:

```txt
https://lifeapi.pulsepoint.com/RestApi/
```

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

## MOMENTS API ENDPOINT

### 1. Get Moments NPI's

This endpoint allows clients to retrieve a list of all NPIs that are currently part of a Moment. You will need to have the Moments List ID in order to retrieve its corresponding NPI’s.

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
  "advertisers": ["Demo"]
}
```

| Error Code                                                                            | Description                                         |
| ------------------------------------------------------------------------------------- | --------------------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       | You do not have permission to view this Smart List. |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests               |

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
