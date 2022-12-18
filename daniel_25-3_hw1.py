class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def double_hp(self):
        self.health_points *= 2
        return self.health_points


    def __str__(self):
        return f'nickname is {self.nickname}\n' \
               f'superpower is {self.superpower}\n' \
               f'health_points {self.health_points} '

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Black Adam', 'Adam', 'fly', 50, 'и следушее твое слово будет ...')
hero.name='Black Adam'
hero.double_hp()
hero.catchphrase
print(hero.name)
print(hero)