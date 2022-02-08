<!-- TABLE OF CONTENTS 
<details open="open">

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

  <summary> :book: Table of Contents</summary>
  <ol>
    <li><a href="#Description"> ➤ Description</a></li>
    <li><a href="#Installation"> ➤ Installation</a></li>
    <li><a href="#Currently-under-develop"> ➤ Currently under develop</a></li>
    <li><a href="#Folder-structure"> ➤ Folder structure</a></li>
  </ol>
</details>

<br>
-->

<details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)](#description)
<a href="#description"></a>
<summary><span> :pencil: Description</span></summary>
This coding challenge consists of developing a simple Rest API using Django and Django Rest Framework. The exercise consists of writing a simple Django application, that has the following features in a Rest API:

- <strong>Models and relations</strong>. Create a model called Mentor, another one called Project, and another one called Mentorship. The models should have the following relationships(*) and fields:

<div align="center">

![](assets/models.png)

</div>

A Project can have multiple Mentors through the Mentorship Model. Also, a Mentor can have multiple Projects related to.

- <strong>Endpoints (urls.py)</strong>. Every model should have an endpoint that is accessible to make requests (create, update, delete mentors or projects).
- <strong>Views (views.py)</strong>. Every model should have an API Rest Viewset that allows all methods but Delete.
- <strong>Serializer (serializers.py)</strong>. Every model should have a Serializer that will return all the fields from the model and in the case of the ProjectSerializer, it should also return the array of Mentors related.
- <strong>(Optional) Admin (admin.py)</strong>. Extend the file so you can access these models and perform certain actions.
- <strong>(Optional +) Mentors Export</strong>. Add a third-party integration that enables Mentors Export in .csv from the Django Admin worked in the previous step.

</details>

<br>

<details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)](#installation)
<a href="#installation"></a>
<summary> :floppy_disk: Installation</summary>

- ## :whale: Install Docker & Docker Compose

  https://docs.docker.com/get-docker/  
  https://docs.docker.com/compose/install/


- ## :closed_lock_with_key: Environment Variables

  To run this project, you will need to add the following environment variables regarding DB mapping to your .env file:

  `POSTGRES_NAME`

  `POSTGRES_USER`

  `POSTGRES_PASSWORD`

  <br/>And the following ones to setup an admin user for Django:

  `DJANGO_SUPERUSER_USERNAME`

  `DJANGO_SUPERUSER_EMAIL`

  `DJANGO_SUPERUSER_PASSWORD`


- ## :wrench: Build and run container

  Build services

  ```bash
  docker-compose build
  ```

  (Optional) For a Django-app seed :arrow_right: <i>DJANGO_APP=<strong>django_app_name</strong> SEED_SIZE=<strong>desired_seed_size</strong> docker-compose run db-seed:</i>

  ```bash
  DJANGO_APP=mentors SEED_SIZE=10 docker-compose run db-seed
  ```

  (Optional) For a Django db migration:

  ```bash
  docker-compose run db-migrations
  ```

  (Optional) If a Django superuser is required for the first setup:

  ```bash
  docker-compose run superuser
  ```

  Launch the app:

  ```bash
  docker-compose up django-dev
  ```
</details>

<br>

<details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)](#aproach)
<a href="#aproach"></a>
  <summary> :triangular_ruler: Approach</summary>

  Document in readme all along the process
  - Project Structure
  - External app architecture
  - DB models & relantionship definitions
  - Django-seed docker-compose service setup
</details>

<br>

<details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)](#testing)
<a href="#testing"></a>
  <summary> :microscope: Testing</summary>

</details>

<br>

<details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)](#bp)
<a href="#bp"></a>
  <summary> :cold_sweat: Blocking points</summary>

  - Django superuser automation. Switched from Dockerfile to docker-compose for dependency order purposes
  - Docker permissions management issues when using Docker & docker-compose. Copied folders from host drag host permissions. A chown command is required when unloading the code base into the container
  - Many to Many reversed relationship

</details>

<br>

<details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)](#cud)
<a href="#cud"></a>
  <summary> :soon: Currently under develop</summary>

  - Mock a Prod / Dev setup with different docker-compose services point to differente data bases.

</details>