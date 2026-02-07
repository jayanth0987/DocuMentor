import time
import requests
from urllib.parse import urlparse
import os

print("🚀 Mass scraping...")
with open("data/raw/full_urls.txt") as f:
    URLS = [line.strip() for line in f if line.strip()]

print(f"Found {len(URLS)} URLs")
os.makedirs("data/raw/full", exist_ok=True)
failed = 0

for i, url in enumerate(URLS, 1):
    print(f"\r[{i}/{len(URLS)}] {url[:60]}...", end="")
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        path = urlparse(url).path.strip("/").replace("/", "_") or "index"
        filename = f"fastapi_{path}.html"
        filepath = f"data/raw/full/{filename}"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(r.text)
    except Exception:
        failed += 1
    time.sleep(0.3)

print(f"\n✅ Complete! Failed: {failed}/{len(URLS)}")
