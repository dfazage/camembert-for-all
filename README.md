# camembert-for-all

API for French camemBERT sentence encoding as a service using docker. 
CamemBERT embedding model is served as a Flask restful API which returns a (,768) array as embedding.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

docker
All requirements can be found in requirements.txt. This version of CamemBERT Model uses the pre trained model from transformers package.

### Installing

1. Clone git project
2. Run docker image build: 
'''console
docker build -t caas1.0 .
'''
3. Launch container with image, and expose ports for api listening:
'''console
docker run -i -t --name=camembert-for-all -p 12345:80 caas1.0
'''

At this point, container should be executed on local machine, and ready for used. Check if http://localhost:12345/ returns a 'hello word' response.

### Demonstration
