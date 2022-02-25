def available(x, y):
    print(x, ':', y)


def item_show(x, y, z):
    print(x, ':', y, ':', z)


def total_commission(x, y):
    print(x, ':', y)


def item_list_mod(a, b):
    for x in range(10):
        b = input(F'Enter item{x} :-')
        a.append(b)
    return a, b


def stock_count_mod(a, b, c):
    for x in range(10):
        b = int(input(F'Enter Count of {c[x]} in stock:-'))
        a.append(b)
    return a, b, c


def stock_prices_mod(a, b, c):
    for x in range(10):
        b = int(input(F'Enter stock price for {c[x]} :-'))
        a.append(b)
    return a, b, c


def selling_prices_mod(a, b, c):
    for x in range(10):
        b = int(input(F'Enter selling price for {c[x]} :-'))
        a.append(b)
    return a, b, c


def sold_count_mod(a, b, c):
    for x in range(10):
        b = int(input(F'Enter count of  {c[x]} sold :-'))
        a.append(b)
    return a, b, c


def commission_mod(a, b, c, d):
    for x in range(10):
        b = (c[x] * d[x]) * 0.1
        a.append(b)
    return a, b, c, d


# list_item_count = int(input('Enter How many items do you want to enter in list :-'))
#
# new_list = []
#
# for x in range(0, list_item_count):
#     list_item = input('Enter list item :-')
#     new_list.append(list_item)
# print(new_list)
# print(type(new_list))
