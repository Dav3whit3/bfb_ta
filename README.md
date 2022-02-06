## Index
- [Description](#Description)
- [Installation](#Installation)
- [Currently under develop](#Currently-under-develop)
- [Folder structure](#Folder-structure)

- ta description
- Assumptions
- Approach


# Description
# Installation
- ### Install Docker :whale:
  https://docs.docker.com/get-docker/

- ### Environment Variables
  To run this project, you will need to add the following environment variables regarding DB mapping to your .env file:

  `POSTGRES_NAME`

  `POSTGRES_USER`

  `POSTGRES_PASSWORD`

  <br/>And the following ones to setup an admin user for Django:

  `DJANGO_SUPERUSER_USERNAME`

  `DJANGO_SUPERUSER_EMAIL`

  `DJANGO_SUPERUSER_PASSWORD`

- ### Build and run container
  ```bash
  $ docker-compose build && docker-compose up
  ```

# Currently under develop

- Make docker-compose service <superuser> run only by flag