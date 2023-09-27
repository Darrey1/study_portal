from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('delete_note/<str:pk>', views.delete_note, name='delete_note'),
    path('note_del_confr/<str:pk>', views.note_del_confr, name='note_del_confr'),
    path('edit_note/<str:pk>', views.edit_note, name="edit_note"),
    path('create_note', views.create_note, name='create_note'),
    path('note_details/<str:pk>', views.note_details, name='note_details'),
    # todo
    path('todo', views.todo, name='todo'),
    path('create_todo', views.create_todo, name='create_todo'),
    path('update_status/<str:pk>', views.update_status, name='update_status'),
    path('delete_todo/<str:pk>',views.delete_todo, name='delete_todo'),
    path('delete_conf/<str:pk>', views.delete_conf, name='delete_conf'),
    path('edit_todo/<str:pk>', views.edit_todo, name='edit_todo'),
    #homework
    path('homework', views.homework, name='homework'),
    path('create_homework', views.create_homework, name='create_homework'),
    path('update_homework/<str:pk>', views.update_homework, name='update_homework'),
    path('delete_homework/<str:pk>', views.delete_homework, name='delete_homework'),
    path('homework_conf/<str:pk>', views.homework_conf, name='homework_conf'),
    path('homework_details/<str:pk>', views.homework_details, name='homework_details'),
    # youtube
    path('youtube', views.youtube, name='youtube'),
    
    #books
    path('books', views.books, name='books'),
    #dictionary
    path('dictionary', views.dictionary, name='dictionary'),
    path('wikipedia', views.wiki, name='wikipedia'),
    path('conversion', views.conversion, name='conversion'),
    #register
    path('register', views.registration, name='register'),
    #sign in
    path('login', views.login_,name='login'),
    #logout
    path('logout',views.user_logout, name='logout'),
    path('confirm_logout', views.confirm_logout, name='confirm_logout'),
    #reset password
    path('reset_password', views.reset_password, name='reset_password'),
]
