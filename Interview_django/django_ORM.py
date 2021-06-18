'''
ORM stands for Object Relation Mapper.
Django ORM is a powerful and elegant way to interact with the database. 
The Django ORM is an abstraction layer that allows us to play with the database.
In the end, Django ORM will convert all operations into SQL statements. 
'''

# we check alll our orm output here (i.e shell)
# to open shell follow the below steps
# go to inside django project where manage.py file exists and type the command as
# py manage.py shell

# Let’s define the sample model Blog. and then we can test it on shell
# class Blog(models.Model):
#     firstname = models.charfield(max_length=20)
#     lastname = models.charfield(max_length=20)
#     age = models.Integerfield()
#     city = models.charfield(max_length=20)

#     def __str__(self) -> str:
#         return self.title

# our database model is ready we can start operation with it using shell

# What is a QuerySet?
# A QuerySet is, in essence, a list of objects of a given Model. QuerySets allow you to read
# the data from the database, filter it and order it.

# It's easiest to learn by example. Let's try this, shall we?
# in django most of the ORM output format will be in Queryset


# ----------------------------------------------------#
# start our shell after import the model field present on inside ourapp(application) like this
''' importing Blog from app model'''
# from app.models import Blog

# ---------------------------------
'''Create a object through console '''

# from app.models import Blog
# >>> Blog.objects.create(firstname = 'chris',lastname='madams',age=40,city='london')
# <Blog: chris>

''' Retrive All objects '''
# >>> Blog.objects.all()
# <QuerySet [<Blog: rajaprasad>, <Blog: chris>]>

''' retrive single object through id/title.... using get() '''
# >>> Blog.objects.get(id=1)
# <Blog: rajaprasad>

# >>> Blog.objects.get(firstname='rajaprasad')
# <Blog: rajaprasad>

''' retrive the superuser '''
# >>> from django.contrib.auth.models import User
# >>> User.objects.all()
# <QuerySet [<User: raj>]>


#### filter ###########

''' Filter objects which are lessthanequal(lte) current time zone '''
# published_date is one field in model and __lte is lessthanequal

# >>> from django.utils import timezone
# >>> Post.objects.filter(published_date__lte=timezone.now())
# <QuerySet [<Post: Sample title>]>

''' filter object according to firstname  '''
# >>> Blog.objects.filter(firstname='rajaprasad')
# <QuerySet [<Blog: rajaprasad>]>

''' __contains acts as sql like '''
# >>> Blog.objects.filter(firstname__contains='raja')
# <QuerySet [<Blog: rajaprasad>]>

#### Ordering objects ########

''' order an elemet with  ascending order '''
# >>> Post.objects.order_by('created_date')
# <QuerySet [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]>

''' order an element with reverse order '''
# >>> Post.objects.order_by('-created_date')
# <QuerySet [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]>
