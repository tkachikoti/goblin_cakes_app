# Inventory Viewer

![A demonstration of a user creating a ticket](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/inventory_viewer/inventory_viewer_app_preview.gif)

This repository contains a small application that visualises sales related data from a database table. 
## Table of contents

- [Description](#description)
- [Installing and running the app](#installing-and-running-the-app)
- [Testing the app](#testing-the-app)
- [References](#references)

## Description

This repository contains a [Flask](https://github.com/pallets/flask) based minimal Python web project.
- The front end interface was built using [Bootstrap](https://github.com/twbs/bootstrap) for HTML/CSS components, [Jinja](https://github.com/pallets/jinja) for the template engine and [Chart.js](https://github.com/chartjs/Chart.js) data visualisation.
- The database was implemented using [PostgreSQL](https://github.com/postgres) with [Flask-SQLAlchemy](https://github.com/pallets-eco/flask-sqlalchemy) for Object-relational mapping and [Psycopg](https://github.com/psycopg/psycopg2) for the database adapter.
- The testing functionality was implemented using [pytest](https://github.com/pytest-dev/pytest)

## Installing and running the app

### Windows and macOS

1. Download and install Docker: https://www.docker.com/products/docker-desktop/

2. Clone the repository:

```
$ git clone https://github.com/tkachikoti/inventory_viewer
```

3. Change directory to access root directory:

```
$ cd inventory_viewer
```

4. Run the app:

```
$ docker-compose up -d
```

5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a web browser.

## Testing the app

1. After following the installation process, tests are executed via Docker container CLI by entering:

```
$ docker exec -i -t flask_app pytest
```