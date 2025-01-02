import argparse
import requests
import json

API_URL = "http://server:8000/categorize"

def categorize_text(text, method="chunk"):
    payload = {"text": text, "method": method}
    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        return response.json()['category']
    else:
        return f"Error: {response.status_code}, {response.json()['detail']}"

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Categorize general text into categories.")
    parser.add_argument("--from-list", help="File containing a list of general texts in JSON format", default=None)
    parser.add_argument("--method", help="Method for categorization (chunk, summary, or full)", default="chunk")
    args = parser.parse_args()

    if args.from_list:
        # Read the JSON file
        with open(args.from_list, "r") as file:
            data = json.load(file)  # Load the JSON content

        # Iterate through each entry in the JSON file
        for idx, entry in enumerate(data, start=1):
            text = entry['text']  # Get the text to categorize
            print(f"Categorizing text {idx}: {text}")
            category = categorize_text(text, args.method)
            print(f"Category: {category}\n")
    else:
        # If no file is provided, proceed with manual input
        text = input("Enter your text: ")
        method = input("Enter method (chunk, summary, or full): ") or "chunk"
        category = categorize_text(text, method)
        print(f"Category: {category}")

if __name__ == "__main__":
    main()
