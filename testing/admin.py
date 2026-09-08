from django.contrib import admin
from .models import Project, TestCase, Bug


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'status',
        'executed_at'
    )

    list_filter = (
        'status',
        'project'
    )

    search_fields = (
        'title',
        'steps',
        'expected_result',
        'actual_result'
    )

    ordering = ('-id',)


@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'severity',
        'priority',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
        'severity',
        'priority',
        'project'
    )

    search_fields = (
        'title',
        'description'
    )

    ordering = ('-created_at',)
