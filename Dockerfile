ARG RASA_SDK_IMAGE
FROM $RASA_SDK_IMAGE

WORKDIR /app

COPY requirements.txt ./
COPY actions.py ./actions/actions.py

RUN pip install -r requirements.txt
