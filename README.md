User Authentication in Flask

API Endpoints

User Model
1. Create User - POST api/v1/users
2. Login User - POST api/v1/users/login
3. Get A User Info - GET api/v1/users/<int:user_id>
4. Get All users - GET api/v1/users
5. Get My Info - GET api/v1/users/me
6. Edit My Info - PUT api/v1/users/me
7. DELETE My Account - DELETE api/v1/users/me

Site Model
1. Create a site - POST api/v1/sites
2. Get All sites - GET api/v1/sites
3. Get A site - GET api/v1/sites/<int:site_id>
4. Update A site - PUT api/v1/sites/<int:site_id>
5. Delete A site - DELETE api/v1/sites/<int:site_id>

In request header, we need api-token, which is generated while creating new user or while logging in.
```
{
    'api-token':"<api token>"
}
```

How to Run?

1. Create `.env` file and include following keys
   ```
    FLASK_ENV = <production> or <development>
    JWT_SECRET_KEY = 
    DATABASE_URL = mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}
   ```
2. Create migrations
   ```
   python manage.py db init
   python manage.py db migrate
   python manage.py db upgrade
   ```
3. `python run.py`