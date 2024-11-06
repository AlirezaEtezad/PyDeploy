# University Database API

## Overview
This is a university database app using postgresql for recording students and their courses.

## Features
- CRUD operations for students (Create, Read, Update, Delete)
- Postgresql database backend
- Dockerized!
- Error handling (will be added soon!)

## Usage
use this link:
```
https://postgres-api.liara.run/docs
```

## There are 2 folders:
### Beginner_app:
It is created for testing and learning purposes.
### Expert_app:
Enter this folder.

# Note:
For local usage you have to change the database url to SQLALCHEMY_DATABASE_URL = "postgresql://admin:123@localhost:5432/uni-db" in 'database.py' file and run a container from postgres docker image

#### Install requiremenst:
```
pip install -r requiremnts.txt
```

#### Pull pstgres image
```
sudo docker pull postgres
```

#### Run a container
```
sudo docker run -p 5432:5432 --name postgres-database -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=admin -e POSTGRES_DB=uni-db -d postgres
```

#### Run the program:
```
uvicorn app.main:app --reload
```
#### Enjoy the app using URL:
```
http://127.0.0.1:8000/docs
```