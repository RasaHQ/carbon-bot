ARG RASA_SDK_IMAGE
FROM $RASA_SDK_IMAGE

WORKDIR /app

COPY action-server-requirements.txt ./
COPY actions.py ./data
COPY data ./actions/data

RUN pip install -r action-server-requirements.txt
