from home.models import *

print("deleting workplaces")
workplace.objects.all().delete()
print("deleting employee")
employee.objects.all().delete()
print("deleting competence_type")
competence_type.objects.all().delete()
print("deleting competence")
competence.objects.all().delete()
print("deleting competece_relevance")
competence_relevance.objects.all().delete()
print("deleting trainings")
education.objects.all().delete()
print("deleting employee_competence")
employee_competence.objects.all().delete()
print("deleting participation")
participation.objects.all().delete()
print("deleting user")
myuser.objects.all().delete()
print("deleting all HR")
HR_user.objects.all().delete()
print("delete notifications")
notifications.objects.all().delete()

print("***FINISHED DATABASE CLEAN***")

