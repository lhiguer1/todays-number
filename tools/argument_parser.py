from argparse import ArgumentParser
import urllib.parse


parser:ArgumentParser = ArgumentParser(description='Helpful database management tools')
subparsers = parser.add_subparsers(dest='command')

##########################################################################################
scrape_parser:ArgumentParser = subparsers.add_parser('scrapevids', description='Scrape videos from playlist')

##########################################################################################
update_parser:ArgumentParser = subparsers.add_parser('updatedb', description='Process videos and update database')
update_parser.add_argument('--baseurl',
    type=urllib.parse.urlparse,
    required=True,
    help='Location of endpoints. Will be used as follows: {baseurl}/api/2022/'
)

update_parser.add_argument('--authtoken',
    type=str,
    help='Authorization token',
    required=True
)

##########################################################################################
auth_token_parser:ArgumentParser = subparsers.add_parser('getauthtoken', description='Get authentication token')
auth_token_parser.add_argument(
    '--username',
    action='store',
    required=True
)

auth_token_parser.add_argument(
    '--password',
    action='store',
    required=True
)

auth_token_parser.add_argument('--baseurl',
    type=urllib.parse.urlparse,
    required=True,
    help='Location of endpoints. Will be used as follows: {baseurl}/api/2022/'
)
