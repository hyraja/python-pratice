# Sample Models

# Let’s define the sample model User.

# from django.db import models
# # Create your models here.
# class Blog(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     age = models.IntegerField()
#     city = models.CharField(max_length=255)

'''
# === > Data in the User table
-------------------------------------------
|id | firstname | lastname | age | city  |
|1  | rajaprasad | paikaray| 24  | bengaluru|
|2  | chris      | madams  | 40  | london|
|3  | sample     | 1       | 20  | city1 |
|4  | sample     | 2       | 25  | city2 |
|5  | sample     | 3       | 30  | city3 |
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

''' count objects '''
# django orm uses count() to count all objects
# >> > Blog.objects.count()
# 5

# # Total number of books with publisher=BaloneyPress
# (name is one field of publisher model so we can call it by __name )
# >>> Book.objects.filter(publisher__name='BaloneyPress').count()
# 73

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

''' SQL ‘IN’ with Django ORM '''
# ‘__in’ is used to filter on multiple values.
# >>> Blog.objects.filter(id__in = [1,2,3])
# <QuerySet [<Blog: rajaprasad>, <Blog: chris>, <Blog: sample>]>

''' exclude() '''
# Excludes objects from the queryset which match with the lookup parameters.
# >>> Blog.objects.exclude(id=1)
# <QuerySet [<Blog: chris>, <Blog: sample>, <Blog: sample>, <Blog: sample>]>

''' Rename objects like ‘As’ in the SQL '''
# The extra() method is used to rename columns in the ORM.

# >>> Blog.objects.extra(select={ 'Firstname':'firstname','Lastname':'lastname'}).values('Firstname','Lastname')
# <QuerySet [{'Firstname': 'rajaprasad', 'Lastname': 'paikaray'}, {'Firstname': 'chris', 'Lastname': 'madams'},
#   {'Firstname': 'sample', 'Lastname': '1'}, {'Firstname': 'sample', 'Lastname': '2'},
#   {'Firstname': 'sample', 'Lastname': '3'}]>
# i've renamed firstname to Firstname and lastname to Lastname

''' aggregate() '''
# The aggregate() function is used to perform aggregation operations like sum, average, min, max, etc.

# >>> from django.db.models import Avg,Min,Max,Sum
# >>> Blog.objects.aggregate(Sum('age'))
# {'age__sum': 139}

# >>> Blog.objects.aggregate(Avg('age'))
# {'age__avg': 27.8}

# >>> Blog.objects.aggregate(Min('age'))
# {'age__min': 20}
# >>> Blog.objects.all().aggregate(Min('age'))
# {'age__min': 20}

# >>> Blog.objects.aggregate(Max('age'))
# {'age__max': 40}

''' The aggregate() function works on the whole dataset only.
 Use annotate() instead of aggregate() if you want an average age group by city. '''
# >>> Blog.objects.values('city').annotate(Sum('age'))
# <QuerySet [{'city': 'Bengaluru', 'age__sum': 24}, {'city': 'city1', 'age__sum': 20},
# {'city': 'city2', 'age__sum': 25}, {'city': 'city3', 'age__sum': 30}, {'city': 'london', 'age__sum': 40}]>


''' order_by '''
# >>> Blog.objects.values('city').annotate(total = Sum('age')).order_by('-total')
# <QuerySet [{'city': 'london', 'total': 40}, {'city': 'city3', 'total': 30},
# {'city': 'city2', 'total': 25}, {'city': 'Bengaluru', 'total': 24}, {'city': 'city1', 'total': 20}]>
# i use total to rename the result of annotate  and order it in reverse method

# >>> Blog.objects.values('city').annotate(total = Sum('age')).order_by('total')
# <QuerySet [{'city': 'city1', 'total': 20}, {'city': 'Bengaluru', 'total': 24},
# {'city': 'city2', 'total': 25}, {'city': 'city3', 'total': 30}, {'city': 'london', 'total': 40}]>

''' Having clause using Filter() '''
# Usually, in the database, we use the ‘HAVING’ clause with the group by queries. In the Django, we can use filter() function

# >>> Blog.objects.values('city').annotate(total = Sum('age')).filter(total__gt = 20).order_by('-total')
# <QuerySet [{'city': 'london', 'total': 40}, {'city': 'city3', 'total': 30}, {'city': 'city2', 'total': 25},
# {'city': 'Bengaluru', 'total': 24}]>
