class SuperHero:
    people='people'
    def __init__(self, name, health, superpowers):
        self.name = name
        self.health = health
        self.superpowers = superpowers
        # self.fly = fly
        # self.damage = damage

    def hp(self):
            self.health *= 2

    def __str__(self):
            return f'name is = {self.name}\n' \
                   f'health is = {self.health}\n'\
                   f'superpower is = {self.superpowers}\n'



Hero = SuperHero('Галактус', 50, 'съедает планеты')
Hero.hp()
print(Hero)


class SuperHero2(SuperHero):
    people ='people'

    def __init__(self,name, health, superpowers, fly=False, damage=False):
          super().__init__(name, health, superpowers)
          self.fly = fly
          self.damage = damage

    def hp(self):
           sss = self.health ** 2
           self.health = sss

    def phrase(self):
           print('fly in the True_phrase')

    def desti(self):
         self.fly = True


Hero = SuperHero2('Black Adam', 50, 'SHAZAM')
Hero.hp()
print(Hero)
print(f'Damage: {Hero.damage}')
Hero.desti()
print(f'Fly: {Hero.fly}')
Hero.phrase()

class SuperHero3(SuperHero2):
    people = "people"

    def __init__(self, name, health, superpowers, fly=False, damage=False):
        super().__init__(name, health, superpowers)
        self.fly = fly
        self.damage = damage

    def hp(self):
        sss = self.health ** 2
        self.health = sss

    def phrase(self):
        print('fly in the True_phrase')

    def desti(self):
        self.fly = True

Hero = SuperHero3('Flash' , 100,'speed' )
Hero.hp()
print(Hero)
print(f'Damage: {Hero.damage}')
Hero.desti()
print(f'Fly: {Hero.fly}')
Hero.phrase()

class Villain(SuperHero3):
    people = 'monster'
    def __init__(self, name, health, superpowers, fly=False, damage=False):
        super().__init__(name, health, superpowers, fly, damage)

    def gen_x(self): ...

    def crit(self):
            print(f'Crit dm: {self ** 2}')

seet = Villain('Vorvols\n',150 , 'fire\n' )
print(seet)
seet.gen_x
Villain.crit(seet.damage)








