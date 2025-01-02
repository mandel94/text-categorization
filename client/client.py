import requests

API_URL = "http://server:8000/categorize"

def main():
    article = input("Enter your article: ")
    method = input("Enter method (chunk, summary, or full): ") or "chunk"

    payload = {"text": article, "method": method}
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        print(f"Category: {response.json()['category']}")
    else:
        print(f"Error: {response.status_code}, {response.json()['detail']}")

if __name__ == "__main__":
    main()
