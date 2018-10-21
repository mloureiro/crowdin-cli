# -*- coding: utf-8 -*-
from typing import Dict

from argparse import ArgumentParser

from src.api import get_project_details
from src.client import CrowdinClient


def define_argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        '-p',
        '--project-identifier',
        help='Project identifier (name)',
        required=True)

    parser.add_argument(
        '-k',
        '--project-key',
        help='Project API key',
        required=True)

    return parser


def print_project_details(details: Dict) -> None:
    formatters = {
        'HEADER': '\033[95m',
        'GREEN': '\033[92m',
        'BOLD': '\033[1m',
        'END': '\033[0m',
    }
    output = """
{BOLD}{HEADER}Project{END}
- {GREEN}name{END}: {name}
- {GREEN}source{END}: {source_language}
- {GREEN}languages{END}: [{language_list}]
- {GREEN}last build{END}: {last_build_date}
- {GREEN}last activity{END}: {last_activity_date}
        """\
        .format(
            name=details['name'],
            source_language=details['source'],
            language_list=', '.join(details['languages']),
            last_build_date=details['last_build'] if details['last_build'] is not None else '',
            last_activity_date=details['last_activity'],
            **formatters)
    print(output)


argument_parser = define_argument_parser()
arguments = argument_parser.parse_args()

client = CrowdinClient(
    key=arguments.project_key,
    project=arguments.project_identifier)

print_project_details(
    get_project_details(client))
