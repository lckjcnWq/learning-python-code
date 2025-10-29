t1  = (100,200,300)
# 定义一个四元组
t2 = ('骆昊', 45, True, '四川成都')

print(type(t1))
print(type(t2))

print(len(t1))
print(t1[0])

print(t2[:2])

for elem in t1:
    print(elem)


s = 'hello, world'
print(s.find('or'))
print(s.index('or'))
print(s.count('or'))
print(s.startswith('hel'))

set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True

person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)

person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

for key in person:
    print(f'{key}:\t{person[key]}')