# Embarr Equestrian Donations


## Overview

[Embarr Equestrian Donations](https://embarr-donations.herokuapp.com/) This project is a Full Stack website built using the Django framework and deployed using Heroku. It is a site for the promotion of a retirement home for senior Horses with the goal to raise money for the care of the horses that reside there. The site is a full stack ecommerce platform , where the user can submit online donations and pay using stripe. the site also follows and displays the CRUD logic, Users can Create (Submit a Comment on a blog post), Retrieve (Search for an Animal to donate to.), Update (Update their blog comments/ Profile) and Delete (Delete their comments). The site was designed with the mobile first approach so it is fully functional across all mobile devices aswell as desktops. Enjoy !!


## The Site Mockup

<img src=media/Readme/Mock_up.jpg>


## UX

Goals:

* To attract new donations, 
* Highlight the benefits of what the charity has to offer, 
* Provide useful information on the care of the senior horse,
* Provide a great user experience on all mobile devices,
* Be easy to navigate
* Give clear calls to action
* Build the brand image
* Raise the conversion rate.
* Promote the welfare of Horses.

As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View a list of Horses in the catalog.
3. Search for an animal via the search bar tool.
4. Add an animal to my cart annonymously to pay a donation.
5. Click on a blog post to read more.
6. View & Read the comments posted on a blogpost.
7. Read about Embarr Donations on the about page.
8. Submit a welfare concern via the about page.
9. Sign up for the newsletter.
10. Navigate to the charitys facebook page
11. Register as an account user.

As logged in website user, I can:

1. Register/Log in as a user.
2. View a catalog of horses that need donations for their care.
3. Select a horse to donate to and submit an online payment.
4. Search for and read blog posts.
5. Comment on blog posts.
6. Edit/Delete my previous blog comments.
7. Manage my profile by updating my details.
8. View a list of my donations.
9. Logout from the website.

As a website superuser, I can:

1. Add/ delete horses to/from the catalog & update their details.
2. Create/ update/delete blog posts
2. Create draft blog posts that can be reviewed and published at a later date.
3. Create a new user.
4. Delete user and comment.
5. Approve user's comments.


## Agile Methodology

This project was managed using the Agile method. All user stories were captured and updated using Githubs Project functionality and can be reviewed [Here](https://github.com/users/chellej80/projects/8).
A list of the issues captured and progressed can be viewed [Here](https://github.com/chellej80/Embarr-Equestrian-Donations/issues)


## Database Entity Diagram

<img src=media/DB_ER.jpg>

## Marketing

The site is B2C focused - I asked the following questrions:

- What are your site users requirements?

  To support and give to a charity they feel is deserving

- What information and features can you provide to meet those needs?

  A clear display of the horses that require support and donations

- How can you make the information easy to understand?

  Intuitive and clear design, high quality clear images, clear and descriptive titles, simple payment process, simple signup/login/logout process.

- Would there be other pages within your own site you could link to from your chosen page?

  Home page, nav bar, custom product pages would also link back to primary shop page. Error pages also link back to shop page.

- Are there opportunities to link back to external websites that already rank highly on Google?

  There would be opportunities to link up to other animal welfare sites.

- Who are your users? 
  Equine enthusiasts, animal lovers.

Marketing Strategies:

 - Facebook page - I created a facebook page to engage with a far reaching audience and attract follows. - [Click Here](https://www.facebook.com/EmbarrEquineTherapy/)
 - Newsletter sign up - A site user can sign up for a monthly newsletter (Please note this function is not fully live - it requires further development - for now it is just an empty form on the site)
 - There is potential to promote open days, or encouraging people to volunteer and help on the farm - this is mentioned in the About us section.
 
<img src=media/Readme/Facebook.jpg> 


## SEO

SEO implementation, including:
- A robots.txt file
- A sitemap.xml file
- Descriptive meta tags
- rel attributes on links to external resources
- Content
- Keywords in the metatags: "Horses, Ponies, Mares, Geldings, Retired, Charity, Donations, Equestrian, Rescue, Animals"


## Site Features 

- __Home Page__

Home page has the hero image and the Donate option prominently displayed. The navigation and search options are also available as well as the shopping cart icon.

 <img src=media/Readme/heroimage.jpg>

- __Navigation Bar__

  Featured on all pages, the full responsive navigation bar includes links to the Home page and all sub pages - About, Blog, Horses, the shopping cart and User Account, it is identical in structure for each page to allow for easy navigation. When the user logs in,the signin/up link is replaced with the logout link. The navigation items are styled to transition to a hamburger menu when the site is reduced in size on a mobile device. This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

  <img src=media/Readme/nav-bar.jpg>

  <img src=media/Readme/nav_mobile.jpg>


- __Logo__

    The logo I created simply using a combination of text and a font awsome icon. The logo is a hyperlink that takes the user to the homepage.

    <img src=media/Readme/logo.jpg>
  

- __Register Page__

    The User register page was created using the out of the box option from Django Auth. Further styling of this page is required but currently out of scope for the timeframe of this project.

    <img src=media/Readme/signup.jpg>

    

- __Login Page & Logout__

    The User login/ logout pages were created using the out of the box option from Django Auth. Further styling of this page is required but currently out of scope for the timeframe of this project.

    <img src=media/Readme/signout.jpg>



- __Profile Page__

  The User pofile page can be accessed by clicking on the Account Icon in the navigation bar, once they are logged in. the user can update their personal details here and view their donations history. There is room to expand the functionality of this page, for example, allow the user to upload a profile picture or add a bio section, but this was out of scope for this project. Further styling of this page is required but currently out of scope for the timeframe of this project.

  <img src=media/Readme/profile.jpg>

  

- __Search Bar__

    The search bar allows a user to search for a Animal in the catalog they would like to donate to/ read about and/or comment on. The search is crude and requires some futher development as it is not functional across the entire site, but this was out of scope for this project due to time constraints.

    <img src=media/Readme/search.jpg>

- __Blog__

  On the bolg page the site user can click on a blog post to to see more detail, or click though the page navigation (pagination is actioned once 8 posts are displayed. to see further blog posts.

<img src=media/Readme/blog_view.jpg>
   
- __Blog Detail Pages__

  The blog detail page(s) are accessed by clicking on the high level view of a blog post. This takes the user to a full page view of the service, that expands on the details, allows the user to read the blogs posted, or if logged in as a registered user they can submit a comment, or delete/ update their comment, they can not eidt delete any other users comments.

  <img src=media/Readme/blog_detail.jpg>


- __Submit Comment__

  The submit comment option is accessed via the blog detail page and is only available for logged in registered users, otherwise this option is hidden. Logged in users can select 'Submit a Comment', a comment form appears, once populated and submitted, a message will display informing the user that their comment has been submitted for approval. An admin must approve the comment before it will display.

<img src=media/Readme/comment.jpg>

<img src=media/Readme/approval.jpg>
  
__Update/ Delete Comment__

  The Update/delete comment option is accessed via the blog detail page and is only available for logged in registered users, otherwise this option is hidden. Logged in users can update/ delete reviews they have posted. They cannot update/ delete other users review. On selection of 'Edit' the user will be presented with a form to edit and submit. On submission the user will receive message feedback to say their message has been updated. If the user selects to 'delete' by clicking on the trash can icon, the user will be asked if they are sure they want to delete, and once selected it will update them their message has been deleted.

  <img src=media/Readme/comment_logged_in.jpg>


__About Us Page__

This page displays Embarr Donations Mission statement. It also provides an annonymous welfare concern form for a site user to report animal welfare cases with revealing their identity. On the page in the footer the site user can also sign up for the monthly newsletter that is handled by mailchimp and see contact details and links to the facebook page and instagram.

<img src=media/Readme/about.jpg>

<img src=media/Readme/footer.jpg>

<img src=media/Readme/contact_submit.jpg>

__Animal Catalog__

The Horses link in the nav bar takes the user to the catalog of horses that are in the care of Embarr Equestrian. The site user can select a horse by clicking on the image. They can read further detail about that horse and opt to make a donation.

<img src=media/Readme/catalog.jpg>


__Create, Update/ Delete Animal__

As a logged in superuser crud functionality is available via the account option by navigating to Animal Management, here the superuser can add/ update an animal in the catalog. The options to edit/ delete an animal in the catalog are also available to the superuser.

<img src=media/Animal_mgt.JPG>

<img src=media/Animal_mgt_add.JPG>

<img src=media/Animal_mgt_delete.JPG>

<img src=media/Animal_mgt_edit.JPG>


__Shopping Cart__

Once a site user selects a horse in the catalog they are brought to the shopping cart page where they add their donation to the cart. They also have the option here can to increase their donation amount by quantities/ remove/update the cart.

<img src=media/Readme/cart.jpg>

__Checkout__

After adding donations to the cart, the user can select 'secure checkout' and they are brought to the checkout page. Here they fill in all their billing details before adding their card details and clicking on complete payment. Payments are handled by 'Stripe'. Users can checkout annonymously and/ or if registered, their orders will be recorded and available as an Order list under their profile.

<img src=media/Readme/checkout.jpg>

<img src=media/Readme/payment.jpg>

__Checkout Success__

Once payment is successful the site user is brought to the success page and an order confirmation is sent via email. This email confirmation is actioned by a scucessful payment intent webhook from stripe.

<img src=media/Readme/pay_confirm.jpg>

<img src=media/Readme/email_Order_confirm.JPG>

__User Profile__

If a user has registered and logged into the site. They can navigate to their account profile via the nav bar. In this view, they can update their personal details and view a list of their donations.

<img src=media/Readme/profile.jpg>

__404 Page__

<img src=media/404.jpg>

### Features Left to Implement and items for further development

- Approval authentication of updated comments (This was out of scope)
- Update Animal Catalog with Donation Target Details and Amount raised to date detail.
- Bespoke forms for the out of the box Django Auth pages - Login/ Logout/ Register and comment forms.
- Improved search functionality
- Add bio/ profile picture to profile
- Improvements of the toasts messaging.
- Improve the CSS/ Images, overall frontend design.
- Add cookie consent and privacy statement.
- Further SEO improvements e.g sitemap google registration.
- Wishlist/ favourites.
- 500 page etc..
    
# Frameworks & Languages Used
- HTML
- CSS
- JavaScript
- Django
- Python

Python Packages:

- Gunicorn - As the server for Heroku
- Cloudinary - Was used to host the static files and media
- Dj_database_url - To parse the database URL from the environment variables in Heroku
- Psycopg2 - As an adaptor for Python and PostgreSQL databases
- Allauth - For authentication, registration, account management
- Crispy Forms -To style the forms
- django coniutries
- Pillow to process and save all the images downloaded through the database

### Frameworks, Libraries and technologies used

- [Git/ Github](https://github.com/) - Git/Github was used for version control, storage and deployment of the project.
- [Heroku](https://www.heroku.com/) - Heroku was used to deploy and create the terminal application.
- [Am I Responsive](https://amiresponsive.co.uk/ ) - This was used for the mockup image in the overview and assist with the       responsiveness testing.
- [Bootstrap](https://getbootstrap.com/) - This was used to style the website, add responsiveness and interactivity
- [PostgreSQL](https://www.postgresql.org/) - Database used through heroku.
- [Lucidchart](https://lucid.app/) - Lucidchart was used to create the database diagram
- [PEP8](http://pep8online.com/) - PEP8 was used to validate all the Python code
- [W3C - HTML](https://validator.w3.org/) - W3C- HTML was used to validate all the HTML code
- [W3C - CSS](https://jigsaw.w3.org/css-validator/) - W3C - CSS was used to validate the CSS code
- [Fontawesome](https://fontawesome.com/) - To add icons to the website
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - To check App responsiveness and debugging
- [aws](https://aws.amazon.com/) - was used to host the static files and media
- [Stripe](https://stripe.com/ie) for processing all online and credit card purchases on the website & for handling the webhooks.


# Testing Conducted 


## Navigation

### Navigation Bar

Test 1

All Navigation bar links are clickable and return the expected pages.

Test Steps:

Click on each nav link in the nav bar, and navigate between all pages using the nav links. Checking that each link brings the user to the correct page.



Test 2

Navigation Bar is responsive and transforms to a Hamburger menu

Test Steps:

Use developer tools to inspect and test the responsiveness and click on all nav links, navigating between all linked pages.

Results:

Transforms to Hamburger menu as expected and links to all correct pages as tested in test 1.

Navbar Expected Results  | Pass y/n
------------- | ------------- 
Login - links to sign in page  | Y
Register - links to register page | Y
Home - brings user to home page  | Y
Embarr Equestrian links to home  | Y
Logout links to sign out page | Y
Username appears in profile when logged in | Y
Login link reappears when logged out | Y
Messages appear as expected when successful login/ logout | Y


Hamburger Navbar Expected Results  | Pass y/n
------------- | ------------- 
Login - links to sign in page | Y
Register - links to register page | Y
Home - brings user to home page | Y
Embarr Equestrian links to home | Y
Logout Link appears when logged in | Y
Logout links to sign out page | Y
Username appears when logged in | Y
Username links to User Profile Page | Y
Login link reappears when logged out | Y
Messages appear as expected when successful login/ logout | Y

<img src=media/Nav_response.JPG>

<img src=media/Nav_response2.JPG>

### Page Navigation

Test 1

Test Steps:

Click on page navigation links in the nav bar


Expected Results  | Pass y/n
------------- | ------------- 
All Links working | Y


## Search Bar

Test 1

Enter text into the search bar to check for return of results
Test Steps:

Enter text into search bar that will return a positive result
For example – Horse, Pony

Test 2

After entering text in the search box click on search magnifier to return a result
After entering text in the search box hit return to return a result

Test 3

Confirm that the link returned from a positive result links to the correct page
Confirm that the page displayed from a negative result return is displaying correctly

Expected Results  | Pass y/n
------------- | -------------
Search returns a positive result | Y
Search link returned links to correct result | Y
Search returns a negative result - page displays as expected | Y
Hitting return after entering text returns the result page | Y
Clicking the search magnifier returns the result page | Y

<img src=media/search.JPG>

## User Registration

Test 1 -Register

Test steps:

Click on register, sign up page displays, populate fields and submit

Test 2 - Email Confirmation

Test steps:

On registering the user is asked to verify their email before they can sign in.

Click on register, sign up page displays, populate fields and submit

<img src=media/Register.JPG>

<img src=media/Readme/Confirm_email2.JPG>

<img src=media/Readme/email_confirm.jpg>

Test 3 – Login

Test steps:

Click on login, enter details and submit

<img src=media/sign_in_tst.JPG>

Test 4 - Update Profile

Test steps:

Login, click on username, enter details and submit

<img src=media/Update_profile.JPG>

Test 5 - Logout

Test steps:

Click on logout, and verify that you are sure

<img src=media/sign_out.JPG>


<img src=media/signout_success.JPG>


Expected Results  | Pass y/n
------------- | -------------
Register brings user to sign up page | Y
User can sucessfully Register | Y
User's Profile name appears in Profile when logged in | Y
User can click on username to go to the profile page & update their profile | Y
Login brings user to sign up page | Y
Logout brings user to sign out page | Y
On registering the user is asked to verify their email before they can sign in.| Y


## Pagination

Pagination is set to '8' in admin for the Blog Posts

Test Steps:

View homepage & Scroll to bottom of homepage click on next

Expected Results  | Pass y/n
------------- | -------------
User can only see eight Service posts per page | Y
User can navigate to next page to view more posts | Y

## View Blog Posts

Test 1 - View Blog Posts

Test Steps:

Navigate to the blog page, view list of blog posts

Test 2 - Click on Blog Post link 

Test Steps:

From the blog page click on each post to navigate to the blog post details page to view the blog post and see the list of reviews.

Expected Results  | Pass y/n
------------- | -------------
User can view all blog posts on homepage | Y
User can click on link on a blog post to navigate to the blog post detail page | Y

## Comments

Test 1 - Submit a Comment

Test Steps:

- Log in via the nav link
- Navigate to the blog post detail page as in Test 1.
- Click submit a comment and populate all fields
- Log in as an admin to approve the review
- Log out and back in as an online user
- View submitted comment
- Confirm that the Edit/delete options are available
- Log out and back in as a different user
- Confirm that the Edit/delete options are not available for other users' comment posts.

Test 2 – Edit/ Delete a Comment

Users when logged in can edit/ delete comments linked to their username only

Test Steps:

- Log in as a user
- Navigate to blog post detail view and select a post to edit and update
- Once completed and confirmed update occurred, click on the trash can to delete it.

Expected Results  | Pass y/n
------------- | -------------
Post Click to Review takes user to correct post detail page | Y
User - not logged in - can only see the post comments and cannot submit | Y
User - logged in - can submit a comment| Y
User - logged in - after submitting a comment the approval message appears | Y
User - logged in can edit comments linked to their username only | Y
User - logged in can delete comments linked to their username only | Y
User - logged in is brought to update comment page as expected on clicking edit | Y
User - logged in receives visual message feedback that their updates have occurred | Y
User - logged in can successfully edit a comment item | Y
User - logged in can successfully delete a comment item | Y

## View Horses Catalog

Test 

Test Steps:

Click on the Horses link in the nav bar to view the horse catalog

Expected Results  | Pass y/n
------------- | ------------- 
Option to select a dropdown category - Horse & Pony | Y
Once a selection is made, the catalog of horses/ ponies is available to view | Y

## Select a Horse from the Catalog

Test 

Test Steps:

Click on a Horses image in the catalog to view more detail and see the add to cart option.

Expected Results  | Pass y/n
------------- | ------------- 
Clicking on a horses image brings the user to detail page where the option to add to cart is displayed | Y

## Add a donation to the cart

Test 

Test Steps:

Select a horse in the catalog, click add to cart.

Expected Results  | Pass y/n
------------- | ------------- 
Clicking on add to cart, increments the shopping cart in the nav bar | Y

## Shopping Cart

Test 1

Test Steps:

After adding an item to the shopping bag, clicking on the bag in the nav bar brings the user to the shopping cart page.

Test 2

Test Steps:

Secure checkout option is available in the shopping cart.

Test 3

Test Steps:

Option to remove items from bag is available and functioning.

Test 3

Test Steps:

Option to remove items from bag is available and functioning.

Test 4

Test Steps:

Option to increase/ decrease quantity & update items in bag is available and functioning.


Test 5

Test Steps:

Shopping bag in nav bar total gets increased/ decreased in line with quantity function after update cart is selected.

Expected Results  | Pass y/n
------------- | ------------- 
Clicking on the populated cart, brings the user to the shopping cart page | Y
Secure checkout option is available in the shopping cart. | Y
Option to remove items from bag is available and functioning.| Y
Option to increase/ decrease quantity & update items in bag is available and functioning.| Y
Shopping bag in nav bar total gets increased/ decreased in line with quantity function after update cart is selected.| Y

## Checkout

Test 1

Test Steps:

After adding an item to the shopping cart, the options to select secure checkout is available and functioning.

Test 2

Test Steps:

Selecting secure checkout in the shopping cart, takes the user to the checkout page.

Test 3

Test Steps:

User can populate the billing details form and submit a payment using a stripe test card.

Test 4

Test Steps:

Payment sucessful - user is brought to the order confirmation page.

Test 5

Test Steps:

Payment un-sucessful - error message is displayed and the user can try again.

Expected Results  | Pass y/n
------------- | ------------- 
After adding an item to the shopping cart, the options to select secure checkout is available and functioning. | Y
Selecting secure checkout in the shopping cart, takes the user to the checkout page.| Y
User can populate the billing details form and submit a payment using a stripe test card.| Y
Payment sucessful - user is brought to the order confirmation page.| Y
Payment un-sucessful - error message is displayed and the user can try again.| Y


## Profile

Test 1

Test Steps:

Once logged in a User has the ability to update their profile.

Test 2

Test Steps:

Selecting secure checkout in the shopping cart, takes the user to the checkout page.

Expected Results  | Pass y/n
------------- | ------------- 
Once logged in a User has the ability to update their profile. | Y
If a logged in user has orders these can be viewed in the Profile view| Y

## Welfare Submission form

Test 1

Test Steps:

User can navigate to the About us page and select to submit a welfare concern via a form.

Expected Results  | Pass y/n
------------- | ------------- 
User can navigate to the About us page and select to submit a welfare concern via a form.| Y

## Site Links

All links were tested and functioning as expected

## External URL Links

All external url links are set to open in a new window and tested, including the footer links
For example the Facebook link on the About page.

## Messaging

All messaging e.g Toasts/ modal - were tested and working as expected

<img src=media/Readme/message.jpg>

<img src=media/Readme/approval.jpg>

## Email Confirmation

Email confirmation on registration is enabled and using gmail. Tested and working as expected.


<img src=media/Readme/verify_email.jpg>

<img src=media/Readme/email_confirm.jpg>

## Responsiveness 

I used chrome developer tools, Techsini & ami throughout all development of the site to ensure that it was responding to all devices down to 280px - 360px width

I tested the site responsiveness on my iphone/ ipad and my family/ friends android mobile devices to ensure the site was rendering and functional across a range of devices.

## Admin 

Expected Results  | Pass y/n
------------- | -------------
Admin User can log in to django auth admin | Y
Admin User can create a service post | Y
Admin User can delete a service post | Y
Admin User can edit a service post | Y
Admin User can approve a review | Y
Admin User can create/update/delete users | Y
Admin User can view the welfare concern submissions | Y
Admin User can see order payments in DB & Stripe | Y
Admin User can see static files in Aws Bucket and upload | Y


## Bugs

Database connection to Heroku failed - This was resolved my re-running migrations.

## Content 

I reviewed all content on the site for:
- Grammar and spelling mistakes.
- Calls to action are clear and contain correct information.
- Verified all text/ headings are displaying correctly.


## Validation

- I ran all the Python Code through [PEP8](http://pep8online.com/)
- I ran HTML through [HTML Validator](https://validator.w3.org/) 
- I ran the CSS through [Jigsaw](Jigsawhttps://jigsaw.w3.org)
- I also ran all code through [code beautifier](https://codebeautify.org/)

## Lighthouse

Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.<br>
The accesibility needs to be improved, but this was out of scope for this project.
<img src=media/Readme/lighthouse.jpg>

# Creation & Deployment

## Creating the Django App

- Go to the Code Institute Gitpod Full Template Template
- Click on Use This Template
- Once the template is available in your repository click on Gitpod
- When the image for the template and the Gitpod are ready open a new - terminal to start a new Django App
- Install Django and gunicorn: pip3 install django gunicorn
- Install supporting database libraries dj_database_url and psycopg2 library: - pip3 install dj_database_url psycopg2
- Create file for requirements: in the terminal window type pip freeze --local > requirements.txt
- Create project: in the terminal window type django-admin startproject your_project_name
- Create app: in the terminal window type python3 manage.py startapp your_app_name
- Add app to the list of installed apps in settings.py file: you_app_name
- Migrate changes: in the terminal window type python3 manage.py migrate
- Run the server to test if the app is installed, in the terminal "The install worked successfully! Congratulations!"

## Deploying to Heroku

- Log in to Heroku or create an account
- On the main page click the button labelled New in the top right corner and - from the drop-down menu select Create New App
- You must enter a unique app name
- Next select your region
- Click on the Create App button
- Click in resources and select Heroku Postgres database
- Click Reveal Config Vars and add:
- A new record with SECRET_KEY
- A new record with the AWS_ACCESS_KEY_ID
- A new record with the AWS_SECRET_ACCESS_KEY
- A new record with the EMAIL_HOST_PASS
- A new record with the EMAIL_HOST_USER
- A new record with the STRIPE_PUBLIC_KEY
- A new record with the STRIPE_SECRET_KEY
- A new record with the STRIPE_WH_SECRET
- A new record with the DISABLE_COLLECTSTATIC = 1
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
- Scroll to the top of the page and choose the Deploy tab
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click Enable Automatic Deploys for automatic deployment when you push updates to Github

## Final Deployment steps

- Create a Procfile "web: gunicorn your_project_name.wsgi"
- When development is complete change the debug setting to: DEBUG = False in settings.py
- In Heroku settings config vars delete the record for DISABLE_COLLECTSTATIC
- In Heroku settings config vars set the record for USE_AWS to True

## Forking

Fork this project by following the steps:
- Open GitHub
- Find the "Fork" button at the top right of the page
- Once you click the button the fork will be in your repository

## Cloning

Clone this project by following the steps:
- Open GitHub
- You will be provided with three options to choose from, HTTPS, SSH or GitHub CLI, click the clipboard icon in order to copy the URL
- Once you click the button the fork will be in your repository
- Open a new terminal
- Change the current working directory to the location that you want the cloned directory
- Type "git clone" and paste the URL copied in step 3
- Press "Enter" and the project is cloned


# Credits

Python Code inspired and adapted from the following tutorials and sources:

Boiler Plate code taken and adapted from:

- Code Institute - I think therefore I Blog 

- Code Institute - Boutique Ado

Other Sources:

- https://inventwithpython.com/invent4thed/chapter8.html

- https://www.w3schools.com/python/default.asp

- https://www.youtube.com/watch?v=pFvSb7cb_Us

- https://note.nkmk.me/en/python-textwrap-wrap-fill-shorten/

- https://www.sololearn.com/Discuss/1582033/how-to-check-if-input-is-empty-in-python

- https://legionscript.medium.com/

- https://getbootstrap.com/docs/4.0/components/modal/

- https://dev.to/earthcomfy/getting-started-custom-user-model-5hc

- https://djangocentral.com/

- https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/

- https://www.geeksforgeeks.org/e-commerce-website-using-django/


### Content

All content was written by the project owner. With the exception of some of the blog post details. I took some content from [Here](https://www.worldhorsewelfare.org/)


### Readme 

- I used the 
[Markdown cheat sheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md) and the [love running template ](https://github.com/Code-Institute-Solutions/readme-template )to help put together my readme.


### Acknowledgments

Special thanks to my mentor Rohit, my colleagues at Code Institute, and Kasia Bogucka


## The Deployed Site 

The live link can be found [Here](https://embarr-donations.herokuapp.com/)