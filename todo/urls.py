from django.urls import path
from .views import TodoGetCreate, TodoUpdateDelete,TodoDeleteView,TodoEditView, TodoDetailView
from todo import views
urlpatterns = [
    path('', views.index, name='todo-index'),
    path('create',views.create, name='todo-create'),
    path(r'done/<int:pk>', views.isDone, name='todo-done'),
    path(r'delete/<int:pk>', TodoDeleteView.as_view(), name='todo-delete'),
    path(r'edit/<int:pk>', TodoEditView.as_view(), name='todo-edit'),
    path(r'detail/<int:pk>', TodoDetailView.as_view(), name='todo-detail'),
    path('api/create',TodoGetCreate.as_view()),
    path(r'<int:pk>', TodoUpdateDelete.as_view()),
]