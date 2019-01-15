# # -*- coding: utf-8 -*-
# class Person(object):
#     def __init__(self, year, month, day, sex):
#         self.year = year
#         self.month = month
#         self.day = day
#         self.sex = sex
#
#     def __str__(self):
#         return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sex)
#
#
# ssn_1 = '900829-1034356'
# ssn_2 = '051224-4061569'
#
#
# def ssn_parser(ssn):
#     front, back = ssn.split('-')
#     sex = back[0]
#
#     if sex == '1' or sex == '2':
#         year = '19' + front[:2]
#     else:
#         year = '20' + front[:2]
#
#     if (int(sex) % 2) == 0:
#         sex = '여성'
#     else:
#         sex = '남성'
#
#     month = front[2:4]
#     day = front[4:6]
#
#     return year, month, day, sex
#
#
# person_1 = Person(*ssn_parser(ssn_1))
# print(person_1)
#
# person_2 = Person(*ssn_parser(ssn_2))
# print(person_2)


# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return '{}년 {}월 {}일생 {}입니다.'.format(self.year, self.month, self.day, self.sex)

    @classmethod
    def ssn_constructor(cls, ssn):
        front, back = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[:2]
        else:
            year = '20' + front[:2]

        if (int(sex) % 2) == 0:
            sex = '여성'
        else:
            sex = '남성'

        month = front[2:4]
        day = front[4:6]

        print(cls)
        print(type(cls))
        print(dir(cls))

        # 2018.12.02
        # return cls(year, month, day)  # -> TypeError: __init__() missing 1 required positional argument: 'sex'
        return cls(year, month, day, sex)
        # By the result of cls(year, month, day), I can know that cls with arguments call the __init__ method.


ssn_1 = '900829-1034356'
ssn_2 = '051224-4061569'

# 1) Create object through 'class method'
person_1 = Person.ssn_constructor(ssn_1)
print(person_1)
print(type(person_1))

person_2 = Person.ssn_constructor(ssn_2)
print(person_2)
print(type(person_2))


# 2) Create object through 'function' outside of the related class
def ssn_parser(ssn):
    front, back = ssn.split('-')
    sex = back[0]

    if sex == '1' or sex == '2':
        year = '19' + front[:2]
    else:
        year = '20' + front[:2]

    if (int(sex) % 2) == 0:
        sex = '여성'
    else:
        sex = '남성'

    month = front[2:4]
    day = front[4:6]

    return year, month, day, sex


print()
person_1 = Person(*ssn_parser(ssn_1))
print(person_1)
print(type(person_1))

person_2 = Person(*ssn_parser(ssn_2))
print(person_2)
print(type(person_2))
