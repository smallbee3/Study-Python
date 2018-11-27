# -*- coding: utf-8 -*-
# from __future__ import division
import os
import psutil
import random
import time

names = ['최용호', '지길정', '진영욱', '김세훈', '오세훈', '김민우']
majors = ['컴퓨터 공학', '국문학', '영문학', '수학', '정치']

process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss / 1024 / 1024


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.clock()
# people = people_list(1000000)  #1 people_list를 호출
# people = people_generator(1000000)  #1 people_generator 호출
people = people_generator(10)  #1 people_generator 호출
t2 = time.clock()
mem_after = process.memory_info().rss / 1024 / 1024
total_time = t2 - t1


print('시작 전 메모리 사용량: {} MB'.format(mem_before))
print('종료 후 메모리 사용량: {} MB'.format(mem_after))
print('총 소요된 시간: {:.6f} 초'.format(total_time))
print(f'총 소요된 시간: {total_time:.6f} 초')


print()
print(os.getpid)
print(psutil.Process(os.getpid()))
print()

print(people)
print(type(people))

# print generator
for i in people:
    print(i)