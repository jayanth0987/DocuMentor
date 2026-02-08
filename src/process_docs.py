import os
import glob
from bs4 import BeautifulSoup
import html2text

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove navigation, sidebars, footers (FastAPI-specific)
    for element in soup.find_all(['nav', 'aside', 'footer', 'header']):
        element.decompose()
    
    # Remove scripts, styles, common noise
    for element in soup.find_all(['script', 'style']):
        element.decompose()
    
    # FastAPI extras: remove toc, sidebar classes
    for elem in soup.find_all(class_=['toc', 'sidebar', 'nav-link']):
        elem.decompose()
    
    # Clean empty tags
    for elem in soup.find_all():
        if elem.name == 'p' and not elem.get_text(strip=True):
            elem.decompose()
    
    return str(soup)

def process_docs():
    raw_dir = 'data/raw/full'
    processed_dir = 'data/processed'
    os.makedirs(processed_dir, exist_ok=True)
    
    html_files = glob.glob(os.path.join(raw_dir, '*.html'))
    print(f"Found {len(html_files)} HTML files in {raw_dir}")
    
    processed_count = 0
    for html_path in html_files:
        try:
            # Read HTML
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Clean HTML
            cleaned_html = clean_html(html_content)
            
            # Convert to Markdown
            h = html2text.HTML2Text()
            h.body_width = 0  # No line wrapping
            h.ignore_links = False
            markdown = h.handle(cleaned_html)
            
            # Save Markdown (preserve filename)
            md_filename = os.path.basename(html_path).replace('.html', '.md')
            md_path = os.path.join(processed_dir, md_filename)
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            processed_count += 1
            if processed_count % 50 == 0:
                print(f"Processed {processed_count}/{len(html_files)}")
                
        except Exception as e:
            print(f"Error processing {html_path}: {e}")
    
    print(f"✅ Complete! Processed {processed_count} files to {processed_dir}")

if __name__ == "__main__":
    process_docs()
