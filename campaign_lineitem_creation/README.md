# Creative & Line Item Creation

TODO: write intro

- [Creative \& Line Item Creation](#creative--line-item-creation)
  - [1. Get a Campaign](#1-get-a-campaign)
    - [Response](#response)
  - [2. Create a Campaign](#2-create-a-campaign)
  - [Request](#request)
  - [Example response](#example-response)
  - [⚠️ Error Handling](#️-error-handling)
    - [❌ Sample Validation Errors](#-sample-validation-errors)
  - [🚦 Rate Limiting](#-rate-limiting)
    - [Sample 429 Error](#sample-429-error)
  - [3. Get a Line Item](#3-get-a-line-item)
    - [Sample response](#sample-response)
  - [4. Get Advertiser IDs by Account ID](#4-get-advertiser-ids-by-account-id)
    - [Sample response](#sample-response-1)
  - [5. Get campaign ID by account and advertiser ID](#5-get-campaign-id-by-account-and-advertiser-id)
    - [Sample response](#sample-response-2)

### 1. Get a Campaign

This endpoint fetches the details, along with the line items, for a given campaign.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

```bash
/v1/campaignImport/{campaignId}
```

#### Response

```json
{
  "id": 84727,
  "name": "Campaign REST API SAMPLE",
  "description": "DESCRIPTION",
  "advertiser": "01- Advertiser",
  "budgetCap": "10000.0",
  "account": "559145",
  "drugName": "Tylenol PM",
  "basketDrugNames": ["Tylenol PM"],
  "customFieldSetting": [
    {
      "fieldId": 14062,
      "fieldName": "New Custom Field Campaign REST",
      "fieldValue": "custom field value"
    }
  ],
  "lineItems": [
    {
      "id": "94019",
      "name": "lineitem"
    }
  ],
  "frequencyCap": {
    "applyFrequencyCap": "true",
    "times": "10",
    "period": "DAY",
    "crossDevice": "Device",
    "untrackable": "false",
    "ipUntrackable": "false"
  },
  "creativeSeparations": [
    {
      "name": "WhatTest",
      "id": 1711
    },
    {
      "name": "TestNewCampaign",
      "id": 1787
    }
  ],
  "approvalStatus": "PendingApproval"
}
```

### 2. Create a Campaign

This endpoint can be used to create a campaign and its subsequent line item(s).

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

```bash
/v1/campaignImport/
```

### Request

```json
{
  "campaign": {
    "name": "Campaign REST API SAMPLE",
    "account": "559145",
    "description": "DESCRIPTION",
    "advertiser": "01- Advertiser",
    "budgetCap": "10000.00",
    "drugName": "Tylenol PM",
    "basketDrugNames": ["Tylenol PM"],
    "customFieldSetting": [
      {
        "isNewField": "true",
        "fieldName": "New Custom Field Campaign REST",
        "fieldValue": "custom field value"
      }
    ],
    "frequencyCap": {
      "applyFrequencyCap": "true",
      "times": "10",
      "period": "day",
      "hoursValue": "1",
      "crossDevice": "Per Device",
      "untrackable": "false",
      "ipUntrackable": "false"
    },
    "lineItems": [
      {
        "name": "lineitem",
        "costModel": "CPM",
        "description": "DESCRIPTION",
        "customFieldSetting": [
          {
            "isNewField": "true",
            "fieldName": "Line Item Custom Field REST",
            "fieldValue": "line item field value"
          }
        ],
        "flights": [
          {
            "budget": 50,
            "startDate": "2025-03-01 00:00",
            "endDate": "2025-03-31 23:59",
            "pacingMode": "Ahead",
            "pacingModePercentage": "12.1"
          },
          {
            "budget": 51,
            "startDate": "2025-04-01 00:00",
            "endDate": "2025-04-30 23:59",
            "pacingMode": "Even"
          }
        ],
        "inventoryType": "Display",
        "frequencyCap": {
          "applyFrequencyCap": "true",
          "times": "9",
          "period": "day",
          "hoursValue": "1",
          "crossDevice": "Per Device",
          "untrackable": "false",
          "ipUntrackable": "false"
        }
      }
    ]
  }
}
```

### Example response

```json
{
  "status": "success",
  "message": "Campaign and Line Items created successfully.",
  "data": {
    "campaignId": "123456",
    "campaignName": " Campaign REST API Sample",
    "lineItems": [
      {
        "lineItemId": "123456",
        "lineItemName": "LINEITEM"
      }
    ]
  }
}
```

## ⚠️ Error Handling

### ❌ Sample Validation Errors

| **Scenario**            | **Error Message**                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------- |
| Custom Field Exists     | `{"errors":{"INVALID_SETUP":["custom field name 'New Custom Field' already exists"]}}` |
| Duplicate Campaign Name | `{"errors":{"DUPLICATE_NAME":["Import Campaign Name is not unique"]}}`                 |
| Invalid Inventory Type  | `{"errors":{"INVALID_SETUP":["LineItem inventory type Displayss is invalid."]}}`       |
| Malformed JSON Payload  | `Invalid JSON payload at line 36, column 14: Unexpected character ('"')`               |

---

## 🚦 Rate Limiting

| **Method** | **Limit**                   |
| ---------- | --------------------------- |
| `GET`      | 50 requests / minute / user |
| `POST`     | 10 requests / minute / user |

### Sample 429 Error

```json
{
  "timestamp": "2025-01-29T15:19:21.2513",
  "status": 429,
  "error": "Too Many Requests",
  "path": "/RestApi/v1/campaignImport/",
  "errorMessage": {
    "errorDescription": "Too Many Requests."
  }
}
```

## 3. Get a Line Item

This endpoint fetches the details, along with the tactics for a given line item.

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

```bash
v1/campaignImport/lineitem/{lineitemID}
```

### Sample response

```json
{
  "id": "12345",
  "name": "LIneitem",
  "costModel": "CPM",
  "flights": [
    {
      "budget": "1.0",
      "startDate": "2025-03-27T00:00:00.000Z",
      "endDate": "2025-03-31T23:59:59.000Z",
      "pacingMode": "3",
      "pacingModePercentage": "12.0"
    },
    {
      "budget": "200.0",
      "startDate": "2024-09-17T00:00:00.000Z",
      "endDate": "2024-09-30T23:59:59.000Z",
      "pacingMode": "1",
      "pacingModePercentage": null
    }
  ],
  "inventoryType": "Display",
  "frequencyCap": {
    "times": "1",
    "hoursValue": "86400",
    "crossDevice": "Household"
  },
  "tactics": [
    {
      "id": "00001",
      "name": "Tactic"
    },
    {
      "id": "00002",
      "name": "NPI Tactic"
    }
  ]
}
```

## 4. Get Advertiser IDs by Account ID

This endpoint retrieves the Advertiser ID for a given account

![GET](https://img.shields.io/badge/HTTP%20Method-GET-61affe?style=for-the-badge)

```bash
v1/campaignImport/account/{accountId}/advertisers
```

### Sample response

```json
{
 "accountName": "CMI
 "accountId": 00001,
 "advertiserId": [
     1,
     2
 ]
}
```

## 5. Get campaign ID by account and advertiser ID

This endpoint retrieves a list of Campaign Ids under an account and adveriser ID

![POST](https://img.shields.io/badge/HTTP%20Method-POST-49cc90?style=for-the-badge)

```bash
v1/campaignImport/advertiser/{advertiserId}/account/{accountId}
```

### Sample response

```json
{
 "advertiserId": 001,
 "advertiserName": "CMIAdvertiser
 "campaignIds": [
     0001,
     0002,
     0003,
     0004,
     0005
   ]
}
```
