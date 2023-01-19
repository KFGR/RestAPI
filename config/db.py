"""connection to our database"""
 #to create a connection to our db
from sqlalchemy import create_engine, MetaData 
engine = create_engine("mysql+pymysql://user:password@server:port/database") 
"""(mysql+pymsql)= modules to use for the database
    ://user:password@where is running(server):port/table name"""
# conn = engine.connect()
meta_data = MetaData()