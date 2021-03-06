# System Requirement

You operating system has to be either:
- Ubuntu 16.04 LTS (“Xenial”)
- Ubuntu 18.04 LTS (“Bionic”)

Other operating systems may also work, but those have not been tested yet.

# Installation for Scrapy

The following tutorial is a condensed version of Scrapy [official documentation](https://docs.scrapy.org/en/latest/intro/install.html)

## Installing Scrapy using conda

`conda install -c conda-forge scrapy`

## Installing Scrapy using pip

`pip install Scrapy`


# Installation for MongoDB

The following tutorial is a condensed version of MongoDB [official documentation](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/).

## Import the public key used by the package management system

From a terminal, issue the following command to import the MongoDB public GPG Key from https://www.mongodb.org/static/pgp/server-4.4.asc:

`wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add`

## Create a list file for MongoDB
Create the list file /etc/apt/sources.list.d/mongodb-org-4.4.list for your version of Ubuntu.

### Ubuntu 16.04

`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list`

### Ubuntu 18.04

`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list`

### Ubuntu 20.04

`echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list`

## Reload local package database

`sudo apt-get update`

## Install the MongoDB packages

`sudo apt-get install -y mongodb-org`

## Run MongoDB

`sudo systemctl start mongod`

or

`sudo service mongod start`

You can optionally ensure that MongoDB will start following a system reboot by issuing the following command:

`sudo systemctl enable mongod`

## Verify that you can use MongoDB

`mongo`