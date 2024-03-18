'''
Program used to generate the most dense rapport groups in the unicorn overlord game.
Parties may not be optimal, but each group will have a lot to talk about.
@author Weston Fiala
'''

# All of the characters in alphabetical order
sorted_character_list = [
    "Alain",
    "Adel",
    "Aramis",
    "Aubin",
    "Auch",
    "Berengaria",
    "Berenice",
    "Bruno",
    "Celeste",
    "Chloe",
    "Clive",
    "Colm",
    "Eltolinde",
    "Fran",
    "Galadmir",
    "Gilbert",
    "Gloucester",
    "Hilda",
    "Hodrick",
    "Ithilion",
    "Jeremy",
    "Josef",
    "Kitra",
    "Leah",
    "Lex",
    "Lhinalagos",
    "Liza",
    "Magellan",
    "Melisandre",
    "Miriam",
    "Monica",
    "Mordon",
    "Nina",
    "Ochlys",
    "Primm",
    "Renault",
    "Ridiel",
    "Rolf",
    "Rosalinde",
    "Scarlett",
    "Selvie",
    "Sharon",
    "Tatiana",
    "Travis",
    "Virginia",
    "Yahna",
]

# Map of all the characters and their personal rapport intensities
# Keys are in order of character recruitment
# Inner intensity keys are in "fuck if I know" order
rapport_map = {
    "Alain" : {
        "Lex": 3,
        "Chloe": 3,
        "Hodrick": 3,
        "Clive": 3,
        "Josef": 3,
        "Travis": 3,
        "Aubin": 2,
        "Rolf": 2,
        "Bruno": 2,
        "Sharon": 3,
        "Mordon": 2,
        "Yahna": 2,
        "Berenice": 2,
        "Adel": 2,
        "Kitra": 2,
        "Miriam": 2,
        "Fran": 2,
        "Scarlett": 3,
        "Auch": 2,
        "Nina": 2,
        "Selvie": 3,
        "Virginia": 3,
        "Leah": 2,
        "Primm": 2,
        "Aramis": 2,
        "Jeremy": 1,
        "Magellan": 1,
        "Liza": 3,
        "Hilda": 1,
        "Gilbert": 3,
        "Gloucester": 1,
        "Berengaria": 3,
        "Tatiana": 2,
        "Monica": 1,
        "Melisandre": 2,
        "Colm": 1,
        "Rosalinde": 3,
        "Ithilion": 1,
        "Lhinalagos": 1,
        "Galadmir": 1,
        "Eltolinde": 3,
        "Ridiel": 3,
        "Celeste": 2,
        "Ochlys": 3,
        "Renault": 1,
    },
    "Scarlett" : {
        "Alain": 3,
        "Lex": 2,
        "Chloe": 2,
        "Virginia": 1,
        "Josef": 1,
        "Melisandre": 1,
        "Rosalinde": 1,
        "Eltolinde": 1,
    },
    "Lex" : {
        "Alain": 3,
        "Clive": 1,
        "Josef": 2,
        "Scarlett": 2,
        "Tatiana": 1,
        "Sharon": 1,
        "Lex": 1,
        "Selvie": 1,
        "Chloe": 2,
        "Hodrick": 2,
        "Colm": 1,
        "Rosalinde": 1,
        "Eltolinde": 1,
    },
    "Josef" : {
        "Alain": 3,
        "Lex": 2,
        "Chloe": 2,
        "Hodrick": 2,
        "Clive": 2,
        "Virginia": 2,
        "Travis": 2,
        "Yahna": 1,
        "Miriam": 1,
        "Scarlett": 1,
        "Selvie": 1,
        "Tatiana": 1,
        "Renault": 1,
    },
    "Chloe" : {
        "Alain": 3,
        "Hodrick": 1,
        "Clive": 1,
        "Lex": 2,
        "Travis": 1,
        "Josef": 2,
        "Rolf": 1,
        "Yahna": 1,
        "Scarlett": 2,
        "Ridiel": 2,
    },
    "Hodrick" : {
        "Alain": 3,
        "Chloe": 1,
        "Josef": 2,
        "Lex": 2,
        "Yahna": 2,
        "Clive": 1,
        "Renault": 2,
    },
    "Clive" : {
        "Alain": 3,
        "Lex": 1,
        "Chloe": 1,
        "Josef": 2,
        "Hodrick": 1,
        "Mordon": 1,
        "Monica": 3,
        "Renault": 1,
        "Berenice": 2,
        "Adel": 2,
        "Liza": 1,
    },
    "Travis" : {
        "Alain": 3,
        "Chloe": 1,
        "Josef": 2,
        "Primm": 1,
        "Bruno": 3,
        "Aramis": 1,
        "Gilbert": 1,
        "Berengaria": 3,
        "Ridiel": 1,
    },
    "Aubin" : {
        "Alain": 2,
        "Liza": 2,
        "Magellan": 2,
        "Jeremy": 2,
        "Gloucester": 1,
        "Ridiel": 1,
    },
    "Rolf" : {
        "Alain": 2,
        "Chloe": 1,
        "Adel": 1,
        "Mordon": 1,
        "Auch": 2,
    },
    "Bruno" : {
        "Alain": 2,
        "Travis": 3,
        "Berengaria": 2,
        "Sharon": 2,
        "Selvie": 1,
    },
    "Sharon" : {
        "Alain": 3,
        "Lex": 1,
        "Bruno": 2,
        "Ochlys": 2,
        "Kitra": 1,
        "Liza": 1,
        "Colm": 1,
    },
    "Mordon" : {
        "Alain": 2,
        "Clive": 1,
        "Rolf": 1,
        "Berenice": 1,
        "Jeremy": 1,
        "Kitra": 3,
        "Lhinalagos": 1,
    },
    "Yahna" : {
        "Alain": 2,
        "Hodrick": 2,
        "Chloe": 1,
        "Nina": 1,
        "Josef": 1,
        "Adel": 1,
        "Auch": 1,
        "Rosalinde": 1,
    },
    "Berenice" : {
        "Alain": 2,
        "Mordon": 1,
        "Jeremy": 1,
        "Clive": 2,
        "Adel": 2,
        "Kitra": 1,
        "Auch": 1,
    },
    "Ochlys" : {
        "Alain": 3,
        "Sharon": 2,
        "Tatiana": 1,
    },
    "Auch" : {
        "Alain": 2,
        "Rolf": 2,
        "Kitra": 1,
        "Selvie": 1,
        "Yahna": 1,
        "Berenice": 1,
        "Melisandre": 1,
    },
    "Adel" : {
        "Alain": 2,
        "Rolf": 1,
        "Yahna": 1,
        "Celeste": 1,
        "Melisandre": 1,
        "Berenice": 2,
        "Clive": 2,
    },
    "Fran" : {
        "Alain": 2,
        "Kitra": 2,
        "Celeste": 1,
        "Miriam": 2,
        "Virginia": 1,
        "Hilda": 1,
    },
    "Selvie" : {
        "Alain": 3,
        "Lex": 1,
        "Miriam": 1,
        "Auch": 1,
        "Josef": 1,
        "Bruno": 1,
        "Monica": 1,
    },
    "Nina" : {
        "Alain": 2,
        "Yahna": 1,
        "Tatiana": 1,
        "Monica": 1,
    },
    "Miriam" : {
        "Alain": 2,
        "Kitra": 2,
        "Selvie": 1,
        "Josef": 1,
        "Fran": 2,
        "Virginia": 1,
        "Colm": 1,
    },
    "Kitra" : {
        "Alain": 2,
        "Mordon": 3,
        "Fran": 2,
        "Sharon": 1,
        "Auch": 1,
        "Berenice": 1,
        "Miriam": 2,
        "Virginia": 1,
    },
    "Renault" : {
        "Alain": 1,
        "Clive": 1,
        "Hodrick": 2,
        "Josef": 1,
    },
    "Tatiana" : {
        "Alain": 2,
        "Lex": 1,
        "Nina": 1,
        "Hilda": 1,
        "Josef": 1,
        "Ochlys": 1,
        "Ridiel": 1,
    },
    "Melisandre" : {
        "Alain": 2,
        "Adel": 1,
        "Scarlett": 1,
        "Auch": 1,
        "Aramis": 1,
        "Liza": 1,
        "Monica": 1,
        "Colm": 2,
    },
    "Colm" : {
        "Alain": 1,
        "Melisandre": 2,
        "Sharon": 1,
        "Miriam": 1,
        "Lex": 1,
    },
    "Monica" : {
        "Alain": 1,
        "Clive": 3,
        "Nina": 1,
        "Selvie": 1,
        "Melisandre": 1,
        "Liza": 1,
    },
    "Virginia" : {
        "Alain": 3,
        "Josef": 2,
        "Scarlett": 1,
        "Leah": 2,
        "Kitra": 1,
        "Miriam": 1,
        "Fran": 1,
        "Aramis": 2,
        "Gilbert": 2,
        "Berengaria": 1,
    },
    "Leah" : {
        "Alain": 2,
        "Virginia": 2,
        "Aramis": 1,
        "Gilbert": 2,
        "Berengaria": 1,
    },
    "Berengaria" : {
        "Alain": 3,
        "Bruno": 2,
        "Travis": 3,
        "Gilbert": 1,
        "Virginia": 1,
        "Leah": 1,
    },
    "Primm" : {
        "Alain": 2,
        "Travis": 1,
        "Aramis": 2,
        "Hilda": 2,
    },
    "Aramis" : {
        "Alain": 2,
        "Primm": 2,
        "Travis": 1,
        "Melisandre": 1,
        "Virginia": 2,
        "Gloucester": 2,
        "Leah": 1,
        "Gilbert": 2,
    },
    "Magellan" : {
        "Alain": 1,
        "Aubin": 2,
        "Hilda": 1,
        "Liza": 2,
        "Rosalinde": 1,
        "Gloucester": 1,
        "Ithilion": 1,
    },
    "Liza" : {
        "Alain": 3,
        "Aubin": 2,
        "Magellan": 2,
        "Clive": 1,
        "Sharon": 1,
        "Melisandre": 1,
        "Monica": 1,
    },
    "Gloucester" : {
        "Alain": 1,
        "Aramis": 2,
        "Gilbert": 1,
        "Jeremy": 1,
        "Magellan": 1,
        "Aubin": 1,
    },
    "Jeremy" : {
        "Alain": 1,
        "Aubin": 2,
        "Mordon": 1,
        "Berenice": 1,
        "Gilbert": 1,
        "Gloucester": 1,
    },
    "Hilda" : {
        "Alain": 1,
        "Primm": 2,
        "Magellan": 1,
        "Tatiana": 1,
        "Fran": 1,
    },
    "Ridiel" : {
        "Alain": 3,
        "Galadmir": 1,
        "Aubin": 1,
        "Travis": 1,
        "Lhinalagos": 1,
        "Tatiana": 1,
        "Chloe": 2,
    },
    "Gilbert" : {
        "Alain": 3,
        "Travis": 1,
        "Virginia": 2,
        "Leah": 2,
        "Aramis": 2,
        "Jeremy": 1,
        "Gloucester": 1,
        "Berengaria": 1,
    },
    "Rosalinde" : {
        "Alain": 3,
        "Magellan": 1,
        "Lex": 1,
        "Yahna": 1,
        "Scarlett": 1,
        "Ithilion": 2,
        "Eltolinde": 2,
    },
    "Lhinalagos" : {
        "Alain": 1,
        "Ithilion": 1,
        "Mordon": 1,
        "Galadmir": 2,
        "Eltolinde": 2,
        "Ridiel": 1,
    },
    "Celeste" : {
        "Alain": 2,
        "Adel": 1,
        "Fran": 1,
    },
    "Ithilion" : {
        "Alain": 1,
        "Rosalinde": 2,
        "Lhinalagos": 1,
        "Magellan": 1,
        "Galadmir": 1,
    },
    "Eltolinde" : {
        "Alain": 3,
        "Galadmir": 2,
        "Lhinalagos": 2,
        "Lex": 1,
        "Scarlett": 1,
        "Rosalinde": 2,
    },
    "Galadmir" : {
        "Alain": 1,
        "Ithilion": 1,
        "Eltolinde": 2,
        "Lhinalagos": 2,
        "Ridiel": 1,
    },
}

# Takes a list of names and finds the intensity of their rapport
def calculate_squad_rapport(squad_names):
    squad_rapport = 0
    for character_name in squad_names:
        for compare_character_name in squad_names:
            if character_name != compare_character_name:
                character_rapport_map = rapport_map[character_name]
                if compare_character_name in character_rapport_map:
                    rapport_intensity = character_rapport_map[compare_character_name]
                    squad_rapport += rapport_intensity
    return squad_rapport / 2

# Gets the maximum possible rapport intenstity that a given member can have in a given squad size
def maximum_possible_rapport_intensity(character_name, squad_size):
    intensity_values = list(rapport_map[character_name].values())

    if intensity_values.__len__() <= squad_size:
        return sum(intensity_values, 0)

    intensity_values.sort(reverse=True)
    max_intensity = 0
    for i in range(squad_size):
        max_intensity += intensity_values[i]

    return max_intensity

# Finds the lowest performing intensity unit in the squad and returns their current intensity value
def get_lowest_intensity_for_given_squad(squad_names):
    if squad_names.__len__() == 0:
        return 0

    # Bonus number because you could never get this intensity.
    minimum_intensity = 1000
    for character_name in squad_names:
        current_rapport = 0
        for compare_character_name in squad_names:
            if character_name != compare_character_name:
                character_rapport_map = rapport_map[character_name]
                if compare_character_name in character_rapport_map:
                    rapport_intensity = character_rapport_map[compare_character_name]
                    current_rapport += rapport_intensity
        if current_rapport < minimum_intensity:
            minimum_intensity = current_rapport
    return minimum_intensity

# Find the best squad in a recursive manner. Returns what it find to be the best squad.
def find_best_squad_recurse(requested_squad_size, current_squad, best_squad, possible_members, tested_sets):
    # Exit the recursion if we have enough members.
    if requested_squad_size == current_squad.__len__():
        if best_squad.__len__() == 0:
            return current_squad.copy()
        current_rapport = calculate_squad_rapport(current_squad)
        best_rapport = calculate_squad_rapport(best_squad)
        if current_rapport > best_rapport:
            print("New best Squad: ", current_squad.__str__(), " - ", current_rapport)
            return current_squad.copy()
        else:
            return best_squad

    # Don't have enough members, add some more if it is useful to do.
    # First, check if the current members have already been tested.
    sorted_current_squad = current_squad.copy()
    sorted_current_squad.sort()
    hashable_current_squad = sorted_current_squad.__str__()
    if hashable_current_squad not in tested_sets:
        # We have not yet tested this config yet, dive down.
        tested_sets.add(hashable_current_squad)
        for new_member in possible_members:
            # Add a new member to the squad, remove it from future recursions
            # If the new member doesn't have a rapport with anyone currently in the squad, skip them.
            should_continue = current_squad.__len__() == 0
            for member in current_squad:
                should_continue |= rapport_map[member].__contains__(new_member)

            # if the maximum intensity of the possible new member is less than the worst intense of the current squad, don't advance.
            max_rapport_intensity = maximum_possible_rapport_intensity(new_member, requested_squad_size)
            lowest_current_intensity = get_lowest_intensity_for_given_squad(best_squad)
            if max_rapport_intensity <= lowest_current_intensity:
                should_continue = False

            # Failsafes
            if best_squad.__len__() == 0:
                should_continue = True

            if calculate_squad_rapport(current_squad) > calculate_squad_rapport(best_squad):
                should_continue = True
            
            if should_continue:
                current_squad.append(new_member)
                new_possible_members = possible_members.copy()
                new_possible_members.remove(new_member)
                best_squad = find_best_squad_recurse(requested_squad_size, current_squad, best_squad, new_possible_members, tested_sets)
                current_squad.remove(new_member)

    # Whatever the best squad is we found it.        
    return best_squad

# How many squads do we need and what size are they.
squad_sizes = [5, 4, 4, 4, 4, 4, 4, 4, 4, 4]

squads = []

modifiable_top_list = sorted_character_list.copy()

for squad_size in squad_sizes:
    best_squad = []
    # Do Alain's Squad alone, to save time.
    if squads.__len__() == 0:
        modifiable_top_list.remove("Alain")
        best_squad = find_best_squad_recurse(squad_size, ["Alain"], [], modifiable_top_list, set())
    else:
        best_squad = find_best_squad_recurse(squad_size, [], [], modifiable_top_list, set())
    squads.append(best_squad)
    for member in best_squad:
        if modifiable_top_list.__contains__(member):
            modifiable_top_list.remove(member)

for squad in squads:
    print(squad)

print("unused: ", modifiable_top_list)
