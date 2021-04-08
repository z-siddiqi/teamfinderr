## *teamfinderr* 
is a network for skilled individuals looking to start collaborating on projects, helping ideas become reality. Whether you're a self-starter or looking to get involved in a project for your portfolio, ***teamfinderr*** provides a skill-based pairing system to meet your needs.

### Key Features

- Create Project
- Project Collaboration System
- Join project teams and be assigned to roles
- Database of users and projects
- Authenticate users
- Documentation
- View

### Setup Locally

1. Clone the repository locally.
2. Set up all necessary dependencies:
 ```python -m venv .env
    source .env/scripts/activate or .env/bin/activate
    pip install -r requirements.txt
 ```

3. Set environment variables:
```
   $env:DJANGO_SECRET_KEY='secret'
```

4. Apply all migrations:
```
   python manage.py migrate
```

5. Deploy web app on localhost:
```
   python manage.py runserver
```

### Tools Used

- Django
- Django Rest Framework
- Postman
