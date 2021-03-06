import pandas as pd


def to_datetime(event_db: pd.DataFrame) -> pd.DataFrame:
    """Transform dates in incident database to datetime objects

    Args:
        event_db: Incident database dates as strings

    Returns:
        Incident database dates as strings
    """
    event_db["date_of_data"] = event_db["date_of_data"].apply(lambda x:
                                                              pd.to_datetime(x,
                                                                             dayfirst=True,
                                                                             errors='coerce',
                                                                             )
                                                              )
    return event_db
