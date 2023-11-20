##   overview 
 
Restaurant Booking system is a web-based application system written in django, SQLLite3, and python.

The system allows the user to create account before booking and then  book a table , view and cancel it.

It typically includes a website or mobile application for users to interact with, and a back-end 

administrative panel for restaurant owner's to manage bookings.

This website has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.

![Mock up](https://ui.dev/amiresponsive?url=https://restaurantbooking2023-4f0b057bd1a0.herokuapp.com/)

##   Features 
  
  - Admin panel features
     - User
         
	  - For the user, The admin can add, update, and delete user information
             and also the admin can change the password  of the user
          
     - Manage Booking    
          
	 - For  the booking, The admin can add, update, and delete booking information.
            
	 - Manage Table
         
         - For the table, The admin can add, update, and delete table information.
 
 - Existing site features

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/8d900519-e2ca-41e2-8e90-3c48a6516ab2)


   - Login
      
      - For the login, the user will login first before he/she can use the system.
      
   - Sign up    
      
      - For  the sign up, the user will sign up first before he/she can use to to login 
        in the system
 
  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/7fe5642e-7f64-426a-aa1b-985ae3fa8321)

  - Homepage
     
     - For the homepage, you will be able to all the basic access in the wholesystem.
     
     - such as home, book table, seebooking, menu list and login
  
  - About
     
     - For about, general information about the booking system.
  
   - Menu list       
 
     - For menu list, the user will be view the available menu.

  - Contact us
     
     - For contact, the user can leave feedback and ask questions 

  - Book a table
     
     - For book a table, the user will be able to book table .
  
  - My booking
     
     - For view booking a table, the user will be able to view the booking list.

##  How  the user make bookings
 
 - First of all they need to register the site
 
 - Second click the link Book a tale  nav element
 
 - Third fill out th form and then click make booking button
 
 - Finally,  they received confirmation
       

## Future Features
			
  - when there is time, I would like to add more functionality for example the user make booking 
     with small amount money depositions but the money is back  when the user come and enjoy in the restaurant.
			 
## DATA MODEL

- In this project I implemented function based views as Python objects.

- The logic patterns to create, read, update and delete model instances in a 
   standard view method.

- I consider a project name restaurant having an app name booking.

- After i have a project and an app, i create a model of which we will  creating instances 
  through our views. In booking/models.py the table presented below


![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/854ca722-e608-4ace-8c64-b17406c7f9ff)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/d9a2eb3e-1fc0-431b-bdad-61519c342827)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/33be3578-a521-4a97-bc73-330eb50725fc)



## Testing User Stories from User Experience (UX)

- From new user point of view 

    - Firstly, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice.
            Underneath there is a Hero Image with Text 

    - Secondly, the user can easily navigate throughout the site to find content. It has been designed with limited content
      so that the user can't enterapped.
    
    - Thirdly, the user has completed looking at Home, Menu, and contact us pages, they might decide to look register and login pages
      and then book a table.
    
    - Fifth, once the account has created and been directed to home page, they can click on the Book A table nav-link.

      This time they see bar section image of the restaurant with lovely wine glass seated attractive way and  Book a Table form

      with the following element.
   	
      - name - username as per what user is logged in as
        
	   - phome number - user phone number 
        
	   - number of persons - number of guest share  available table
        
	   - booking date and time

        Once user has completed and then  clicks on Making a booking  button, they are redirected to  a new  page. At the same time green tickmark

        including username  message appears on top the middle of the page: "your booking has confirmed now"

  	As we have seen the image below 

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/e7647213-a250-4529-bc4e-7ca71c3b20b5)


    - sixth, if user decide that they wish update or delete their booking, they must click on mybookings nav-link. The editing and deleting booking

      page will appear on the same page, the edit form like booking form.  As we have seen the image below 

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/59efd818-362e-43d9-98a1-186fa7f80e2e)

 
 - Once user clicks on Delete  booking  button, user sees the following popup message "Are you sure  you want delete this booking?"
         
   if the user clicks on the "cancel booking" button, they are stay the same  page and booking would remain but 
  
   user clicks on the "ok booking" button that particular booking details deleted permanently. As the image below


![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/59ce7afc-5bc8-4ee5-a18c-8a6512308980)


  - Finally, the user need sign out at the end of the session so that keep their account safe and secure.

- From  Admin point of view 
    
     - Firstly,  register  admin site and then login into the admin page
     
     - Secondly, able to create, view, edit and delete bookings.

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/97e875fd-96e6-4e35-9631-69b6b42865aa)


![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/bf85f482-586e-474f-878f-a6410056f26f)


![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/174f0ecf-fe4a-494d-a28b-8dd2e7f06518)


## Testing
   
   - I have mannually test this project by doing the following:-

     - below generate tested values screen shot  from my local and code institute Heroku terminal
      presented:-

       - by supplied 3 different user:- to check whether the user try to book or not
       
       - by checking each  user view their own booking or not

       - by checking form validation works properly or not

       - by checking if  once user book a table, it is expected seen in the admin site

 - Below i have checked form validation work as expected

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/fced3509-ed90-4ebc-8464-d6712dd5e67d)

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/afc82ede-582f-4030-ad46-49f7fddd8fbc)

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/f23b2e4f-7503-49c1-83b1-546a9f63173b)

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/77c8b599-7077-4b52-a26e-00c499a81f07)


 - Below i have checked user Degu book a table

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/4fecde62-8da5-44d6-92d1-b6d44788e39e)

 - Below i have checked user Degu edit booking

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/9441dbb9-111a-4fe2-b042-94d277fc16f8)

 - Below i have checked user Degu delete booking , popup there are two options if he click 'ok' delete or click 'cancel' booking remain
  
  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/f6f48a1a-1453-424f-9100-34110c4f78ad)

 - Below i have checked user Degu  after delete booking
 
 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/d61bd2ca-40a0-4f10-ab18-ea070784a806)

- Below i have checked user Tamiru book a table
 
 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/d10384d0-6f3f-4437-b6db-13f351c2c047)

- Below i have checked user Nesi book a table

 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/401e3cf6-73f0-4402-86f5-60d4dd3a3957)

- Below i have checked all the above three users booking expected seen in admin site

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/888791b8-cc26-4547-994b-4b4912a6e7cf)


## Validator Testing

  - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page for HTML and CSS of the project 
    to ensure there were no syntax errors in the project.

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/b0b41f7f-468f-4923-baff-163f58fd2197)

 - PEP8			
	  - No errors were returned from PEP8online.com
  
## Lighthouse Testing

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/1bf4caac-1ac1-4d14-a7a5-e3c3bb6dc295)

## Further Testing
  
  - The Website was tested on Google Chrome, Firefox, Microsoft Edge, safari and Internet Explorer browsers. The site renders fine in all browsers. 
 
  - The website was viewed on a variety of devices such as Desktop, Laptop, Samsung Galaxy A51 by using Google Developer Tools.

 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/ee4390cd-800e-4b5b-a689-196b9eb68d47)

 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/295ac63f-a430-4429-bb0a-ec3affad7219)

 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/5f0ff9b0-2a11-4807-8f29-3e5129887e81)

 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/e3220023-1506-4a82-8d3b-185ec0ed5f26)

 ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/1bdf4cd8-70a2-4213-9350-2a65020ad332)


  - It is responsive on all devices and all features work as expected.
  
  - A large amount of testing was done to ensure that a user can add, update and delete booking.


## Automated Testing

  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/73e8ff47-ed1e-45ba-9c09-3017c2bd60d6)


  ![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/20a4c732-cedb-450a-ade2-c1109f39e0c0)
   

## Bugs
 
  -  Remaining bugs

       - I am attempting to create a booking website where booking has been made for the currently logged in user name otherwise not
     
          When I tested, I found that logged in user can do booking by changing name but he/she couldnot not seen it their respective mybooking page 

           only I see it in admin site
      
      - I am running my code through HTML checker validation and it is coming back with a few errors which i don't know
     
           how to fix as the code has been django's template engine

##  Form validation

   - validation I could implement
      
      - make booking form
        
   - validation I couldn't implement

      - I intended to implement for name field just check if and only if booking allowed logged in user name, i tried as much as i couldn't
      
         due time shortage, I'm not pursuing a further solution at the moment. In the future I would like to add this issue.

## Testing after deployment by creating user helen
    
 -Add booking
	
![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/f3918138-6f94-442e-b795-b6e055dec7bc)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/055f625a-d6c2-4bf6-af8d-83ed25288807)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/6e0f3eea-1ea0-4e58-833c-3f919af46a7a)

 - Edit booking

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/f71441b4-bd7d-447b-8677-ef694a894806)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/79c045a4-7956-4b29-b975-75e6adc07fe5)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/0545adf9-9522-46b3-a73d-bee77875f45b)

- Delet booking

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/f35f641a-aaf9-4ddc-af3d-77d19d0a19ad)

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/73007a89-b413-42fc-abd4-e2d3380b4b5a)


- check validation work as expected or not if  the same user name and phone number

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/bc4f4c26-bbfd-45a7-bc04-b960bbb76fb4)

- check if user helen can book previous date and time or not

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/434e3d12-e3ad-4cd1-bd81-6472933c2f02)

- check if user helen can book number_of _person field equalt to zero  or not

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/92502647-ab74-44f4-b948-8b3e4622e080)

- check Contact section can respond messages to user or not

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/b2a94338-7aa8-421c-a763-8560891b4d08)


## Deployment

- The site was deployed to GitHub pages and Heroku terminal.
   
   	- steps for deployment

    - Step 1: Installing Django and supporting libraries
    
    - Step 2: Create a new external database

	  - Postgres database  was created in Elephant SQL using  my project name:- django_booking

    - Step 3: Create the Heroku app

         - A Heroku app was created in Heroku.  Mine is called restaurantbooking2023
     
    - Step 4: Attach the Database:

	   - In env.py
	
 		Import os library

		Set environment variables

	        Add in secret key
   	
    	 - In heroku.com

		Add Secret Key to Config Vars :- SECRET_KEY, “randomSecretKey”

    - Step 5: Prepare our environment and settings.py file:

      - In settings.py

                Reference env.py

		Remove the insecure secret key and replace  SECRET_KEY = os.environ.get('SECRET_KEY')

		Comment out the old DataBases Section and add new DATABASES Section

	  - In the Terminal

		Save all files and Make Migrations , python3 manage.py migrate

 	- Step 6: Get our static and media files stored on Cloudinary:

	   - In env.py:

		Add Cloudinary URL 

	   - In Heroku:

		Add Cloudinary URL to Heroku Config Vars*
 
		Add DISABLE_COLLECTSTATIC to Heroku Config Vars (temporary step for the moment, will be removed before deployment)

		 e.g. DISABLE_COLLECTSTATIC =1

	    - In settings.py:

		 Add Cloudinary Libraries to installed apps

		  Tell Django to use Cloudinary to store media and static file Place under the Static files Note

		  Link file to the templates directory in Heroku Place under the BASE_DIR line

                  Change the templates directory to TEMPLATES_DIR Place within the TEMPLATES array

	- step7: I added the Heroku name followed by herokuapp.com to the ALLOWED_HOSTS variable name in setting.py followed by

  		             a comma and 'localhost' ( to allow running in the IDE)

       - step8: In the IDE file explorer or terminal

		  create 3 new folders on top level directory media, static, templates

                  create a Procfile on the top level directory Procfile

	- step9: In Procfile

		 Add code  web: gunicorn restaurant.wsgi

	- step10: In the Terminal:

  	         Add, Commit and Push

 	- step11: In Heroku:

		  11.1: initial deployment stage disable collectstatic value and 1 key  assign
	
 	          11.2: At final stage only disable collectstatic with its value removed

		  11.3: At last Debug=False    in setting.py file

		  11.4: After that go Heroku dashboard page  then click deploymnet tab

		  11.5: just click Github then connect and confirm connect Github

		  11.6: scroll down the page click deploy branch and the app being built

		  11.7: Finally, we see deployement the app successful message and

			  click the view button to take a look

- The live link can be found here:- [Booking](https://restaurantbooking2023-4f0b057bd1a0.herokuapp.com/)

## Technology Used
   
   - python
   
   - HTML
   
   - CSS
   
   - Javascript

## Frameworks, Library and Program

1. python module

   - from django.shortcuts import render, redirect, get_object_or_404

   - from .models import Booking

   - from django import forms

   - from django.forms import  widgets

   - from django.core.exceptions import ValidationError

   - from django.core.validators import MinValueValidator

   - from django.utils import timezone

   - from phonenumber_field.modelfields import PhoneNumberField
 
   - from django.db import models

   - from django.contrib import admin

   - from .forms import BookingForm

   - from django.contrib import messages
  
   - from django.test import TestCase
  
3. jQuery

   - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript. 

   - It is also used for current date for in footer and find table.

5. Bootstrap 4

6. SQLite3 database:

   - SQLite3 is Django's default database system.

8. Font Awesome:

    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

10. Cloudinary:
   
   - I used cloudinary for cloud-based storage and partly for linking of my website images.

11. Git
   
   - used Git terminal to commit to Git and push to Git hub

11. GitHub

12. Heroku
   
   - store the project code after being pushed from Git

## Credits
   
   - Code

      - walk through project Hello Django and I think I can blog 
      
      - From online source I got some further information how to link url vs views
        [w3schools](https://www.w3schools.com/django/showdjango.php?filename=demo_master_index)

      - I have got more detaial explanation, for syntax, code expressions, code functionalities.

         [Django documentation](https://docs.djangoproject.com/en/4.2/topics/forms/)

	 [Django-phone-number](https://django-phonenumber-field.readthedocs.io/en/latest/)

	 [Django-validators](https://docs.djangoproject.com/en/4.2/ref/validators/)
     
      -  Hero image come from this  [site](https://familydestinationsguide.com/wp-content/uploads/2022/08/Heroes-Restaurant-and-Brewery.jpg)
      
      -  MDN web docs
   
- content
	   
    - Content comes from the Bootstrap template, I made slight changes to the prewritten content there. Food descriptions in Menu page come fully from the Burger seller web page .




