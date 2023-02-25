import datetime


async def date_getter(**kwargs) -> dict:
    """Function for getting today's date and sending it to the Date part of Memorizing an event - dialog"""

    today_dict = {"date_today": datetime.date.today().strftime('%d-%m-%y')}
    return today_dict
