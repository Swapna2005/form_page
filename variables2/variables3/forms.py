from django import forms
from .models import MovieModel

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = SignupModel
#         fields = [
#             "Email",
#             "Username",
#             "Password",
#         ]
        
class MovieForm(forms.ModelForm):
    class Meta:
        model = MovieModel
        fields = [
            "title",
            "year",
            "summary",
        ]