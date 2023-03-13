from time import strptime, strftime
from aiogram_dialog import DialogManager

from database.bot_db import BotDB


async def all_dates_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    dates_list = []
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


async def dates_by_state_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    dates_list = []
    with BotDB() as db:
        fetched_dates = db.get_dates_by_states(user_id=dialog_manager.current_context().start_data,
                                               state=dialog_manager.current_context().dialog_data["state"])

    for date_tuple in fetched_dates:
        prepared_date_tuple = strftime("%d-%m-%y", strptime(date_tuple[0], "%Y-%m-%d")), date_tuple[0]
        dates_list.append(prepared_date_tuple)

    dates_dict = {
        "dates": dates_list,
        "count": len(dates_list)
    }

    return dates_dict


async def event_info_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    with BotDB() as db:
        event_info = db.get_event_by_day(user_id=dialog_manager.current_context().start_data,
                                         date=dialog_manager.current_context().dialog_data["event_date"])

    event_info_dict = {
        "event_info": event_info,
        "count": len(event_info)
    }

    print(event_info_dict)
    return event_info_dict
