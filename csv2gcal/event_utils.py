import csv
from csv2gcal import date_utils


def stage_events(events):
    events = remove_garbage(events)
    events = merge_all_cols(events,  cols=[2, 3], sep=', ')
    events = conv_dates(events)
    events = to_dicts(events)
    return events


def load_csv(path):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        return list(spamreader)


def remove_garbage(events):
    return [event for event in events if is_valid_event(event)]


def merge_all_cols(events, **kwargs):
    return [merge_cols(event, **kwargs) for event in events]


def to_dicts(events):
    return [to_dict(event) for event in events]


def to_dict(event):
    return {'date': event[0], 'title': event[1], 'location': event[2]}


def conv_dates(events):
    return [event_date_conv(event) for event in events]


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_valid_event(event):
    if not event[0]:
        return False
    return is_int(event[0][0])


def event_date_conv(event):
    event[0] = date_utils.date_conv(event[0])
    return event


def merge_cols(event, cols=None, sep=''):
    if not cols:
        return event
    event[cols[0]] = event[cols[0]]+sep+event[cols[1]]
    return event
