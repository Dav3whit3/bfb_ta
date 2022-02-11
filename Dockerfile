FROM python:3.8-slim-buster as basic

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN  apt-get update \
  && python -m pip install --upgrade pip \
  # setting master user for file permmission purposes
  && useradd -m master 

WORKDIR /code

RUN chown master:master -R /code/

USER master

COPY --chown=master:master . /code/

RUN python -m venv venv \
 && venv/bin/pip install --no-cache-dir -r requirements/requirements.txt


# ===== SETUP =====
FROM basic AS setup

RUN chmod +x boot/boot_main_setup.sh

ENTRYPOINT [ "./boot/boot_main_setup.sh" ]



# ===== DEV =====
#FROM basic AS django-dev

# COPY --chown=master:master ./boot/start.sh .

# RUN chmod +x start.sh

# ENTRYPOINT [ "./start.sh" ]



# ===== DEVELOPMENT =====
FROM basic AS django-dev
COPY --chown=master:master . .