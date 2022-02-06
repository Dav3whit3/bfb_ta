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

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<summary><span> :pencil: Description</span></summary>
</details>

<br>

<details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<summary> :floppy_disk: Installation</summary>

- ### Install Docker :whale:

  https://docs.docker.com/get-docker/

- ### :closed_lock_with_key: Environment Variables

  To run this project, you will need to add the following environment variables regarding DB mapping to your .env file:

  `POSTGRES_NAME`

  `POSTGRES_USER`

  `POSTGRES_PASSWORD`

  <br/>And the following ones to setup an admin user for Django:

  `DJANGO_SUPERUSER_USERNAME`

  `DJANGO_SUPERUSER_EMAIL`

  `DJANGO_SUPERUSER_PASSWORD`

- ### Build and run container

  Build services

  ```bash
  docker-compose build
  ```

  For a Django db migration:

  ```bash
  docker-compose run db-migration
  ```

  If a Django superuser is required for the first setup:

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

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

  <summary> :soon: Currently under develop</summary>
</details>