# USER AUTHENTICATION (OAUTH 2.0)

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
