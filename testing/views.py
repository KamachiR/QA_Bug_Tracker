from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Project, TestCase, Bug


# =========================
# DASHBOARD
# =========================

@login_required(login_url='login')
def home(request):
    projects = Project.objects.all()
    test_cases = TestCase.objects.all()
    bugs = Bug.objects.all()

    total_projects = projects.count()
    total_test_cases = test_cases.count()

    passed_tests = test_cases.filter(status='Pass').count()
    failed_tests = test_cases.filter(status='Fail').count()
    not_tested = test_cases.filter(status='Not Tested').count()

    executed_tests = test_cases.filter(executed_at__isnull=False).count()

    if total_test_cases > 0:
        test_coverage = round((executed_tests / total_test_cases) * 100)
    else:
        test_coverage = 0

    total_bugs = bugs.count()
    open_bugs = bugs.filter(status='Open').count()
    fixed_bugs = bugs.filter(status='Fixed').count()
    critical_bugs = bugs.filter(severity='Critical').count()

    return render(request, 'testing/home.html', {
        'projects': projects,
        'test_cases': test_cases,
        'bugs': bugs,
        'total_projects': total_projects,
        'total_test_cases': total_test_cases,
        'passed_tests': passed_tests,
        'failed_tests': failed_tests,
        'not_tested': not_tested,
        'executed_tests': executed_tests,
        'test_coverage': test_coverage,
        'total_bugs': total_bugs,
        'open_bugs': open_bugs,
        'fixed_bugs': fixed_bugs,
        'critical_bugs': critical_bugs
    })


# =========================
# PROJECTS
# =========================

@login_required(login_url='login')
def projects(request):
    projects = Project.objects.all()

    return render(request, 'testing/projects.html', {
        'projects': projects
    })


@login_required(login_url='login')
def add_project(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        Project.objects.create(
            name=name,
            description=description
        )

        return redirect('projects')

    return render(request, 'testing/add_project.html')


@login_required(login_url='login')
def edit_project(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.save()

        return redirect('projects')

    return render(request, 'testing/edit_project.html', {
        'project': project
    })


@login_required(login_url='login')
def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'testing/delete_project.html', {
        'project': project
    })


# =========================
# TEST CASES
# =========================

@login_required(login_url='login')
def test_cases(request):
    test_cases = TestCase.objects.all()

    status_filter = request.GET.get('status')
    search_query = request.GET.get('search')

    if status_filter:
        test_cases = test_cases.filter(status=status_filter)

    if search_query:
        test_cases = test_cases.filter(
            title__icontains=search_query
        )

    return render(request, 'testing/test_cases.html', {
        'test_cases': test_cases,
        'status_filter': status_filter,
        'search_query': search_query
    })


@login_required(login_url='login')
def add_test_case(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        project_id = request.POST.get('project')
        title = request.POST.get('title')
        steps = request.POST.get('steps')
        expected_result = request.POST.get('expected_result')
        actual_result = request.POST.get('actual_result')
        status = request.POST.get('status')

        project = Project.objects.get(id=project_id)

        TestCase.objects.create(
            project=project,
            title=title,
            steps=steps,
            expected_result=expected_result,
            actual_result=actual_result,
            status=status
        )

        return redirect('test_cases')

    return render(request, 'testing/add_test_case.html', {
        'projects': projects
    })


@login_required(login_url='login')
def edit_test_case(request, test_case_id):
    test_case = TestCase.objects.get(id=test_case_id)
    projects = Project.objects.all()

    if request.method == 'POST':
        project_id = request.POST.get('project')

        test_case.project = Project.objects.get(id=project_id)
        test_case.title = request.POST.get('title')
        test_case.steps = request.POST.get('steps')
        test_case.expected_result = request.POST.get('expected_result')
        test_case.actual_result = request.POST.get('actual_result')
        test_case.status = request.POST.get('status')

        test_case.save()

        return redirect('test_cases')

    return render(request, 'testing/edit_test_case.html', {
        'test_case': test_case,
        'projects': projects
    })


@login_required(login_url='login')
def delete_test_case(request, test_case_id):
    test_case = TestCase.objects.get(id=test_case_id)

    if request.method == 'POST':
        test_case.delete()
        return redirect('test_cases')

    return render(request, 'testing/delete_test_case.html', {
        'test_case': test_case
    })


@login_required(login_url='login')
def execute_test_case(request, test_case_id):
    test_case = TestCase.objects.get(id=test_case_id)

    if request.method == 'POST':
        test_case.actual_result = request.POST.get('actual_result')
        test_case.status = request.POST.get('status')
        test_case.executed_at = timezone.now()

        test_case.save()

        return redirect('test_cases')

    return render(request, 'testing/execute_test_case.html', {
        'test_case': test_case
    })


# =========================
# BUGS
# =========================

@login_required(login_url='login')
def bugs(request):
    bugs = Bug.objects.all()

    status_filter = request.GET.get('status')
    severity_filter = request.GET.get('severity')
    priority_filter = request.GET.get('priority')
    search_query = request.GET.get('search')

    if status_filter:
        bugs = bugs.filter(status=status_filter)

    if severity_filter:
        bugs = bugs.filter(severity=severity_filter)

    if priority_filter:
        bugs = bugs.filter(priority=priority_filter)

    if search_query:
        bugs = bugs.filter(
            title__icontains=search_query
        )

    return render(request, 'testing/bugs.html', {
        'bugs': bugs,
        'status_filter': status_filter,
        'severity_filter': severity_filter,
        'priority_filter': priority_filter,
        'search_query': search_query
    })


@login_required(login_url='login')
def add_bug(request):
    projects = Project.objects.all()
    test_cases = TestCase.objects.all()

    if request.method == 'POST':
        project_id = request.POST.get('project')
        test_case_id = request.POST.get('test_case')
        title = request.POST.get('title')
        description = request.POST.get('description')
        severity = request.POST.get('severity')
        priority = request.POST.get('priority')
        status = request.POST.get('status')

        project = Project.objects.get(id=project_id)

        test_case = None

        if test_case_id:
            test_case = TestCase.objects.get(id=test_case_id)

        Bug.objects.create(
            project=project,
            test_case=test_case,
            title=title,
            description=description,
            severity=severity,
            priority=priority,
            status=status
        )

        return redirect('bugs')

    return render(request, 'testing/add_bug.html', {
        'projects': projects,
        'test_cases': test_cases
    })


@login_required(login_url='login')
def edit_bug(request, bug_id):
    bug = Bug.objects.get(id=bug_id)

    projects = Project.objects.all()
    test_cases = TestCase.objects.all()

    if request.method == 'POST':
        project_id = request.POST.get('project')
        test_case_id = request.POST.get('test_case')

        bug.project = Project.objects.get(id=project_id)

        if test_case_id:
            bug.test_case = TestCase.objects.get(id=test_case_id)
        else:
            bug.test_case = None

        bug.title = request.POST.get('title')
        bug.description = request.POST.get('description')
        bug.severity = request.POST.get('severity')
        bug.priority = request.POST.get('priority')
        bug.status = request.POST.get('status')

        bug.save()

        return redirect('bugs')

    return render(request, 'testing/edit_bug.html', {
        'bug': bug,
        'projects': projects,
        'test_cases': test_cases
    })


@login_required(login_url='login')
def delete_bug(request, bug_id):
    bug = Bug.objects.get(id=bug_id)

    if request.method == 'POST':
        bug.delete()
        return redirect('bugs')

    return render(request, 'testing/delete_bug.html', {
        'bug': bug
    })


# =========================
# LOGIN / LOGOUT
# =========================

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        return render(request, 'testing/login.html', {
            'error': 'Invalid username or password.'
        })

    return render(request, 'testing/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
