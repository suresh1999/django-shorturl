# Django URL Shortener




### Getting started with the url shortener

1. Download or pull the repository
2. Add the shorturl app and djangorestframework to your installed apps in django
	
    	INSTALLED_APPS = [
        	...
            
            'shorturl',
            'rest_framework'
        ]
    > Note : This app requires djangorestfrawork as it works only with it
3. Use ``` python manage.py makemigrations ``` to perform migrations
4. Use ```python manage.py migrate``` to save the migrations and store the table to the database.

### Using the shorturl app

1. Using the already defined urls.
	
    	app_name = "short_urls"
		urlpatterns = [
        path('shorturl/generate/', GenerateURL.as_view()),
        path('longurl/', CheckURL.as_view()),
        path('shorturls/generate/', GenerateURLS.as_view()),
        path('longurls/', CheckURLS.as_view())
    	]
   one can use the above urls to easily generate and get the long url for an given short url
   >Note : All the above urls are defined under the POST method only.
   
 	The data should be send through the post request as folows
   	
    	{
        	"long_url":"www.google.com/search/hello/"
        }
        
        Response
        {
        	"short_url":"www.goo.gl/43er21"
        }


2. Te View can also be linked with the custom url according to the need of the developer
			
            from shorturl.views import *
            from django.urls import path
            
            urlpatterns = [
            	path('/my/generate', GenerateURL.as_view()) # short url will be generated
            ]
            
            
 ##### This django package can be modified and used according to your needs even for production.
 
 #### Hope we will be make this package available in python universal package repository. We will also be coming up with some new updates.
