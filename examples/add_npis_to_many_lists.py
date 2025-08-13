import requests

list_ids = [123456, 789012, 678345]  # Replace with your actual list IDs
npis = [
    "1993840271",
    "2359846710",
    "3092816742",
    "1875902345",
    "2294836715",
]  # Replace with your actual NPIs

"""
NOTE:
This example shows how you're able to send the same NPIs to multiple lists using a for loop.
The for loop iteratres through the list_ids list sending the list of NPIs to each liust ID.

You may need to use a timer to avoid hitting rate limits if you have a large number of lists or NPIs.
"""

try:
    for list_id in list_ids:
        res = requests.post(
            f"https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list/{list_id}",
            json=npis,
        )
        res.raise_for_status()  # Raise an error for bad responses
        if res.status_code == 200:
            print(f"Successfully added NPIs to list {list_id}")
except requests.exceptions.RequestException as e:
    raise e
