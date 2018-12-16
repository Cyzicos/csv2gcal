

def date_conv(date):
    schema = id_date_schema(date)
    if schema == 'single':
        parsed = parse_single_schema(date)
    elif schema == 'mult':
        parsed = parse_sep_schema(date, meta_sep='-')
    elif schema == 'plus':
        parsed = parse_sep_schema(date, meta_sep='+')

    return (f'{parsed[0]}-{parsed[1]}-{parsed[2]}',
            f'{parsed[3]}-{parsed[4]}-{parsed[5]}')


def id_date_schema(date):
    if '/' in date and len(date) == 10:
        return 'single'
    if '-' in date:
        return 'mult'
    if '+' in date:
        return 'plus'

    raise ValueError('No fitting schema found for:', date)


def parse_single_schema(date):
    mon, day, year = date.split('/')
    return year, mon, day, year, mon, day


def parse_sep_schema(date, meta_sep='-'):
    split = date.split(meta_sep)

    if len(split[0]) < 4:
        # Same month
        day, mon, year = split[1].split('.')
        return year, mon, split[0][:-1], year, mon, day

    start_day, start_mon, _ = split[0].split('.')
    day, mon, year = split[1].split('.')
    return year, start_mon, start_day, year, mon, day
