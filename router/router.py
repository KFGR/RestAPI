from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
# from config.db import conn
from config.db import engine
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()

@user.get("/")
def root():
    # conn.execute("SELECT * FROM asceweb.asceclients;")
    # items = conn.execute(user.)
    return {"message": "Hi, I am FASTAPI with a Router"}

@user.get('/api/user', response_model=List[UserSchema])
def get_users():
    """returns an array of dictionaries with all the data in a database table"""
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return result

@user.post("/api/user", status_code=HTTP_201_CREATED) #to introduce new users to the database
def create_user(data_user : UserSchema ):
    """creates a new user in a database table and returns an HTTP 201 code if it is succesfully created"""
    with engine.connect() as conn: #best practice to connect to a database
        new_user = data_user.dict()
        new_user["usersDPT"] =  generate_password_hash(data_user.usersDPT, "pbkdf2:sha256:30", 30) #generating a hash to encrypt the password
        print(new_user)
        conn.execute(users.insert().values(new_user)) 
        return Response(status_code=HTTP_201_CREATED)


@user.get('/api/user/{user_id}', response_model= UserSchema)
def get_user(user_id:str):
    """return a single user from a database table using the userID, returns a dictionary with the information"""
    with engine.connect() as conn:
        result =  conn.execute(users.select().where(users.c.idusers == user_id)).first()

        return result


@user.put('/api/user/{user_id}', response_model=UserSchema)
def update_user(data_update:UserSchema, user_id:str):
    """updates the information of a user in a database table"""
    with engine.connect() as conn:
        conn.execute(users.update().values(idusers=data_update.idusers, usersName=data_update.usersName, usersAge=data_update.usersAge, usersDPT=data_update.usersDPT).where(users.c.idusers == user_id))
        result = conn.execute(users.select().where(users.c.idusers == user_id)).first()
        return result


@user.delete('/api/user/{user_id}', status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    """delete an user from a database table"""
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.idusers == user_id))

        return Response(status_code=HTTP_204_NO_CONTENT)

@user.post('/api/user/login', status_code=200)
def user_login(data_user: DataUser):
    """Authenticates a user. 
        For testing purposes it authenticates by userID and userDepartment"""
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.idusers == data_user.idusers)).first()
        if result != None:
            check_password = check_password_hash(result[3], data_user.usersDPT )
            if check_password:return {"status": 200, 
                                        'message': 'Access success, password is the same'}
            else: return {"status": HTTP_401_UNAUTHORIZED, 
                            'message': 'Access denied, password is not the same'}
            print(check_password)
        print (result)

"""To test functions go to localhost/docs"""