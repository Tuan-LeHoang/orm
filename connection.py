import sqlalchemy as db
from sqlalchemy import text

engine = db.create_engine("sqlite:///demo.db")
try:
    connection = engine.connect()
except:
    print("Error")

create_table_query = "create table test(\
    id int primary key unique not null,\
    name text,\
    age int);"

insert_query = "insert into test ( id, name, age)\
                values (1, 'nhat', 25);"

select_query = "select * from test;"
# connection.execute(text(create_table_query))

connection.execute(text(insert_query))
connection.execute(text(select_query))

connection.commit()
