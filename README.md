# Django-Angular-Blog
Tutorial on django2 backend and angular6 frontend blog webapp and delpoying on heroku

**This Repository contains Django as backend and Angular as frontend together in a blog web application including a custom django user model and serving the angular directly from django views and finally deploying the project to [Heroku](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwjvmr6qsa3eAhUJ148KHSN2D-MQFjAAegQIARAC&url=https%3A%2F%2Fwww.heroku.com%2F&usg=AOvVaw1V4lhSv6mb_lZj6UUCUXpS)**

## Initial Setup

1. Create virtualenv by directly installing the packages using [pipenv](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=2ahUKEwj8s_GIsK3eAhXDRY8KHRBnDrUQFjAAegQIBxAB&url=https%3A%2F%2Fpipenv.readthedocs.io%2F&usg=AOvVaw05wG9pN4CIwQzTMOYs-vQ2)
	```
	pipenv install django djangorestframework djangorestframework-jwt python-decouple
	```

2. Activate the virtualenv using **(run the next commands in activated virtualenv)**
	```
	pipenv shell
	```

3. Start django Project
	```
	django-admin startproject backend .
	```
	**trailing dot at end tell django to create files in the current folder**

4. Create apps for django
	```
	python manage.py startapp accounts
	python manage.py startapp blogs
	```

5. Add apps in **backend/settings.py** ```INSTALLED_APPS``` list
	
```
INSTALLED_APPS = [	
    # django apps
    'accounts',
    'blogs',
    # django packages
    'rest_framework',
]
```

Configure django rest framework and rest framework JWT authentication by adding 

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```

6. I assume that you have NodeJS and Angular CLI already installed on your local machine
	```
	```
