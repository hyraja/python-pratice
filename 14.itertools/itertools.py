# Itertools means that the functions in itertools “operate” on iterators to produce more complex iterators.

# Consider, for example, the built-in zip() function, which takes any number of iterables as arguments
# and returns an iterator over tuples of their corresponding elements:

# >>> list(zip([1, 2, 3], ['a', 'b', 'c']))
# [(1, 'a'), (2, 'b'), (3, 'c')]

# How, exactly, does zip() work?

# [1, 2, 3] and ['a', 'b', 'c'], like all lists, are iterable, which means they can return their elements one at a time.
# Technically, any Python object that implements the .__iter__() or .__getitem__() methods is iterable.
# The iter() built-in function, when called on an iterable, returns an iterator object for that iterable:

# >>> iter([1, 2, 3, 4])
# <list_iterator object at 0x7fa80af0d898>
# Under the hood, the zip() function works, in essence, by calling iter() on each of its arguments,
# then advancing each iterator returned by iter() with next() and aggregating the results into tuples.
# The iterator returned by zip() iterates over these tuples.

# map()
# The map() built-in function is another “iterator operator” that, in its simplest form,
# applies a single-parameter function to each element of an iterable one element at a time:

# >>> list(map(len, ['abc', 'de', 'fghi']))
# [3, 2, 4]

# The map() function works by calling iter() on its second argument, advancing this iterator with next()
# until the iterator is exhausted, and applying the function passed to
# its first argument to the value returned by next() at each step. In the above example,
# len() is called on each element of ['abc', 'de', 'fghi'] to return an iterator over the lengths of each string
#  in the list.

# Since iterators are iterable, you can compose zip() and map() to produce an iterator over combinations of elements
#  in more than one iterable. For example, the following sums corresponding elements of two lists:

# >>> list(map(sum, zip([1, 2, 3], [4, 5, 6])))
# [5, 7, 9]
# This is what is meant by the functions in itertools forming an “iterator algebra.”
# itertools is best viewed as a collection of building blocks that can be combined to form specialized “data pipelines”
# like the one in the example above.
