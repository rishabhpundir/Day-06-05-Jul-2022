#Overloading

# def product(a, b):
#     print(a*b)

# def product(a, b, c):
#     print(a*b*c)


# print(product(4, 5, 2))


# --------------------------------------------------------------------------
#Overloading class function

# class NameDisplay:
#     def display(self, name=None):
#         if name is not None:
#             print(f'Hello! {name}')
#         else:
#             print('Hello!')

# display_obj = NameDisplay()
# display_obj.display()
# display_obj.display('Peter...')


# --------------------------------------------------------------------------


# Overloading Built-in Functions

# class items:
#     def __init__(self, items_list):
#         self.items_list=list(items_list)

#     def __len__(self):
#         print('The total items are : ')
#         return len(self.items_list)
# a = items(['a', 'b', 23, 995.78])
# print(len(a))


# --------------------------------------------------------------------------


# Overiding Inherited functions

# class Parent:
#     def __init__(self):
#         print('Parent constructor ran...')

#     def display(self, name):
#         print(name)

#     def display2(self):
#         print('display2() called from Parent class by Child Class.')


# class Child(Parent):
#     def __init__(self):
#         print('Child constructor ran...')

#     def display(self, name, age):
#         print(f'My name is {name} and I am {age} years old.')

# parent_obj = Parent()
# child_obj = Child()

# parent_obj.display('Rishabh')
# child_obj.display('Rishabh', 25)
# child_obj.display2()
        

# --------------------------------------------------------------------------


# Multilevel Overiding

# class Parent:
#     def __init__(self):
#         print('Parent constructor ran...')

#     def display(self, name):
#         print(name)

#     def display2(self):
#         print('display2() called from Parent class by GrandChild Class.')


# class Child(Parent):
#     def __init__(self):
#         print('Child constructor ran...')

#     def display(self, name, age):
#         print(f'My name is {name} and I am {age} years old.')

# class GrandChild(Child):
#     def __init__(self):
#         print('Grand Child constructor ran...')

#     def display(self, name, age, occupation):
#         print(f'My name is {name} and I am {age} years old. I work as an {occupation} at Genrosys Mohali.')


# parent_obj = Parent()
# grandchild_obj = GrandChild()

# parent_obj.display('Rishabh')
# grandchild_obj.display('Rishabh', 25, 'Intern')
# grandchild_obj.display2()
        

# --------------------------------------------------------------------------


# Calling Overided Function within child class function

# class Parent:
#     def __init__(self):
#         print('Parent constructor ran...')

#     def display(self, name):
#         print(name)


# class Child(Parent):
#     def __init__(self):
#         print('Child constructor ran...')

#     def display(self, name, age):
#         super().display(name)
#         print(f'My name is {name} and I am {age} years old.')

# parent_obj = Parent()
# child_obj = Child()

# child_obj.display('Rishabh', 25)
        