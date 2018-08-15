from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.

class CreateNewComment(forms.Form):
    #The only thing I need to render in this form is the content box to allow users to enter a comment, the blog and the
    #user commenting I will get from the page directing to the commenting area(the blog itself) and the user I will get 
    #from request.user
    content = forms.CharField(max_length=700, help_text="Please type your comment here")

    def clean_content(self):
        data = self.cleaned_data['content']
        
        return data