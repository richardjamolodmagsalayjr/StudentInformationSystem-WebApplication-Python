#from ssis_website import database
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, DB_PORT
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
        students = cursor.fetchall()
        return students 

    @classmethod
    def delete_student(cls, student_id):
        query = "DELETE FROM students WHERE student_id=%s"
        data = [student_id]
        cursor.execute(query, data)
        database.commit()
    
    @classmethod
    def edit_student(cls, id_number, firstname, lastname, gender, year_level, course_code, old_id_number):
        query = "UPDATE students SET student_id=%s, firstname=%s, lastname=%s, gender=%s, year=%s, \
                course_code_id=%s WHERE student_id=%s"
        data = [id_number, firstname, lastname, gender, year_level, course_code, old_id_number]
        cursor.execute(query,data)
        database.commit()

    @classmethod 
    def search_student(cls, key):
        query = "SELECT * FROM students WHERE student_id=%s or firstname=%s or lastname=%s or course_code_id=%s \
            or year=%s or gender=%s"

        data = [key,key,key,key,key,key]
        cursor.execute(query,data)
        results = cursor.fetchall()
        return results

class Course():
    def __init__(self, course_code, course_name, college_code):
        self.course_code = course_code 
        self.course_name = course_name
        self.college_code = college_code

    #this method is used to display course options in the add student form
    #returns a list of tuples
    @classmethod
    def get_course(cls):
        query = "SELECT * FROM courses"
        cursor.execute(query)
        courses = cursor.fetchall()
        return courses 
    
    def add_course(self):
        query = "INSERT INTO courses(course_code, course_name, college_code_id) VALUES \
                 (%s,%s,%s)"
        data = [self.course_code, self.course_name, self.college_code]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def display_courses(cls):
        query = "SELECT * FROM courses"
        cursor.execute(query)
        courses = cursor.fetchall()
        return courses 

    @classmethod
    def edit_course(cls, course_code, course_name, college_code, old_course_code):
        query = "UPDATE courses SET course_code=%s, course_name=%s, college_code_id=%s WHERE course_code=%s"
        data = [course_code, course_name, college_code, old_course_code]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def delete_course(cls, course_code):
        query = "DELETE FROM courses WHERE course_code=%s"
        data = [course_code]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def search_course(cls, key):
        query = "SELECT * FROM courses WHERE course_code=%s or course_name=%s or college_code_id=%s"
        data = [key,key, key]
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

class College():
    def __init__(self, college_code, college_name):
        self.college_code = college_code
        self.college_name = college_name

    #use to get available colleges in the database as dropdown options    
    @classmethod
    def get_colleges(cls):
        query = "SELECT * FROM colleges"
        cursor.execute(query)
        colleges = cursor.fetchall()
        return colleges

    def add_college(self):
        query = "INSERT INTO colleges(college_code, college_name) VALUES (%s,%s)"
        data = [self.college_code, self.college_name]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def display_colleges(cls):
        query = "SELECT * FROM colleges"
        cursor.execute(query)
        colleges = cursor.fetchall()
        return colleges

    @classmethod
    def delete_college(cls, college_code):
        query = "DELETE FROM colleges WHERE college_code=%s"
        data = [college_code]
        cursor.execute(query,data)
        database.commit()

    @classmethod
    def edit_college(cls, college_code, college_name, old_college_code):
        query = "UPDATE colleges SET college_code=%s, college_name=%s WHERE college_code=%s"
        data = [college_code, college_name, old_college_code]
        cursor.execute(query, data)
        database.commit()

    @classmethod
    def search_college(cls, key):
        query = "SELECT * FROM colleges WHERE college_code=%s or college_name=%s"
        data = [key,key]
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result