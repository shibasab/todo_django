from django import forms
from django.forms.widgets import NumberInput
from .models import Post
import bootstrap_datepicker_plus as datetimepicker

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'detail', 'deadline', 'achievement')
        widgets = {
            'deadline': datetimepicker.DatePickerInput(
                #format='%Y/%m/%d',
                #attrs={'readonly': 'true'},
                options={
                    'format':'YYYY/MM/DD',
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY/MM/DD',
                    'showClose': True,
                    'showClear': True,
                    'showTodayButton': True,

                }
            ),
            'achievement': NumberInput(
                attrs={
                    'type':'range',
                    'step':'1', 
                    'min':'0', 
                    'max':'100',
                    'class': 'form-control', 
                }
            ),
        }