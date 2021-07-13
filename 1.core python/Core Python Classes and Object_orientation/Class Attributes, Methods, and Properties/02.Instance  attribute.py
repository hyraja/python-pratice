# These are the attributes assigned with per object basics usually in the dunder init method of a class

# ex: Instance attibutes
# class Rectangle:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

# real life example with shipping container
class ShippingContainer:

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents


# instanciate an object using instance attributes
c1 = ShippingContainer('YML', ["Books"])
# Accessing the instance attribute through the instance(object) which we created.
print(c1.owner_code, c1.contents)  # YML ['Books']

# if we create another instance, it should contain own independent value .
c2 = ShippingContainer('MAE', ['clothes'])
print(c2.owner_code, c2.contents)  # MAE ['clothes']

# N.b instance attributes are per object, so each objects have it's own instance attributes
