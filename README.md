## Project Structure

```text
.
├── app/
│   ├── agents/
│   ├── api/
│   ├── retrieval/
│   ├── schema/
│   └── main.py
├── config.py
├── data/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── scripts/
│   └── build_vector_db.py
├── services/
│   └── gemini_services.py
└── tests/
```

## Setup and Implementation

### 1. Environment Setup

Create a `.env` file in the root directory and configure your Gemini API Key.
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 2. Build the Vector Database

Before running the server, you need to process the SHL catalog and store its embeddings in ChromaDB. Ensure you have activated your virtual environment, then run:

```bash
python -m scripts.build_vector_db
```
*(Note: This step downloads the sentence-transformer models and embeds your catalog data into `data/chroma_db/`)*

### 3. Run the Application

You can run the API server either natively or via Docker.

**Option A: Native Setup (Uvicorn)**
```bash
# Install dependencies if you haven't already
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

**Option B: Docker Compose**
```bash
# Build and run the container
docker compose up --build
```

### 4. Make a Recommendation Request

The engine provides a `/recommend` endpoint that accepts POST requests. It analyzes your query, determines the user's intent, and retrieves relevant assessments using vector search.

**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
     -H "Content-Type: application/json" \
     -d '{"query": "Need Python Developer assessment"}'
```

**Response:**
```json
{
  "reply": "Here are the recommended assessments for a Python Developer...",
  "recommendations": [
    {
      "name": "Python (New)",
      "url": "https://www.shl.com/products/product-catalog/view/python-new/",
      "duration": "11 minutes"
    },
    {
      "name": "Programming Concepts",
      "url": "https://www.shl.com/products/product-catalog/view/programming-concepts/",
      "duration": "25 minutes"
    }
  ]
}
```

### 5. Health Check

You can verify the API is running by hitting the health endpoint:
```bash
curl http://127.0.0.1:8000/health
```
