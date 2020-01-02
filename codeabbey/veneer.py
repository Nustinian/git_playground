class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return "{artist}. {title}. {year}, {medium}. {owner}, {location}.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner = self.owner.name, location = self.owner.location)




class Marketplace:
    def __init__(self, name):
        self.name = name
        self.listings = []
        self.art_on_market = []

    def __repr__(self):
        return self.name

    def add_listing(self, new_listing):
        self.listings.append(new_listing)
        self.art_on_market.append(new_listing.art)

    def remove_listing(self, index):
        self.listings.pop(index)

    def show_listings(self):
        for listing in self.listings:
            print(listing)

class Client:
    def __init__(self, name, location, is_museum = False):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def __repr__(self):
        return self.name

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

    def buy_artwork(self, artwork):
        if artwork.owner != self:
            if artwork in veneer.art_on_market:
                index = veneer.art_on_market.index(artwork)
                artwork.owner = self
                veneer.remove_listing(index)
                veneer.art_on_market.remove(artwork)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return "{title}. {price}.".format(title = self.art.title, price = self.price)

veneer = Marketplace("Veneer")

print(veneer.show_listings())

edytta = Client("Edytta Halpirt", "Private Collection")

moma = Client("The MOMA", "New York", is_museum = True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, "$6m (USD)")

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
