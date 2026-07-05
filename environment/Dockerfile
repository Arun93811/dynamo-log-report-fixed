FROM python:3.11-slim@sha256:888fb400b13380b2a76ed995777feaf00455db4d1a49fa729bc15f0119859f7b

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
