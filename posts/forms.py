from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_text', 'post_image', 'chatroom')

    def clean_post_text(self):
        post_text = self.cleaned_data['post_text']
        '''
        validations go here
        '''
        return post_text
