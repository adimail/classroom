---
layout: default
title: Building Django apps with MLFlow
parent: Machine Learning
---

# Building Django apps with MLFlow and PGAdmin

Notes for building an basic application with Django as a backend and PGAdmin for database. Django is popular miccroservice framework used to build scalable applications. Following are instructions for creating an Django app and comfiguting templates, migrations and models and connecting them with PostgreSQL using psycopg2.

Below is a minimal step‐by‐step guide with commands and code snippets to build a Django app that:

- Uses PostgreSQL (which you can manage via PGAdmin) with the `psycopg2-binary` driver.
- Includes a basic view with a form for data submission.
- Optionally integrates MLFlow (installed separately) for experiment tracking.

You can copy the following content into a Markdown file (e.g., `building_django_apps_with_mlflow.md`) that already contains your YAML front matter.

---

## Building Django apps with MLFlow and PGAdmin

Below are the bare minimum instructions to set up a Django application connected to PostgreSQL, create a simple form view, and run migrations and the development server.

---

## 1. Set Up Your Environment

Create a virtual environment and install Django, psycopg2 (for PostgreSQL), and MLFlow:

```bash
python3 -m venv env
source env/bin/activate   # On Windows: .\Scripts\activate
pip install django psycopg2-binary mlflow
```

---

## 2. Create a New Django Project and App

Create a new project (e.g., `mlops`) and an app (e.g., `core`):

```bash
django-admin startproject mlops
cd mlops
python manage.py startapp core
```

---

## 3. Configure the PostgreSQL Database

Edit `mlops/settings.py` to add your app and configure the PostgreSQL database connection:

```python
# mlops/settings.py

INSTALLED_APPS = [
    # Default apps...
    'core',  # Add your app here
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydatabase',         # Replace with your database name
        'USER': 'myuser',             # Replace with your PostgreSQL username
        'PASSWORD': 'mypassword',     # Replace with your PostgreSQL password
        'HOST': 'localhost',          # Use your host (or 'localhost' if local)
        'PORT': '5432',
    }
}
```

*Note:* Use PGAdmin or psql to create the PostgreSQL database (`mydatabase`) if it doesn't already exist.

---

## 4. Create a Simple Model

Define a basic model in `models.py` (e.g., a model to hold form data):

```python
# models.py
from django.db import models

class USER(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    bmi = models.FloatField()
    children = models.IntegerField()
    smoker = models.IntegerField()
    region = models.IntegerField()
    charges = models.FloatField()
```

---

## 5. Create a View for Form Submission

Create a view that renders a form and processes POST submissions in `views.py`:

```python
# views.py
from django.shortcuts import render, redirect
from .models import USER

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        USER.objects.create(name=name, description=description)
        return redirect('form')
    return render(request, 'form.html')
```

---

## 6. Set Up URLs

Create a URL configuration for the `core` app.

1. **Create `urls.py`:**

    ```python
    # urls.py
    from django.urls import path
    from .views import submit_form

    urlpatterns = [
        path('form/', submit_form, name='form'),
    ]
    ```

2. **Include the app's URLs in the main project URL configuration (`mlops/urls.py`):**

    ```python
    # mlops/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('result/', views.result, name='result')
        path('admin/', admin.site.urls),
    ]
    ```

---

## 7. Create the HTML Template

Create the template for the form:

1. **Make the template directory:**

    ```bash
    mkdir -p templates
    ```

2. **Create `templates/form.html`:**

    ```html
    <!-- templates/form.html -->
    <!DOCTYPE html>
    <html>
    <head>
        <title>Submit Form</title>
    </head>
    <body>
        <h1>Submit Form</h1>
        <form method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br><br>
            <label for="description">Description:</label><br>
            <textarea id="description" name="description"></textarea><br><br>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    ```

---

## 8. Migrate and Create the Database Tables

Run the following commands to create migrations and update your database:

```bash
python manage.py makemigrations
python manage.py migrate
```

*Note:* Ensure your PostgreSQL database (`mydatabase`) exists. Use PGAdmin to create it if necessary.

---

## 9. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Now, open your browser and navigate to [http://127.0.0.1:8000/form/](http://127.0.0.1:8000/form/) to view and submit the form.

---

## 10. (Optional) Run MLFlow for Experiment Tracking

If you wish to use MLFlow alongside your Django app, simply start the MLFlow UI by running:

```bash
mlflow ui
```
