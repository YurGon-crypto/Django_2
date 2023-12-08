from django.urls import path
from .views import home, create_or_edit_note, delete_note

urlpatterns = [
    path('', home, name='home'),
    path('create_or_edit_note/', create_or_edit_note, name='create_or_edit_note'),
    path('delete/<int:note_id>/', delete_note, name='delete_note'),
]