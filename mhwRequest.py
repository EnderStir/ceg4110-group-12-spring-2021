import requests

api_url = "https://mhw-db.com/"


def get_all(object_type):
    """
    Used to get all objects of a type
    Ex. https://mhw-db.com/monsters would return all monsters
    :param object_type: dict/array of object(s)
    :return: dict/array of object(s)
    """
    request_url = api_url + object_type
    return get_json_from_server(request_url)


def get_id(object_type, object_id):
    """
    Used to get one object of a type with specific id
    Ex. https://mhw-db.com/monsters/1 would return the monster with id 1
    :param object_type: Object type requesting
    :param object_id: Id of Object
    :return: dict/array of object(s)
    """
    request_url = api_url + object_type + "/" + object_id
    return get_json_from_server(request_url)


def get_name(object_type, object_name):
    """
    Used to get any object of a type who's name matches part of the string
    Ex. get_name("monsters", "ja"), would return all monsters with 'ja' anywhere in their name
    (i.e. "Jagras" and "Anjanath")
    :param object_type: Object type requesting
    :param object_name: Full or partial name
    :return: dict/array of object(s)
    """
    request_url = api_url + object_type + "?q={\"name\":{\"$like\":\"%" + object_name + "%\"}}"
    return get_json_from_server(request_url)


def get_json_from_server(request_url):
    """
    Does a GET request to the server, waits for the response, and returns the parsed json.
    :param request_url:
    :return: dict/array of object(s)
    """
    with requests.get(request_url) as results:
        if results.status_code == 200:
            return results.json()
        else:
            return {"error": "Server Failed to respond properly."}
