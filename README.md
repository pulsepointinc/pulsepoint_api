# NPI LIST API DOCUMENTATION

## INTRODUCTION

PulsePoint's clients use NPI lists for campaign targeting. These lists can change often and are customizable by each client. Clients now have direct access and complete control of their standard NPI lists and NPI lists with attributes via the NPI List API.

This document describes the functionality supported by the NPI List API. PulsePoint provides a REST API to access and manage the following actions for two different types of NPI lists:

### NPI LISTS

1. [Get an NPIs liss](#1-get-an-npi-list)
2. [Get all NPI list](#2-get-all-npi-lists)
3. [Create an NPI list]()
4. [Replace NPIs in a list]()
5. [Get Add NPIs into a list]()
6. [Delete NPIs from a list]()

### NPI lists with attributes

1. [Create an NPI list with attributes]()
2. [Replace an NPI list with attributes]()
3. [View an NPI list with attributes]()

---

All examples in this documentation use the `curl` command line tool: `http://curl.haxx.se/` Note that for all statements including `<username>:<password>` and `<client_secret>` you will need to replace with your Life username and password and client_secret respectively.

## USER AUTHENTICATION (OAUTH 2.0)

The NPI List API uses OAuth 2.0 in order to authorize its users. A typical client's Life account has many users and each user is assigned a unique username/password combination that they use to access the Life Platform. The same username/password credentials can be used to access the NPI Life API as well. Additionally, a unique client_secret is assigned to each organization in Life. Your PulsePoint Representative will provide you with access to this client_secret.

Developers in an organization can use any username/password combination to authenticate the NPI List API. We now provide each step for authentication in detail below with examples.

### 1. Send username/password credentials to the endpoint, providing additional parameters

**ENDPOINT**

```txt
https://lifeapi.pulsepoint.com/RestApi/oauth/token
```

- `grant_type=password`
- user `client_id:client_secret`
- username
- password

**EXAMPLE CURL REQUEST**

```bash
> curl --request POST \
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
> curl --request POST \
--url 'https://lifeapi.pulsepoint.com/RestApi/oauth/token' \
--header 'content-type: application/x-www-form-urlencoded' \
--user '$client:$secret'
--data grant_type=refresh_token \
--data refresh_token=$REFRESH_TOKEN

```

a. `--user '$client:$secret'`
b. `--data grant_type=refresh_token`
c. `--data refresh_token=$REFRESH_TOKEN`

### 3. Using the refresh token, we can get a “new” access token alongside a new refresh token using the parameters

## NPI API ENDPOINTS, NPI ONLY LISTS

### 1. Get an NPI list

This endpoint allows clients to retrieve a list of all NPI's that are in a single NPI list.

**ENDPOINT**

```txt
https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{listID}
```

**SAMPLE REQUEST**

```txt
https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/4210
```

**SAMPLE RESPONSE**

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

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for Python, Java and JavaScript
<br><br>

#### PYTHON

```python
import requests
url = 'https://api.ouraring.com/v2/usercollection/daily_sleep'
params={
    'start_date': '2021-11-01',
    'end_date': '2021-12-01'
}
headers = {
  'Authorization': 'Bearer <token>'
}
response = requests.request('GET', url, headers=headers, params=params)
print(response.text)
```

---

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01")
  .method("GET", null)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

---

#### JAVASCRIPT

```javascript
var myHeaders = new Headers();
myHeaders.append('Authorization', 'Bearer <token>');
var requestOptions = {
  method: 'GET',
  headers: myHeaders,
fetch('https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

</details>

### 2. Get all NPI lists

This endpoint allows clients to get a list of all NPI lists associated with an account.

**ENDPOINT**

```txt
https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/{accountID}
```

**SAMPLE REQUEST**

```txt
https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/559145
```

**SAMPLE RESPONSE**

```json
[
  {"id": 30, "advertisers": ["Demo"], "name": "mylisttwo"},
  {
    "id": 38,
    "advertisers": ["Demo"],
    "name": "mylisttwo1sdfafdsmylisttwo1sdfafdsmylisttwo1sdfafd"
  },
  {"id": 39, "advertisers": ["Demo"], "name": "myNPItest"}
]
```

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for Python, Java and JavaScript
<br><br>

#### PYTHON

```python
import requests
url = 'https://api.ouraring.com/v2/usercollection/daily_sleep'
params={
    'start_date': '2021-11-01',
    'end_date': '2021-12-01'
}
headers = {
  'Authorization': 'Bearer <token>'
}
response = requests.request('GET', url, headers=headers, params=params)
print(response.text)
```

---

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01")
  .method("GET", null)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

---

#### JAVASCRIPT

```javascript
var myHeaders = new Headers();
myHeaders.append('Authorization', 'Bearer <token>');
var requestOptions = {
  method: 'GET',
  headers: myHeaders,
fetch('https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

</details>

### 3. Create an NPI list

This endpoint allows clients to create a new NPI list and add NPIs to the new list.

**ENDPOINT**

```txt
https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/{accountid}
```

**SAMPLE REQUEST**

```txt
https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/account/559145
```

```json
{
  "name": "TEST_2022_1",
  "npis": ["3137933127", "3134730121"],
  "advertisers": ["Demo"],
  "applications": ["LIFE"]
}
```

**Note**: The applications field accepts either `[“LIFE”]`, `[“SIGNAL”]` or `[‘SOCIAL”]`

**SAMPLE RESPONSE**

```json
[
  {"id": 30, "advertisers": ["Demo"], "name": "mylisttwo"},
  {
    "id": 38,
    "advertisers": ["Demo"],
    "name": "My Demo list"
  },
  {"id": 39, "advertisers": ["Demo"], "name": "myNPItest"}
]
```

<details>
<summary>
    <strong>REQUEST EXAMPLES</strong>
</summary>
<br>
Below are a list of code examples for Python, Java and JavaScript
<br><br>

#### PYTHON

```python
import requests
url = 'https://api.ouraring.com/v2/usercollection/daily_sleep'
params={
    'start_date': '2021-11-01',
    'end_date': '2021-12-01'
}
headers = {
  'Authorization': 'Bearer <token>'
}
response = requests.request('GET', url, headers=headers, params=params)
print(response.text)
```

---

#### JAVA

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01")
  .method("GET", null)
  .addHeader("Authorization", "Bearer <token>")
  .build();
Response response = client.newCall(request).execute();
```

---

#### JAVASCRIPT

```javascript
var myHeaders = new Headers();
myHeaders.append('Authorization', 'Bearer <token>');
var requestOptions = {
  method: 'GET',
  headers: myHeaders,
fetch('https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2021-11-01&end_date=2021-12-01', requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

</details>
