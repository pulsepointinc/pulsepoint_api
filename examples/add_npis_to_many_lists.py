import time
import requests

API_ROOT = "https://lifeapi.pulsepoint.com/RestApi/v1/npi/npi-list"
TIMEOUT = 10           # seconds
MAX_RETRIES = 3        # simple retry loop
BACKOFF_SECONDS = 1.0  # grows linearly per retry

def post_npis_to_lists(list_ids, npis):
    session = requests.Session()  # reuse connection; easy speed win
    
    for list_id in list_ids:
        url = f"{API_ROOT}/{list_id}"
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                res = session.post(url, json=npis, timeout=TIMEOUT)
                if 200 <= res.status_code < 300:
                    print(f"OK: list {list_id} ({len(npis)} NPIs)")
                    break
                    
                # retry only on likely-transient statuses
                if res.status_code in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES:
                    time.sleep(BACKOFF_SECONDS * attempt)
                    continue
                    
                print(f"FAIL: list {list_id} status {res.status_code}: {res.text[:200]}")
                break
                
            except requests.RequestException as e:
                if attempt < MAX_RETRIES:
                    time.sleep(BACKOFF_SECONDS * attempt)
                    continue
                    
                print(f"ERROR: list {list_id}: {e}")

if __name__ == "__main__":
    list_ids = [123456, 789012, 678345]  # your list IDs
    npis = ["1993840271", "2359846710", "3092816742", "1875902345", "2294836715"]  # your NPIs
    post_npis_to_lists(list_ids, npis)
