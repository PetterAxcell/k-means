FROM python:3.10

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pylint /app/index.py
RUN pylint /app/index.py > /app/logs/errors.txt

CMD ["python","index.py"]