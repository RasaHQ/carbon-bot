ARG RASA_SDK_IMAGE
ARG CLIMATIQ_API_KEY
FROM $RASA_SDK_IMAGE

ENV CLIMATIQ_API_KEY=$CLIMATIQ_API_KEY

COPY action-server-requirements.txt ./
COPY actions.py ./
COPY data ./data

RUN pip install -r action-server-requirements.txt

CMD ["start", "--actions", "actions"]
