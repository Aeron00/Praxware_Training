class DataEntry:
    c_name = input("company name:-")
    e_name = input("employee name:-")
    e_id = input("employee id:-")
    mo = int(input("mobile no.:-"))
    add = input("Address:-")
    pos = input("position:-")
    salary = int(input("salary:-"))
    ta = salary * 0.02
    da = salary * 0.05
    hra = salary * 0.2
    pf = salary * 0.15
    total_salary = salary + ta + da + hra - pf


class DataStore(DataEntry):
    def data_store(self):
        class_db = open('class_db.txt', 'w')
        class_db.write(f'\ncompany name   :-  {DataEntry.c_name}')
        class_db.write(f'\nemployee name  :-  {DataEntry.e_name}')
        class_db.write(f'\nemployee id    :-  {DataEntry.e_id}')
        class_db.write(f'\nmobile no.     :-  {DataEntry.mo}')
        class_db.write(f'\nAddress        :-  {DataEntry.add}')
        class_db.write(f'\nposition       :-  {DataEntry.pos}')
        class_db.write(f'\nsalary         :-  {DataEntry.salary}')
        class_db.write(f'\nTA             :-  {DataEntry.ta}')
        class_db.write(f'\nDA             :-  {DataEntry.da}')
        class_db.write(f'\nHRA            :-  {DataEntry.hra}')
        class_db.write(f'\nPF             :-  {DataEntry.pf}')
        class_db.write(f'\nTotal salary   :-  {DataEntry.total_salary}')
        class_db.close()

    def data_saw(self):
        class_db = open('class_db.txt', 'r')
        for x in range(12):
            print(f'{class_db.readline(100)}')
        class_db.close()


obj = DataStore()
obj.data_store()
obj.data_saw()

