class Employee(object):
    raise_amount = 1.1
    num_of_emps = 0  # 1 클래스 변수 정의

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

        print('self', self.num_of_emps)
        Employee.num_of_emps += 1  # 2 인스턴스가 생성될 때마다 1씩 증가
        # self.num_of_emps += 1    # This is wrong !
                                   # self.num-of_emps can get the value of class variable 'num_of_emps'
                                   # But it is impossible to save a value to class variable using self(instance variable)

    def __del__(self):
        Employee.num_of_emps -= 1  # 3 인스턴스가 제거될 때마다 1씩 감소
        # self.num_of_emps -= 1     # This is wrong !

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # 1 인스턴스 변수부터 참조를 합니다.


print(Employee.num_of_emps)  # 처음 직원 수
emp_1 = Employee('Sanghee', 'Lee', 50000)  # 직원 1명 입사
emp_2 = Employee('Minjung', 'Kim', 60000)  # 직원 1명 입사
print(Employee.num_of_emps)  # 직원 수 확인

del emp_1  # 직원 1명 퇴사
del emp_2  # 직원 1명 퇴사
print(Employee.num_of_emps)  # 직원 수 확인
