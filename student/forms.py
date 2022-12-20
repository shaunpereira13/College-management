from django.forms import ModelForm
from .models import StudentModel,marksModel

class studentform(ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        

class marksform(ModelForm):
    class Meta:
        model=marksModel
        fields='__all__'