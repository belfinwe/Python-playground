def get_stuff(name):
    list_of_names = ("Bob", "Kate", "Baldrick")
    if name in list_of_names:
        return name,
    
    return False,


def query_config(name):
    res = get_stuff(name)

    # We just want one item, or know there should only be one item 
    assert len(res) == 1  

    return res[0]


print(query_config("Percy"))  # False
print(query_config("Baldrick"))  # Baldrick
print(query_config(("Bob", "Kate")))  # False
