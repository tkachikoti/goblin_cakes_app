# Inventory Viewer

![A demonstration of a the inventory app](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/inventory_viewer/inventory_viewer_app_preview.gif)

This repository contains a small application that visualises sales related data from a database table. 
## Table of contents

- [Description](#description)
- [Installing and running the app](#installing-and-running-the-app)
- [Uninstalling and Shutting down the app](#uninstalling-and-shutting-down-the-app)
- [Testing the app](#testing-the-app)
- [Functionality overview](#functionality-overview)

## Description

This repository contains a [Flask](https://github.com/pallets/flask) based minimal Python web project.
- The front end interface was built using [Bootstrap](https://github.com/twbs/bootstrap) for HTML/CSS components, [Jinja](https://github.com/pallets/jinja) for the template engine and [Chart.js](https://github.com/chartjs/Chart.js) data visualisation.
- The database was implemented using [PostgreSQL](https://github.com/postgres) with [Flask-SQLAlchemy](https://github.com/pallets-eco/flask-sqlalchemy) for Object-relational mapping and [Psycopg](https://github.com/psycopg/psycopg2) for the database adapter.
- The testing functionality was implemented using [pytest](https://github.com/pytest-dev/pytest)

## Installing and running the app

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

1. After following the installation process, tests are executed by entering:

```
$ docker exec -i flask_app pytest
```

## Uninstalling and shutting down the app

1. From the root directory execute the following command:

```
$ docker-compose down --rmi all
```

## Functionality overview

### Filter Options

Users can filter the data by selecting a specific product category, or by selecting a specific calendar quarter. In addition to this users can change the order that the data is displayed by selecting the desired column.

![A demonstration of the inventory app's filter options](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/inventory_viewer/inventory_viewer_app_filter_options.gif)