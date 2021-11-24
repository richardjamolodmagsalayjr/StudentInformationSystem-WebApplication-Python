#from ssis_website import database
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, DB_PORT, CLOUD_NAME, API_KEY, API_SECRET
import mysql.connector
import cloudinary
import cloudinary.uploader

database = mysql.connector.connect(
    host = DB_HOST,
    user = DB_USERNAME,
    port = DB_PORT,
    passwd= DB_PASSWORD,
    database = DB_NAME
    )
cloudinary.config(
        cloud_name = CLOUD_NAME,
        api_key=API_KEY, 
        api_secret=API_SECRET,
        secure = True
    )
cursor = database.cursor() 

class Student():
    
    def __init__(self, id_number, firstname, lastname, gender, year, course, photo_url = None):
        self.id_number = id_number
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.year = year
        self.course = course
        self.photo_url = photo_url

    def add_student(self):
        query = "INSERT INTO students(student_id, firstname, lastname, course_code_id, gender, year, photo_url) \
                VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = [self.id_number, self.firstname, self.lastname, self.course, self.gender,
                self.year, self.photo_url]
        cursor.execute(query, data)
        database.commit() 
    
    @classmethod
    def display_students(cls, offset):
        query = "SELECT * FROM students LIMIT 8 OFFSET %s"
        cursor.execute(query, [offset])    
        students = cursor.fetchall()
        return students 

    @classmethod
    def delete_student(cls, student_id):
        query = "DELETE FROM students WHERE student_id=%s"
        data = [student_id]
        cursor.execute(query, data)
        database.commit()
    
    @classmethod
    def edit_student(cls, id_number, firstname, lastname, gender, year_level, course_code, photo_url, old_id_number,):
        query = "UPDATE students SET student_id=%s, firstname=%s, lastname=%s, gender=%s, year=%s, \
                course_code_id=%s, photo_url=%s WHERE student_id=%s"
        data = [id_number, firstname, lastname, gender, year_level, course_code, photo_url, old_id_number]
        cursor.execute(query,data)
        database.commit()

    @classmethod
    def paginate_student_page(cls, offset):
        query = "SELECT * FROM students LIMIT 8, {offset}"
        cursor.execute(query)    
        students = cursor.fetchall()
        return students

    @classmethod 
    def search_student(cls, key):
        query = "SELECT * FROM students WHERE student_id LIKE %s or firstname LIKE %s or lastname LIKE %s or course_code_id LIKE %s \
            or year LIKE %s or gender LIKE %s"

        data = ['%'+key+'%','%'+key+'%','%'+key+'%','%'+key+'%','%'+key+'%','%'+key+'%']
        cursor.execute(query,data)
        results = cursor.fetchall()
        print(results)
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
    def display_courses(cls, offset):
        query = "SELECT * FROM courses LIMIT 5 OFFSET %s"
        cursor.execute(query, [offset])
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
        query = "SELECT * FROM courses WHERE course_code LIKE %s or course_name LIKE %s or college_code_id LIKE %s"
        data = ['%'+key+'%','%'+key+'%','%'+key+'%']
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
    def display_colleges(cls, offset):
        query = "SELECT * FROM colleges LIMIT 5 OFFSET %s"
        cursor.execute(query, [offset])
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
        query = "SELECT * FROM colleges WHERE college_code LIKE %s or college_name LIKE %s"
        data = ['%'+key+'%','%'+key+'%']
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result