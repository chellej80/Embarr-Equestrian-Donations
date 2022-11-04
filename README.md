# Embarr Equestrian Donations


## Overview

[Embarr Equestrian Donations](https://embarr-donations.herokuapp.com/) This project is a Full Stack website built using the Django framework and deployed using Heroku. It is a site for a retirement home for senior Horses. The site is a full stack ecommerce platform, where the user can submit online donations and pay using stripe. the site also follows and displays the CRUD logic, Users can Create (Submit a Comment on a blog post), Retrieve (Search for an Animal/ blogpost), Update (Update their blog comments/ Profile) and Delete (Delete their comments).


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

As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View a list of Services.
3. Search for services via the search bar tool.
4. Click on a service post to read more.
5. View the number of reviews posted on a service.
6. Register as an account user.

As logged in website user, I can:

1. Register/Log in as a user.
2. View a catalog of horses that need donations for their care.
3. Select a horse to donate to and submit an online payment.
4. Search for and read blog posts.
5. Comment on blog posts.
6. Edit/Delete my previous blog comments.
7. Manage my profile by updating my details.
8. Sign up for the monthly newsletter
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


## Marketing

The site is B2C focused 

 - Facebook page
 - Mailchimp
 - Newsletter sign up

## SEO

SEO implementation, including:
- A robots.txt file
- A sitemap.xml file
- Descriptive meta tags
- rel attributes on links to external resources
- Content

## Site Features 

- __Navigation Bar__

  Featured on all pages, the full responsive navigation bar includes links to the Home page and all sub pages - About, Blog, Hoses shopping bag and User Account, and is identical in structure for each page to allow for easy navigation. When the user logs in,the signin/up link is replaced with the logout link. The navigation items are styled to transition to a hamburger menu when the site is reduced in size on a mobile device. This section will allow the user to easily navigate from page to page across all devices without having to revert back to the previous page via the ‘back’ button. 

    


- __Logo__

    The logo I created simply using a combination of text and a font awsome icon. The logo is a hyperlink that takes the user to the homepage.
    
    

- __Register Page__

    The User register page was created using the out of the box option from Django Auth. Further styling of this page is required but currently out of scope for the timeframe of this project.

    

- __Login Page__

    The User login page was created using the out of the box option from Django Auth. Further styling of this page is required but currently out of scope for the timeframe of this project.

    

- __Logout Page__

  The User logout page was created using the out of the box option from Django Auth. Further styling of this page is required but currently out of scope for the timeframe of this project.

  

- __Profile Page__

  The User pofile page can be accessed by clicking on the Account Icon in the navigation bar, once they are logged in. the user can update their personal details here and view their donations history. There is room to expand the functionality of this page, for example, allow the user to upload a profile picture or add a bio section, but this was out of scope for this project. Further styling of this page is required but currently out of scope for the timeframe of this project.

  

- __Search Bar__

    The search bar allows a user to search for a Animal/blog they would like to donate to/ read about and/or comment on. The search is crude and requires some futher development, but this was out of scope for this project.

    

- __Blog__

  

   



- __Blog Detail Pages__

  The service post detail page(s) are accessed by clicking on the high level view of a service post. This takes the user to a full page view of the service, that expands on the details, allows the user to read the reviews posted, or if logged in submit a review, or delete/ update a review.

  


- __Submit Comment__

  The submit review option is accessed via the service post detail page and is only available for logged in registered users, otherwise this option is hidden. Logged in users can select 'Submit a Review', a review form appears, once populated and submitted, a message will display informing the user that their review has been submitted for approval. An admin must approve the review before it will display.

  
- __Update/ Delete Comment__

  The Update/delete review option is accessed via the service post detail page and is only available for logged in registered users, otherwise this option is hidden. Logged in users can update/ delete reviews they have posted. They cannot update/ delete other users review. On selection of 'Edit' the user will be presented with a form to edit and submit. On submission the user will receive message feedback to say their message has been updated. If the user selects to 'delete' by clicking on the trash can icon, the user will be asked if they are sure they want to delete, and once selected it will update them their message has been deleted.

  



### Features Left to Implement

- Approval authentication of updated comments (This was out of scope)
- Bespoke forms for the out of the box Django Auth pages - Login/ Logout/ Register and update review form
- Contact Page
- Improved search functionality
- Add bio/ profile picture to profile


    
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
-django coniutries

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
Logout Link appears when logged in | Y
Logout links to sign out page | Y
Username appears when logged in | Y
Username links to User Profile Page | Y
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

### Page Navigation

Test 1

Test Steps:

Click on page navigation links at bottom of page to navigate between pages

Expected Results  | Pass y/n
------------- | ------------- 
Click on 'Next' moves to next page | Y
Click on previous returns user to previous page | Y

## Search Bar

Test 1

Enter text into the search bar to check for return of results
Test Steps:

Enter text into search bar that will return a positive result
For example – Livery, EAL, Coaching
Enter text into search bar that will return a negative result
For example – Horse, Rider

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
Clicking the e search magnifier returns the result page | Y
Clicking x after entering text in the search bar clears the text | Y
Default text displays in the search Box | Y


## User Registration

Test 1 -Register

Test steps:

Click on register, sign up page displays, populate fields and submit

Test 2 – Login

Test steps:

Click on login, enter details and submit

Test 3 - Update Profile

Test steps:

Login, click on username, enter details and submit

Test 4 - Logout

Test steps:

Click on logout, and verify that you are sure

Expected Results  | Pass y/n
------------- | -------------
Register brings user to sign up page | Y
User can sucessfully Register | Y
User's Profile name appears in Navbar when logged in | Y
User can click on username to go to the profile page & update their profile | Y
Login brings user to sign up page | Y
Logout brings user to sign out page | Y

## View 


## Pagination

Pagination is set to '6' in admin

Test Steps:

View homepage & Scroll to bottom of homepage click on next

Expected Results  | Pass y/n
------------- | -------------
User can only see three Service posts per page | Y
User can navigate to next page to view more posts | Y


## External URL Links

All external url links are set to open in a new window and tested, including the footer links

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

## Bugs



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

# Deployment

The site was first developed in Github (Repository created using the Code Institute Template) and tested there locally before deploying to Heroku:

The steps to deploy are as follows: 

- Log in to Heroku or create an account
- On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
- You must enter a unique app name
- Next select your region
- Click on the Create App button
- Add Database to App Resources,  Resources Located in the Resources Tab, Add-ons, search and add ‘Heroku Postgres’
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Click Reveal Config Vars and add a new record with SECRET_KEY
- Click Reveal Config Vars and add a new record with the `CLOUDINARY_URL`
- Click Reveal Config Vars and add a new record with the `DISABLE_COLLECTSTATIC = 1`
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click either Enable Automatic Deploys for automatic deployment when you push updates to Github

- On submission the project is forked in Github, by forking the project a copy of the original repository is made that can be viewed without affecting the original repository by following these steps: In the GitHub repository, locate the settings, above this is the option to 'fork', select this to create a copy

  - Cloning a repository: When you create a repository on GitHub.com, it exists as a remote repository. You can clone your repository to create a local copy on your computer and sync between the two locations. It makes it easier to fix merge conflicts, add or remove files, and push larger commits. 


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

All content was written by the project owner.


### Readme 

- I used the 
[Markdown cheat sheet](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md) and the [love running template ](https://github.com/Code-Institute-Solutions/readme-template )to help put together my readme.


### Acknowledgments

Special thanks to my mentor Rohit, my colleagues at Code Institute, and Kasia Bogucka


## The Deployed Site 

The live link can be found [Here](https://embarr-donations.herokuapp.com/)