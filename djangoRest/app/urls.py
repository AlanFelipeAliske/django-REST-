from app.views import TodoListAndCreate, TodoDetailAndDelete
from django.urls import path

urlpatterns = [
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailAndDelete.as_view()),
]