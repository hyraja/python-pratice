
''' select_releated and prfetch_related '''
# ------------------------------------

'''

In django select_releated and prefetch_releated used to reduces number of queries and make program much faster.

select_related() ==> “follows” foreign-key relationships, selecting additional related-object data when it executes its query.
prefetch_related() ==>  does a separate lookup for each relationship, and does the “joining” in Python.

class A(models.Model):
   pass
  
class B(models.Model):
   a = ForeignKey(ModelA)
  
  
# Forward ForeignKey relationship
A.objects.select_related('a').all()
  
# Reverse ForeignKey relationship
A.objects.prefetch_related('modelb_set').all() 

------------------------------------------------------------
select_related obtains all data at one time through multi-table join Association query, and improves performance by reducing the number of 
database queries. It uses JOIN statements of SQL to optimize and improve performance by reducing the number of SQL queries.
The latter is to solve the problem in the SQL query through JOIN statement.

However, for many-to-many relationships, it is not wise to use SQL statements to solve them, because the tables obtained by JOIN will be very long, 
which will lead to the increase of running time and memory occupation of SQL statements. The solution to prefetch_related() is to query each table 
separately and then use Python to handle their relationship!
'''
