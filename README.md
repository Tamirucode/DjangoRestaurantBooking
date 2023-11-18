##   overview 
 
Table Reservation system is a web-based application system written in django, SQLLite3, and python.

The system allows the user to create account before booking and then  book a table , view and cancel it.

It typically includes a website or mobile application for users to interact with, and a back-end 

administrative panel for restaurant owner's to manage bookings.

This website has been designed to be fully responsive on desktop, laptop, tablet and mobile devices.


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


![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/2b495698-3dad-4aa0-8d80-fa6b6364aefb)


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

- Below i have checked all the above three users expected seen in admin site

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/888791b8-cc26-4547-994b-4b4912a6e7cf)


## Validator Testing

  - The W3C Markup Validator and W3C CSS Validator Services were used to validate every page for HTML and CSS of the project 
    to ensure there were no syntax errors in the project.

![image](https://github.com/Tamirucode/DjangoRestaurantBooking/assets/116649197/b0b41f7f-468f-4923-baff-163f58fd2197)

 - PEP8			
	  - No errors were returned from PEP8online.com



