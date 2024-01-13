FROM python:3.11-alpine

RUN pip install cqlsh

ADD cqlshrc /root/.cassandra/cqlshrc
ADD entrypoint.py /entrypoint.py

ENTRYPOINT [ "python", "entrypoint.py", "--ssl" ]