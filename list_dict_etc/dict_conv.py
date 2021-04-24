def heimetesting():
    """Teste korleis ein kan konvertere ein tekststreng med nøkkel/verdi par til ein dict."""
    streng = "ost=snacks;lakris=best;gras=ugh;"

    streng_som_liste = streng.split(";")
    streng_som_liste.pop()  # Med ein ";" på slutten blir det eit tomt element på slutten.

    # print(f"streng_som_liste: {streng_som_liste}")

    ny_dict = {}
    for i in streng_som_liste:
        print(i)
        key, value = i.split("=")
        ny_dict[key] = value
    return ny_dict


def tilES(key_list: list, value) -> dict:
    """Skal ta imot ein tekststreng på følgende format, og konveretere til JSON/dict: ost.kvitost.skivet:True"""

    if len(key_list) > 1:
        element = key_list.pop()
        results = tilES(key_list, {element: value})

        # print(f"key_list: {key_list}, element: {element}, value: {value}")
        # print(f"resultatet: {results}")
        return results

    elif len(key_list) == 1:
        element = key_list.pop()
        results = {element: value}
        return results


def es_starter():
    streng = ["ost.kvit.skivet:True",
              "ost.brun.skivet:False", "bil.person.kombi.dører:5",
              "bil.person.kombi.motor.hestekrefter:97 hk", "bil.person.kombi.motor.volum:1.4l"]
    new_dicts = []
    for stuff in streng:
        kolon = stuff.find(":")
        first_value = stuff[kolon + 1:]
        new_str = stuff[:kolon]
        new_list = new_str.split(".")
        # print(f"stuff: {stuff}, type: {type(stuff)}")
        # print(f"first: {first_value}, new: {new_str}, new_list: {new_list}")

        new_dicts.append(tilES(new_list, first_value))
    print(f"new_dicts: {new_dicts}")
    # Testing, finding all info about engine
    for i in new_dicts:
        try:
            print(f"""Motor på bil: {i["bil"]["person"]["kombi"]["motor"]}""")
        except:
            try:
                print(f"""Annet om bilen: {i["bil"]}""")
            except:
                pass
        print()


if __name__ == "__main__":
    print(f"heimetesting: {heimetesting()}")
    es_starter()
