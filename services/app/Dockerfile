FROM python:3.6.8-alpine3.9


WORKDIR /opt/

ADD . /opt/
RUN pip install -r requirements.txt

CMD ["python", "app.py" ]
