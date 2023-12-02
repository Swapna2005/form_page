from django.db import models

# class LoginModel(models.Model):
#     Username = models.CharField(max_length=256)
#     password = models.TextField( )
#     img = models.ImageField(upload_to='images/')
#     def __str__(self) -> str:
#         return self.name
    

# class  RegisterModel(models.Model):
#     Username = models.CharField(max_length=256)
#     password = models.TextField( )
#     img = models.ImageField(upload_to='images/')
#     def __str__(self) -> str:
#         return self.name
    

# class SignupModel(models.Model):
#     Email = models.EmailField(max_length=256)
#     Username = models.CharField(max_length=256)
#     Password = models.TextField()
# def __str__(self) -> str:
#     return self.name

class MovieModel(models.Model):
    title = models.CharField(max_length=50)
    year = models.TextField( )
    summary= models.CharField(max_length=256)
def __str__(self) -> str:
    return self.name

        