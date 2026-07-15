
import asyncio
import time
import httpx
 
# ---- Configuration -------------------------------------------------------
STUDENT_ID = "6720301003"
BASE_URL = "http://172.16.2.117:8088"   # change if your server address differs
 
LIGHT_IDS = ["light_1", "light_2", "light_3", "light_4"]
 
 
async def set_light(client: httpx.AsyncClient, light_id: str, status: str) -> dict:
    """Send a POST request to turn a single light ON or OFF."""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/{light_id}"
    start = time.monotonic()
 
    resp = await client.post(url, json={"status": status})
    resp.raise_for_status()
    data = resp.json()
 
    elapsed = time.monotonic() - start
    print(f"[{light_id}] -> {status} | took {elapsed:.2f}s | server response: {data}")
    return data
 
 
async def get_all_status(client: httpx.AsyncClient) -> dict:
    """Fetch the current status of all lights."""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights"
    resp = await client.get(url)
    resp.raise_for_status()
    return resp.json()
 
 
async def turn_on_all_lights_sequentially():
    # Give each request generous timeout since the server intentionally
    # delays responses (up to 2.0s) to simulate hardware latency.
    async with httpx.AsyncClient(timeout=10.0) as client:
        print("Current status before:")
        before = await get_all_status(client)
        print(before, "\n")
 
        print(f"--- Turning ON all {len(LIGHT_IDS)} lights one by one (left to right) ---")
        start = time.monotonic()
 
        results = []
        for light_id in LIGHT_IDS:
            # await here means we wait for this light to finish
            # before moving on to the next one - no concurrency.
            result = await set_light(client, light_id, "ON")
            results.append(result)
 
        total_elapsed = time.monotonic() - start
        print(f"\nAll lights are ON. Total elapsed time: {total_elapsed:.2f}s")
        print("(Should be ~4.5s - the sum of all delays - since we run one at a time)")
 
        return results
 
 
async def reset_all_lights():
    """Optional helper: reset all lights back to OFF."""
    url = f"{BASE_URL}/api/{STUDENT_ID}/lights/reset"
    async with httpx.AsyncClient() as client:
        resp = await client.delete(url)
        resp.raise_for_status()
        print(resp.json())
 
 
if __name__ == "__main__":
    asyncio.run(turn_on_all_lights_sequentially())
