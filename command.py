import mhwRequest
from discord import Embed


def add_fields_to_embed(results_dict):
    """
    Create a Discord Embed object and populate it
    :param results_dict: The dictionary to be added as fields
    :return: A Discord Embed object with Fields Populated
    """
    embedded = Embed()
    for key in results_dict.keys():
        if key == "Description":
            embedded.add_field(name=key, value=results_dict[key], inline=False)
        else:
            embedded.add_field(name=key, value=results_dict[key], inline=True)
    return embedded


def overview():
    return "The overview command was called"


def monster(args):
    """
    Run monster query and return results.
    :param args: input from user
    :return: Either a string or a Discord Embed object
    """
    search_term = str(args)
    # Check if searching for ID or name
    if search_term.isnumeric():
        results = [mhwRequest.get_id("monsters", search_term)]
    else:
        results = mhwRequest.get_name("monsters", search_term)

    if len(results) == 0:
        return "No monsters matched your search."

    # One results return Discord Embed object
    if len(results) == 1:
        results_dict = dict()
        single_result = results[0]

        single_keys = ["name", "type", "species", "description"]
        for each_key in single_keys:
            results_dict.update({each_key.capitalize(): single_result[each_key]})

        # Make lists into comma separated strings
        if len(single_result["locations"]) > 0:
            locations_names = []
            for locations in single_result["locations"]:
                locations_names.append(locations["name"])
            results_dict["Locations"] = ", ".join(locations_names)

        if len(single_result["ailments"]) > 0:
            ailment_names = []
            for ailment in single_result["ailments"]:
                ailment_names.append(ailment["name"].capitalize())
            results_dict["Ailments"] = ", ".join(ailment_names)

        if len(single_result["resistances"]) > 0:
            resistances_names = []
            for resistances in single_result["resistances"]:
                resistances_names.append(resistances["element"].capitalize())
            results_dict["Resistances"] = ", ".join(resistances_names)

        if len(single_result["weaknesses"]) > 0:
            weaknesses_names = []
            for weaknesses in single_result["weaknesses"]:
                weaknesses_names.append(weaknesses["element"].capitalize())
            results_dict["Weaknesses"] = ", ".join(weaknesses_names)

        return add_fields_to_embed(results_dict)


def help_monster():
    return "Monster was called with no args"


def weapon(args):
    return "Called weapon with the input: " + str(args)


def help_weapon():
    return "Monster was called with no args"


def material(args):
    return "Called material with the args: " + str(args)


def help_material():
    return "Material was called with no args"


def save(args):
    return "Called save with the inputs: " + str(args)


def help_save():
    return "Save was called with no args"


def vendor():
    return "Vendor was called"


def products(args):
    return "Called products with the input: " + str(args)


def help_products():
    return "Products was called with no args"


def events():
    return "Events were called"


def location(args):
    return "Called location with the input: " + str(args)


def help_location():
    return "Location was called with no args"


def hunters_tools():
    return "Called hunters tools"


def tip():
    return "Called tip"


def guiding(args):
    return "Called guiding with the input: " + str(args)


def help_guiding():
    return "Guiding was called with no args"


def item(args):
    return "Called item with the inputs: " + str(args)


def help_item():
    return "Item was called with no args"


def defeated_monster(args):
    return "Called defeated monster with the input: " + str(args)


def help_defeated_monster():
    return "Defeated monster was called with no args"


def who_killed_me(args):
    return "Called who killed me with the input: " + str(args)


def help_who_killed_me():
    return "Who killed me was called with no args"


def armor(args):
    return "Called armor with the input: " + str(args)


def help_armor():
    return "Armor was called with no args"


def skill(args):
    return "Called skill with the input: " + str(args)


def help_skill():
    return "Skill was called with no args"
