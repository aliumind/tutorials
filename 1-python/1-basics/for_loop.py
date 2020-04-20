l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('You can check the type of l this way -> {0}'.format(type(l)))

print('SIMPLE LOOP')
for item in l:
    print(item)
print()

print('EVEN LOOP')
for item in l:
    if item % 2 == 0:
        print('> Even number skipped')
        continue
    print(item)
print()

print('BREAK LOOP')
for item in l:
    if(item == 6):
        print('I break the loop on the number 6')
        break
    print(item)
