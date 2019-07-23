from django import forms
from crispy_forms.helper import FormHelper

from Blog.models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):
    #crisy form area
    helper = FormHelper()
    helper.form_show_labels = False

    # this is the form used to create a blog post.
    # it is a model form so there are no fields declared
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'image',
            'content',
        ]


class CommentForm(forms.ModelForm):
    # this is the form used to create a comment.
    # it is a model form so there are no fields declared
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
