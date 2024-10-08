﻿# Planetarium API service

DRF project for managing planetarium.

## Installation

```shell
# Clone the repository
git clone https://github.com/b3v3kt0r/planetarium-api-service.git

# Set up .env file
You have create .env using .env.sample. like example

# Build docker-compose container
docker-compose build

# Run docker compose
docker-compose up

# Go into docker-container
docker exec -it <container id> sh

# Create super user
python manage.py createsuperuser

# Check it out
http://localhost:8000/api/planetarium/
```

## Features

* JWT authenticated.
* Admin panel.
* Documentation for views(go to api/schema/swagger-ui/).
* CRUD implementation for planetarium.
* Filtering for astronomy show.

## Structure

![Website Interface](static/readme3.png)

## Demo

![Website Interface](static/readme1.png)
![Website Interface](static/readme2.png)

## Contact
For contact me:
* Fullname: Stanislav Sudakov
* Email: stasiksudakov@gmail.com
* Telegram: @sssvvvff
