from schemas import Student, Professor, Person


class Processor:
    def visit_student(self, student: Student):
        student.academic_score += 10

    def visit_professor(self, professor: Professor):
        professor.academic_score += 5

    def make_compliant(self, person: Person):
        if isinstance(person, Student):
            person.academic_score -= 5
        elif isinstance(person, Professor):
            person.academic_score -= 2
