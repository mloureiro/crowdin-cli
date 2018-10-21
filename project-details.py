# -*- coding: utf-8 -*-
import argparse

from src.api import retrieve_info

parser = argparse.ArgumentParser()

parser.add_argument(
    '-p', '--project-identifier', help='Project identifier (name)',
    required=True)

parser.add_argument(
    '-k', '--project-key', help='Project API key', required=True)

args = parser.parse_args()

if __name__ == '__main__':
    retrieve_info(args)
