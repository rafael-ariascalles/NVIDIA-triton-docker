FROM python:3.8
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt
ENV TRITON_URL "triton:0000"
COPY . .
CMD ["uvicorn", "api:app","--host", "0.0.0.0"]