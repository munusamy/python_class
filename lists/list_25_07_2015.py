Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[1,2,3,4,5,6]
>>> len(list)
6
>>> list.append(7)
>>> print(list)
[1, 2, 3, 4, 5, 6, 7]
>>> list.pop()
7
>>> print(list)
[1, 2, 3, 4, 5, 6]
>>> list.extend('a')
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print(list)
[1, 2, 3, 4, 5, 6, 'a']
>>> list.index(3)
2
>>> list.insert(2, 'b')
>>> print(list)
[1, 2, 'b', 3, 4, 5, 6, 'a']
>>> list.index(0)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list.index(0)
ValueError: 0 is not in list
>>> list.index(1)
0
>>> list.remove('a')
>>> print(list)
[1, 2, 'b', 3, 4, 5, 6]
>>> list.reverse()
>>> print(list)
[6, 5, 4, 3, 'b', 2, 1]
>>> print(list.sort())
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(list.sort())
TypeError: unorderable types: str() < int()
>>> list.sort()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list.sort()
TypeError: unorderable types: str() < int()
>>> A=['a', 'b', 'd', 'f', 'e', 'i', 'j']
>>> A.sort()
>>> print(A)
['a', 'b', 'd', 'e', 'f', 'i', 'j']
>>> tuple(A)
('a', 'b', 'd', 'e', 'f', 'i', 'j')
>>> print(A)
['a', 'b', 'd', 'e', 'f', 'i', 'j']
>>> list.count()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list.count()
TypeError: count() takes exactly one argument (0 given)
>>> list.count(3)
1
>>> list.del('b')
SyntaxError: invalid syntax
>>> del(list[2])
>>> print(list)
[6, 5, 3, 'b', 2, 1]
>>> print(A+list)
['a', 'b', 'd', 'e', 'f', 'i', 'j', 6, 5, 3, 'b', 2, 1]
>>> print((A+list).sort())
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print((A+list).sort())
TypeError: unorderable types: int() < str()
>>> testing=set(list)
>>> print(testing)
{1, 2, 3, 5, 6, 'b'}
>>> print(list)
[6, 5, 3, 'b', 2, 1]
>>> 2 in testing
True
>>> 'b' in testing
True
>>> print(list - A)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(list - A)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> testing
{1, 2, 3, 5, 6, 'b'}
>>> a=(1, 2, 'b', 'c')
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(a)
TypeError: 'list' object is not callable
>>> a.list()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.list()
AttributeError: 'tuple' object has no attribute 'list'
>>> print(a)
(1, 2, 'b', 'c')
>>> del list
>>> list(a)
[1, 2, 'b', 'c']
>>> 
