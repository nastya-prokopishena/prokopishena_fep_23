from enum import Enum
from typing import Dict
from pydantic import BaseModel


class Roles(str, Enum):
    STUDENT = "student"
    TEACHING_STAFF = "teaching_staff"
    RESEARCH_STAFF = "research_staff"
    ADMINISTRATION_STAFF = "administration_staff"


class PersonBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    role: Roles


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    class Config:
        orm_mode = True


class StudentCreate(PersonCreate):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    visited_lectures: int = 0


class Student(Person):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    visited_lectures: int = 0


class ProfessorCreate(PersonCreate):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    unique_attribute: str = ""


class Professor(Person):
    research_score: Dict[str, int] = {}
    academic_score: int = 0
    unique_attribute: str = ""


class GrantRequest(BaseModel):
    student_id: int
    professor_id: int
