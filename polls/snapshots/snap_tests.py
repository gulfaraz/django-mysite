# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['SnapshotTests::test_choices_list_zero 1'] = {
    'count': 0,
    'next': None,
    'previous': None,
    'results': [
    ]
}

snapshots['SnapshotTests::test_choices_list_one 1'] = {
    'count': 1,
    'next': None,
    'previous': None,
    'results': [
        {
            'choice_text': 'Beautiful instead ahead despite measure ago current.',
            'question': 'http://testserver/api/questions/1/',
            'votes': 8928
        }
    ]
}

snapshots['SnapshotTests::test_choices_list_two 1'] = {
    'count': 2,
    'next': None,
    'previous': None,
    'results': [
        {
            'choice_text': 'Choice whatever from behavior benefit.',
            'question': 'http://testserver/api/questions/2/',
            'votes': 5635
        },
        {
            'choice_text': 'Beautiful instead ahead despite measure ago current.',
            'question': 'http://testserver/api/questions/1/',
            'votes': 8928
        }
    ]
}
