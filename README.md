# Blog Redesign
You have a very simple Blog Application written in Django. PyCharm was the IDE used but you can use whatever editor you want, you are using JavaScript, .

This is a functioning blog system with 4 templates you will restyle (view.html, create.html, create_comment.html, and edit.html)

Interface and Forms should be styled to look like a production application, we need a designer for this position.

## Specific Features:
- Choose a nice design for the interface and implement it, styling is important here.
- JavaScript Pagination of Blog Posts
- Truncation of Comments so they don't overtake the screen (allow comments to be made visible again as well, think of a blog, you can view all comments but they don't take up the whole page)
- Forms need JavaScript Form Validation for empty fields, and legnth of content input less than 5 characters
- Alter the navigation to work however you need
- JavaScript Modals for successful submission of posts, comments, and deletions
- JavaScript image slider on the "View Posts" page with overlaying text stating the current time with counting seconds, and the total number of posts submitted

## Django Information:
#### If setting up for the first time:
Install the requirements like so with the terminal from the directory with requirements.txt file in it:

```pip3 install -r requirements.txt```

Now run migrations to update the database:

```python manage.py migrate```

#### Run the server to view the site:
Now to run the server enter this command, then go to 127.0.0.1:8000 in your browser:

```python manage.py runserver 127.0.0.1:8000```


You will be working with Django here but **you do not have to mess with the base framework, we want styling of pages and forms, along with standard JavaScript features**. You will have to use `crispy-forms` or `widget-tweaks` in Django's template tags to style the forms, but how to do that is shown below:

```
{% for field in form %}
      <div class="form-group">
        <label>{{ field.label }}</label>
         # here, this is where you add classes to fields
        {{ field|add_class:'form-control' }} # like: |add_class:'[your_class_name]'
        {% for error in field.errors %}
          <span class="help-block">{{ error }}</span>
        {% endfor %}
      </div>
    {% endfor %}
```

If you want to go over some starters in the documentation as you being looking at the files, they are listed below, but remember we only need you to design the way this looks and implement the features listed above, do not waste time looking at the framework, (unless you want to).

**Django Docs:** 

https://docs.djangoproject.com/en/2.2/

**Polls App (Starter Django App):**  

https://docs.djangoproject.com/en/2.2/intro/tutorial01/

We have already added `crispy-forms` and `django-widget-tweaks` to the project and they are loaded to each page so simply look up the documentation and implement them if you wish. Alternatively it is fine to implement a different pakckage if you feel the need or want to experiment, but a nice design is what is wanted. Here is the documentation for both packages:

**Crsipy-Forms:** 

https://django-crispy-forms.readthedocs.io/en/latest/index.html

**Django-Widget-Tweaks:** 

https://github.com/jazzband/django-widget-tweaks

Use any custom JQuery or CSS, or JQuery Packages/CSS frameworks you want to accomplish the task at hand. JQuery is already loaded in the base.html template

