from time import sleep


class Details:
    def __init__(self, names, adds, purposes, ids, times, solutions, lists):
        meetings = int(input('Enter how many meeting we have today:-'))
        self.meeting = meetings
        for x in range(meetings):
            print('\n-:Enter details:-'.center(100))
            name = input('\nEnter your name:-')
            add = input('Enter your city and state:-')
            purpose = input('Enter purpose of meeting:-')
            print(f'Your allocated id is {x + 1}')
            self.names = names
            self.adds = adds
            self.purposes = purposes
            self.ids = ids
            self.times = times
            self.solutions = solutions
            self.lists = lists
            names.append(name)
            adds.append(add)
            purposes.append(purpose)
            ids.append(x + 1)


class Data(Details):
    def show(self):
        print('\nToday_s meeting persons details\n')
        for x in range(self.meeting):
            lst = [f'Name:{self.names[x]}', f'Address:{self.adds[x]}', f'Purpose:{self.purposes[x]}', f'Id:{self.ids[x]}']
            self.lists.append(lst)
            print(lst)

    def select(self):
        for x in range(self.meeting):
            selection = int(input('\nplease select any one id from above list for further process:-'))
            for y in range(self.meeting):
                if selection == y+1:
                    print(self.lists[y])
                    time = int(input('Select session time:-'))
                    self.times.append(time)
                    solution = input('Enter solution for his purpose:-')
                    self.solutions.append(solution)
                    sleep(time)
                    self.lists[y] = ['This meeting is done']
                elif selection >= self.meeting+1:
                    print('Select proper id!!!'.center(50))
                    break
            print('\n')
            print('Remaining meetings'.center(50))
            for z in range(len(self.lists)):
                print(f'\n{self.lists[z]}')

    def meet(self):
        print('Visited persons today'.center(50))
        for x in range(self.meeting):
            print([f'Name:{self.names[x]}', f'Address:{self.adds[x]}', f'Purpose:{self.purposes[x]}', f'Id:{self.ids[x]}', f'Solution:{self.solutions[x]}', f'Session time:{self.times[x]}'])


aeron = Data([], [], [], [], [], [], [])
aeron.show()
aeron.select()
aeron.meet()
