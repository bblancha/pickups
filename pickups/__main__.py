import argparse
import logging
import os
import sys

import appdirs
import hangups.auth

from .server import Server

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logging.getLogger('hangups').setLevel(logging.WARNING)
    dirs = appdirs.AppDirs('hangups', 'hangups')

    parser = argparse.ArgumentParser(description='IRC Gateway for Hangouts')
    parser.add_argument('--cookies', help='cookies filename', default='cookies.json')
    parser.add_argument('--address', help='bind address', default='127.0.0.1')
    parser.add_argument('--port', help='bind port', default=6667)
    parser.add_argument('--ascii-smileys', action='store_true',
                        help='display smileys in ascii')
    parser.add_argument('--certificate_file', default='default.cert')
    parser.add_argument('--certificate_key', default='default.key')
    args = parser.parse_args()

    default_cookies_path = os.path.join(dirs.user_cache_dir, args.cookies)
    cookies = hangups.auth.get_auth_stdin(default_cookies_path)

    Server(cookies, args.ascii_smileys).run(args.address, args.port)
