# -*- coding: utf-8 -*-
from typing import Dict

from argparse import ArgumentParser
import asciiplotlib as apl

from src.api import get_project_status
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


def print_project_status(details: Dict) -> None:
    formatters = {
        'HEADER': '\033[95m',
        'GREEN': '\033[92m',
        'BOLD': '\033[1m',
        'END': '\033[0m',
    }

    output = """
{BOLD}{HEADER}Status{END}
- {GREEN}phrases{END}: {phrases}
- {GREEN}words{END}: {words}
        """\
        .format(
            phrases=details['phrases'],
            words=details['words'],
            **formatters)

    language_list = list(map(
        lambda language: [
            language['code'],
            "{value} ({progress}%)".format(
                value=language['translated']['phrases'],
                progress=language['translated']['progress']),
            "{value} ({progress}%)".format(
                value=language['approved']['phrases'],
                progress=language['approved']['progress'])],
        details['languages']))

    data = [
        [['languages', 'translated', 'approved']],
        language_list]

    fig = apl.figure()
    fig.table(data, border_style="thin", padding=(0, 1))

    print(output)
    fig.show()



argument_parser = define_argument_parser()
arguments = argument_parser.parse_args()

client = CrowdinClient(
    key=arguments.project_key,
    project=arguments.project_identifier)

print_project_status(
    get_project_status(client))
