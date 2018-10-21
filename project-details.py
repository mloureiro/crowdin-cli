# -*- coding: utf-8 -*-
import argparse

from src.client import CrowdinClient

parser = argparse.ArgumentParser()

parser.add_argument(
    '-p', '--project-identifier', help='Project identifier (name)',
    required=True)

parser.add_argument(
    '-k', '--project-key', help='Project API key', required=True)

args = parser.parse_args()

if __name__ == '__main__':
    client = CrowdinClient(
        key=args.project_key, project=args.project_identifier)
    results = client.get(method='info')
    client.process_results(results)
