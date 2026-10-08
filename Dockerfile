FROM python:3.13.14-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY evaldb.ipynb .
CMD ["python", "-m", "jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]