import datetime
import random
import django
import os

first_names = ['Иван', 'Андрей', 'Степан', 'Алексей', 'Мансур', 'Максим', 'Александр']
last_names = ['Иванов', 'Попово', 'Сидоров', 'Петраков']
patronymics = ['Иванович', 'Андреевич', 'Степанович', 'Алексеевич', 'Максимович', 'Александрович']


def generate_employees():
    from apps.employees.models import Employee, Position, Division

    position = Position.objects.create(name='Работник')
    counter = 0
    for root in range(1, 6):
        parent = Division.objects.create(name=f'Подразделение {root}')
        for employee in range(2000):
            Employee.objects.create(
                full_name=' '.join([random.choice(last_names), random.choice(first_names),
                                    random.choice(patronymics)]),
                position=position,
                date_employment=datetime.date.today(),
                salary=random.randint(50000, 100000),
                division=parent
            )
            counter += 1
            print(f'Employee #{counter} - add')

        for node in range(1, 5):
            parent = Division.objects.create(name=f'Подразделение {root}.{".".join(["1" for _ in range(1, node + 1)])}',
                                             parent=parent)
            for employee in range(2000):
                Employee.objects.create(
                    full_name=' '.join([random.choice(last_names), random.choice(first_names),
                                        random.choice(patronymics)]),
                    position=position,
                    date_employment=datetime.date.today(),
                    salary=random.randint(50000, 100000),
                    division=parent
                )
                counter += 1
                print(f'Employee #{counter} - add')


if __name__ == '__main__':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
    django.setup()
    generate_employees()
