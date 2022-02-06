import re

# p = re.compile('\d')
# print(p.match('1234'))

p2 = re.compile(r'(\d{4})-(\d{2}|\d{1})-(\d{2}|\d{1})')
# print(p2.match('2022-1-20sda2011-1-23').groups())
print(p2.search('aasdsada2022-1-20sda').groups())

phone = '1881-2345-678 #dasdaasda'
p3 = re.sub('#.*$', '',phone )
p3 = re.sub(r'\D', '', p3)
print(p3)
