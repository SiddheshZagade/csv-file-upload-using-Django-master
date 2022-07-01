from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import upload_file_view
 
app_name='csvs'
app_name='migrations'

urlpatterns = [
    path('', upload_file_view, name='upload-view'),
]