# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV HABITAT="container"
ENV PRODUCT_STAGE="production"

ARG USER_ID_ARG
ARG USER_NAME_ARG
ARG APP_DIR_ARG
####
ENV USER_ID=${USER_ID_ARG}
ENV USER_NAME=${USER_NAME_ARG}
ENV APP_DIR=${APP_DIR_ARG}

# Install pip requirements
COPY ./buildings/production/requirements.production.txt ./requirements.txt
#RUN python3 -m pip install --upgrade pip && python3 -m pip install -r requirements.txt
#RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

WORKDIR ${APP_DIR}
COPY ./entry ${APP_DIR}/entry
COPY ./lode ${APP_DIR}/lode

## Creates a non-root user with an explicit UID and adds permission to access the /app folder
## For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
## RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#RUN adduser -u ${USER_ID} --disabled-password --gecos "" ${USER_NAME}
##RUN mkdir -p ${PY_SRC_DIR}; touch ${PY_SRC_DIR}/blob; chown -R ${USER_NAME} ${APP_DIR}
#RUN chown -R ${USER_NAME} ${APP_DIR}

RUN adduser -u ${USER_ID} --disabled-password --gecos "" ${USER_NAME} && chown -R ${USER_NAME} ${APP_DIR}

USER ${USER_NAME}

CMD ["python", "entry/app.py"]

