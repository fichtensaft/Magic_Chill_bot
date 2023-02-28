import datetime


# All getters should return a dict for aiogram-dialog library

async def date_getter(**kwargs) -> dict:
    """Function for getting today's date and sending it to the Date part (1st part) of Memo-dialog"""
    today_dict = {"date_today": datetime.date.today().strftime('%d-%m-%y')}

    return today_dict


async def places_getter(**kwargs) -> dict:
    """
    Function to get places for the second window of Memorizing Dialog (place's part (2))
    :param kwargs: Usually no input
    :return: dict. The dictionary is a tuple (place - id) -> (items in web-docs)
             Though 'count' can be deleted, it used in web-docs for... counting items. Should leave it this way
    """
    places = [("Quarry 🦫🪨", "Иля"),
              ("Shaman hut 🛖", "Кирилл"),
              ("CyberFactory 🏭", "Потап"),
              ("Casa grande 🦄", "Лёха"),
              ("Po-Lounge ⚙", "Диман"),
              ("Le Garage 🏴‍☠", "Паша"),
              ("The forest 🌳", "Лёня"),
              ("Other 🌋...", "Атолл"),
              ]

    places_dict = {
        "places": places,
        "count": len(places)
    }

    return places_dict


async def get_friends(**kwargs) -> dict:
    """
    Function to get dictionary of friends for the Friends part (3) of Memo-dialog
    :param kwargs: Usually no input
    :return: dict. The dictionary is a tuple (place - id) -> (items in web-docs)
    """
    friends = [("Иля 🧙‍♂", "Иля"),
               ("Кирилл 🧑‍🚀️", "Кирилл"),
               ("Потап 👨‍🏭", "Потап"),
               ("Лёха 👨‍🌾", "Лёха"),
               ("Диман 🧑‍🍳", "Диман"),
               ("Паша 🧛", "Паша"),
               ("Лёня 👷🏻‍♂️", "Лёня"),
               ("Атолл️ 💂‍♂️", "Атолл"),
               ("Рита 👰‍♀️", "Рита"),
               ("Варя 🧝‍♀️", "Варя"),
               ("Мари 🙇‍♀️", "Мари"),
               ("Настя 🧚‍♀️️", "Настя"),
               ]

    out_dict = {
        "friends": friends,
        "count": len(friends)
    }

    return out_dict
