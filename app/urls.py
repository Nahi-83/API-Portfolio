from django.urls import path

from .views import ProjectView

urlpatterns=[

path('projects/', ProjectView.as_view()),
path('projects/<int:id>/', ProjectView.as_view()),

]