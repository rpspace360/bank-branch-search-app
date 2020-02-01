# Bank branch search app

## Instructions to run the branch search locally: 


### 1. Setup Database
```
CREATE DATABASE bank;
CREATE USER root WITH PASSWORD 'root';
ALTER ROLE root SET client_encoding TO 'utf8';
ALTER ROLE root SET default_transaction_isolation TO 'read committed';
ALTER ROLE root SET timezone TO 'UTC';
```

We'll use the `root` user with password to access the database. Please modify your `settings.py` in case you want to use another username or password. 
Then go to adminApp/, then run `./manage.py migrate`

### 2. Install requirements.txt
First configure a virtual environment.
In adminApp directory, do `virtualenv --python=python3 --prompt='(branch-search) ' venv`
then run `source venv/bin/activate`
```
pip install -r requirements.txt
```
This will install all the requirements


### 3. Run Django server
Go in project dir
then run

```
./manage.py runserver
```
```
psql -h hostname -d databasename -U username -f file.sql
```