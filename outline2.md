 
 # etapes de creation de projet Web Django *****

 - frontend template   :(upload your template)
 - virtualenv :
     - create virtualenv                     :  virtualenv -p python3.8 Job-Board 
     - activate virtualenv                   :  .\Scripts\activate 
     - cd src , - pip install django         : install django in src
     - pip freeze > requirements.txt         : to show all your librairies in txt
     - deactivate                            : if you want todeactivate the project


- upload project on Github

# how django project work ***************
- url       : path
- view       : logic
- models     : db data base
- templates  : frontend


Relations : use it in (category : in model)  : exp (every job has a category)

  - One to many : [user --> posts : user has many posts] : name it = Foreginkey
  - Many to many : [ user -- groups : in this groups there are many admins, and admins has many groups]
  - One to one   : [user --> profile : user has one profile]
