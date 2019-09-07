class Pokemon:
    __init__(self, name, level, type, maximum_health, current_health, knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.maximum_health = maximum_health
    self.current_health = current_health
    self.knocked_out = knocked_out

    __repr__(self):
    return "Level {level} {name}. {type} type.".format(level = self.level, name = self.name, type = self.type)

    def lose_health(self, damage):
        self.current_health -= damage
        if current_health <= 0:
            current_health = 0
            print("{name} was knocked out!".format(name = self.name))
            self.knocked_out = True
        else:
            print("{name} took {damage} damage. {name} has {current_health} remaining.".format(name = self.name, damage = damage, name = self.name, current_health = self.current_health))

items_dict = {
  "Potion": 20,
  "Super Potion": 50,
  "Hyper Potion": 200,
  "Max Potion": 713,
}
class Trainer:
    __init__(self, name, pokemon, items):
    self.name = name
    self.pokemon = pokemon
    self.items = items

    def use_item(self, item, pokemon):
        self.items.remove(item)
        item.effect(pokemon)

class Item:
    __init__(self, name)
    self.name = name

    def effect(self, pokemon):
        if self.name == "Revive":
            if pokemon.knocked_out != True:
                print("{name} is not knocked out! The Revive had no effect!")
            else:
                pokemon.current_health += (current.maximum_health // 2)
                pokemon.knocked_out = False
                print("{name} was revived with {current_health} health.".format(name = pokemon.name, current_health = pokemon.current_health))
        else:
            if pokemon.knocked_out == True:
                print("{name} is knocked out. The {item} had no effect!".format(name = pokemon.name, item = self.name))
            else:
                before_potion = pokemon.current_health
                pokemon.current_health += items_dict[self.name]
                if pokemon.current_health > pokemon.maximum_health:
                    pokemon.current_health = pokemon.maximum_health
