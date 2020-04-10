User Authentication in Flask

API Endpoints

1. Create User - POST api/v1/users
2. Login User - POST api/v1/users/login
3. Get A User Info - GET api/v1/users/<int:user_id>
4. Get All users - GET api/v1/users
5. Get My Info - GET api/v1/users/me
6. Edit My Info - PUT api/v1/users/me
7. DELETE My Account - DELETE api/v1/users/me


In request header, we need api-token, which is generated while creating new user or while logging in.
```
{
    'api-token':"<api token>"
}
```

How to Run?

1. `export FLASK_ENV=development`
2. `python run.py`