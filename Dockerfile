FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir gradio python-dotenv openai

COPY main.py ./

EXPOSE 8000

CMD ["python", "main.py"]
