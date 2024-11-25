from school.models.school_model import SchoolModel
from student.models.student_model import StudentModel
from user.models.user_model import UserModel
from teacher.models.teacher_model import TeacherModel

 
def count(request):
    students_number = StudentModel.objects.filter(status=True).count()
    # schools_number = School.objects.filter(status=True).count()
    students_female = StudentModel.objects.filter(gender="FEMALE").count()
    students_male = StudentModel.objects.filter(gender="MALE").count()
    teachers_number = TeacherModel.objects.filter(status=True).count()
    users_number = UserModel.objects.filter(is_active=True).count()
    
    return  {'students_number': students_number,
            #  'schools_number': schools_number,
             'students_female': students_female,'students_male': students_male,
             'teachers_number': teachers_number,'users_number': users_number
             }
    