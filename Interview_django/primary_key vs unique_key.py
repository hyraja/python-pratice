'''

Primary key: 
------------
A primary key is a column of table which uniquely identifies each tuple (row) in that table.
ex: 
we take table named as Student table, having attributes such as Roll_number, Name, Batch, Phone_number, Citizen_ID.

The roll number attribute can never have identical and NULL value, because every student enrolled in a university 
can have unique Roll_number, therefore two students cannot have same Roll_number and each row in a table is uniquely
 identified with student’s roll number. So, we can make Roll_number attribute as a primary key in this case.

unique key:
-------------
Unique key constraints also identifies an individual tuple uniquely in a relation or table

ex:
Roll number attribute is already assigned with the primary key and Citizen_ID can have unique constraints where 
each entry in a Citizen_ID column should be unique because each citizen of a country must have his or her Unique 
identification number like Aadhaar Number. But if student is migrated to another country in that case, 
he or she would not have any Citizen_ID and the entry could have a NULL value as only one NULL is allowed 
in the unique constraint.



Key Differences Between Primary key and Unique key:

Primary key will not accept NULL values whereas Unique key can accept one NULL value.
A table can have only primary key whereas there can be multiple unique key on a table.
A Clustered index automatically created when a primary key is defined whereas Unique key generates the non-clustered index
that's why primary key is firster than unique key

'''
