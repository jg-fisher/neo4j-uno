"""
Inherited by the class
"""
from py2neo.data import GraphObject

"""
For defining nodes without class mappings
"""
from py2neo.data import Node, Relationship

class Person(GraphObject):
    # Name of the Primary Key
    __primarykey__ = 'name'

    # Primary Key Property Instance
    name = Property()
    hair_color = Property()
    age = Property()


