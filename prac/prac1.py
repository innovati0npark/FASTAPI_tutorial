from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

#1 대학행사등록
class Event(BaseModel):
    name: str
    date: date
    attendees: int


@app.post("/events")
def create_event(event: Event):
    # return {"name": event.name, "date123": event.date, "attendees": event.attendees}
    return {"message": "Event created successfully", "event": event}


#2 도서대출기록
class Book(BaseModel):
    title: str
    author: str
    borrow_date: date

@app.post("/books/{book_id}/borrow")
def borrow_book(book: Book):
    return {"message": "Book borrowed successfully", "book": book}



from pydantic import EmailStr
#3 멋쟁이사자 회원등록
class LionUser(BaseModel):
    name: str
    email: EmailStr
    date: date

@app.post("/members")
def register_member(user: LionUser):
    return {"message": "User created successfully", "user": user}


class Menu(BaseModel):
    menu: str
    price: float
    date: date

@app.post("/meals")
def create_meal(menu: Menu):
    return {"message": "Meal created successfully", "menu": menu}


class StudyGroup(BaseModel):
    name: str
    topic: str
    people: int

@app.post("/studygroups")
def create_studygroup(group: StudyGroup):
    return {"message": "Study group created successfully", "group": group}