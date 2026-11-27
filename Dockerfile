FROM python:3.13-slim

# set working dir
WORKDIR /app

# copy requirements.txt and install dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project

COPY . .

# expose the application port

EXPOSE 8000

# run
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# uvicorn : ASGI server too run fastapi
# app:app  : First app is the Python filename (app.py); second app is the FastAPI object inside that file
