import re

from utils import my_utils


def clean_urls(event_db):
    event_db = my_utils.split_strings_at_comma_and_distribute_to_new_rows(event_db, 'URL_1')
    event_db.URL_1 = event_db.URL_1.str.strip()
    event_db.URL_1 = event_db.URL_1.apply(_remove_guillemets).apply(_only_keep_valid_urls)
    return event_db


def _remove_guillemets(url):
    # Remove the first and last guillemets. Found in URLs of edb
    try:
        url = re.sub(r'<', '', url, 1)
        url = re.sub(r'>', '', url[::-1], 1)
        url = url[::-1]
    except TypeError:
        url = None
    return url


def _only_keep_valid_urls(url):
    # Inspired from django
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, str(url)):
        return url
    else:
        return None