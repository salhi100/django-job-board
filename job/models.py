from django.db import models


'''
caracterstic of : django model fields 
    - html widget
    - validation
    -db size
'''

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

class Job(models.Model):    # Table 
    title = models.CharField(max_length=50)    # field = column
    description = models.TextField(max_length=1000)  # field = column
    job_type = models.CharField(max_length=15, choices = JOB_TYPE) # use choices to shoose 'fulltime or partime'
    published_at = models.DateTimeField(auto_now=True)   # time when you create your post
    vacancy = models.IntegerField(default=1)   # vacancy : 9adech min mara maoujoud post
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # every category has many jobs => so one to many (foreginkey)



    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



    
    
    

    
