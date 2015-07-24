Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> test="This is working"
>>> test[0:]
'This is working'
>>> test[-1:-3]
''
>>> test[-1:4]
''
>>> test[0:5]=Munu
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    test[0:5]=Munu
NameError: name 'Munu' is not defined
>>> test[0:5]
'This '
>>> test[0:4]
'This'
>>> test[0:4]=work
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    test[0:4]=work
NameError: name 'work' is not defined
>>> test[0:4].insert('This', 'Munu')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    test[0:4].insert('This', 'Munu')
AttributeError: 'str' object has no attribute 'insert'
>>> test[0:4]
'This'
>>> test[0:4]="That"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    test[0:4]="That"
TypeError: 'str' object does not support item assignment
>>> test.list[]
SyntaxError: invalid syntax
>>> list(test)
['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g']
>>> list[0:4]=That
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list[0:4]=That
NameError: name 'That' is not defined
>>> list[0:4]=['T', 'h', 'a','t']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list[0:4]=['T', 'h', 'a','t']
TypeError: 'type' object does not support item assignment
>>> test[0:4]=That
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    test[0:4]=That
NameError: name 'That' is not defined
>>> test[0:4]=['T','h','a','t']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    test[0:4]=['T','h','a','t']
TypeError: 'str' object does not support item assignment
>>> del test
>>> test="Munu is working"
>>> list(test)
['M', 'u', 'n', 'u', ' ', 'i', 's', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g']
>>> test[0:4]
'Munu'
>>> test[0:1]="Mun"
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    test[0:1]="Mun"
TypeError: 'str' object does not support item assignment
>>> test
'Munu is working'
>>> test1=list(test)
>>> test1
['M', 'u', 'n', 'u', ' ', 'i', 's', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g']
>>> test1[0:4]=['M','u','n','u','s']
>>> test1
['M', 'u', 'n', 'u', 's', ' ', 'i', 's', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g']
>>> test2=str(test1)
>>> test2
"['M', 'u', 'n', 'u', 's', ' ', 'i', 's', ' ', 'w', 'o', 'r', 'k', 'i', 'n', 'g']"
>>> test
'Munu is working'
>>> a="All is\tgood"
>>> print(a)
All is	good
>>> b="All is\sgood"
>>> print(b)
All is\sgood
>>> c="All is \s good"
>>> print(c)
All is \s good
>>> d="All is \n good"
>>> print(d)
All is 
 good
>>> e="This is\s working"
>>> print(e)
This is\s working
>>> f="those are \\s working"
>>> print(f)
those are \s working
>>> print(d)
All is 
 good
>>> g="This is r"\n" working"
SyntaxError: unexpected character after line continuation character
>>> g="This is r"(\n)" working"
SyntaxError: unexpected character after line continuation character
>>> h="This is r(\n) working"
>>> print(h)
This is r(
) working
>>> i="This is r'\n' working"
>>> print(i)
This is r'
' working
>>> abc="This is r"\n" great"
SyntaxError: unexpected character after line continuation character
>>> abc=r"this is \n working"
>>> print(abc)
this is \n working
>>> abc.capitalize()
'This is \\n working'
>>> file="this has to work"
>>> file.center(30,#)

	    
KeyboardInterrupt
>>> testing="Good"
>>> testing.center(20, $)
SyntaxError: invalid syntax
>>> testing.center(20,$)
SyntaxError: invalid syntax
>>> testing.center(20,'$')
'$$$$$$$$Good$$$$$$$$'
>>> sub="This is good, this is great, this is awesome"
>>> sub.count(this,0,50)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sub.count(this,0,50)
NameError: name 'this' is not defined
>>> sub.count('this',0,50)
2
>>> sub.count('this',0, 100)
2
>>> sub.count('this',0,20)
1
>>> sub.count('This',0,10)
1
>>> name="Munu"
>>> name.encode()
b'Munu'
>>> name.encode('base64', 'strict')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    name.encode('base64', 'strict')
LookupError: 'base64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> name=munu
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    name=munu
NameError: name 'munu' is not defined
>>> name1=munu
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    name1=munu
NameError: name 'munu' is not defined
>>> name="Munu"
>>> name.encode(base64, strict)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    name.encode(base64, strict)
NameError: name 'base64' is not defined
>>> name.encode('base64', strict)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    name.encode('base64', strict)
NameError: name 'strict' is not defined
>>> name.encode('base64', 'strict')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    name.encode('base64', 'strict')
LookupError: 'base64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> name.encode('UTF-8')
b'Munu'
>>> name.encode('UTF-8', 'strict')
b'Munu'
>>> name.decode('UTF-8', 'strict')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    name.decode('UTF-8', 'strict')
AttributeError: 'str' object has no attribute 'decode'
>>> name.encode('base-64', 'strict')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name.encode('base-64', 'strict')
LookupError: 'base-64' is not a text encoding; use codecs.encode() to handle arbitrary codecs
>>> name.encode('base32', 'strict')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    name.encode('base32', 'strict')
LookupError: unknown encoding: base32
>>> name.encode('UTF-32','strict')
b'\xff\xfe\x00\x00M\x00\x00\x00u\x00\x00\x00n\x00\x00\x00u\x00\x00\x00'
>>> name1=name.encode('UTF-32','strict')
>>> print(name1)
b'\xff\xfe\x00\x00M\x00\x00\x00u\x00\x00\x00n\x00\x00\x00u\x00\x00\x00'
>>> name1.decode()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    name1.decode()
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
>>> 
>>> name1.decode('UTF-32')
'Munu'
>>> name.isalnum()
True
>>> print(name)
Munu
>>> name.isnum()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    name.isnum()
AttributeError: 'str' object has no attribute 'isnum'
>>> alp="this is great"
>>> alp.isalnum
<built-in method isalnum of str object at 0x00000000037ADE70>
>>> alp.isalnum()
False
>>> alp.isnum()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    alp.isnum()
AttributeError: 'str' object has no attribute 'isnum'
>>> alp.isnumeric
<built-in method isnumeric of str object at 0x00000000037ADE70>
>>> alp.isnumeric()
False
>>> alp.isalpha()
False
>>> alp.isalpha()
False
>>> alp.isalpha()
False
>>> offer="this is great work 123"
>>> offer.isalpha()
False
>>> offer.isalnum()
False
>>> offer.isnumeric()
False
>>> str="123abc"
>>> str.isalpha()
False
>>> str.isalnum()
True
>>> str.isnumeric()
False
>>> work="this has to work"
>>> work.isalpha()
False
>>> work.isnumeric)()
SyntaxError: invalid syntax
>>> work.isnumeric()
False
>>> work.isalnum()
False
>>> work1="thisisworinggreat"
>>> work1.isalpha()
True
>>> work.isspace()
False
>>> work.isspace()
False
>>> num=123
>>> num.isnumeric()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    num.isnumeric()
AttributeError: 'int' object has no attribute 'isnumeric'
>>> num.isdigit()
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    num.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> num="123"
>>> num.isnumeric()
True
>>> num.isdigit()
True
>>> num1="123"
>>> num1.isdigit()
True
>>> num2="ab123"
>>> num2.isdigit()
False
>>> num2.isnumeric()
False
>>> num2.isalnum()
True
>>> nam="Great"
>>> nam.lower()
'great'
>>> nam.upper()
'GREAT'
>>> nam.islower()
False
>>> nam1="Great123!!!"
>>> nam1.lower
<built-in method lower of str object at 0x00000000037A6630>
>>> nam1.lower()
'great123!!!'
>>> nam1.upper()
'GREAT123!!!'
>>> nam1.islower()
False
>>> t=nam1.lower()
>>> t.islower()
True
>>> t.isupper()
False
>>> u=nam1.upper()
>>> n.isupper()
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    n.isupper()
NameError: name 'n' is not defined
>>> u.isupper()
True
>>> te=" "
>>> te.isspace()
True
>>> len(anme)
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    len(anme)
NameError: name 'anme' is not defined
>>> len(nam)
5
>>> te.len()
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    te.len()
AttributeError: 'str' object has no attribute 'len'
>>> max(nam)
't'
>>> min(nam)
'G'
>>> tes="all is greatzzand"
>>> max(tes)
'z'
>>> min(tes)
' '
>>> tes1="allisgreatsayandzthi"
>>> max(tes1)
'z'
>>> min(tes1)
'a'
>>>  Q
