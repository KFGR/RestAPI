from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

#creating moodel for our database named asceweb
users = Table("asceclients", meta_data, 
            Column("idusers", Integer, primary_key = True),
            Column("usersName", String(255), nullable = False),
            Column("usersAge", String(255), nullable = False),
            Column("usersDPT", String(255), nullable = False))
#nullable means that the information is required, cannot be empty

# meta_data.create_all(engine) #creating our database
meta_data.create_all(engine) #creating our table