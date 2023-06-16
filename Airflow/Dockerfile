FROM apache/airflow:2.2.3
COPY requirements.txt /requirements.txt
COPY .env /.env
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt # --no-cache-dir 




