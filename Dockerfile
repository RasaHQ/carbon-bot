ARG RASA_SDK_IMAGE
FROM $RASA_SDK_IMAGE

COPY action-server-requirements.txt ./
COPY actions.py ./actions
COPY data ./data

RUN pip install -r action-server-requirements.txt
