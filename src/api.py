# -*- coding: utf-8 -*-
import json
from typing import Dict, NamedTuple

from src.client import CrowdinClient


def process_results(result: Dict) -> Dict:
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
        'last_build': response_json.get("details").get("last_build"),
        'last_activity': response_json.get("details").get("last_activity")
    }

    return contents


def retrieve_info(args: NamedTuple) -> None:
    """

    :return:
    """
    client = CrowdinClient(
        key=args.project_key, project=args.project_identifier)
    results = client.get(method='info')
    process_results(results)
