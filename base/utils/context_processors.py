from school.models.school import School
from student.models.student import Student
from user.models.user import User   
from teacher.models.teacher import Teacher

 
def count(request):
    students_number = Student.objects.filter(status=True).count()
    # schools_number = School.objects.filter(status=True).count()
    students_female = Student.objects.filter(gender="FEMALE").count()
    students_male = Student.objects.filter(gender="MALE").count()
    teachers_number = Teacher.objects.filter(status=True).count()
    users_number = User.objects.filter(is_active=True).count()
    
    return  {'students_number': students_number,
            #  'schools_number': schools_number,
             'students_female': students_female,'students_male': students_male,
             'teachers_number': teachers_number,'users_number': users_number
             }
    