# -*- coding: utf-8 -*-
from typing import Dict

from src.client import CrowdinClient


def get_project_details(client: CrowdinClient) -> Dict:
    result = client.get(method='info')

    return {
        'name': result.get("details").get("name"),
        'source':
            result.get("details").get("source_language").get("code"),
        'languages':
            [lang.get('code') for lang in result.get("languages")],
        'last_build': result.get("details").get("last_build"),
        'last_activity': result.get("details").get("last_activity")
    }
