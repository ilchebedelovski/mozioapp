Mozio Google Maps API

About the Project
I usually work with Linux and I do not have a habit to use Windows products that much, but this project is created in VisualStudio because they offer a Virtual Machine where I can build and run my application, and that was the fastest way for me to create this project.
I do not have any running Linux server where I can deploy the application and I can only push my files to Github where you can see the code.
I am using Django 1.8 and maybe some of the files are part of the Virtual Machine or some different files that are out of scope of the project, I am providing a list of modified files into the framework:
- mozioapp/app/models.py
- mozioapp/app/views.py
- mozioapp/MozioProject/settings.py
- mozioapp/MozioProject/urls.py
- mozioapp/app/templates/app/firstpage.html
- mozioapp/app/templates/app/secondpage.html

Application Overview

The first page is a home page and there you will see a google map with random center, and above the map there are few html elements: 
- input field - In this field the client's name can be stored.
- clear button - For removing all markers and pointers from the map.
- submit button - Submit button for saving the data in the backend, after saving the data the map is empty againsssss
- go to seccond page. - For accessing the second page.

On the second page, there aren't that much functionality, you can only see your service area marked with polygon and by clicking inside the service area there is a info window where you can see exact details or coordinates on the clicked point.

Steps for using the application:
- Draw your service area on the first page
- Click submit for saving the data or clear for cleaning the map if you want to draw another service area
- Click on the button "Go to the second page" where you can see the last saved area in polygon view and there you can check if some of specific region is included in the service area or not and you will see info window with the coordinates for points inside the service area.