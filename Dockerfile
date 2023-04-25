FROM python:3.11

RUN mkdir /service
WORKDIR /service
COPY service/ /service/
RUN pip install pip -U

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/requirements.txt

EXPOSE 8000

HEALTHCHECK --interval=21s --timeout=3s --start-period=10s CMD curl --fail http://web:8000/healthcheck || exit 1

CMD ["uvicorn", "server:app", "--host", "web", "--port", "8000"]
