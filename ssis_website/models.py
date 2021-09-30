#from ssis_website import database
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, DB_PORT, DB_AUTH
import mysql.connector

database = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USERNAME,
    port = DB_PORT,
    passwd= DB_PASSWORD,
    database = DB_NAME
    )

cursor = database.cursor() 
class Student():

    def __init__(self, id_number, firstname, lastname, gender, year, course):
        self.id_number = id_number
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.year = year
        self.course = course

    def add_student(self):
        query = "INSERT INTO students(student_id, firstname, lastname, course_code_id, gender, year) \
                VALUES (%s,%s,%s,%s,%s,%s)"
        data = [self.id_number, self.firstname, self.lastname, self.course, self.gender,
                self.year]
        cursor.execute(query, data)
        database.commit() 
        
    @classmethod
    def display_students(cls):
        query = "SELECT * FROM students"
        cursor.execute(query)    
        result = cursor.fetchall()
        return result 
