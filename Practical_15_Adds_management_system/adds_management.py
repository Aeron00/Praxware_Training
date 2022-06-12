title = []
detail = []
prize = []
quantity = []
budget = []
phase_select = []

print('Normal time'.center(100))
print('\nPhase 1:- 23 to 24, 1 to 2')
print('Phase 2:- 3 to 6')
print('Phase 3:- 7 to 10')
print('Phase 4:- 11 to 14')
print('Phase 5:- 15 to 18')
print('\nNormal time prize = 100k\n')
print('Prime time'.center(100))
print('Phase 6:- 19 to 22')
print('\nPrime time prize = 200k')


def phase(i):
    print('Advertise name:', title[i])
    print('Details of Advertisement:', detail[i])
    print('Prize of product:', prize[i])
    print('Quantity of product:', quantity[i])


advertise = int(input('\nHow many advertisement do want to add:-'))
for x in range(advertise):
    print('\n')
    print('Enter details of advertisement'.center(100))
    title.append(input('\nEnter title of your advertisement:-'))
    detail.append(input('Enter details about advertisement:-'))
    prize.append(int(input('Enter prize of the item you advertise:-')))
    quantity.append(int(input('Enter quantity of items you advertise as per prize:-')))
    budget.append(int(input('Enter your budget for advertisement:-')))
    phase_select.append(int(input('\nIn which phase do want to show advertisement(please select any number):- Phase ')))


for x in range(len(phase_select)):
    if phase_select[x] == 1:
        print(phase(x))

for x in range(len(phase_select)):
    if phase_select[x] == 2:
        print(phase(x))

for x in range(len(phase_select)):
    if phase_select[x] == 3:
        print(phase(x))

for x in range(len(phase_select)):
    if phase_select[x] == 4:
        print(phase(x))

for x in range(len(phase_select)):
    if phase_select[x] == 5:
        print(phase(x))

for x in range(len(phase_select)):
    if phase_select[x] == 6:
        print(phase(x))


# time = float(input('What time is it:-'))
# if time >= 23 <= 24 or time >= 1 <= 2:
# elif time >= 3 <= 6:
#     for x in range(len(phase_select)):
#         if phase_select[x] == 2:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 3:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 4:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 5:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 6:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 1:
#             print(phase(x))
#
# elif time >= 7 <= 10:
#     for x in range(len(phase_select)):
#         if phase_select[x] == 3:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 4:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 5:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 6:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 1:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 2:
#             print(phase(x))
#
# elif time >= 11 <= 14:
#     for x in range(len(phase_select)):
#         if phase_select[x] == 4:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 5:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 6:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 1:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 2:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 3:
#             print(phase(x))
#
# elif time >= 15 <= 18:
#     for x in range(len(phase_select)):
#         if phase_select[x] == 5:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 6:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 1:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 2:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 3:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 4:
#             print(phase(x))
#
# elif time >= 19 <= 22:
#     for x in range(len(phase_select)):
#         if phase_select[x] == 6:
#             print(phase(x))
#     for x in range(len(phase_select)):
#         if phase_select[x] == 1:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 2:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 3:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 4:
#             print(phase(x))
#
#     for x in range(len(phase_select)):
#         if phase_select[x] == 5:
#             print(phase(x))
