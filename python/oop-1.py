# -*- coding: utf-8 -*-


# class 정의
class Character(object):
    def __init__(self, name, health, damage, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory

    def __repr__(self):
        return self.name


# Character 클래스의 오브젝트 생성
heroes = []

print('[인스턴스 생성]')
a = Character('아이언맨', 100, 200, {'gold': 500, 'weapon': '레이저'})
print(a)
print(type(a), '\n')
print(dir(a))

print(a.name)
print(a.health)
print(a.damage)
print(a.inventory)


heroes.append(a)
heroes.append(Character('데드풀', 300, 30, {'gold': 300, 'weapon': '장검'}))
heroes.append(Character('울버린', 200, 50, {'gold': 350, 'weapon': '클로'}))

monsters = []
monsters.append(Character('고블린', 90, 30, {'gold': 50, 'weapon': '창'}))
monsters.append(Character('드래곤', 200, 80, {'gold': 200, 'weapon': '화염'}))
monsters.append(Character('뱀파이어', 80, 120, {'gold': 1000, 'weapon': '최면술'}))

print('[type 검사]')
print(type(heroes))
print(type(heroes[0]))
print(type(heroes[1]))
print(type(heroes[2]), '\n')

print('[값 검사]')
print(heroes)
print(heroes[0])
print(heroes[1])
print(heroes[2], '\n')


# print(heroes)  # 히어로 리스트 확인
# print(monsters)  # 몬스터 리스트 확인
# del heroes[0]  # 히어로 리스트에서 아이언맨 삭제
# print(heroes)  # 히어로 리스트 재확인


