############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        
        # Make seedless and bestseller into booleans
        if is_seedless.lower() == "seedless":
            self.is_seedless = True
        else:
            self.is_seedless = False

        if is_bestseller.lower() == "bestseller":
            self.is_bestseller = True
        else:
            self.is_bestseller = False
        
        self.name = name

        # # Test code
        # print(self.name, self.is_bestseller, self.is_seedless,
        #       self.color, self.first_harvest, self.code)

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)
        # print(self.pairings)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    # Add muskmelon
    muskmelon = MelonType(name='Muskmelon', code='musk', first_harvest=1998,
                          color='green', is_seedless='seedless', 
                          is_bestseller='Bestseller')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    # Add casaba melon
    casaba = MelonType(name='Casaba', code='cas', first_harvest=2003, 
                       color='orange', is_seedless='has seeds', 
                       is_bestseller='')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    # Add crenshaw melon
    crenshaw = MelonType(name='Crenshaw', code='cren', first_harvest=1996,
                         color='green', is_bestseller='', 
                         is_seedless='has seeds')
    crenshaw.add_pairing('prosciutto')
    all_melon_types.append(crenshaw)

    # Add yellow watermelon
    yellow_watermelon = MelonType(name='Yellow Watermelon', code='yw',
                                  first_harvest=2013, color='yellow',
                                  is_seedless='has seeds', 
                                  is_bestseller='Bestseller')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")

        # Loop throug the pairings printing them individually
        for pairing in melon.pairings:
            print(f"- {pairing}")
            
        print("")


    return



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_codes = dict()

    for melon in melon_types:
        code = melon.code
        melon_codes[code] = melon_codes.get(code, melon)
    
    return melon_codes


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(
            self, type, shape_rating, color_rating, harvest_field, harvest_by
    ):
        """Initialize a melon harvest"""
        
        # Add attributes
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvest_by = harvest_by

    def is_sellable(self):
        """Return a boolean of whether or not a melon is sellable"""

        # Check if melon ratings are above five and it's not from field three
        if (self.shape_rating > 5 and self.color_rating > 5
            and self.harvest_field != 3):

            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons = []

    # Initialize melons and add attributes
    melon1 = Melon('yw', 8, 7, 2, 'Sheila')
    melons.append(melon1)
    
    melon2 = Melon('yw', 3, 4, 2, 'Sheila')
    melons.append(melon2)

    melon3 = Melon('yw', 9, 8, 3, 'Sheila')
    melons.append(melon3)

    melon4 = Melon('cas', 10, 6, 35, 'Sheila')
    melons.append(melon4)

    melon5 = Melon('cren', 8, 9, 35, 'Michael')
    melons.append(melon5)

    melon6 = Melon('cren', 8, 2, 35, 'Michael')
    melons.append(melon6)

    melon7 = Melon('cren', 2, 3, 4, 'Michael')
    melons.append(melon7)

    melon8 = Melon('musk', 6, 7, 4, 'Michael')
    melons.append(melon8)

    melon9 = Melon('yw', 7, 10, 3, 'Sheila')
    melons.append(melon9)


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
