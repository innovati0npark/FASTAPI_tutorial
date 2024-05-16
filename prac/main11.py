from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}


#강사님 연습문제
class Student(BaseModel):
    student_id: int
    name: str
    email: str

@app.get("/likelion/{student_id}")
def read_student(student_id: int, student: Student):
    return { "student_id": student_id, "name":"이두희", 'email': student.email}

class Project(BaseModel):
    name: str
    description: str

@app.post("/item/")
def itemCreate(item: Item):
    return {"name": item.name, "description": item.description}

@app.post("/projects/")
def create_project(project: Project):
    return {"name": project.name, "description": project.description}


@app.delete("/projects/{project_id}")
def delete_project(project_id: int):
    return {"message": "Project deleted successfully"}