# ULSTU-quiz

## Project setup
```
cd server
```
```
docker-compose up -d --build
```

### Migrate
```
docker-compose exec web python manage.py migrate
```

### Create Superuser 
```
docker-compose exec web python manage.py createsuperuser
```