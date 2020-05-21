"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
# Using one_step.views allows us to skip email verification for now,
# but if you need to set it up, you can learn how to do that here:
# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # Path to custom version of registration view provided by django-registration
    # This is used to create new accounts via browser
    path('accounts/register/', RegistrationView.as_view(
        form_class=CustomUserForm,
        success_url='/',),
        name='django_registration_register'
    ),

    # Other urls used by the django-registration package
    path('accounts/', include('django_registration.backends.one_step.urls')),

    # The login urls provided by django to login via the browser
    path('accounts/', include('django.contrib.auth.urls')),

    # Pulls in urls.py from our users app
    path('api/', include('users.api.urls')),

    # Pulls in urls.py from questions.api
    path('api/', include('questions.api.urls')),

    # Login via browsable api
    path('api-auth/', include('rest_framework.urls')),

    # Login via rest
    path('api/rest-auth/', include('rest_auth.urls')),

    # Registration via rest
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    re_path(r'^.*$', IndexTemplateView.as_view(), name='entry-point')
]
