from time import strptime, strftime
from aiogram_dialog import DialogManager

from database.bot_db import BotDB


async def dates_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    dates_list = []
    with BotDB() as db:
        fetched_dates = db.get_dates(user_id=dialog_manager.current_context().start_data)

    for date_tuple in fetched_dates:
        prepared_date_tuple = strftime("%d-%m-%y", strptime(date_tuple[0], "%Y-%m-%d")), date_tuple[0]
        dates_list.append(prepared_date_tuple)

    # print("fetched:", fetched_dates)
    # print("for-looped:", dates_list)

    dates_dict = {
        "dates": dates_list,
        "count": len(dates_list)
    }

    return dates_dict


async def event_info_getter(**kwargs) -> dict:
    pass
