from django.urls import incude, path
import views

urlpatterns = [
    path('' views.news, name='news'),
]