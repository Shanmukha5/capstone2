from django.test import TestCase
from CRUDemployee.models import Employee

from django.core.files import File

class EmployeeTestCase(TestCase):
	def setUp(self):
		Employee.objects.create(id=100, name="Employee100", age=100)

	def test_employee_retrieve(self):
		obj = Employee.objects.get(id=100)
		self.assertEqual(obj.name, "Employee100")

	def test_employee_update(self):
		obj = Employee.objects.get(id=100)
		obj.name = "Employee100UpdatedFromTestcases"
		obj.save()
		print("\nObject updated!")
		newObj = Employee.objects.get(id=100)
		self.assertEqual(newObj.name, 'Employee100UpdatedFromTestcases')

	def test_employee_delete(self):
		count = Employee.objects.count()
		obj = Employee.objects.get(id=100)
		obj.delete()
		newCount = Employee.objects.count()
		print(count, newCount)
		self.assertEqual(count-1, newCount)


