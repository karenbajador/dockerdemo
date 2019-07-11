FROM python:3.5-jessie
RUN pip install Flask==0.11.1 pytest==3.8.1
COPY app /app
WORKDIR /app
CMD ["python", "app.py"] 