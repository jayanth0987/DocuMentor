 
import requests
from urllib.parse import urlparse
import os

URLS = [
    "https://fastapi.tiangolo.com/",
    "https://fastapi.tiangolo.com/tutorial/",
    "https://fastapi.tiangolo.com/tutorial/first-steps/",
    "https://fastapi.tiangolo.com/tutorial/path-params/",
    "https://fastapi.tiangolo.com/tutorial/body/"
]

print("🚀 FastAPI Scraper")
os.makedirs("../../data/raw", exist_ok=True)

for i, url in enumerate(URLS, 1):
    print(f"[{i}/5] {url}")
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        
        path = urlparse(url).path.strip('/').replace('/', '_') or 'index'
        filename = f"fastapi_{path}.html"
        # filepath = f"../../data/raw/{filename}"
        filepath = r"D:\Documentor\DocuMentor\data\raw\fastapi_tutorial_" + path + ".html"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(r.text)
        print(f"✅ {filename}")
    except Exception as e:
        print(f"❌ {e}")

print("✅ Complete!")
