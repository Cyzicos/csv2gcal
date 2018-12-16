from csv2gcal import date_utils


def test_id_date_schema():
    single_day = '11/05/2018'
    assert date_utils.id_date_schema(single_day) == 'single'
    multiple_days = '22.-24.03.2019'
    assert date_utils.id_date_schema(multiple_days) == 'mult'
    plus_days = '29.+30.05.2019'
    assert date_utils.id_date_schema(plus_days) == 'plus'


def test_parse_single_schema():
    parsed = date_utils.parse_single_schema('11/05/2018')
    assert parsed == ('2018', '11', '05', '2018', '11', '05')


def test_parse_mult_schema():
    parsed = date_utils.parse_sep_schema('22.-24.03.2019')
    assert parsed == ('2019', '03', '22', '2019', '03', '24')
    parsed = date_utils.parse_sep_schema('31.03.-02.04.2019')
    assert parsed == ('2019', '03', '31', '2019', '04', '02')


def test_parse_plus_schema():
    parsed = date_utils.parse_sep_schema('22.+24.03.2019', '+')
    assert parsed == ('2019', '03', '22', '2019', '03', '24')
    parsed = date_utils.parse_sep_schema('31.03.+02.04.2019', '+')
    assert parsed == ('2019', '03', '31', '2019', '04', '02')


def test_date_conv():
    assert date_utils.date_conv('11/05/2018') == ('2018-11-05', '2018-11-05')
    assert date_utils.date_conv(
        '22.-24.03.2019') == ('2019-03-22', '2019-03-24')
    assert date_utils.date_conv(
        '29.+30.05.2019') == ('2019-05-29', '2019-05-30')
