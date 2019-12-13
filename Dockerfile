FROM pytorch/pytorch:latest

COPY ./ /camembert-resources

WORKDIR /camembert-resources

RUN apt-get update && apt-get install -y --no-install-recommends && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir /camembert-model

WORKDIR /camembert-resources/src/

EXPOSE 80

CMD ["python", "./init_models.py"]
    
