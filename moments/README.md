# MOMENTS API DOCUMENTATION

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

## USER AUTHENTICATION (OAUTH 2.0)

The NPI List API uses OAuth 2.0 in order to authorize its users. A typical client's Life account has many users and each user is assigned a unique username/password combination that they use to access the Life Platform. The same username/password credentials can be used to access the NPI Life API as well. Additionally, a unique client_secret is assigned to each organization in Life. Your PulsePoint Representative will provide you with access to this client_secret.

Developers in an organization can use any username/password combination to authenticate the NPI List API. We now provide each step for authentication in detail below with examples.

### 1. Send username/password credentials to the endpoint, providing additional parameters

#### ENDPOINT

```txt
oauth/token
```

- `grant_type=password`
- user `client_id:client_secret`
- username
- password

**EXAMPLE CURL REQUEST**

```bash
curl --request POST \
--url 'https://lifeapi.pulsepoint.com/RestApi/oauth/token' \
--user '$client_id:$client_secret'
--header 'content-type: application/x-www-form-urlencoded' \
--data 'username=$USERNAME' \
--data 'password=$PASSWORD' \
--data grant_type=password
```

### 2. The response will be JSON which includes fields expires_in, as well as access_token and refresh_token

- `expires_in` is in seconds. Please ensure that if you need to refresh the token, to check the expires_in
- The `access_token` is valid for 6000 seconds (100 minutes) and the `refresh_token` is valid for 604800 seconds (7 days)
- The `access_token` and `refresh_token` type is bearer.

**SAMPLE RESPONSES**

```json
{
  "access_token": "49923c00-bfca-4591-a54a-b308dc811a76",
  "token_type": "bearer",
  "refresh_token": "22bedfd4-62d3-42bc-9467-668b20966110",
  "expires_in": 4887,
  "scope": "read write"
}
```

**EXAMPLE CURL REQUEST**

```bash
curl --request POST \
--url 'https://lifeapi.pulsepoint.com/RestApi/oauth/token' \
--header 'content-type: application/x-www-form-urlencoded' \
--user '$client:$secret'
--data grant_type=refresh_token \
--data refresh_token=$REFRESH_TOKEN

```

- `--user '$client:$secret'`
- `--data grant_type=refresh_token`
- `--data refresh_token=$REFRESH_TOKEN`

### 3. Using the refresh token, we can get a “new” access token alongside a new refresh token using the parameters

```bash
curl --request POST \
--url 'https://lifeapi.pulsepoint.com/RestApi/oauth/token' \
--header 'content-type: application/x-www-form-urlencoded' \
--user '$client:$secret'
--data grant_type=refresh_token \
--data refresh_token=$REFRESH_TOKEN
```

When using the access token, include the same header when calling the NPI API. `“Authorization: Bearer {access_token}”`

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for CURL, Python, Java and JavaScript
<br><br>

#### PYTHON

```python
import requests

url = "https://lifeapi.pulsepoint.com/RestApi/oauth/token"

payload = 'username=<your-username>&password=<your-password>&grant_type=password'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


```

---

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "username=<your-username>&password=<your-password>&grant_type=password");
Request request = new Request.Builder()
  .url("https://lifeapi.pulsepoint.com/RestApi/oauth/token")
  .method("POST", body)
  .addHeader("Content-Type", "application/x-www-form-urlencoded")
  .build();
Response response = client.newCall(request).execute();
```

---

#### JAVASCRIPT

```javascript
const myHeaders = new Headers()
myHeaders.append('Content-Type', 'application/x-www-form-urlencoded')

const urlencoded = new URLSearchParams()
urlencoded.append('username', '<your-username>')
urlencoded.append('password', '<your-password>')
urlencoded.append('grant_type', 'password')

const requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: urlencoded,
  redirect: 'follow',
}

fetch('https://lifeapi.pulsepoint.com/RestApi/oauth/token', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.error(error))
```

</details>

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

| Error Code                                                                            | Description                           |
| ------------------------------------------------------------------------------------- | ------------------------------------- |
| ![400 Bad Request](https://img.shields.io/badge/400-f93e3e?style=for-the-badge)       |                                       |
| ![401 Bad Request](https://img.shields.io/badge/401-f93e3e?style=for-the-badge)       | UNAUTHORIZED                          |
| ![429 Too many requests](https://img.shields.io/badge/429-f93e3e?style=for-the-badge) | Server has received too many requests |

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
