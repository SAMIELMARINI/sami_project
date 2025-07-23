from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    address = models.TextField(blank=True, null=True)
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f"{self.name} ({self.email})"
    

class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    )

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee.name} - {self.date} ({self.status})"


class Performance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField()  
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - Rating: {self.rating}"