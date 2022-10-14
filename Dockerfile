FROM python:3.8
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt
ENV SERVICE_BOKE "service:80"
ENV SERVICE_EMOTION "service:80"
COPY . .
CMD ["uvicorn", "main:app","--host", "0.0.0.0"]