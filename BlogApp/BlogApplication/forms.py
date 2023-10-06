from django import forms
from . models import *


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','category']
    
    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)

        # Add the 'form-control' class to the widgets of specific fields
        self.fields['title'].widget.attrs['class'] = 'form-control my-2'
        self.fields['content'].widget.attrs['class'] = 'form-control my-2'
        self.fields['category'].widget.attrs['class'] = 'form-control my-2'

class BlogCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogCategory
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(BlogCategoryForm, self).__init__(*args, **kwargs)

        # Add the 'form-control' class to the widgets of specific fields
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        # Add the 'form-control' class to the widgets of specific fields
        self.fields['name'].widget.attrs['class'] = 'form-control'