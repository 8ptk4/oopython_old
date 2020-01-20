#!/usr/bin/env python3
"""
Handler file
"""

from employee import Employee

persons = []

emil = Employee("Pelle", "Scriptsson", 30000)
mikael = Employee("Mikael", "Roos", 31000)
kenneth = Employee("Kenneth", "Lewenhagen", 75000)
andreas = Employee("Andreas", "Arnesson", 12000)
patrik = Employee("Patrik", "Karlsson", 45000)

persons.append(emil)
persons.append(mikael)
persons.append(kenneth)
persons.append(andreas)
persons.append(patrik)

def add_employee(form):
    """ Add employee to persons """
    persons.append(Employee(
        form["firstname"],
        form["lastname"],
        form["salary"])
                  )

def get_persons():
    """ Return persons """
    return persons
