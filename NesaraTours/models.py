from django.db import models
from django.contrib.auth.models import User,Group 

# # Create your models here.
# class Hotel(models.Model):
#     # status=(
#     #     ('Available','Available'),
#     #     ('Not Available','Not Available'),
#     # )
#     types = (
#         ('3 Star','3Star'),
#         ('5 Star','5Star'),
#     )
    


#     Name=models.CharField(max_length=255)
#     Place=models.CharField(max_length=255)
#     # Pack=models.ForeignKey(Package,on_delete=models.SET_NULL,null=True)
#     # Status=models.CharField(max_length=255,choices=status)
#     Types= models.CharField(max_length=255,choices=types,null=True)
#     Price=models.IntegerField(null=True)

#     def __str__(self):
#         return self.Name
    




class Package(models.Model):
    Name = models.CharField(null=True,max_length=255)
    Discription=models.TextField(null=True,max_length=1024)
    StartDate=models.DateField()
    EndDate=models.DateField()
    Price=models.IntegerField(null=True)
    # Hotel=models.ForeignKey(Hotel,on_delete=models.SET_NULL,null=True)
    Image = models.CharField(null=True,max_length=1024)
    def __str__(self):  
        return self.Name




class Branch(models.Model):
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    
    def __str__(self):        
        return self.Name

class Employee(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    role = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    Name = models.CharField(max_length=255,null=True)
    Phone = models.CharField(max_length=255,null=True)
    Email = models.EmailField(null=True)
    Sal = models.CharField(max_length=10,null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    def __str__(self):        
        return self.Name


class Client(models.Model):
    status=(
        ('Active','Active'),
        ('Inactive','Inactive'),
        ('Not verified','Not verified')
    )
    Name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=255)
    Email= models.EmailField(null=True)
    Status = models.CharField(max_length=255,choices=status) 
    def __str__(self):        
        return self.Name

class Tour(models.Model):
    status = (
        ('Complete' , 'Complete' ),
        ('Not complete', 'Not complete'),
        ('Ongoing','Ongoing')
    )

    Name = models.CharField(max_length=255,null=True)
    Destinations = models.TextField(max_length=255,null=True)
    DateStarted = models.DateField(null=True)
    DateCompleated = models.DateField(null=True)
    Client = models.ManyToManyField(Client)
    Branch = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    Employee = models.ManyToManyField(Employee)
    Status = models.CharField(max_length=255,null=True,choices=status)
    Expences = models.IntegerField(null=True)
    Profit = models.IntegerField(null=True)
    def __str__(self):
        return self.Name

# class TourConducted(models.Model):
#     Tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, null=True)
    
    

    
