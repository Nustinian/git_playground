import random

class Pokemon:
    def __init__(self, name, level, type, maximum_health, current_health, attack, defense, speed, knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.maximum_health = maximum_health
        self.current_health = current_health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.knocked_out = knocked_out
        self.move_list = []

    def __repr__(self):
        return self.name

    def lose_health(self, damage):
        self.current_health -= damage
        if self.current_health <= 0:
            self.current_health = 0
            print("{name} was knocked out!".format(name = self.name))
            self.knocked_out = True
        else:
            print("{name} took {damage} damage. {name} has {current_health} HP remaining.".format(name = self.name, damage = damage, current_health = self.current_health))

    def learn_move(self, move):
        self.move_list.append(move)
        print("{pokemon} learned {move}!".format(pokemon = self.name, move = move.name))

    def attack_enemy(self, enemy, move):
        hit_roll = random.randint(0, 99)
        if hit_roll > move.accuracy:
            print("{pokemon} used {move}... but it missed!".format(pokemon = self.name, move = move.name))
        else:
            multiplier = 1
            for type in enemy.type:
                if move.type in no_effect_dict[type]:
                    multiplier *= 0
                elif move.type in not_very_effective_dict[type]:
                    multiplier /= 2
                elif move.type in super_effective_dict[type]:
                    multiplier *= 2
            print("{pokemon} used {move}!".format(pokemon = self.name, move = move.name))
            if multiplier == 0:
                print("... but it had no effect!")
            elif multiplier < 1:
                print("... it's not very effective!")
            elif multiplier > 1:
                print("It's super effective" + '!' * multiplier)
            critical_roll = random.randint(0, 99)
            if critical_roll < move.critical_hit:
                multiplier *= 2
                print("A critical hit!")
            enemy.lose_health(round(multiplier * self.attack * move.damage / enemy.defense))


class Move:
    def __init__(self, name, damage, type, critical_hit = 10, accuracy = 100):
        self.name = name
        self.damage = damage
        self.type = type
        self.critical_hit = critical_hit
        self.accuracy = accuracy

    def __repr__(self):
        return self.name

items_dict = {
  "Potion": 20,
  "Super Potion": 50,
  "Hyper Potion": 200,
  "Max Potion": 713,
  "Revive": True
}

super_effective_dict = {
  "Normal": ["Fighting"],
  "Fire": ["Water", "Rock", "Ground"],
  "Water": ["Grass", "Electric"],
  "Grass": ["Fire", "Bug", "Flying", "Ice", "Poison"],
  "Flying": ["Rock", "Ice", "Electric"],
  "Poison": ["Ground", "Psychic"],
  "Electric": ["Ground"]
}
no_effect_dict = {
  "Normal": ["Ghost"],
  "Fire": [],
  "Water": [],
  "Grass": [],
  "Flying": ["Ground"],
  "Poison": [],
  "Electric": []
}
not_very_effective_dict = {
  "Normal": [],
  "Fire": ["Fire", "Grass", "Steel", "Ice", "Bug", "Fairy"],
  "Water": ["Fire", "Water", "Ice", "Steel"],
  "Grass": ["Water", "Electric", "Grass", "Ground"],
  "Flying": ["Grass", "Fighting", "Bug"],
  "Poison": ["Grass", "Fighting", "Poison", "Bug", "Fairy"],
  "Electric": ["Electric", "Flying", "Steel"]
}

class Trainer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.party = []
        self.items = []
        if gender == "Male":
            self.possessive = "his"
        else:
            self.possessive = "her"

    def __repr__(self):
        return self.name

    def get_item(self, item):
        if item.name not in items_dict:
            print("{item} is not an approved item. Item discarded!")
            return
        self.items.append(item)
        print("{trainer} added {item} to {possessive} bag!".format(trainer = self.name, item = item, possessive = self.possessive))

    def use_item(self, item, pokemon):
        self.items.remove(item)
        item.effect(pokemon)

    def add_pokemon_to_party(self, pokemon):
        if len(self.party) == 6:
            print("{trainer}'s party is already full!".format(trainer = self.name))
            return
        self.party.append(pokemon)
        print("Added {pokemon} to {trainer}'s party.".format(pokemon = pokemon, trainer = self.name))

    def remove_pokemon_from_party(self, pokemon, which = 0):
        if pokemon not in self.party:
            print("{trainer} does not have a {pokemon} in {possessive} party.".format(trainer = self.name, pokemon = pokemon, possessive = self.possessive))
            return
        if self.party.count(pokemon) > 1:
            numbers = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
            indices_of_pokemon = [i for i, x in enumerate(self.party) if x == pokemon]
            index_to_remove = indices_of_pokemon[which - 1]
            del self.party[index_to_remove]
            print("Removed the {nth} {pokemon} from {trainer}'s party.".format(nth = numbers[which - 1], pokemon = pokemon, trainer = self.name))
        else:
            self.party.remove(pokemon)
            print("Removed {pokemon} from {trainer}'s party.".format(pokemon = pokemon, trainer = self.name))

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def effect(self, pokemon):
        if self.name == "Revive":
            if pokemon.knocked_out != True:
                print("{name} is not knocked out! The Revive had no effect!".format(name = pokemon.name))
            else:
                pokemon.current_health += (current.maximum_health // 2)
                pokemon.knocked_out = False
                print("{name} was revived with {current_health} health.".format(name = pokemon.name, current_health = pokemon.current_health))
        else:
            if pokemon.knocked_out == True:
                print("{name} is knocked out. The {item} had no effect!".format(name = pokemon.name, item = self.name))
            elif pokemon.current_health == pokemon.maximum_health:
                print("{name} is already fully healed. The {item} had no effect!".format(name = pokemon.name, item = self.name))
            else:
                before_potion = pokemon.current_health
                pokemon.current_health += items_dict[self.name]
                if pokemon.current_health > pokemon.maximum_health:
                    pokemon.current_health = pokemon.maximum_health
                amount_healed = pokemon.current_health - before_potion
                print("Used {item} on {name}. {name} restored {amount_healed} hit points!".format(item = item.name, name = pokemon.name, amount_healed = amount_healed))

hyper_potion = Item("Hyper Potion")
potion = Item("Potion")
super_potion = Item("Super Potion")
max_potion = Item("Max Potion")
revive = Item("Revive")

venusaur = Pokemon("Venusaur", 100, ["Grass", "Poison"], 364, 364, 328, 328, 284, False)
charizard = Pokemon("Charizard", 100, ["Fire", "Flying"], 360, 360, 348, 295, 328, False)
blastoise = Pokemon("Blastoise", 100, ["Water"], 362, 362, 295, 339, 280, False)
pikachu = Pokemon("Pikachu", 100, ["Electric"], 274, 274, 229, 218, 306, False)
snorlax = Pokemon("Snorlax", 100, ["Normal"], 524, 524, 350, 350, 174, False)
jigglypuff = Pokemon("Jigglypuff", 100, ["Normal"], 434, 434, 207, 163, 152, False)

ember = Move("Ember", 40, "Fire")
razor_leaf = Move("Razor Leaf", 55, "Grass", critical_hit = 30, accuracy = 95)
water_gun = Move("Water Gun", 40, "Water")
thunder = Move("Thunder", 110, "Electric", accuracy = 70)
body_slam = Move("Body Slam", 85, "Normal")
hyper_voice = Move("Hyper Voice", 90, "Normal")
bubble_beam = Move("Bubble Beam", 65, "Water")
wing_attack = Move("Wing Attack", 60, "Flying")
austin = Trainer("Austin", "Male")


austin.add_pokemon_to_party(charizard)
austin.add_pokemon_to_party(blastoise)
austin.add_pokemon_to_party(venusaur)

austin.get_item(super_potion)
austin.get_item(revive)

asako = Trainer("Asako", "Female")


asako.add_pokemon_to_party(jigglypuff)
asako.add_pokemon_to_party(snorlax)
asako.add_pokemon_to_party(pikachu)

asako.get_item(max_potion)
asako.get_item(max_potion)
asako.get_item(revive)

venusaur.learn_move(razor_leaf)
charizard.learn_move(wing_attack)
blastoise.learn_move(bubble_beam)
pikachu.learn_move(thunder)
snorlax.learn_move(body_slam)
jigglypuff.learn_move(hyper_voice)


austin_current_pokemon = 0
asako_current_pokemon = 0

while austin.party[austin_current_pokemon].knocked_out != True and asako.party[asako_current_pokemon].knocked_out != True:
    if austin.party[austin_current_pokemon].speed < asako.party[asako_current_pokemon].speed:
        asako.party[asako_current_pokemon].attack_enemy(austin.party[austin_current_pokemon], asako.party[asako_current_pokemon].move_list[0])
        if austin.party[austin_current_pokemon].knocked_out == True:
            austin_current_pokemon += 1
            if austin_current_pokemon == 3:
                print("Asako wins the battle!!!")
                break
        austin.party[austin_current_pokemon].attack_enemy(asako.party[asako_current_pokemon], austin.party[austin_current_pokemon].move_list[0])
        if asako.party[asako_current_pokemon].knocked_out == True:
            asako_current_pokemon += 1
            if asako_current_pokemon == 3:
                print("Austin wins the battle!!!")
                break
    else:
        austin.party[austin_current_pokemon].attack_enemy(asako.party[asako_current_pokemon], austin.party[austin_current_pokemon].move_list[0])
        if asako.party[asako_current_pokemon].knocked_out == True:
            asako_current_pokemon += 1
            if asako_current_pokemon == 3:
                print("Austin wins the battle!!!")
                break
        asako.party[asako_current_pokemon].attack_enemy(austin.party[austin_current_pokemon], asako.party[asako_current_pokemon].move_list[0])
        if austin.party[austin_current_pokemon].knocked_out == True:
            austin_current_pokemon += 1
            if austin_current_pokemon == 3:
                print("Asako wins the battle!!!")
                break
