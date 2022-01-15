def add_to_dict(dict_obj, key, value):
    """
    Utility function to add the results to the dictionary and handles duplicacy.
    """
    if key not in dict_obj:
        dict_obj[key] = value
    elif isinstance(dict_obj[key], list):
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [dict_obj[key], value]

    return dict_obj
