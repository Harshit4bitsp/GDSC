from django.urls import path
import home.views as views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('add_note/', views.add_note, name='add'),
    path('delete_note/<int:note_id>', views.delete_note, name='delete'),
    path('edit_note/<int:note_id>', views.edit_note, name='edit'),
    path('search/', views.search_tags, name='search')
]
