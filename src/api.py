# -*- coding: utf-8 -*-
from typing import Dict

from src.client import CrowdinClient


def get_project_details(client: CrowdinClient) -> Dict:
    result = client.get(method='info')

    return {
        'name': result.get('details').get('name'),
        'source':
            result.get('details').get('source_language').get('code'),
        'languages':
            [lang.get('code') for lang in result.get('languages')],
        'last_build': result.get('details').get('last_build'),
        'last_activity': result.get('details').get('last_activity')
    }


def map_language_status(language: Dict) -> Dict:
    return {
        'name': language.get('name'),
        'code': language.get('code'),
        'translated': {
            'phrases': language.get('translated'),
            'words': language.get('words_translated'),
            'progress': language.get('translated_progress'),
        },
        'approved': {
            'phrases': language.get('approved'),
            'words': language.get('words_approved'),
            'progress': language.get('approved_progress'),
        },
    }


def get_project_status(client: CrowdinClient) -> Dict:
    result = client.get(method='status')

    return {
        'phrases': result[0].get('phrases'),
        'words': result[0].get('words'),
        'languages': [map_language_status(lang) for lang in result],
    }
