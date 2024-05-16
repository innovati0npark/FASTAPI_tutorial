from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()
#1
@app.get("/hello/")
def say_hello():
    return {"message": "Hello, LikeLion!"}

class User(BaseModel):
    name: str
    age: int
#2
@app.get("/user/{user_id}", response_model=User)
def get_user(user_id: int):
    # 실제 구현에서는 데이터베이스에서 사용자 정보를 조회하겠지만, 여기서는 예시 데이터를 사용합니다.
    # return User(name="Alice", age=30)
    # return {"name":"Alice", "age":30, "more":"good"}
    return {"user_id": user_id , "name": "User_name", "email": "User_email"}

#5
@app.get("/age/{age}", response_model=User)
def respond_based_on_age(age: int, user: User):
    if user.age < 20:
        return {"message": "You are a Alpha Generation !"}
    elif user.age >= 20 and user.age < 35:
        return {"message": "You are Generation Z"}
    elif user.age >= 35 and user.age < 50:
        return {"message": "You are Generation Y"}
    else:
        return {"message": "You are Generation X"}

class Student(BaseModel):
    student_id: int
    name: str
    email: str
#3
@app.post("/create_student", status_code=201)
def create_student(student: Student, response: Response):
    response.status_code = 201
    return {"student_id": student.student_id, "name": student.name, "email": student.email}

from typing import List
@app.get("/students", response_model=List[Student])
def read_students():
    # 실제 구현에서는 데이터베이스에서 학생 목록을 조회하겠지만, 여기서는 예시 데이터를 사용합니다.
    return [{"student_id": 1, "name": "Alice", "email": "alice@example.com"},
            {"student_id": 2, "name": "Bob", "email": "bob@example.com"}]

#4
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return {"message": "Student deleted successfully"}

@app.get("/search")
def search(query: str):
    return {"search_query": query}


from fastapi import FastAPI, HTTPException

@app.get("/error")
def custom_error():
    raise HTTPException(status_code=400, detail="Invalid request")