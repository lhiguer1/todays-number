import argparse
from utils import update_database

def main():
    parser = argparse.ArgumentParser(description='Helpful tools for database')
    sub_parsers = parser.add_subparsers(title='Available subcommands', dest='subcommand')
    sub_parsers.add_parser('updatedatabase', description='Extract info from playlist to update database', help='Update database')

    args = parser.parse_args()
    subcommand = args.subcommand

    if subcommand == 'updatedatabase':
        update_database()
    else:
        parser.print_usage()

if __name__=="__main__":
    main()
