from get_auth_token import get_auth_token
from argument_parser import parser
from scrapevids import scrapevids
from constants import DATA_PATH, PLAYLIST
from updatedatabase import updatedb

args = parser.parse_args()

if __name__=='__main__':
    if args.command == 'getauthtoken':
        token = get_auth_token(args.username, args.password, args.baseurl)
        print(f'Token {token}')

    elif args.command == 'scrapevids':
        scrapevids(PLAYLIST, DATA_PATH)

    elif args.command == 'updatedb':
        updatedb(args.baseurl, args.authtoken)

    else: 
        parser.print_help()


