from django import forms
from .models import Notes,Todo,Homework

class Date(forms.DateInput):
    input_type = 'date'
class Note_Form(forms.ModelForm):
    class Meta:
        model = Notes
        widgets = {'created_at': Date()}
        fields = ('title','author', 'description', 'created_at')


class Todo_form(forms.ModelForm):
    class Meta:
        model = Todo
        widgets = {'due_date': Date()}
        fields = ('title', 'due_date', 'status')


class homework_Form(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due_date':Date()}
        fields = ('subject', 'title','description', 'due_date','status')
        


class Books(forms.Form):
    search = forms.CharField(max_length=100, label='Search:')
# sign up


class Register(forms.Form):
    username =forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()

# login form
class Login_Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    
#reset password form
class Reset_Pass(forms.Form):
    Former_username = forms.CharField()
    new_password = forms.CharField()
    confirm_pass = forms.CharField()
