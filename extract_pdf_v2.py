import re

def extract_content(pdf_path):
    print(f"Reading: {pdf_path}")
    try:
        with open(pdf_path, 'rb') as f:
            data = f.read()
            
        # Attempt to find text streams
        # 1. Split by 'stream' and 'endstream' markers if standard PDF
        # 2. Or just brute force regex for paragraphs
        
        # Simple bruteforce for text-like patterns in Latin-1
        text = data.decode('latin-1', errors='ignore')
        
        # Look for (Title Case Name) or (Dates) or (Keywords)
        # Filter for standard ASCII text chunks > 50 chars
        
        # Clean up PDF formatting chars
        clean_text = re.sub(r'[^A-Za-z0-9\s@\.,\-\(\)]', '', text)
        
        # Look for chunks of text
        matches = re.findall(r'[A-Za-z0-9\s@\.,\-\(\)]{20,}', text)
        
        unique_matches = sorted(list(set(matches)), key=len, reverse=True)
        
        print("--- EXTRACTED CANDIDATES ---")
        for m in unique_matches[:20]: # Print top 20 longest strings
             if "obj" not in m and "endobj" not in m:
                print(f"[CANDIDATE]: {m.strip()}")
                
    except Exception as e:
        print(e)

if __name__ == "__main__":
    extract_content("d:\\Work\\Portofolio\\CV ATS_Iqbal.pdf")
