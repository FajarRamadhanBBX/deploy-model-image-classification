FROM python:3.12-slim
WORKDIR /predict-disease

RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY models/ /predict-disease/models/
CMD ["python", "-m", "flask", "run","--host=0.0.0.0"]
