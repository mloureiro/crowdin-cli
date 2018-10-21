# -*- coding: utf-8 -*-
import json
from typing import Dict

import requests


class CrowdinClient:
    URL = 'https://api.crowdin.com/api/project/{{name}}/{{method}}'

    def __init__(self, key: str, project: str):
        self.key = key
        self.project = project

    def get(self, method: str, params: Dict=None) -> Dict:
        """
        Retrieve request from api
        """
        if params is None:
            params = {}

        params['key'] = self.key
        params['json'] = ''

        result = requests.get(self._make_url(method), params)

        return json.loads(result.content.decode('utf-8'))

    def _make_url(self, method: str) -> str:
        """
        Generate the api url
        """
        return self.URL\
            .replace('{{name}}', self.project)\
            .replace('{{method}}', method)
