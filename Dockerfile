FROM python:3.10
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . /app/ 

#RUN pylint /app/index.py > ./errors.txt

CMD ["python","index.py"]


#CMD ["sh", "-c", "pylint /app/index.py > /app/logs/pylint_output.txt"]