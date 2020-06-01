# Mysterygram

![Mysterygram(/static/photo_blog/Circles.jpg)

## Built By [Dan Kariuki](https://github.com/Buttonupd/)

## Description
This is an application which resembles the popular instagram

## User Stories

Users would like to:

   * Sign in to the application to start using.
   * Upload my pictures to the application.
   * See my profile with all my pictures.
   * Follow other users and see their pictures on my timeline.
   * Like a picture and leave a comment on it.


## Admin Abilities

Admin should:
* Sign in to the mysterygram
* Create a new post
* Delete images
* Update image and post details.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display Users| **Home page** | Clickable links to open any User  |
| Display single images on click | **On  click** | All details should be viewed|
| To add post  | **In app** | Add and add categories and tag location of Image|
| To edit image  | **Through App** | Redirected to the  image form details and editing happens|
| To delete an image  | **Through app ** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by user|
| To filter by users  | **Click drop-down on navbar** | Users can view users by Location|


## SetUp / Installation Requirements
### Prerequisites
* python3.7
* pip3
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/Buttonupd/Mistergram
        $ cd Mistergram

## Running the Application
* Creating the virtual environment

        $ Virtualenv env(* 'env is the name of the enviroment')
        $ source env/bin/activate
        

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ ./manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ ./manage.py test 

## Technologies Used
* Python3.7
* Django Framework
* DjangoRestFramework
* Postgresql Database

