from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "name"       : "name",
            "class"      : "form-control",
            "placeholder": "Enter your name",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Enter your name'",
        }
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "name"       : "email",
            "class"      : "form-control",
            "placeholder": "Enter email address",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Enter email address'",
        }
    ))
    to = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "name"       : "to",
            "class"      : "form-control",
            "placeholder": "Enter email address",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Enter email address'",
        }
    ))
    comments = forms.CharField(required=False,
        widget=forms.Textarea(attrs={
            "name"       : "comments",
            "class"      : "form-control mb-10",
            "placeholder": "comments",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'comments'",
        }
    ))

class CommentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "name"        : "contact-form-name",
            "class"       : "form-control",
            "placeholder" : "Enter your name",
            "aria-invalid": "true",
        }
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "name"        : "contact-form-email",
            "class"       : "form-control",
            "placeholder" : "Enter email address",
            "aria-invalid": "true",
        }
    ))
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "name"        : "contact-form-message",
            "class"       : "text-area-messge form-control",
            "placeholder" : "Enter your comment",
            "aria-invalid": "false",
            "rows"        : "2",
        }
    ))
    class Meta:
        model  = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "id":"search_input",
            "name" : "query",
            "placeholder":"Search Here",
        }
    ))

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "name"       : "name",
            "class"      : "common-input mb-20 form-control",
            "placeholder": "Enter your name",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Enter your name'",
        }
    ))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "name"       : "email",
            "class"      : "common-input mb-20 form-control",
            "placeholder": "Enter email address",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Enter email address'",
        }
    ))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={
            "name"       : "subject",
            "class"      : "common-input mb-20 form-control",
            "placeholder": "Enter your subject",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Enter your subject'",
        }
    ))
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "name"       : "message",
            "class"      : "common-textarea form-control",
            "placeholder": "Messege",
            "onfocus"    : "this.placeholder = ''",
            "onblur"     : "this.placeholder = 'Messege'",
        }
    ))
