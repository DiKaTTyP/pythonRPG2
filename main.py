import random
import time
Classs = ["Маг","Танк"]#,"Лучник","Целитель"]
Type= ["Огонь","Холод","Яд"]
atack = ''
gg = 0
class RPG():
    def __init__(self,name,Class):
        self.name = name
        self.Class = Class
        if name == "Компьютер":
            print(f"Персонаж {self.name} создан, класс: {self.Class}")
        else:
            print(f"Персонаж {self.name} создан, класс: {self.Class}.Вывести данные о персонаже?")
class Mage(RPG):
    def __init__(self,name,Class,HP,DP,punch,atack_type,HP1,DP1,punch1,atack_type1,Class1,gg,person):
        self.gg = gg
        self.name = name
        self.Class = Class
        self.HP = HP
        self.DP = DP
        self.punch = punch
        self.atack_type = atack_type
        self.HP1 = HP1
        self.DP1 = DP1
        self.punch1 = punch1
        self.atack_type1 = atack_type1
        self.Class1 = Class1
        self.person = person
    def info(self):
        print(f"Имя персонажа: {self.name} Класс персонажа: { self.Class} Здоровье персонажа: {self.HP} Броня персонажа:{ self.DP} Урон персонажа: {self.punch} Тип урона персонажа: {self.atack_type}")

    def Atack(self):
        if self.atack_type1 == 'Огонь':
            self.atack = self.punch + 4
        elif self.atack_type1 == 'Холод':
            self.atack = self.punch + 3
        else:
            self.atack = self.punch + 6
        if self.Class1 == "Маг":
            if self.atack_type1 == 'Огонь':
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == 'Холод':
                self.atack1 = self.punch1 + 3
            else:
                self.atack1 = self.punch1 + 6
            if self.person == 1:
                print(f"Урон противника равен: {self.atack}")
            else:
                print(f"Ваш урон равен : {self.atack}")
        else:
            self.atack1 = self.punch1
            if self.person == 1:
                print(f"Урон противника равен: {self.atack}")
            else:
                print(f"Ваш урон равен : {self.atack}")
    def Defence(self):
        if self.person == 1:
            print(f"Здоровье противника равно: {self.HP}")
        else:
            print(f"Ваше здоровье равно: {self.HP}")
        if self.atack1 <self.DP:
            print("Персонаж противника слишком слаб, вы забрали все его сокровища")
            self.HP = 0
            self.HP1 = 0
            self.gg = 1
        else:
            if self.HP > (self.atack1 - self.DP):
                self.HP = self.HP - (self.atack1 - self.DP)
                if self.person == 1:
                    print(f"Вы нанесли противнику {(self.atack1) - self.DP} урона, его здоровье равно:{self.HP}")
                else:
                    print(f"Вам был нанесен урон {(self.atack1) - self.DP}, ваше здоровье равно:{self.HP}")
            else:
                if self.person == 1:
                    if (self.atack1 - self.DP -self.HP) > (self.atack1 - self.DP -self.HP) :
                        print("Игра окончена.Ваш персонаж был убит и ограблен")
                    else:
                        print("Игра окончена.Ваш персонаж одолел противника и пополнил запасы сокровищ")
                    self.HP = 0
                    self.HP1 = 0
                    self.gg=1
                else:
                    if (self.atack1 - self.DP -self.HP) > (self.atack1 - self.DP -self.HP) :
                        print("Игра окончена.Ваш персонаж одолел противника и пополнил запасы сокровищ")
                    else:
                        print("Игра окончена.Ваш персонаж был убит и ограблен")

                    self.HP = 0
                    self.HP1 = 0
                    self.gg=1

class Tank(RPG):
    def __init__(self, name, Class, HP, DP, punch, atack_type, HP1, DP1, punch1, atack_type1, Class1, gg,person):
        self.gg = gg
        self.name = name
        self.Class = Class
        self.HP = HP
        self.DP = DP
        self.punch = punch
        self.atack_type = atack_type
        self.HP1 = HP1
        self.DP1 = DP1
        self.punch1 = punch1
        self.atack_type1 = atack_type1
        self.Class1 = Class1
        self.person = person

    def info(self):
        print(f"Имя персонажа: {self.name} Класс персонажа: { self.Class} Здоровье персонажа: {self.HP} Броня персонажа:{ self.DP} Урон персонажа: {self.punch} Тип урона персонажа: {self.atack_type}")

    def Atack(self):
        self.atack = self.punch

        if self.Class1 == 'Маг':
            if self.atack_type1 == 'Огонь':
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == 'Холод':
                self.atack1 = self.punch1 + 3
            else:
                self.atack1 = self.punch1 + 6
            if self.person == 1:
                print(f"Урон противника равен: {self.atack}")
            else:
                print(f"Ваш урон равен : {self.atack}")
        else:
            self.atack1 =self.punch1
            if self.person == 1:
                print(f"Урон противника равен: {self.atack}")
            else:
                print(f"Ваш урон равен : {self.atack}")


    def Defence(self):
        if self.person == 1:
            print(f"Здоровье противника равно: {self.HP}")
        else:
            print(f"Ваше здоровье равно: {self.HP}")
        if self.atack1 <self.DP:
            print("Персонаж противника слишком слаб, вы забрали все его сокровища")
            self.HP = 0
            self.HP1 = 0
            self.gg = 1
        else:
            if self.HP > (self.atack1 - self.DP):
                self.HP = self.HP - (self.atack1 - self.DP)
                if self.person == 1:
                    print(f"Вы нанесли противнику {(self.atack1) - self.DP} урона, его здоровье равно:{self.HP}")
                else:
                    print(f"Вам был нанесен урон {(self.atack1)-self.DP}, ваше здоровье равно:{self.HP}")
            else:
                if self.person == 1:
                    if (self.atack1 - self.DP - self.HP) > (self.atack1 - self.DP - self.HP):
                        print("Игра окончена.Ваш персонаж был убит и ограблен")
                    else:
                        print("Игра окончена.Ваш персонаж одолел противника и пополнил запасы сокровищ")
                    self.HP = 0
                    self.HP1 = 0
                    self.gg = 1
                else:
                    if (self.atack1 - self.DP - self.HP) > (self.atack1 - self.DP - self.HP):
                        print("Игра окончена.Ваш персонаж одолел противника и пополнил запасы сокровищ")
                    else:
                        print("Игра окончена.Ваш персонаж был убит и ограблен")
                    self.HP = 0
                    self.HP1 = 0
                    self.gg = 1


print("Игра против компьютера/ игра с игроком?")
a=input()
if a == '1':
    print("Введите имя персонажа: ")
    name = input()
    b= Classs[random.randint(0,len(Classs)-1)]
    p1 = RPG('Компьютер',b)
    if b=="Маг":
        HP1= random.randint(125,250)
        DP1 = random.randint(5,15)
        punch1 = random.randint(25,45)
        atack_type1 = Type[random.randint(0,len(Type)-1)]
#   elif b=="":

#    elif b=="":

    else:
        HP1= random.randint(225,400)
        DP1 = random.randint(10,25)
        punch1 = random.randint(15,25)
        atack_type1 = "Площадь"
    print(f'Выберите класс персонажа из предложенных:{Classs}')
    c= input()
    if c=="Маг":
        p2=RPG(name,c)
        HP2= random.randint(125,250)
        DP2 = random.randint(5,15)
        punch2 = random.randint(25,45)
        atack_type2 = Type[random.randint(0,len(Type)-1)]

#   elif b=="":

#    elif b=="":

    elif c == "Танк":
        p2 = RPG(name, c)
        HP2 = random.randint(225,400)
        DP2 = random.randint(10,25)
        punch2 = random.randint(15,25)
        atack_type2 = "Площадь"
    else:
        print("Такого класса не существует")
    if b == "Танк":
        person1 = Tank('Компъютер', b, HP1, DP1, punch1, atack_type1,HP2, DP2, punch2, atack_type2,c,gg,1)
    else:
        person1 = Mage('Компъютер', b, HP1, DP1, punch1, atack_type1, HP2, DP2, punch2, atack_type2, c,gg,1)
    if c == "Маг":
        j = input()
        person2 = Mage(name, c, HP2, DP2, punch2, atack_type2,HP1, DP1, punch1, atack_type1,b,gg,2)
        if j == "Да" or j == "да":
            person2.info()
    else:
        j = input()
        person2 = Tank(name, c, HP2, DP2, punch2, atack_type2, HP1, DP1, punch1, atack_type1, b,gg,2)
        if j == "Да" or j == "да":
            person2.info()
print(f"Ваше здоровье равно: {person1.HP1}")
person1.Atack()
while person1.HP >0 and person2.HP>0:
    if person1.HP <=0 or person2.HP<=0:
        break
    time.sleep(1)
    person2.Atack()
    person1.Defence()
    if person1.HP <=0 or person2.HP<=0:
        break
    time.sleep(1)
    person1.Atack()
    person2.Defence()
    if person1.HP <=0 or person2.HP<=0:
        break