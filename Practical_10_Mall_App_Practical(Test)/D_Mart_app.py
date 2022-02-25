import D_mart_module_file

# for items in D-Mart
item_list = []
item = ''

print('\nEnter D-Mart items\n')
D_mart_module_file.item_list_mod(item_list, item)


# for stock count of each item
stock_count_items = []
stock_count_item = ''

print('\nEnter stock item count of each product\n')
D_mart_module_file.stock_count_mod(stock_count_items, stock_count_item, item_list)


# for stock prices of each item
stock_prices = []
prices = ''

print('\nEnter stock price of each product\n')
D_mart_module_file.stock_prices_mod(stock_prices, prices, item_list)


# for selling prices of each item
selling_prices = []
selling_price = ''

print('\nEnter selling price of each product\n')
D_mart_module_file.selling_prices_mod(selling_prices, selling_price, item_list)


# for sold items count
sold_count_items = []
sold_count_item = ''

print('\nEnter sold item count of each product\n')
D_mart_module_file.sold_count_mod(sold_count_items, sold_count_items, item_list)


# salesman information
salesman = input('\nEnter salesman Name:-')

commission = []
for x in range(10):
    commissions = (sold_count_items[x] * selling_prices[x]) * 0.1
    commission.append(commissions)


# for available stock display
available_stock = []
available_stock_items = ''

D_mart_module_file.commission_mod(available_stock, available_stock_items, stock_count_items, sold_count_items)

print('')
print('*'*50)
print('Total Available Stock')
print('*'*50)
for x in range(10):
    D_mart_module_file.available(item_list[x], available_stock[x])


# for all prices of all products
print('*'*50)
print('Arriving prices and Selling prices of each product')
print('*'*50)
for x in range(10):
    D_mart_module_file.item_show(item_list[x], stock_prices[x], selling_prices[x])


# for commission of salesman
print('*'*50)
print('Total Commission to salesman on each product')
print('*' * 50)
for x in range(10):
    D_mart_module_file.total_commission(item_list[x], commission[x])
