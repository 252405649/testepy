class Player():     #定义一个类
    def __init__(self, name, hp, occu):
        self.name = name   #变量被称作属性
        self.hp = hp
        self.occu = occu
    #定义一个方法
    def print_role(self):
        print('% s: %s %s' %(self.name, self.hp, self.occu))

    def updateName(self, newName):
        self.name = newName

# 定义怪物属性
class Monster():
    def __init__(self, hp=100):
        self.hp = hp
    def run(self):
        print('移动到某个位置')

# 普通怪物
class Animals(Monster):
    def __init__(self, hp=10):
       super().__init__(hp)

# boss级别的怪物
class Boss(Monster):
    pass

a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(1)
print(a2.hp)
print(a2.run())
# # 类的实例化
# user1 = Player('dmj', 100, 'war')
# user2 = Player('SLX', 120, 'master')
#
# user1.print_role()
# user1.updateName('zzz')
# user1.print_role()
# user2.print_role()