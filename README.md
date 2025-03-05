**Text Summarization API**

This project provides a FastAPI-based Text Summarization API using the facebook/bart-large-cnn model from Hugging Face, containerized with Docker for easy deployment.

🚀 **Getting Started**

1️⃣ **Clone the Repository**

git clone [https://github.com/balexandroff/AI-Text-Summarize-API]https://github.com/balexandroff/AI-Text-Summarize-API.git
cd AI-Text-Summarize-API

2️⃣ **Run Locally (Without Docker)**

Install Dependencies

Ensure you have Python 3.9+ installed, then install dependencies:

pip install -r requirements.txt

Run FastAPI Server

uvicorn api:app --host 0.0.0.0 --port 8000 --reload

FastAPI will now be available at: http://localhost:8000/docs 🚀

🐳 **Running with Docker**

1️⃣ **Build the Docker Image**

docker build -t summarization-api .

2️⃣ **Run the Container**

docker run -d --restart=always -p 8000:8000 summarization-api

3️⃣ **Verify it’s Running**

docker ps

The API will be accessible at: http://localhost:8000/docs

🛠** Using Docker Compose (Optional)**

If you prefer using Docker Compose, create a docker-compose.yml file and run:

docker compose up -d

📡 **API Usage**

1️⃣ **Send a Summarization Request**

curl -X POST "http://localhost:8000/summarize" -H "Content-Type: application/json" -d '{"text": "Your long text here..."}'

2️⃣** Response Format**

{
  "summary": "Generated summary here."
}

📌 **Additional Commands**

Stop Running Containers

docker stop summarization-api

Remove the Container

docker rm summarization-api

Rebuild & Restart the Container

docker build --no-cache -t summarization-api .
docker run -d --restart=always -p 8000:8000 summarization-api

📜 **License**

This project is open-source and available under the MIT License.
