"""dejango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

## https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK


"""
To create a new app like I have here called music, using cmd go to the project directory, 
and use python manage.py startapp music (change app name after startapp to whatever you want )

handy tip for getting to the location you want using cmd without have to ude dir and navigate is to 

Navigate to the folder in Windows Explorer, highlight the complete folder path in the top pane and type "cmd" - voila!

"""



from django.contrib import admin
from django.urls import include, path # Added include to refer music\urls.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]



































