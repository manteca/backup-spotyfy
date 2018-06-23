import argparse


def get_parameters():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('username', type=str, help='The username of the Spotify account')
    parser.add_argument('-v',"--verbose", help='Detail output on screen', action="store_true")
    # TODO: Export om json
    # TODO: Export om CVS
    # TODO: Export om TXT


    return parser.parse_args()
