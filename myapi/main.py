from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


# amazon.com/create-user
# GET - GET an information
# POST - CREATE something new
# PUT - update
# DELETE - DELETE something

students = {
	1: {
		'name': 'john',
		'age': 17,
		'class': 'year'
	}
}

class Student(BaseModel):
	name: str 
	age: int 
	year: str 

class UpdateStudent(BaseModel):
	name: Optional[str] = None
	age: Optional[int] = None 
	year: Optional[str] = None

@app.get("/")
def index():
	return{'name': 'First Data'}

@app.get("/get-student/{student_id}")
def get_student(student_id: int  = Path(None, description="The ID of the student you want to view", gt=0, lt=3)):
	return students[student_id]

@app.get("/get-by-name")
def get_student(*, name : Optional[str] = None, test: int):
	# None means required is uncessary above 
	for student_id in students:
		if students[student_id]['name'] == name:
			return(students[student_id])
	return {'Data': 'Not Found'}

@app.get("/get-by-name_or_id")
def get_student_id(*, student_id:int, name : Optional[str] = None, test: int):
	# None means required is uncessary above 
	for student_id in students:
		if students[student_id]['name'] == name:
			return(students[student_id])
	return {'Data': 'Not Found'}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
	if student_id in students:
		return{'Error': 'Student exists'}
	studenst[student_id] = student
	return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
	if student_id not in students:
		return{'Error': 'Student does not exists'}

	if student.name != None:
		studenst[student_id] = student.name
	if student.age != None:
		studenst[student_id] = student.age

	if student.year != None:
		studenst[student_id] = student.year
	return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
	if student_id not in students:
		return{'Error': 'Student does not exists'}

	delete students[student_id]
	return {'Message': 'Student deleted succefully'}