# Catalog App

## Introduction
This web application lists all the items from a variety of sports categories. Users can go around and see the details for each sports item. Users can log in to the application using their Google or Facebook account. Once logged in they can create new categories or add items to the existing categories. They can also remove and edit their items. 

The following  REST endpoints are also implemented to provide all information in JSON.
- `https://34.228.186.63.xip.io/catalog/catalog.json` provides complete information of all the categories and items within each category
- `https://34.228.186.63.xip.io/catalog/catalog/<category name>/<item name>/json` provides all information about specific item of specific category

## How to access
This app can be accessed using `https://34.228.186.63.xip.io/catalog/`
Public IP address is `34.228.186.63`
SSH port is `2200`

## Deployment details

### Softwares installed:
- Apache
- Flask
- SqlAlchemy
- PostgreSQL
- WSGI module
- GIT
- Python-pip
- Certbot Let's Encrypt client
- Cryptography (upgrade)
- pyOpenSSL (upgrade)


### Configurations
- Firewall is configured to allow SSH, HTTP, NTP
- Default SSH port is changed to 2200
- A new user `grader` is created with sudo access and public key is installed
- A new database user `catalog` is created
- A new role `catalog` is created in database
- Owner of `catalog.db` and the directory it is saved is changed to `www-data` so that database operations can be performed
- A configuration file `CatalogApp.config` is created
- Enabled HTTPS using Let's Encrypt
- Redirect urls are added to Google and Facebook

### Resources
- `https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps`
- `https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04`
