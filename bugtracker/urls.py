from django.contrib import admin
from django.urls import path

from testing.views import (
    home,
    projects,
    test_cases,
    bugs,
    add_project,
    edit_project,
    delete_project,
    add_test_case,
    edit_test_case,
    delete_test_case,
    execute_test_case,
    add_bug,
    edit_bug,
    delete_bug,
    login_view,
    logout_view
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('', home, name='home'),

    path('projects/', projects, name='projects'),
    path('test-cases/', test_cases, name='test_cases'),
    path('bugs/', bugs, name='bugs'),

    path('projects/add/', add_project, name='add_project'),

    path(
        'projects/edit/<int:project_id>/',
        edit_project,
        name='edit_project'
    ),

    path(
        'projects/delete/<int:project_id>/',
        delete_project,
        name='delete_project'
    ),

    path(
        'test-cases/add/',
        add_test_case,
        name='add_test_case'
    ),

    path(
        'test-cases/edit/<int:test_case_id>/',
        edit_test_case,
        name='edit_test_case'
    ),

    path(
        'test-cases/delete/<int:test_case_id>/',
        delete_test_case,
        name='delete_test_case'
    ),

    path(
        'test-cases/execute/<int:test_case_id>/',
        execute_test_case,
        name='execute_test_case'
    ),

    path(
        'bugs/add/',
        add_bug,
        name='add_bug'
    ),

    path(
        'bugs/edit/<int:bug_id>/',
        edit_bug,
        name='edit_bug'
    ),

    path(
        'bugs/delete/<int:bug_id>/',
        delete_bug,
        name='delete_bug'
    ),
]
