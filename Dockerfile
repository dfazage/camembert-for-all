FROM pytorch/pytorch:latest

COPY ./ /camembert-resources

WORKDIR /camembert-resources

RUN apt-get update && apt-get install -y --no-install-recommends && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir /camembert-model

RUN python ./src/init_model.py 

EXPOSE 80

CMD ["python", "./src/app.py"]
    
