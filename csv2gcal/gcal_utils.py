'''Uses google calender api utils'''

import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def get_service():
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('calendar', 'v3', http=creds.authorize(Http()))


def create_gcal_event(title,
                      date,
                      location='',
                      start_time='00:00:00',
                      end_time='01:00:00',
                      time_zone_diff='+01:00',
                      time_zone_loc='Europe/Berlin',
                      ):
    start_date, end_date = date
    event = {
        'summary': title,
        'location': location,
        'start': {
            'dateTime': f'{start_date}T{start_time}{time_zone_diff}',
            'timeZone': time_zone_loc,
        },
        'end': {
            'dateTime': f'{end_date}T{end_time}{time_zone_diff}',
            'timeZone': time_zone_loc,
        },

    }
    return event


def to_gcal_events(events):
    return [create_gcal_event(**event) for event in events]


def add_event(service, calendarId, event_dict):
    service.events().insert(calendarId=calendarId, body=event_dict).execute()


def add_events(service, cal_id, event_dicts):
    for event in event_dicts:
        add_event(service, cal_id, event)
