#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

from __future__ import print_function

import argparse
import sys

from btsbots import metadata
import json


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """
    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '--config', type=argparse.FileType('r'),
        help='config file for btsbots')
    arg_parser.add_argument(
        '--profile', type=argparse.FileType('r'),
        help='profile file for btsbots')
    arg_parser.add_argument(
        'command',
        choices=['run_trade', 'update_profile'], nargs='?',
        help='the command to run')
    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))

    args = arg_parser.parse_args(args=argv[1:])

    config_info = {}
    if (args.config):
        config_info = json.load(args.config)

    if args.command == "run_trade":
        print("wait ....")
        pass
    elif args.command == "update_profile":
        profile_info = {}
        if (args.profile):
            profile_info = json.load(args.profile)

        from btsbots.profile_op import ProfileOP
        profile_op = ProfileOP(config_info)
        profile_op.update_profile(profile_info)
    else:
        print(epilog)

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()