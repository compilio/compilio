from django.test import TestCase

from .models import Task


class CompilerTestCase(TestCase):
    def tests_task_initialization(self):
        task = Task()
        self.assertEqual(task.status, 'PENDING')
