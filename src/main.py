import re
import sys
import json
import argparse
import os

def extract_strings(data):
    return re.findall(b'[ -~]{4,}', data)

def classify(strings):
    results = {
        "urls": [],
        "ips": [],
        "emails": [],
        "base64_suspects": []
    }
    
    for s in strings:
        try:
            text = s.decode('utf-8')
        except:
            continue
            
        if re.search(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text):
            if text not in results["urls"]:
                results["urls"].append(text)
                
        elif re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text):
            if text not in results["ips"]:
                results["ips"].append(text)
                
        elif re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', text):
            if text not in results["emails"]:
                results["emails"].append(text)
                
        elif re.match(r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', text) and len(text) > 30:
            if text not in results["base64_suspects"]:
                results["base64_suspects"].append(text)
                
    return results

def main():
    parser = argparse.ArgumentParser(description="Static String Extractor")
    parser.add_argument('-f', '--file', required=True, help="Analiz edilecek dosya")
    parser.add_argument('-o', '--out', default='report.json', help="Cikti dosyasi")
    
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print("Hata: Dosya bulunamadi.")
        sys.exit(1)

    with open(args.file, 'rb') as f:
        data = f.read()

    raw_strings = extract_strings(data)
    classified_data = classify(raw_strings)

    out_dir = os.path.dirname(args.out)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(classified_data, f, indent=4)

    print(f"Analiz tamamlandi. Sonuclar: {args.out}")

if __name__ == '__main__':
    main()
