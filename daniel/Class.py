class Hero:
    fly='fly'
    run='run'
    def __init__(self, name, abyliti):
        self.name = name
        self.abyliti = abyliti
class Hero_super(Hero):
    def __str__(self):
        return f' {self.name}'
    def f(self):
     print('it is super_hero')

class Three(Hero_super):...

h=Three('Adam' , 'скрость')
h.name='Adam'
h.f()
print(h)