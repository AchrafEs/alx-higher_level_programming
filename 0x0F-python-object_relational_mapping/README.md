## 0x0F. Python - Object-relational mapping

Python Object-Relational Mapping (ORM) is a technique used to bridge the gap between the object-oriented programming
(OOP) world of Python and the relational database world. It provides a way to interact with relational databases using
Python objects, making database operations more intuitive and Pythonic. ORM frameworks automate many of the tasks
involved in database management, such as creating tables, executing SQL queries, and mapping database records to Python
objects.

Here are the key components and concepts of Python ORM:

1. `Object-Relational Mapping:` ORM is essentially a programming technique that allows you to represent database tables
as Python classes and database records as instances of those classes. It enables developers to work with databases
using Python objects and methods instead of writing raw SQL queries.

2. `Models:` In ORM frameworks, Python classes that represent database tables are called models.
These models define the structure of the data, including the fields (columns) and their data types.

3. `Database Session:` ORM frameworks typically provide a session or session-like object that acts as a communication
channel between your Python code and the database. You can use this session to perform various database operations like
inserting, updating, querying, and deleting records.

4. `Querying:` ORM frameworks offer a high-level query language or methods that allow you to retrieve data from the
database without writing raw SQL queries. These query methods are often more Pythonic and abstract away many of the
database-specific details.

5. `Data Relationships:` ORM allows you to define relationships between different models, such as one-to-one,
one-to-many, and many-to-many relationships. These relationships are represented in Python code and are automatically
managed by the ORM framework.

6. `Schema Generation:` Many ORM frameworks can automatically generate database schemas based on your model classes,
saving you the effort of writing SQL scripts to create tables.

7. `Database Agnosticism:` ORM frameworks are designed to work with multiple database management systems (DBMS), such
as MySQL, PostgreSQL, SQLite, and more. This allows you to switch between databases with minimal code changes.

Popular Python ORM frameworks include:

`Django ORM:` Part of the Django web framework, Django ORM is a high-level ORM that comes with many built-in
features for web development.

`SQLAlchemy:` SQLAlchemy is a powerful and highly customizable ORM that provides both a high-level ORM API and a
lower-level SQL expression language.

`Peewee:` A lightweight and easy-to-use ORM that focuses on simplicity and is often chosen for small to medium-sized
projects.

Here's a simplified example of defining a model and querying data using SQLAlchemy:
```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a database engine and session
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define a model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

# Create the table in the database
Base.metadata.create_all(engine)

# Insert a new user
new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)
session.commit()

# Query users
users = session.query(User).filter_by(username='john_doe').all()
for user in users:
    print(f'Username: {user.username}, Email: {user.email}')
```
This code demonstrates how you can define a User model, create a table, insert data, and query it using SQLAlchemy. Python ORM frameworks simplify database interactions and make database code more readable and maintainable.
