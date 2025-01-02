# **Text Categorization API**

A machine-learning-powered API that assigns a given piece of text to the most relevant category from a predefined index. Built for businesses and professionals who need to quickly and accurately categorize content, such as websites, blogs, or other textual data.

---

## **Overview**

The **Text Categorization API** uses state-of-the-art Natural Language Processing (NLP) models to analyze input text and match it to a predefined list of categories. This service is highly customizable, scalable, and containerized for easy deployment. 

### **Key Features**
- **Text Embeddings**: Processes text using cutting-edge NLP models to understand semantic meaning.
- **Customizable Methods**: Three different methods for processing text:
  1. **Chunk-based**: Breaks the text into smaller segments for processing (default).
  2. **Summarization-based**: Summarizes the text before processing.
  3. **Full-text**: Processes the entire text without segmentation or summarization.
- **Containerized Architecture**: Fully Dockerized for easy deployment and scaling.
- **REST API**: Built with FastAPI for fast, asynchronous operations.

---

## **How It Works**

1. **Define a Category Index**: The API uses a predefined set of categories, each associated with a representative description or example text.
   - Example:
     ```json
     {
       "Technology": "Advancements in AI, programming, and computing.",
       "Health": "Tips and practices for a healthy lifestyle.",
       "Finance": "Advice on saving, investing, and managing money."
     }
     ```

2. **Process Input Text**: The input text is processed using one of three methods:
   - **Chunk-based**: Splits the text into smaller segments and averages the embeddings.
   - **Summarization-based**: Summarizes the text first and then calculates embeddings.
   - **Full-text**: Uses the full text for embeddings without chunking or summarization.

3. **Match Text to Category**: Using semantic embeddings, the API calculates the similarity between the input text and each category's description. The category with the highest similarity score is returned.

---

## **Getting Started**

### **Prerequisites**
- Docker and Docker Compose installed on your system.

---

### **Setup**

#### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/text-categorization-api.git
cd text-categorization-api
```

#### **2. Run the Application Using Docker Compose**
Build and start the containers:
```bash
docker-compose up --build
```

#### **3. Use the Client**
The client runs interactively in the terminal. You can provide your text input and select the processing method (default is chunk-based).

---

## **Using the API**

The API exposes an endpoint to categorize text. Below is the reference for making requests.

### **POST /categorize**

#### **Request**
- **Body** (JSON):
  ```json
  {
    "text": "Your input text here.",
    "method": "chunk"  // Optional: "chunk", "summary", or "full" (default is "chunk")
  }
  ```

#### **Response**
- **Success** (HTTP 200):
  ```json
  {
    "category": "Technology"
  }
  ```
- **Error** (HTTP 400):
  ```json
  {
    "detail": "Summarizer must be provided for 'summary' method."
  }
  ```

---

## **Architecture**

### **Tech Stack**
- **Backend**: FastAPI for API operations.
- **Text Processing**: SentenceTransformers for embeddings and HuggingFace Transformers for summarization.
- **Containerization**: Docker for easy deployment and portability.

### **Directory Structure**
```plaintext
project/
├── server/
│   ├── app.py                # FastAPI application
│   ├── categorizer.py        # Text categorization logic
│   ├── Dockerfile            # Dockerfile for the server
│   ├── requirements.txt      # Dependencies for the server
│
├── client/
│   ├── client.py             # Interactive client for testing the API
│   ├── Dockerfile            # Dockerfile for the client
│   ├── requirements.txt      # Dependencies for the client
│
├── docker-compose.yml        # Orchestration for server and client containers
```

---

## **Example Workflow**

### **1. Define Categories**
Define a list of categories in the `server/app.py` file:
```python
INDEX = {
    "Technology": "Advancements in AI, programming, and computing.",
    "Health": "Tips and practices for a healthy lifestyle.",
    "Finance": "Advice on saving, investing, and managing money."
}
```

### **2. Input Text**
Input:
```plaintext
"Artificial intelligence and machine learning are revolutionizing industries worldwide."
```

### **3. Processing Method**
Select a method:
- **Chunk-based** (default)
- **Summarization-based**
- **Full-text**

### **4. Output**
The API assigns the text to the most relevant category:
```json
{
  "category": "Technology"
}
```

---

## **Development**

### **Run Locally**

#### **1. Install Server Dependencies**
```bash
cd server
pip install -r requirements.txt
```

#### **2. Run the Server**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

#### **3. Test the Client**
Run the client interactively:
```bash
cd client
python client.py
```

---

## **Contributing**

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them to your fork.
4. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any questions or feedback, please open an issue or contact us at [your-email@example.com](mailto:your-email@example.com).

---

### **Docker Compose Example**

Here’s how the containers are connected using Docker Compose:

#### **docker-compose.yml**
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

## **Common Questions**

### **1. What types of text can I use?**
You can input any text (e.g., blog content, website descriptions, or other textual data) that needs categorization.

### **2. How accurate is the categorization?**
Accuracy depends on the quality of the index. Use descriptive and representative text for each category in the index to achieve optimal results.

### **3. Can I add or modify categories?**
Yes, you can customize the `INDEX` variable in the `server/app.py` file with new categories and descriptions.
