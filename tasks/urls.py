# Creamos todas las urls o rutas de acceso relacionadas con las tareas (tasks)

# Primero importamos el metodo path que nos va a permitir definir las rutas de acceso
from django.urls import path
from .views import list_tasks, create_task  # Importamos list_tasks desde views que esta en la misma carpeta, para utilizarla en la lista, con la funcion path 
from django.conf.urls import include
from . import views
# Creamos una lista con las rutas o urls que vamos a utilizar
# Luego utilizamos la funcion path, donde sus parametros seran el nombre que le colocamos y la ruta que va a ejecutar, para cada ruta que incluiremos en esta lista

urlpatterns =[
    #Dejamos el string en blanco para acceda a la ruta directamente 
    path('', views.list_tasks),
     
    path('new/', views.create_task, name='create_task'), # En este caso accederemos a la lista de tareas del programa, que sera la ruta inicial del programa
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),


]


