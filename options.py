import argparse


def get_parameters():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('username', type=str, help='The username of the Spotify account')

    return parser.parse_args()
