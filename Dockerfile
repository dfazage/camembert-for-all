FROM pytorch/pytorch:latest

RUN apt-get update && apt-get install -y --no-install-recommends

COPY ./ /camembert-resources

WORKDIR /camembert-resources

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN mkdir /camembert-model && \
    python /camembert-resources/src/init_models.py
    
EXPOSE 80