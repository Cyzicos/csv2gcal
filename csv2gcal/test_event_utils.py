from csv2gcal import event_utils
import numpy as np


def test_is_int():
    assert event_utils.is_int('1')
    assert not event_utils.is_int('s')


def test_remove_garbage():
    pass
    with_garbage = [['MVG Terminkalender 2018', '', '', ''],
                    ['November', '', '', ''],
                    ['11/05/2018', 'Ständle – 70 Jahre', '', 'Grafenau'],
                    ['11/10/2018', 'SWR 1 Disco', 'Graf Ulrich Bau', 'Döffingen']]
    without_garbage = [['11/05/2018', 'Ständle – 70 Jahre', '', 'Grafenau'],
                       ['11/10/2018', 'SWR 1 Disco', 'Graf Ulrich Bau', 'Döffingen']]
    removed = event_utils.remove_garbage(with_garbage)
    assert len(removed) == 2


def test_is_valid_event():
    assert not event_utils.is_valid_event(
        ['MVG Terminkalender 2018', '', '', ''])
    assert event_utils.is_valid_event(
        ['11/05/2018', 'Ständle – 70 Jahre', '', 'Grafenau'])


def test_time_conv():
    assert event_utils.time_conv('11/05/2018') == '2018-05-11'


def test_event_time_conv():
    conv_event = event_utils.event_time_conv(['11/10/2018',
                                              'SWR 1 Disco',
                                              'Graf Ulrich Bau',
                                              'Döffingen'])
    assert conv_event[0] == '2018-10-11'


def test_merge_cols():
    event = event_utils.event_time_conv(['11/10/2018',
                                         'SWR 1 Disco',
                                         'Graf Ulrich Bau',
                                         'Döffingen'])
    merged_event = event_utils.merge_cols(event, cols=[2, 3], sep=', ')
    assert merged_event[2] == 'Graf Ulrich Bau, Döffingen'


def test_stage_event():
    clean_event = ['2018-10-11', 'SWR 1 Disco', 'Graf Ulrich Bau, Döffingen']
    events = event_utils.stage_events(
        [['11/10/2018', 'SWR 1 Disco', 'Graf Ulrich Bau', 'Döffingen']])

    event = events[0]
    bools = [clean_elem == elem for clean_elem,
             elem in zip(clean_event, event)]
    assert np.logical_and.reduce(bools)
