from django.test import TestCase
from django.contrib.auth.models import User

from .models import Project, TestCase as TestCaseModel, Bug


class AuthenticatedTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        self.client.login(
            username='testuser',
            password='testpassword123'
        )


# =========================================================
# MODEL TESTS
# =========================================================

class ProjectModelTest(TestCase):

    def test_project_creation(self):
        project = Project.objects.create(
            name="QA Test Project",
            description="Testing project creation"
        )

        self.assertEqual(project.name, "QA Test Project")
        self.assertEqual(
            project.description,
            "Testing project creation"
        )


class TestCaseModelTest(TestCase):

    def test_test_case_creation(self):
        project = Project.objects.create(
            name="Login Project",
            description="Testing login functionality"
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title="Login with valid credentials",
            steps="Enter username and password",
            expected_result="User should login successfully",
            actual_result="",
            status="Not Tested"
        )

        self.assertEqual(
            test_case.title,
            "Login with valid credentials"
        )

        self.assertEqual(
            test_case.project,
            project
        )

        self.assertEqual(
            test_case.status,
            "Not Tested"
        )


class BugModelTest(TestCase):

    def test_bug_creation(self):
        project = Project.objects.create(
            name="Bug Testing Project",
            description="Testing bug creation"
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title="Login Test",
            steps="Enter invalid password",
            expected_result="Error message should appear",
            actual_result="No error message",
            status="Fail"
        )

        bug = Bug.objects.create(
            project=project,
            test_case=test_case,
            title="Error message not displayed",
            description="The error message is missing after invalid login.",
            severity="High",
            priority="High",
            status="Open"
        )

        self.assertEqual(
            bug.title,
            "Error message not displayed"
        )

        self.assertEqual(
            bug.project,
            project
        )

        self.assertEqual(
            bug.test_case,
            test_case
        )

        self.assertEqual(
            bug.severity,
            "High"
        )

        self.assertEqual(
            bug.priority,
            "High"
        )

        self.assertEqual(
            bug.status,
            "Open"
        )


# =========================================================
# PAGE VIEW TESTS
# =========================================================

class HomeViewTest(AuthenticatedTestCase):

    def test_home_page_loads(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'testing/home.html'
        )


class ProjectsViewTest(AuthenticatedTestCase):

    def test_projects_page_loads(self):
        response = self.client.get('/projects/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'testing/projects.html'
        )


class TestCasesViewTest(AuthenticatedTestCase):

    def test_test_cases_page_loads(self):
        response = self.client.get('/test-cases/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'testing/test_cases.html'
        )


class BugsViewTest(AuthenticatedTestCase):

    def test_bugs_page_loads(self):
        response = self.client.get('/bugs/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'testing/bugs.html'
        )


# =========================================================
# ADD PROJECT
# =========================================================

class AddProjectViewTest(AuthenticatedTestCase):

    def test_add_project(self):
        response = self.client.post(
            '/projects/add/',
            {
                'name': 'Automation Project',
                'description': 'Testing project creation through form'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Project.objects.count(),
            1
        )

        project = Project.objects.first()

        self.assertEqual(
            project.name,
            'Automation Project'
        )


# =========================================================
# ADD TEST CASE
# =========================================================

class AddTestCaseViewTest(AuthenticatedTestCase):

    def test_add_test_case(self):
        project = Project.objects.create(
            name='Test Project',
            description='Testing test case creation'
        )

        response = self.client.post(
            '/test-cases/add/',
            {
                'project': project.id,
                'title': 'Valid Login Test',
                'steps': 'Enter valid username and password',
                'expected_result': 'User should login successfully',
                'actual_result': '',
                'status': 'Not Tested'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            TestCaseModel.objects.count(),
            1
        )

        test_case = TestCaseModel.objects.first()

        self.assertEqual(
            test_case.title,
            'Valid Login Test'
        )

        self.assertEqual(
            test_case.project,
            project
        )


# =========================================================
# ADD BUG
# =========================================================

class AddBugViewTest(AuthenticatedTestCase):

    def test_add_bug(self):
        project = Project.objects.create(
            name='Bug Test Project',
            description='Testing bug creation'
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title='Login Test',
            steps='Enter invalid password',
            expected_result='Error message should appear',
            actual_result='No error message',
            status='Fail'
        )

        response = self.client.post(
            '/bugs/add/',
            {
                'project': project.id,
                'test_case': test_case.id,
                'title': 'Error message not displayed',
                'description': 'Error message is missing.',
                'severity': 'High',
                'priority': 'High',
                'status': 'Open'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Bug.objects.count(),
            1
        )

        bug = Bug.objects.first()

        self.assertEqual(
            bug.title,
            'Error message not displayed'
        )

        self.assertEqual(
            bug.project,
            project
        )

        self.assertEqual(
            bug.test_case,
            test_case
        )


# =========================================================
# EXECUTE TEST CASE
# =========================================================

class ExecuteTestCaseViewTest(AuthenticatedTestCase):

    def test_execute_test_case(self):
        project = Project.objects.create(
            name='Execution Test Project',
            description='Testing test case execution'
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title='Login Execution Test',
            steps='Enter valid username and password',
            expected_result='User should login successfully',
            actual_result='',
            status='Not Tested'
        )

        response = self.client.post(
            f'/test-cases/execute/{test_case.id}/',
            {
                'actual_result': 'User successfully logged in.',
                'status': 'Pass'
            }
        )

        self.assertEqual(response.status_code, 302)

        test_case.refresh_from_db()

        self.assertEqual(
            test_case.actual_result,
            'User successfully logged in.'
        )

        self.assertEqual(
            test_case.status,
            'Pass'
        )

        self.assertIsNotNone(
            test_case.executed_at
        )


# =========================================================
# BUG FILTER
# =========================================================

class BugFilterViewTest(AuthenticatedTestCase):

    def test_bug_status_filter(self):
        project = Project.objects.create(
            name='Filter Test Project',
            description='Testing bug filters'
        )

        Bug.objects.create(
            project=project,
            title='Open Bug',
            description='This bug is open.',
            severity='High',
            priority='High',
            status='Open'
        )

        Bug.objects.create(
            project=project,
            title='Fixed Bug',
            description='This bug is fixed.',
            severity='Low',
            priority='Low',
            status='Fixed'
        )

        response = self.client.get(
            '/bugs/?status=Open'
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Open Bug'
        )

        self.assertNotContains(
            response,
            'Fixed Bug'
        )


# =========================================================
# TEST CASE FILTER
# =========================================================

class TestCaseFilterViewTest(AuthenticatedTestCase):

    def test_test_case_status_filter(self):
        project = Project.objects.create(
            name='Test Case Filter Project',
            description='Testing test case filters'
        )

        TestCaseModel.objects.create(
            project=project,
            title='Passing Login Test',
            steps='Enter valid credentials',
            expected_result='Login succeeds',
            actual_result='Login successful',
            status='Pass'
        )

        TestCaseModel.objects.create(
            project=project,
            title='Failing Login Test',
            steps='Enter invalid credentials',
            expected_result='Error appears',
            actual_result='No error',
            status='Fail'
        )

        response = self.client.get(
            '/test-cases/?status=Pass'
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Passing Login Test'
        )

        self.assertNotContains(
            response,
            'Failing Login Test'
        )


# =========================================================
# TEST CASE SEARCH
# =========================================================

class TestCaseSearchViewTest(AuthenticatedTestCase):

    def test_test_case_search(self):
        project = Project.objects.create(
            name='Search Test Project',
            description='Testing test case search'
        )

        TestCaseModel.objects.create(
            project=project,
            title='Login with valid credentials',
            steps='Enter username and password',
            expected_result='Login succeeds',
            actual_result='Login successful',
            status='Pass'
        )

        TestCaseModel.objects.create(
            project=project,
            title='Logout functionality',
            steps='Click logout',
            expected_result='User should logout',
            actual_result='User logged out',
            status='Pass'
        )

        response = self.client.get(
            '/test-cases/?search=Login'
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Login with valid credentials'
        )

        self.assertNotContains(
            response,
            'Logout functionality'
        )


# =========================================================
# BUG SEARCH
# =========================================================

class BugSearchViewTest(AuthenticatedTestCase):

    def test_bug_search(self):
        project = Project.objects.create(
            name='Bug Search Project',
            description='Testing bug search'
        )

        Bug.objects.create(
            project=project,
            title='Login button not working',
            description='Login button does nothing.',
            severity='High',
            priority='High',
            status='Open'
        )

        Bug.objects.create(
            project=project,
            title='Logout button not working',
            description='Logout button does nothing.',
            severity='Medium',
            priority='Medium',
            status='Open'
        )

        response = self.client.get(
            '/bugs/?search=Login'
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Login button not working'
        )

        self.assertNotContains(
            response,
            'Logout button not working'
        )


# =========================================================
# BUG SEVERITY FILTER
# =========================================================

class BugSeverityFilterViewTest(AuthenticatedTestCase):

    def test_bug_severity_filter(self):
        project = Project.objects.create(
            name='Severity Filter Project',
            description='Testing severity filter'
        )

        Bug.objects.create(
            project=project,
            title='Critical Bug',
            description='Critical issue.',
            severity='Critical',
            priority='High',
            status='Open'
        )

        Bug.objects.create(
            project=project,
            title='Low Bug',
            description='Low issue.',
            severity='Low',
            priority='Low',
            status='Open'
        )

        response = self.client.get(
            '/bugs/?severity=Critical'
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Critical Bug'
        )

        self.assertNotContains(
            response,
            'Low Bug'
        )


# =========================================================
# BUG PRIORITY FILTER
# =========================================================

class BugPriorityFilterViewTest(AuthenticatedTestCase):

    def test_bug_priority_filter(self):
        project = Project.objects.create(
            name='Priority Filter Project',
            description='Testing priority filter'
        )

        Bug.objects.create(
            project=project,
            title='High Priority Bug',
            description='High priority issue.',
            severity='Medium',
            priority='High',
            status='Open'
        )

        Bug.objects.create(
            project=project,
            title='Low Priority Bug',
            description='Low priority issue.',
            severity='Medium',
            priority='Low',
            status='Open'
        )

        response = self.client.get(
            '/bugs/?priority=High'
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'High Priority Bug'
        )

        self.assertNotContains(
            response,
            'Low Priority Bug'
        )


# =========================================================
# ADD PROJECT PAGE
# =========================================================

class AddProjectPageViewTest(AuthenticatedTestCase):

    def test_add_project_page_loads(self):
        response = self.client.get(
            '/projects/add/'
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'testing/add_project.html'
        )


# =========================================================
# ADD TEST CASE PAGE
# =========================================================

class AddTestCasePageViewTest(AuthenticatedTestCase):

    def test_add_test_case_page_loads(self):
        project = Project.objects.create(
            name='Page Test Project',
            description='Testing add test case page'
        )

        response = self.client.get(
            '/test-cases/add/'
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'testing/add_test_case.html'
        )


# =========================================================
# ADD BUG PAGE
# =========================================================

class AddBugPageViewTest(AuthenticatedTestCase):

    def test_add_bug_page_loads(self):
        response = self.client.get(
            '/bugs/add/'
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTemplateUsed(
            response,
            'testing/add_bug.html'
        )


# =========================================================
# EDIT PROJECT
# =========================================================

class EditProjectViewTest(AuthenticatedTestCase):

    def test_edit_project(self):
        project = Project.objects.create(
            name='Old Project Name',
            description='Old description'
        )

        response = self.client.post(
            f'/projects/edit/{project.id}/',
            {
                'name': 'Updated Project Name',
                'description': 'Updated description'
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        project.refresh_from_db()

        self.assertEqual(
            project.name,
            'Updated Project Name'
        )

        self.assertEqual(
            project.description,
            'Updated description'
        )


# =========================================================
# EDIT TEST CASE
# =========================================================

class EditTestCaseViewTest(AuthenticatedTestCase):

    def test_edit_test_case(self):
        project = Project.objects.create(
            name='Edit Test Project',
            description='Testing edit test case'
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title='Old Test Case',
            steps='Old steps',
            expected_result='Old expected result',
            actual_result='Old actual result',
            status='Not Tested'
        )

        response = self.client.post(
            f'/test-cases/edit/{test_case.id}/',
            {
                'project': project.id,
                'title': 'Updated Test Case',
                'steps': 'Updated steps',
                'expected_result': 'Updated expected result',
                'actual_result': 'Updated actual result',
                'status': 'Pass'
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        test_case.refresh_from_db()

        self.assertEqual(
            test_case.title,
            'Updated Test Case'
        )

        self.assertEqual(
            test_case.status,
            'Pass'
        )


# =========================================================
# EDIT BUG
# =========================================================

class EditBugViewTest(AuthenticatedTestCase):

    def test_edit_bug(self):
        project = Project.objects.create(
            name='Edit Bug Project',
            description='Testing edit bug'
        )

        bug = Bug.objects.create(
            project=project,
            title='Old Bug',
            description='Old description',
            severity='Low',
            priority='Low',
            status='Open'
        )

        response = self.client.post(
            f'/bugs/edit/{bug.id}/',
            {
                'project': project.id,
                'test_case': '',
                'title': 'Updated Bug',
                'description': 'Updated description',
                'severity': 'High',
                'priority': 'High',
                'status': 'Fixed'
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        bug.refresh_from_db()

        self.assertEqual(
            bug.title,
            'Updated Bug'
        )

        self.assertEqual(
            bug.severity,
            'High'
        )

        self.assertEqual(
            bug.status,
            'Fixed'
        )


# =========================================================
# DELETE PROJECT
# =========================================================

class DeleteProjectViewTest(AuthenticatedTestCase):

    def test_delete_project(self):
        project = Project.objects.create(
            name='Delete Project',
            description='Project to delete'
        )

        response = self.client.post(
            f'/projects/delete/{project.id}/'
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertEqual(
            Project.objects.count(),
            0
        )


# =========================================================
# DELETE TEST CASE
# =========================================================

class DeleteTestCaseViewTest(AuthenticatedTestCase):

    def test_delete_test_case(self):
        project = Project.objects.create(
            name='Delete Test Project',
            description='Testing delete test case'
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title='Delete Test Case',
            steps='Steps',
            expected_result='Expected',
            actual_result='Actual',
            status='Pass'
        )

        response = self.client.post(
            f'/test-cases/delete/{test_case.id}/'
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertEqual(
            TestCaseModel.objects.count(),
            0
        )


# =========================================================
# DELETE BUG
# =========================================================

class DeleteBugViewTest(AuthenticatedTestCase):

    def test_delete_bug(self):
        project = Project.objects.create(
            name='Delete Bug Project',
            description='Testing delete bug'
        )

        bug = Bug.objects.create(
            project=project,
            title='Delete Bug',
            description='Bug to delete',
            severity='Low',
            priority='Low',
            status='Open'
        )

        response = self.client.post(
            f'/bugs/delete/{bug.id}/'
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertEqual(
            Bug.objects.count(),
            0
        )


# =========================================================
# EXECUTION TIMESTAMP
# =========================================================

class TestCaseExecutionTimestampTest(AuthenticatedTestCase):

    def test_execution_timestamp(self):
        project = Project.objects.create(
            name='Timestamp Project',
            description='Testing execution timestamp'
        )

        test_case = TestCaseModel.objects.create(
            project=project,
            title='Timestamp Test',
            steps='Execute test',
            expected_result='Test passes',
            actual_result='',
            status='Not Tested'
        )

        response = self.client.post(
            f'/test-cases/execute/{test_case.id}/',
            {
                'actual_result': 'Test passed successfully',
                'status': 'Pass'
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        test_case.refresh_from_db()

        self.assertIsNotNone(
            test_case.executed_at
        )


# =========================================================
# DASHBOARD STATISTICS
# =========================================================

class DashboardStatisticsTest(AuthenticatedTestCase):

    def test_dashboard_statistics(self):
        project = Project.objects.create(
            name='Dashboard Project',
            description='Testing dashboard statistics'
        )

        TestCaseModel.objects.create(
            project=project,
            title='Passing Test',
            steps='Steps',
            expected_result='Pass',
            actual_result='Passed',
            status='Pass'
        )

        TestCaseModel.objects.create(
            project=project,
            title='Failing Test',
            steps='Steps',
            expected_result='Pass',
            actual_result='Failed',
            status='Fail'
        )

        Bug.objects.create(
            project=project,
            title='Open Bug',
            description='Open issue',
            severity='High',
            priority='High',
            status='Open'
        )

        response = self.client.get('/')

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response.context['total_projects'],
            1
        )

        self.assertEqual(
            response.context['total_test_cases'],
            2
        )

        self.assertEqual(
            response.context['passed_tests'],
            1
        )

        self.assertEqual(
            response.context['failed_tests'],
            1
        )

        self.assertEqual(
            response.context['open_bugs'],
            1
        )


# =========================================================
# AUTHENTICATION TESTS
# =========================================================

class AuthenticationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='authuser',
            password='authpassword123'
        )

    def test_login_with_valid_credentials(self):
        response = self.client.post(
            '/login/',
            {
                'username': 'authuser',
                'password': 'authpassword123'
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_login_with_invalid_credentials(self):
        response = self.client.post(
            '/login/',
            {
                'username': 'authuser',
                'password': 'wrongpassword'
            }
        )

        self.assertEqual(response.status_code, 200)

        self.assertContains(
            response,
            'Invalid username or password.'
        )

    def test_logout(self):
        self.client.login(
            username='authuser',
            password='authpassword123'
        )

        response = self.client.get('/logout/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')

    def test_home_requires_login(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/'
        )

    def test_projects_requires_login(self):
        response = self.client.get('/projects/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/projects/'
        )

    def test_test_cases_requires_login(self):
        response = self.client.get('/test-cases/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/test-cases/'
        )

    def test_bugs_requires_login(self):
        response = self.client.get('/bugs/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/bugs/'
        )

    def test_add_project_requires_login(self):
        response = self.client.get('/projects/add/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/projects/add/'
        )

    def test_add_test_case_requires_login(self):
        response = self.client.get('/test-cases/add/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/test-cases/add/'
        )

    def test_add_bug_requires_login(self):
        response = self.client.get('/bugs/add/')

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(
            response,
            '/login/?next=/bugs/add/'
        )
