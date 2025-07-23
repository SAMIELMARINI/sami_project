from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Department, Employee, Attendance, Performance

class Command(BaseCommand):
    help = "Seed the database with fake employees, attendance, and performance data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        
        dept_names = ['HR', 'IT', 'Finance', 'Marketing', 'Sales']
        departments = []

        for name in dept_names:
            dept, _ = Department.objects.get_or_create(name=name)
            departments.append(dept)

        self.stdout.write(self.style.SUCCESS(f"{len(departments)} departments ensured."))

        
        for _ in range(50):
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-2y', end_date='today'),
                department=random.choice(departments)
            )

            
            for _ in range(10):  
                Attendance.objects.create(
                    employee=employee,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )

            
            Performance.objects.create(
                employee=employee,
                rating=random.randint(1, 5),
                review_date=fake.date_between(start_date='-1y', end_date='today')
            )

        self.stdout.write(self.style.SUCCESS("Seeded 50 employees with attendance and performance data."))
