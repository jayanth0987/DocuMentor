import xml.etree.ElementTree as ET
import os

print("📥 Parsing sitemap...")

tree = ET.parse("data/sitemap.xml")
root = tree.getroot()

urls = [loc.text for loc in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

print(f"Total URLs: {len(urls)}")

fastapi_urls = [url for url in urls if "fastapi.tiangolo.com" in url and not url.endswith(".xml")]

print(f"FastAPI URLs: {len(fastapi_urls)}")

with open("data/raw/full_urls.txt", "w") as f:
    f.write("\n".join(fastapi_urls))

print("✅ data/raw/full_urls.txt created!")
print("First 5:")
for url in fastapi_urls[:5]:
    print(f"  {url}")
