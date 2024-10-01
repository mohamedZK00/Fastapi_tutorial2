from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



# انشاء تطبيق FastAPI
app = FastAPI()

# لتشغيل ال api علي انترنت بدون حدوث اي مشاكل
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, # يسمح بالوصول الي اي مصدر 
    allow_methods=["*"],
    allow_headers=["*"],
)

# تعريف نموذج البيانات بستخدام pydantic
class Student(BaseModel):
    id: int
    name: str
    grade: float
    
# قائمة لتخزين البيانات في الذاكرة
students = [
    Student(id=1,name="karim ali",grade=5),
    Student(id=2,name="khaled ahmed",grade=3)
]

# قراءة جميع العناصر باستخدام طريقة (GET-1) 
@app.get('/students/') # get using read data

def read_students():
    return students

# انشاء عنصر جديد بااستخدام طريقة (POST-2) 
@app.post('/students/') # post using creat a new data

def create_student(New_student: Student):
    students.append(New_student)
    return New_student

# تحديث عنصر معين بناء علي معرفة باستخدام طريقة (PUT(update)-3)
@app.put('/students/{student_id}')

def update_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):  # حلقة للبحث عن الطالب حسب رقمه ثم تقوم بتحديث المعلومات
        if student.id == student_id:
            students[index] = update_student
            return update_student
    return {"error": "Student not found"}


# حذف عنصر معين بناء علي معرفة عن طريق استخدام (DELETE-4)
@app.delete('/students/{student_id}')

def delete_student(student_id: int):
    for index,student in enumerate(students): # حلقة للبحث عن الطالب حسب رقمه ثم تقوم بحذف معلومات هذا الطالب
        if student.id == student_id:
            del students[index] 
            return {"message": "Student deleted"}
    return {"error": "Student not found"}


        
