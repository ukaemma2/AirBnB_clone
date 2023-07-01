def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger kind", "It's very runny, sir.",
           "It's really very, VERY runny, sir.", "my type is Victoria",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    

# args = [3, 6]
# print(list(range(*args)))


# # # list of items'
# list2 = ['cat', 'bat', 'mat', 'cat', 'pet', 'bat']
 
# # Will print the index of 'bat' in list2
# list2.pop()
# print(list2)

# combo = []
# x = [1,2,3, 4,7, 9 ,0]
# y = [4, 1, 4,6]

# for i in x:
#     for t in y:
#         if i != t:
#             combo.append((i,t ))

# print(combo)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# transposed = []

# for i in range(4):

#     transposed_row = []

#     for row in matrix:
#         transposed_row.append(row[i])
#     print(transposed_row)
#     transposed.append(transposed_row)
# print(transposed)

# print(list(zip(*matrix)))

# lst = ['u', 'i', 'o', 'l','t','e','r','r']

# del lst[2:4]
# print(lst)

# del lst[:]
# print(lst)

# dit = {
#     '': 'h',
#     'k': { },
# }

# t = 2.77, 'emma', 'Ola', 55, 'uka'
# t[1] = 'Peter'
# print(t)

# dt = dict([('firstName', 'Emmanuel'), ('LastName', 'John') ])
# print(dt)

# nm = (1,2,3,4)

# print({x: x**2 for x in nm})

# list_of_index = [4, 6, 90, 22, 5, 68, 1, 2, 3, 10 ]

# print(list_of_index.index(68, 5, 10 ))

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {}?  It is {}.'.format(q, a))


# year = 1016
# event= 'Referendum'
# result = F'Results of the {year} {event}' 
# print (result)

# yes_votes = 42_572_654
# no_votes = 43_132_495

# percentage = yes_votes / no_votes
# yes_v = '{} yes votes {}'.format(yes_votes, percentage)

# print (yes_v)

# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + str(x) + ', and y is ' + str(y) + '...'
# print(s)

# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)          

# import math
# print(f'The value of pi is approximately {math.pi:.5f}.')

# animals = 'eels'
# print(f'My hovercraft is full of {animals!s}.')

# print(f'My hovercraft is full of {animals!r}.')

name = ['Beans', 'Spiders', 200, 500, 88, [2, 4, 6, 6], 'Chika', 'Finn']

more = 'I had a {3} today but {0} took about {1} plates to {4} meanwhile {2} plates were rejected'.format(name[0], name[1], name[4], name[6], name[5][3])
print (more)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
ww = 'Dcab: {0[Dcab]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'.format(table)
print (ww)
