Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> book={'social': 2, 'english':3}
>>> print(book)
{'english': 3, 'social': 2}
>>> book[social]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    book[social]
NameError: name 'social' is not defined
>>> book{social}
SyntaxError: invalid syntax
>>> book(social)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    book(social)
NameError: name 'social' is not defined
>>> book['social']
2
>>> book{'social'}
SyntaxError: invalid syntax
>>> book('social')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    book('social')
TypeError: 'dict' object is not callable
>>> book['social']=5
>>> print(book)
{'english': 3, 'social': 5}
>>> for keys() in book:
	print(keys)
	
SyntaxError: can't assign to function call
>>> for keys in book:
	print(keys)

	
english
social
>>> book.keys()
dict_keys(['english', 'social'])
>>> book.del()
SyntaxError: invalid syntax
>>> del book
>>> print(book)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(book)
NameError: name 'book' is not defined
>>> book={'science':'5', 'maths': '10'}
>>> print(book)
{'maths': '10', 'science': '5'}
>>> book.clear()
>>> print(book)
{}
>>> 
