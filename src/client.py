# -*- coding: utf-8 -*-
import json
from typing import Dict

import requests


class CrowdinClient:
    URL = 'https://api.crowdin.com/api/project/{{name}}/{{method}}'

    def __init__(self, key: str, project: str):
        self.key = key
        self.project = project

    def get(self, method: str, params: Dict=None):
        """
        Retrieve request from api
        :param method:
        :param params:
        :return:
        """
        if params is None:
            params = {}

        params['key'] = self.key
        params['json'] = ''

        return requests.get(self._make_url(method), params)

    def _make_url(self, method: str) -> str:
        """
        Generate the api url
        :param method:
        :return:
        """
        url = self.URL
        return url\
            .replace('{{name}}', self.project).replace('{{method}}', method)

    def process_results(self, result: Dict) -> Dict:
        """

        :param result:
        :return:
        """
        response_json = json.loads(result.content.decode('utf-8'))
        contents = {
            'name': response_json.get("details").get("name"),
            'source':
                response_json.get("details").get("source_language").get("code"),
            'languages':
                [lang.get('code') for lang in response_json.get("languages")],
            'last_build':  response_json.get("details").get("last_build"),
            'last_activity':  response_json.get("details").get("last_activity")
        }

        return contents
