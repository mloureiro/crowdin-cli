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
