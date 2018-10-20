# sprint2-TDD
# sprint2-TDD
Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses.
How to accomplish this in Python? The answer is – by convention. By prefixing the name of your member
with a single underscore, you’re telling others “don’t touch this, unless you’re a subclass”.
For ex : _name is a protected attribute.

By declaring your data member private you mean, that nobody should be able to access it from
outside the class, i.e. strong you can’t touch this policy. Python supports a technique called
name mangling. This feature turns every member name prefixed with at least two underscores and suffixed
with at most one underscore into _<className><memberName> .
For ex : __name is a private attribute and if it is member of class A(), it can be accessed as A._A__name

The default can be overridden by defining __slots__ in a new-style class definition. The __slots__ declaration
takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each
variable. Space is saved because __dict__ is not created for each instance.
This class variable can be assigned a string, iterable, or sequence of strings with variable names
used by instances.
