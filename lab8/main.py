from fastapi import FastAPI, HTTPException
from schemas import Student, Professor, GrantRequest, Roles
from processor import Processor

app = FastAPI()

persons = {
    1: Student(id=1, first_name="Anastasiia", last_name="Prokopishena", role=Roles.STUDENT),
    2: Professor(id=2, first_name="Kosach", last_name="Valeria", role=Roles.TEACHING_STAFF,
                 unique_attribute="Research Chair"),
}

processor = Processor()


@app.post("/students/{student_id}/apply_grant")
def apply_grant(student_id: int, grant_request: GrantRequest):
    if student_id not in persons or grant_request.professor_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")

    student = persons[student_id]
    professor = persons[grant_request.professor_id]

    if not isinstance(student, Student) or not isinstance(professor, Professor):
        raise HTTPException(status_code=400, detail="Invalid person type")

    processor.visit_student(student)
    processor.visit_professor(professor)

    return {"message": "Grant applied successfully"}


@app.post("/students/{student_id}/make_compliant")
def make_compliant(student_id: int):
    if student_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")

    person = persons[student_id]

    if not isinstance(person, (Student, Professor)):
        raise HTTPException(status_code=400, detail="Invalid person type")

    processor.make_compliant(person)

    return {"message": "Made compliant successfully"}
