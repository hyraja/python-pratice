# There are different relationship available in django

# a. one-to-many relationship
# b. one-to-one relationship
# c. many-to-many relationship

'''one-to-many relationship
   -------------------------- '''
# this is also called parent child relationship bcz
# one parent can have multiple children but one children can have only one parent.

# lets create 2 model fields to demonstrate the relationship
# class Language(models.Model):
#     name = models.CharField(max_length=20)


# class Framework(models.Model):
#     name = models.CharField(max_length=20)
#     language = models.ForeignKey(Language, on_delete=models.CASCADE)

# open our shell and verify
# >>> from app.models import Language,Framework
# >>> python = Language(name = 'Python')
# >>> python.save()

# >>> django = Framework(name = 'Django')
# >>> flask = Framework( name  = 'Flask')

# >>> python
# <Language: Language object (1)>
# >>> django.language = python
# >>> flask.language = python

# >>> bottle = Framework(name = 'bottle',language=python)
# >>> django.save()
# >>> flask.save()
# >>> bottle.save()

# language table(parent table)
'''
id	name
1	Python
'''

# framework table(child table)
'''
id	name	language_id
1	Django	1
2	Flask	1
3	bottle	1
'''

# language_id we don't create on our framework table due to foregn_key relation of language table

# lets create another language as java and create a framework models as spring using the foregnkey.
# and lets see how the database is looking
# >>> java = Language(name='Java')
# >>> java.save()

# >>> spring = Framework(name='Spring', language=java)
# >>> spring.save()

# language table             # framework table
'''
id	name                 # id	name	language_id
1	Python               # 1	Django	1
2	Java                 # 2	Flask	1
'''                      # 3	bottle	1
'''                      # 4	Spring	2 '''

# spring framework's language_id is 2 which is referencing the java language id(2) from the language table.

# lets work on some filter
# >>> Framework.objects.all()
# <QuerySet [<Framework: Django>, <Framework: Flask>, <Framework: bottle>, <Framework: Spring>]>

# we can filter with parent class field in this way
# we are checking here Framework objects with foregnkey (language) then __name(which is one field of Language model)
# here we are checking our data from child to parent

# >>> Framework.objects.filter(language__name = 'Python')
# <QuerySet [<Framework: Django>, <Framework: Flask>, <Framework: bottle>]>

# >>> Framework.objects.filter(language__name='Java')
# <QuerySet [ < Framework: Spring > ] >

# >>> Framework.objects.filter(language__name__startswith = 'Py')
# <QuerySet [<Framework: Django>, <Framework: Flask>, <Framework: bottle>]>

# we can also filter our data from parent to child method
# django access our Framework model as small letter 'framework__name'

# >>> Language.objects.filter(framework__name = 'Spring')
# <QuerySet [<Language: Java>]>

# >>> Language.objects.filter(framework__name = 'Django')
# <QuerySet [<Language: Python>]>

''' Many-To-Many relationship
------------------------------ '''
# one table can have multiple elements of other and other table can have multiple elements of first table

# we can understand it through an movie and character model
# one superhero-movie can have multiple characters and one character can in multiple superhero-movie

# lets create 2 models for example
# class Movie(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self) -> str:
#         return self.name


# class Character(models.Model):
#     name = models.CharField(max_length=20)
#     movies = models.ManyToManyField(Movie)

#     def __str__(self) -> str:
#         return self.name

# open our shell for testing relationship
# importing models and add one movie element

# >> > from app.models import Character, Movie
# >> > avengers = Movie(name='Avengers')
# >> > avengers.save()

# # add an character element
# >> > captain_america = Character(name='Captain America')
# >> > captain_america.save()
# # adding character element with the movie table
# >> > captain_america.movies.add(avengers)
# >> >
# >> > civil_war = Movie(name='Civil War')
# >> > thor = Movie(name='Thor:  Dark world')
# >> > thor_character = Character(name='Thor')
# >> > civil_war.save()
# >> > thor.save()
# >> > thor_character.save()
# >> > # adding characters to the respected movie table
# >> > captain_america.movies.add(civil_war)
# >> > thor_character.movies.add(avengers)
# >> > thor_character.movies.add(thor)

# >>> captain_america.movies.create(name = 'Winter soldier')
# <Movie: Winter soldier>

# movie table
'''
id	name
1	Avengers
2	Civil War
3	Thor:  Dark world
4	Winter soldier
'''

# character table
'''
id	name
1	Captain America
2	Thor
'''

# relationship table
'''
id	character_id	movie_id
1	   1	          1
2	   1	          2
3	   2	          1
4	   2	          3
5	   1	          4
'''
# we can able to see many-to-many relation with relationship table

# looking for its query

#  character side query
# >>> Character.objects.filter(movies__name = 'Civil War')
# <QuerySet [<Character: Captain America>]>

# Movie side query(using lower case character instead of Character model)
# >>> Movie.objects.filter(character__name = 'Captain America')
# <QuerySet [<Movie: Avengers>, <Movie: Civil War>, <Movie: Winter soldier>]>

# looking for one character
# captain_america = Character.objects.get(name='Captain America')
# captain_america
# <Character: Captain America>

# captain america all movies
# >>> captain_america.movies.all()
# <QuerySet [<Movie: Avengers>, <Movie: Civil War>, <Movie: Winter soldier>]>

# looking for one movie and it's character information
# >>> avengers = Movie.objects.get(name= 'Avengers')
# >>> avengers
# <Movie: Avengers>
# >>> avengers.character_set.all()
# <QuerySet [<Character: Captain America>, <Character: Thor>]>

''' one-to-one relationship
------------------------'''
# one to one relation refers to one user can only have one profile at a time.

# ex:

'''
class Userprofile(models.Model):
user = models.OneToOnefield(model_name, on_delete=models.cascade) 

 '''
