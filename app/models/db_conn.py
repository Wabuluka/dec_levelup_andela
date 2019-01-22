import psycopg2
import os
from psycopg2.extras import RealDictCursor 
"""
Initializing my database
"""
class DatabaseConnection:   
    def __init__(self):
        self.commands = (
            """
            CREATE TABLE IF NOT EXISTS users(
                    userid SERIAL PRIMARY KEY,
                    firstname VARCHAR(50) NOT NULL,
                    lastname VARCHAR(50) NOT NULL,
                    othernames VARCHAR(50) NULL,
                    email VARCHAR(100) NOT NULL,
                    phonenumber INT NOT NULL,
                    username VARCHAR(50) NOT NULL,
                    password VARCHAR(200) NOT NULL,
                    role BOOLEAN DEFAULT FALSE NOT NULL
                    )
            """,
            """
                 CREATE TABLE IF NOT EXISTS intervention (                    
                    id SERIAL PRIMARY KEY,
                    casetype VARCHAR(50) NOT NULL,
                    createdby VARCHAR(50) NOT NULL,
                    createdon TIMESTAMP DEFAULT NOW(),
                    location VARCHAR(20) NOT NULL,
                    status VARCHAR(50) NOT NULL,
                    comment VARCHAR(50) NOT NULL
                )
            """,
            """
                 CREATE TABLE IF NOT EXISTS redflag (                    
                    id SERIAL PRIMARY KEY,
                    casetype VARCHAR(50) NOT NULL,
                    createdby VARCHAR(50) NOT NULL,
                    createdon TIMESTAMP DEFAULT NOW(),
                    location VARCHAR(20) NOT NULL,
                    status VARCHAR(50) NOT NULL,
                    comment VARCHAR(50) NOT NULL
                )
            """
        )
        try:
            if os.getenv("FLASK_ENV") == "production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"), cursor_factory=RealDictCursor)

            elif os.getenv("FLASK_ENV") == "TESTING":
                print('Connecting to test db')
                self.connection = psycopg2.connect(dbname='ireporter_test_db',
                                                   user='postgres',
                                                   password='123',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            else:
                print('Connecting development db')
                self.connection = psycopg2.connect(dbname='ireporter_db',
                                                   user='postgres',
                                                   password='123',
                                                   host='localhost',
                                                   port='5432', cursor_factory=RealDictCursor)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            for command in self.commands:
                self.cursor.execute(command)
        except Exception as error:
            print(f"error: {error}")

    """
    method to drop tables being used in my tests
    """
    def drop_tables(self):
        query = "DROP TABLE IF EXISTS {} CASCADE"
        tabl_names = ["users, intervention, redflag"]
        for name in tabl_names:
            self.cursor.execute(query.format(name))

    def create_tables(self):
        for command in self.commands:
            self.cursor.execute(command)
