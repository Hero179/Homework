def add(a, b):
    if a > b:
        print(a)
    else:
        print(b)

add(5, 3)

print('\n')

def add(a, b):
    if abs(a-b) == 135:
        print('Yes')
    else:
        print('No')

add(1, 2)

print('\n')

def season(month):
    if 3 <= month <= 5:
        print('Spring')
    elif 6 <= month <= 8:
        print('Summer')
    elif 9 <= month <= 11:
        print('Autumn')
    elif month == 12 or month == 1 or month == 2:
        print('Winter')

season(2)

print('\n')

def add(a, b, c):
    if a + b + c > 10:
        print('Yes')
    else:
        print('No')

add(1, 2, 3)