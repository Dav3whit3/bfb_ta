FROM python:3.8-slim-buster as basic


RUN  apt-get update \
  && python -m pip install --upgrade pip \
  # setting master user for file permmission purposes
  && useradd -m master \
  && mkdir bfb_tech_assessment \
  && chown -R master:master /bfb_tech_assessment

WORKDIR /bfb_tech_assessment

USER master

COPY requirements requirements
RUN python -m venv venv \
 && venv/bin/pip install --no-cache-dir -r requirements/requirements.txt

# ===== DEVELOPMENT =====
FROM basic AS development
COPY . .