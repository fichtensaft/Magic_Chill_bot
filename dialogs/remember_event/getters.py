from time import strptime, strftime
from aiogram_dialog import DialogManager

from database.bot_db import BotDB


async def dates_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    """
    from .dialog_data passing the state (was written in handler) - so we can fetch the dates according to the state
    from DataBase
    :return: dict -> all event dates
    """
    dates_list = []
    if dialog_manager.current_context().dialog_data["state"] != "both":
        with BotDB() as db:
            fetched_dates = db.get_dates_by_states(user_id=dialog_manager.current_context().start_data,
                                                   state=dialog_manager.current_context().dialog_data["state"])
    else:
        with BotDB() as db:
            fetched_dates = db.get_dates(user_id=dialog_manager.current_context().start_data)

    for date_tuple in fetched_dates:
        prepared_date_tuple = strftime("%d-%m-%y", strptime(date_tuple[0], "%Y-%m-%d")), date_tuple[0]
        dates_list.append(prepared_date_tuple)

    dates_dict = {
        "dates": dates_list,
        "count": len(dates_list)
    }

    return dates_dict


async def event_info_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    """
    from .dialog_data returns the exact date of the event. After that the func fetches info on that day from DataBase
    :return: dict -> all info on the event day
    """
    with BotDB() as db:
        event_info = db.get_event_by_day(user_id=dialog_manager.current_context().start_data,
                                         date=dialog_manager.current_context().dialog_data["event_date"])

    event_info_list = list(event_info)
    event_info_list[1] = strftime("%d-%m-%Y, %A", strptime(event_info_list[1], "%Y-%m-%d"))

    event_info_dict = {
        "event_info": event_info_list,
        "count": len(event_info)
    }

    return event_info_dict


async def change_event_getter(**kwargs) -> dict:
    change_dict = {
        "columns": [("More memes!", "memes"),
                    ("Delete the event", "delete")
                    ]
    }

    return change_dict
