from django.views.generic import ListView

from .models import Student, Teacher


def add_data(students_param, teachers_param):
    for student in students_param:
        for teacher in teachers_param:
            if student.id == 1 and teacher.id == 1:
                student.teachers.add(teacher)
            elif student.id == 2 and teacher.id == 3:
                student.teachers.add(teacher)
            elif student.id == 3 and teacher.id == 3:
                student.teachers.add(teacher)


def db_values_check():
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    interval_table_list = [student.teachers.all() for student in students]
    for i, val in enumerate(interval_table_list):
        if len(val) == 0 and interval_table_list[-1] == interval_table_list[i]:
            add_data(students, teachers)
        elif len(val) == 0:
            continue
        else:
            break


class StudentListView(ListView):
    model = Student
    template_name = 'school/students_list.html'

    def get_context_data(self, **kwargs):
        db_values_check()
        context = super().get_context_data(**kwargs)
        context['object_list'] = Student.objects.all().order_by('group').prefetch_related('teachers')
        return context
