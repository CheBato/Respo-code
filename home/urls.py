
"""
This is where all the paths are going to be written. Format is as below
path('/test' views.<name_of_view>, name='<name>'
the login url pattern is an example of how it works. The views.login tells url which function to use in the views.py
file.
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('upload', views.upload, name='upload'),
    path("employees", views.employees, name="employees"),
    path('competencies', views.competencies, name='competencies'),
    path('workplaces', views.workplaces, name='workplaces'),
    path('options', views.options, name='options'),
    path('history', views.history, name='history'),
    path('trainings', views.trainings, name='trainings'),
    path('analytics', views.analytics, name='analytics'),
    path('status', views.status, name='status'),
    #API
    path('employees/add', views.employeeAdd, name="add"),
    path('employees/edit', views.employeeEdit, name="edit"),
    path('competencies/add', views.competencyAdd, name="competencyAdd"),
    path('competencies/edit', views.competenciesEdit, name="competenciesEdit"),
    path('competencies-type/edit', views.competencies_type_edit, name="competencies_type_edit"),
    path('trainings/add', views.trainingsAdd, name="trainingsAdd"),
    path('workplace/add', views.workplaceAdd, name='workplaceAdd'),
    path('workplace/edit', views.workplaceEdit, name='workplaceEdit'),
    path('workplace/addExtra', views.addExtraRelevanceToWorkplace, name='addExtraCompetence'),
    path('file/upload', views.uploadFile, name='uploadFile'),
    path('analytics/compute',views.analyticsCompute, name='analyticsCompute'),
    #User
    path('user_history', views.user_history_recent, name='user_history'),
    path('user_history/timeline', views.user_history_timeline, name='user_history/timeline'),
    path('user_competencies', views.user_competencies, name='user_competencies'),
    path('user_status', views.user_status, name='user_status'),
    path('user_trainings', views.user_trainings, name='user_trainings'),
    #AJAX
    url(r'^ajax/findemployee/$', views.findEmployees, name="findEmployees"),
    url(r'^ajax/findCompetenceType/$', views.findCompetenceType, name="findCompetenceType"),
    url(r'^ajax/deleteCompType/$', views.deleteCompetenceType, name="deleteCompetenceType"),
    url(r'^ajax/findCompetences/$',views.findCompetencesByType, name="findCompetencesByType"),
    url(r'^ajax/deleteComp/$', views.deleteCompetence, name="deleteCompetence"),
    url(r'^ajax/getEditCompetence/$', views.getEditCompetences, name="getEditCompetences"),
    url(r'^ajax/findCompetencesSearch/$', views.findCompetencesByTwo, name="findCompetencesByTwo"),
    url(r'^ajax/addCompetenciesUser/$', views.addCompetenciesToUser, name="addCompetenciesForUser"),
    url(r'^ajax/deleteEmployee/$', views.deleteEmployee, name="deleteEmployee"),
    url(r'^ajax/getEditEmployee/$', views.getEditEmployee, name="getEditEmployee"),
    url(r'^ajax/findCompetenciesByType/$', views.getCompetenciesByTypeOnRequest, name="getByType"),
    url(r'^ajax/getEditCompetenceType/$', views.getEditCompetenceType, name="getEditCompetenceType"),
    url(r'^ajax/getEditWorkplace/$', views.getEditWorkplaces, name="getEditWorkplaces"),
    url(r'^ajax/findWorkplaceCompetences/$', views.findWorkplaceRelevance, name="findWorkplaceRelevance"),
    url(r'^ajax/deleteCompetenceRelevance/$', views.deleteCompetence_relevance, name="delete_competence_relevance"),
    url(r'^ajax/editCompetencyRelevance/$', views.editCompetencyRelevanceForWorkplace, name="editCompetencyRelevanceForWorkplace"),
    url(r'^ajax/deleteWorkplace/$', views.deleteWorkplaceAndRelevance, name='deleteWorkplaceAndRelevance'),
    url(r'^ajax/findTrainingCompetencies/$', views.findTrainingCompetencies, name='findTrainingCompetencies'),
    url(r'^ajax/getEditEducation/$', views.getEditEducation, name="getEditEducation"),
    url(r'^ajax/deleteTraining/$', views.deleteTrainings, name="deleteTraining"),
    url('', views.index, name='index'),


]