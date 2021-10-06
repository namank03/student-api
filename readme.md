# Student-management-in-django

Student Management system using Django REST Framework and SQLite

##

I implemented a student management system, using Django REST Framework (www.django-rest-framework.org) and SQLite, with the following functionality via RESTful endpoints:

- Get, adds, updates, and deletes students
- Get, adds, updates, and deletes teachers
- Get, adds, updates, and deletes classrooms
- Get, adds, updates, and deletes subjects
- Get students enrolled in a given class

- Get subjects a given student is enrolled in Filter/Search subject,student,class,teacher by name

Read (`GET`) actions are not restricted.

Write (`POST`, `PUT`, and `DELETE`) actions are authenticated.

**Authentication** and **permissions** is handled by SIMPLE_JWT

**Rate-limiting** is supported and configured by `REST_FRAMEWORK` in courses/settings.py.
It’s possible to configure **policies** in different ways:
https://www.django-rest-framework.org/api-guide/throttling.
