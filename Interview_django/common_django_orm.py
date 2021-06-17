# Sample Models

# Let’s define the sample model User.

# from django.db import models
# # Create your models here.
# class User(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     age = models.IntegerField()
#     city = models.CharField(max_length=255)

'''
# === > Data in the User table
-------------------------------------------
|id | firstname | lastname | age | city  |
|1  | rajaprasad | paikaray  | 24  | bengaluru|
|2  | chris      | madams    | 40  | london|
|3  | sample     | 1         | 20  | city1 |
|4  | sample     | 2         | 25  | city2 |
|5  | sample     | 3         | 30  | city3 |
-------------------------------------------
'''

''' Filter NULL values '''
# ‘__isnull’ is used to filter the null values in the Django ORM. It accepts True or False.

# >>> Blog.objects.filter(age__isnull = True)
# <QuerySet []>

# >>> Blog.objects.filter(age__isnull = False)
# <QuerySet [<Blog: rajaprasad>, <Blog: chris>]>

# >>> Blog.objects.filter(age__isnull=False).values('id', 'age')
# <QuerySet [{'id': 1, 'age': 24}, {'id': 2, 'age': 40}]>

''' exists() '''
# The exists() method is used to check the result of the query.
# Returns True if the queryset contains any results, and False if not.

# >>> Blog.objects.filter(age__isnull = True).exists()
# False

# >>> Blog.objects.filter(age__isnull = False).exists()
# True

''' SQL ‘LIKE’ opearation with django orm '''
# >>> Blog.objects.filter(city__contains = 'lon').values('id','city')
# <QuerySet [{'id': 2, 'city': 'london'}]>

# >>> Blog.objects.filter(city__contains = 'cit').values('id','city')
# <QuerySet [{'id': 3, 'city': 'city1'}, {'id': 4, 'city': 'city2'}, {'id': 5, 'city': 'city3'}]>

''' we can check exact matching string using __exact '''
# >>> Blog.objects.filter(city__exact='city1').values('id','city')
# <QuerySet [{'id': 3, 'city': 'city1'}]>

''' ‘__startswith’ to check the start of the string. '''
# >>> Blog.objects.filter(city__startswith='ci').values('id','city')
# <QuerySet [{'id': 3, 'city': 'city1'}, {'id': 4, 'city': 'city2'}, {'id': 5, 'city': 'city3'}]>

''' ‘__endswith’ to check the end of the string. '''
# >>> Blog.objects.filter(city__endswith='on').values('id','city')
# <QuerySet [{'id': 2, 'city': 'london'}]>

'''
Relational operators
gt -Greater than.
gte -Greater than or equal to.
lt -Less than.
lte -Less than or equal to. 
'''

# >>> Blog.objects.filter(age__gt=30)
# <QuerySet [ < Blog: chris > ] >

# >> > Blog.objects.filter(age__gte=20)
# <QuerySet [< Blog: rajaprasad > , < Blog: chris > , < Blog: sample > , < Blog: sample > , < Blog: sample > ] >

# >>> Blog.objects.filter(age__lt=30)
# <QuerySet [ < Blog: rajaprasad > , < Blog: sample > , < Blog: sample > ] >

# >>> Blog.objects.filter(age__lte = 30)
# <QuerySet [<Blog: rajaprasad>, <Blog: sample>, <Blog: sample>, <Blog: sample>]>

''' Select a few columns of the table '''
# In Django ORM values() method is used to select a few column values of the table.

# >>> Blog.objects.values('id')
# <QuerySet [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}]>

# >>> Blog.objects.values('firstname')
# <QuerySet [{'firstname': 'rajaprasad'}, {'firstname': 'chris'}, {'firstname': 'sample'}, {'firstname': 'sample'}, {'firstname': 'sample'}]>
