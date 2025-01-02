# Text Categorization API Documentation

## Overview
The **Text Categorization API** is a machine-learning-powered API designed to assign a given piece of text to the most relevant category from a predefined index. This service is ideal for businesses and professionals who need to quickly and accurately categorize various content such as websites, blogs, or any textual data.

The service uses state-of-the-art **Natural Language Processing (NLP)** models for categorization and provides easy-to-deploy, containerized solutions.

---

## Key Features
- **Text Embeddings**: Utilizes advanced NLP models to understand the semantic meaning of text.
- **Customizable Methods**: Three categorization methods are available:
  - **Chunk-based**: Breaks the text into smaller segments (default method).
  - **Summarization-based**: Summarizes the text before processing.
  - **Full-text**: Processes the entire text without segmentation or summarization.
- **Containerized Architecture**: Fully Dockerized for easy deployment and scaling.
- **REST API**: Fast, asynchronous operations powered by **FastAPI**.

---

## How It Works
1. **Define a Category Index**: The API uses a predefined set of categories. Each category is associated with a description or example text.
    - Example of predefined categories:
      ```json
      {
        "Technology": "Advancements in AI, programming, and computing.",
        "Health": "Tips and practices for a healthy lifestyle.",
        "Finance": "Advice on saving, investing, and managing money."
      }
      ```

2. **Input Text**: The input text can be anything, from blog content to website descriptions.

3. **Process Input Text**: The input text is processed using one of the following methods:
   - **Chunk-based**: The text is broken into smaller segments and embeddings are averaged.
   - **Summarization-based**: The text is summarized before calculating embeddings.
   - **Full-text**: The entire text is processed as a single unit for embeddings.

4. **Match Text to Category**: Using semantic embeddings, the API calculates the similarity between the input text and each category’s description. The category with the highest similarity score is returned.

---

## Getting Started

### Prerequisites
1. Docker and Docker Compose should be installed on your system.

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/text-categorization-api.git
   cd text-categorization-api
   ```

2. **Run the Application Using Docker Compose**:
   Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. **Use the Client**:
   The client runs interactively in the terminal. You can input your text and select the processing method (default is chunk-based).

---

## Using the API

### Client Usage
The client interacts with the API and categorizes the provided text. It can process text either manually (via input) or from a JSON file containing multiple texts.

- **POST /categorize**: This endpoint receives the input text and categorizes it according to the predefined index.

#### Request Body (JSON):
```json
{
  "text": "Your input text here.",
  "method": "chunk"  // Optional: "chunk", "summary", or "full" (default is "chunk")
}
```

#### Response (Success):
```json
{
  "category": "Technology"
}
```

#### Response (Error):
```json
{
  "detail": "Summarizer must be provided for 'summary' method."
}
```

---

## Client Command-Line Interface (CLI)

### Description
The client script categorizes **general text** into predefined categories. The client allows you to either manually input text or read multiple texts from a JSON file for batch processing.

### Client Code
The client code reads from a JSON file containing general text entries. Each entry should have a `text` field containing the text to categorize.

#### Command-line arguments:
- **`--from-list`**: Path to the JSON file containing a list of texts to categorize.
- **`--method`**: Categorization method. Options: `chunk`, `summary`, `full`. Default is `chunk`.

### Usage

#### Manually Categorize Text
Run the following command and input text when prompted:
```bash
python client.py
```

#### Categorize Text from a JSON File
To categorize multiple pieces of text from a JSON file:
```bash
python client.py --from-list path/to/your/general_texts.json
```

---

## Example JSON Structure for `--from-list`:
The JSON file should contain an array of objects, where each object has a `text` field.

```json
[
  {
    "text": "The rapid advancement of artificial intelligence is transforming industries across the globe."
  },
  {
    "text": "Maintaining a healthy lifestyle involves regular exercise, balanced nutrition, and mental wellness."
  },
  {
    "text": "Financial planning is crucial for managing personal budgets, investments, and savings."
  }
]
```

---

## Docker Compose Example
The following `docker-compose.yml` file connects the server and client containers:

```yaml
version: '3.8'

services:
  server:
    build:
      context: ./server
    ports:
      - "8000:8000"
    container_name: text_categorization_server

  client:
    build:
      context: ./client
    depends_on:
      - server
    container_name: text_categorization_client
    stdin_open: true
    tty: true
```

---

## Common Questions

1. **What types of text can I use?**
   - Any general text (e.g., website descriptions, blog posts, or other textual content) that needs categorization.

2. **How accurate is the categorization?**
   - Accuracy depends on the quality of the predefined category index. Ensure each category is well-described for optimal results.

3. **Can I add or modify categories?**
   - Yes! You can modify or add new categories by editing the `INDEX` variable in the `server/app.py` file.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact

For questions or feedback, please open an issue or contact us at `your-email@example.com`.

--- 

