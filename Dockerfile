FROM python:3.11-slim

# Install system dependencies needed for compiling heavy packages if necessary
RUN apt-get update && apt-get install -y gcc g++ build-essential --no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install them smoothly using the 16GB RAM limit
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your bot code
COPY main.py .

# Hugging Face runs on port 7860 by default
ENV PORT=7860
EXPOSE 7860

# Run your script
CMD ["python", "main.py"]
