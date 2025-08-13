# Pulsepoint API Documentation

![ThingsToNote](https://img.shields.io/badge/THINGS_TO_NOTE-blue?style=for-the-badge)

1. **Regarding API Key Management**: Pulsepoint currently do not rotate API Keys for a user. However, keys are restricted to a user on an account level. Furthermore, usage of the API using the key is limited to users who have permission to the account on the Life platform with additional permission to use the API. This is all managed by our engineering team.

   Please see [Section 2 of our Auth documentation](https://github.com/pulsepointinc/pulsepoint_api/blob/main/AUTH.md#2-the-response-will-be-json-which-includes-fields-expires_in-as-well-as-access_token-and-refresh_token) for TTL for our tokens.

2. **API Updates**: Any additional endpoints added to the API will be part of our regular development process. Which means that they will be initially scoped out by our Product team and then in added to a development cycle in an upcoming sprint. As with our releases, any changes will be communicated to stakeholders through external release notes and direct communication from Pulsepoint to the partner. These will include updated documentation to include the new endpoints added to the API.

3. **API Maintenance**: Our API should be up at all times. However, during major deployments that usually happen monthly, it may be down for a few minutes only.

## AUTHENTICATION

For documentation on how to use OAuth 2.0 in order to authorize your requests please read through our [Authentication documentation](AUTH.md)

![Important to Note](https://img.shields.io/badge/IMPORTANT_TO_NOTE-red?style=for-the-badge)

- Clients may only GET Smart Lists, lists created by file name and lists with labels. `POST` requests are not allowed for these type of lists.
- The max amount of NPI's per list is 1 million.
- The max usage of the API per client is:
  - Create/Modify/Delete: 1 call per second, max 10 calls per minute
  - GET List = 1 per second

## NPI LIST API

PulsePoint's clients use NPI lists for campaign targeting. These lists can change often and are customizable by each client. Clients now have direct access and complete control of their standard NPI lists and NPI lists with attributes via the NPI List API.

[Link to Documentation](npi/README.md)

## MOMENTS API

The purpose of this API is to provide the list of NPIs that reach brand moment qualification criteria.

[Link to Documentation](moments/README.md)

## CREATIVES API

Effortlessly upload new creatives and modify existing ones directly through an ad server's user interface

[Link to Documentation](creatives/README.md)

## CAMPAIGN & LINEITEM CREATION

TODO: Write blurb

[Link to Documentation](campaign_lineitem_creation/README.md)

## CAMPAIGN MGNT API

PulsePoint's clients use budgeting to strategically optimize their
campaigns and tactics. Clients may want to change budgeting
and allocations rapidly. Now with access to the new Campaign API,
clients can seamlessly change budgeting options on their tactics
without logging into the platform.

[Link to Documentation](campaign_mgnt/README.md)

---

![IMPORTANT](https://img.shields.io/badge/PLEASE_NOTE-661DE1?style=for-the-badge)

The base URL for all API calls is the following:

```txt
https://lifeapi.pulsepoint.com/RestApi/
```

<p align="center"><img src="https://raw.githubusercontent.com/pulsepointinc/npiapi_docs/main/misc/banner.png" /></p>
<p align="center">&copy; 2025  <a href="https://www.pulsepoint.com/" target="_blank">PulsePoint, Inc</a>
