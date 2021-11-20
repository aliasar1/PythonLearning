import re

str = '''
Hello I am ali_123@gmai.com
Applied to 12ba.mae@malx.pk
java.123.21ac@mail.com
'''

l1 = re.findall(r'\S+@\S+', str)
file = 'OOP\emails.txt'
with open(file, 'a') as f:
    for emails in l1:
        f.write(emails + '\n')
