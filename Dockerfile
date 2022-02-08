FROM python:3.8-slim-buster as basic


RUN  apt-get update \
  && python -m pip install --upgrade pip \
  # setting master user for file permmission purposes
  && useradd -m master \
  && mkdir bfb_tech_assessment \
  && chown master:master -R /bfb_tech_assessment/

WORKDIR /bfb_tech_assessment

USER master

COPY requirements requirements
RUN python -m venv venv \
 && venv/bin/pip install --no-cache-dir -r requirements/requirements.txt

COPY --chown=master:master . .

# ===== DEVELOPMENT =====
FROM basic AS setup

COPY --chown=master:master boot_main_setup.sh .

RUN chmod +x boot_main_setup.sh

ENTRYPOINT [ "./boot_main_setup.sh" ]

