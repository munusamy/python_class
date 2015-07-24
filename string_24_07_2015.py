Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> first=munu
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    first=munu
NameError: name 'munu' is not defined
s
>>> first='munu'
>>> second='samy'
>>> print(first+second)
munusamy
>>> print(first,second)
munu samy
>>> print(first, second)
munu samy
>>> test='   god is great   '
>>> print(test)
   god is great   
>>> test.capitalize()
'   god is great   '
>>> help(center)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    help(center)
NameError: name 'center' is not defined
>>> help(str.center)
Help on method_descriptor:

center(...)
    S.center(width[, fillchar]) -> str
    
    Return S centered in a string of length width. Padding is
    done using the specified fill character (default is a space)

>>> test.center(2)
'   god is great   '
>>> test.center(5)
'   god is great   '
>>> test.center(20, #)
	    
KeyboardInterrupt
>>> test.center(20, '#')
'#   god is great   #'
>>> test.center(50, '#')
'################   god is great   ################'
>>> test.count()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    test.count()
TypeError: count() takes at least 1 argument (0 given)
>>> test.count(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    test.count(a)
NameError: name 'a' is not defined
>>> test.count(a, 1, 15)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    test.count(a, 1, 15)
NameError: name 'a' is not defined
>>> test.count('a', 1, 15)
1
>>> test.count('g', 0, 20)
2
>>> test.endswith()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    test.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> test.endswith(t, 9, 20)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    test.endswith(t, 9, 20)
NameError: name 't' is not defined
>>> test.endswith('t', 9, 20)
False
>>> test.endswith('t')
False
>>> test.endswith(' ')
True
>>> work='All\tis\tgreat'
>>> print work
SyntaxError: Missing parentheses in call to 'print'
>>> print(work)
All	is	great
>>> work.expandtabs(10)
'All       is        great'
>>> work.expandtabs(20)
'All                 is                  great'
>>> work.find('a')
10
>>> work.find('a', 0, 5)
-1
>>> work.index('is', 3, 10)
4
>>> work.index('is')
4
>>> work.isalnum()
False
>>> work.isalpha()
False
>>> work.islower()
False
>>> w='god'
>>> w.isalpha()
True
>>> w.islower()
True
>>> work.isspace()
False
>>> w.isspace()
False
>>> work.istitle()
False
>>> t='All Is Great'
>>> t.istitle()
True
>>> t.isupper()
False
>>> t.islower()
False
>>> w.islower()
True
>>> w.join('is great')
'igodsgod godggodrgodegodagodt'
>>> w.join(great)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    w.join(great)
NameError: name 'great' is not defined
>>> w.join('great')
'ggodrgodegodagodt'
>>> w.join(' ')
' '
>>> w.join('')
''
>>> w.join('\t')
'\t'
>>> w.join('1')
'1'
>>> w.join('to')
'tgodo'
>>> w.join('12')
'1god2'
>>> w.join('  ')
' god '
>>> print(w)
god
>>> print(t)
All Is Great
>>> t.lower()
'all is great'
>>> t.upper()
'ALL IS GREAT'
>>> w.title()
'God'
>>> w.swapcasae()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    w.swapcasae()
AttributeError: 'str' object has no attribute 'swapcasae'
>>> w.swapcase()
'GOD'
>>> a='All indians scored morethan 99 marks in Maths'
>>> a.isalnum()
False
>>> a.isalpha()
False
>>> a.join('    ')
' All indians scored morethan 99 marks in Maths All indians scored morethan 99 marks in Maths All indians scored morethan 99 marks in Maths '
>>> print(a)
All indians scored morethan 99 marks in Maths
>>> b='god99'
>>> b.isalnum()
True
>>> a.partition('0')
('All indians scored morethan 99 marks in Maths', '', '')
>>> a.partition('a')
('All indi', 'a', 'ns scored morethan 99 marks in Maths')
>>> a.partition('99')
('All indians scored morethan ', '99', ' marks in Maths')
>>> a.replace('indians', 'Indians')
'All Indians scored morethan 99 marks in Maths'
>>> a.replace('r', 'R')
'All indians scoRed moRethan 99 maRks in Maths'
>>> a.replace('r', 'R', 1)
'All indians scoRed morethan 99 marks in Maths'
>>> a.find('a')
8
>>> a.rfind('a')
41
>>> a.rindex('i')
37
>>> a.index('i')
4
>>> a.ljus(70, '#')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.ljus(70, '#')
AttributeError: 'str' object has no attribute 'ljus'
>>> a.ljust(70, '#')
'All indians scored morethan 99 marks in Maths#########################'
>>> a.rjust(80, '@')
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@All indians scored morethan 99 marks in Maths'
>>> a.rpartition('s')
('All indians scored morethan 99 marks in Math', 's', '')
>>> a.lpartition('s')
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.lpartition('s')
AttributeError: 'str' object has no attribute 'lpartition'
>>> a.split()
['All', 'indians', 'scored', 'morethan', '99', 'marks', 'in', 'Maths']
>>> a.rsplit(A)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.rsplit(A)
NameError: name 'A' is not defined
>>> a.rsplit('A')
['', 'll indians scored morethan 99 marks in Maths']
>>> a.rsplit('h')
['All indians scored moret', 'an 99 marks in Mat', 's']
>>> a.rsplit('h',35)
['All indians scored moret', 'an 99 marks in Mat', 's']
>>> a.split(10)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    a.split(10)
TypeError: Can't convert 'int' object to str implicitly
>>> a.split('l', 2)
['A', '', ' indians scored morethan 99 marks in Maths']
>>> a.split('l', 1)
['A', 'l indians scored morethan 99 marks in Maths']
>>> a.lstrip('i')
'All indians scored morethan 99 marks in Maths'
>>> print(a)
All indians scored morethan 99 marks in Maths
>>> a.lstrip('s')
'All indians scored morethan 99 marks in Maths'
>>> a.lstrip('A')
'll indians scored morethan 99 marks in Maths'
>>> a.rstrip('s')
'All indians scored morethan 99 marks in Math'
>>> a.rsplit('i')
['All ', 'nd', 'ans scored morethan 99 marks ', 'n Maths']
>>> a.rsplit('i', 1)
['All indians scored morethan 99 marks ', 'n Maths']
>>> help(str.splitlines)
Help on method_descriptor:

splitlines(...)
    S.splitlines([keepends]) -> list of strings
    
    Return a list of the lines in S, breaking at line boundaries.
    Line breaks are not included in the resulting list unless keepends
    is given and true.

>>> a.splitlines('i')
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a.splitlines('i')
TypeError: an integer is required (got type str)
>>> a.splitlines(1)
['All indians scored morethan 99 marks in Maths']
>>> a.splitlines(2)
['All indians scored morethan 99 marks in Maths']
>>> '''god is great and
I want to be a good king
I want to be a good programmer'''
'god is great and\nI want to be a good king\nI want to be a good programmer'
>>> a.splitlines()
['All indians scored morethan 99 marks in Maths']
>>> c='''god is great and
I want to be a good king
I want to be a good programmer'''
>>> c.splitlines()
['god is great and', 'I want to be a good king', 'I want to be a good programmer']
>>> c.splitlines(2)
['god is great and\n', 'I want to be a good king\n', 'I want to be a good programmer']
>>> c.splitlines(1)
['god is great and\n', 'I want to be a good king\n', 'I want to be a good programmer']
>>> c.splitlines(4)
['god is great and\n', 'I want to be a good king\n', 'I want to be a good programmer']
>>> a.sta
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.sta
AttributeError: 'str' object has no attribute 'sta'
>>> a.startswith('l')
False
>>> a.startswith('l', 1)
True
>>> a.startswith('l', 2)
True
>>> a.startswith('i', 4)
True
>>> a.strip('i')
'All indians scored morethan 99 marks in Maths'
>>> a.strip('i', 1)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a.strip('i', 1)
TypeError: strip() takes at most 1 argument (2 given)
>>> a.zfill(55)
'0000000000All indians scored morethan 99 marks in Maths'
>>> d=a.encode('base64', 'strict')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    d=a.encode('base64', 'strict')
LookupError: 'base64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> d=a.decode(encoding='UTF-8',errors='strict')
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d=a.decode(encoding='UTF-8',errors='strict')
AttributeError: 'str' object has no attribute 'decode'
>>> a.encode('base64','strict')
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.encode('base64','strict')
LookupError: 'base64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> from codecs import encode, decode
>>> d=a.encode('base64','strict')
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    d=a.encode('base64','strict')
LookupError: 'base64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> d=a.encode(hex)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    d=a.encode(hex)
TypeError: encode() argument 1 must be str, not builtin_function_or_method
>>> d=a.encode('hex')
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    d=a.encode('hex')
LookupError: 'hex' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> d=encode('a','hex')
Traceback (most recent call last):
  File "C:\Python34\lib\encodings\hex_codec.py", line 15, in hex_encode
    return (binascii.b2a_hex(input), len(input))
TypeError: 'str' does not support the buffer interface

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    d=encode('a','hex')
TypeError: encoding with 'hex' codec failed (TypeError: 'str' does not support the buffer interface)
>>> encode(c"hi", 'hex')
SyntaxError: invalid syntax
>>> encode(c"hi", "hex")
SyntaxError: invalid syntax
>>> 
