FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean

# Install requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose gradio port
EXPOSE 80 

CMD ["sh", "-c", "fastapi run main.py --port 80"]