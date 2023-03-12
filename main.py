import random
import time
Classs = ["Маг","Танк"]#,"Лучник","Целитель"]
TypeMage= ["Огонь","Холод","Яд"]
TypeTank = ["Площадь","Сильный удар","Колющий удар"]
atack = ''
gg = 0
atk2 = "Не выбрано"
atk1 = "Не выбрано"
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
        self.Heal = 5
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

    def Atack(self,atack_type,atack_type1):
        self.atack_type = atack_type
        self.atack_type1 = atack_type1
        if self.atack_type == 'Огонь':
            self.atack = self.punch + 4
        elif self.atack_type1 == 'Холод':
            self.atack = self.punch + 3
        elif self.atack_type == "Яд":
            self.atack = self.punch + 6
        else:
            self.atack = self.punch
        if self.Class1 == "Маг":
            if self.atack_type1 == 'Огонь':
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == 'Холод':
                self.atack1 = self.punch1 + 3
            elif self.atack_type1 == "Яд":
                self.atack1 = self.punch1 + 6
            else:
                self.atack1 = self.punch1

        else:
            if self.atack_type1 == "Площадь":
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == "Сильный удар":
                self.atack1 = self.punch1 + 8
            elif self.atack_type1 == "Колющий удар":
                self.atack1 = self.punch1 + 6
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
        if self.atack1 < self.DP:
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
    def heal(self):
        if self.person == 2:
            print(f"{self.name}?, у вас есть {self.Heal} зелий лечения, вы хотите полечиться?")
            ph = input()
            if ph == "Да" or ph == "да":
                self.HP += 50
                print("Вы подлечились на 50, ваше здоровьбе равно: ",self.HP)
                self.Heal -=1
                if self.Heal == 0:
                    print("Ваши зелья лечения з0акончились")
            else:
                self.HP = self.HP
        if self.person == 1:
            ph = random.randint(0,9)
            if ph == 6:
                self.HP += 50
                print("Противник подлечился на 50, его здоровьбе равно: ",self.HP)
                self.Heal -= 1

            else:
                self.HP = self.HP

class Tank(RPG):
    def __init__(self, name, Class, HP, DP, punch, atack_type, HP1, DP1, punch1, atack_type1, Class1, gg,person):
        self.Heal = 5
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

    def Atack(self,atack_type,atack_type1):
        self.atack_type = atack_type
        self.atack_type1 = atack_type1
        if self.atack_type == "Площадь":
            self.atack = self.punch + 4
        elif self.atack_type == "Сильный удар":
            self.atack = self.punch + 8
        elif self.atack_type == "Колющий удар":
            self.atack = self.punch + 6
        else:
            self.atack = self.punch
        if self.Class1 == "Маг":
            if self.atack_type1 == 'Огонь':
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == 'Холод':
                self.atack1 = self.punch1 + 3
            elif self.atack_type1 == "Яд":
                self.atack = self.punch + 6
            else:
                self.atack = self.punch

        else:
            if self.atack_type1 == "Площадь":
                self.atack1 = self.punch1 + 4
            elif self.atack_type1 == "Сильный удар":
                self.atack1 = self.punch1 + 8
            elif self.atack_type1 == "Колющий удар":
                self.atack1 = self.punch1 + 6
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

    def heal(self):
        if self.person == 2:
            print(f"{self.name}?, у вас есть {self.Heal} зелий лечения, вы хотите полечиться?")
            ph = input()
            if ph == "Да" or ph == "да":
                self.HP += 50
                print("Вы подлечились на 50, ваше здоровьбе равно: ",self.HP)
                self.Heal -=1
                if self.Heal == 0:
                    print("Ваши зелья лечения з0акончились")
            else:
                self.HP = self.HP
        if self.person == 1:
            ph = random.randint(0,9)
            if ph == 6:
                self.HP += 50
                print("Противник подлечился на 50, его здоровьбе равно: ",self.HP)
                self.Heal -= 1
            else:
                self.HP = self.HP

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
        atack_type1 = "Не выбрано"
#   elif b=="":

#    elif b=="":

    elif b=="Танк":
        HP1= random.randint(225,400)
        DP1 = random.randint(10,25)
        punch1 = random.randint(15,25)
        atack_type1 = "Не выбрано"
    else:
        print("Такого класса не существует")
    print(f'Выберите класс персонажа из предложенных:{Classs}')
    c= input()
    if c=="Маг":
        p2=RPG(name,c)
        HP2= random.randint(125,250)
        DP2 = random.randint(5,15)
        punch2 = random.randint(25,45)
        atack_type2 = "Не выбрано"

#   elif b=="":

#    elif b=="":

    elif c == "Танк":
        p2 = RPG(name, c)
        HP2 = random.randint(225,400)
        DP2 = random.randint(10,25)
        punch2 = random.randint(15,25)
        atack_type2 = "Не выбрано"
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
person1.Atack(atk2,atk1)
while person1.HP >0 and person2.HP>0:
    if person1.HP <=0 or person2.HP<=0:
        break
    print(f"{person2.name}, выберите тип атаки")
    if person1.Class == "Маг":
        atk1 = TypeMage[random.randint(0,len(TypeMage)-1)]
    elif person1.Class == "Танк":
        atk1 = TypeTank[random.randint(0, len(TypeTank) - 1)]
    if person2.Class == "Маг":
        print("Огонь/Холод/Яд")
        atk2 = input()
    elif person2.Class == "Танк":
        print("Площадь/Сильный удар/Колющий удар")
        atk2 = input()
    time.sleep(1)
    person2.Atack(atk1,atk2)
    if person1.Heal != 0:
        person1.heal()
    person1.Defence()
    if person1.HP <=0 or person2.HP<=0:
        break
    time.sleep(1)
    person1.Atack(atk2,atk1)
    if person2.Heal != 0:
        person2.heal()
    person2.Defence()
    if person1.HP <=0 or person2.HP<=0:
        break