FROM python:3.13-slim

WORKDIR /app

ARG PIP_DEFAULT_TIMEOUT=120
ARG PIP_RETRIES=10

ENV PIP_DEFAULT_TIMEOUT=${PIP_DEFAULT_TIMEOUT}
ENV PIP_RETRIES=${PIP_RETRIES}

COPY requirements.txt .

COPY pydantic_core-2.50.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl .

RUN pip install --no-cache-dir \
    ./pydantic_core-2.50.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl \
    -r requirements.txt

COPY src ./src

EXPOSE 8000

CMD ["python", "src/server.py"]