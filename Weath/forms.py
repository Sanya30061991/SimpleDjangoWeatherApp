from .models import Req
from django.forms import ModelForm, TextInput

class ReqForm(ModelForm):
    class Meta:
        model = Req
        fields = ['r']
        widgets = {
            'r' : TextInput(attrs = 
            {
                'type':"text",
                'placeholder':"City, State Code, Country Code" ,
                'class':"form-control"
            })
        }