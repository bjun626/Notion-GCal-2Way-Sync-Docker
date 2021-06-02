FROM python:3.8-alpine

WORKDIR /root/python

COPY main.py .

COPY Notion_GCal_2WaySync.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python","./main.py"]