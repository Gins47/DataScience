# Covid Data visualization

**Requirements**

1. Postgress

```shell
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get -y install postgresql

# Docker Installation

cd docker

docker-compose up -d

https://www.postgresqltutorial.com/postgresql-create-table/

```

**SQLAlchemy**

```shell
# Helps to load the data from csv to database
pip install SQLAlchemy
```
