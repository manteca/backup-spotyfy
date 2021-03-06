#!/usr/bin/env python3.5

import sys
import spotipy
import spotipy.util as util
import options

import os
import math
import json

CEND    = '\33[0m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

def Main():
    os.environ["SPOTIPY_CLIENT_ID"]='6762886347a94279b49ef02426037de6'
    os.environ["SPOTIPY_CLIENT_SECRET"]='795e1767ff204191b23c0fc69389c01a'
    os.environ["SPOTIPY_REDIRECT_URI"]='http://localhost'

    scope = 'user-library-read'

    # if len(sys.argv) > 1:
    #     username = sys.argv[1]
    # else:
    #     print("Usage: %s username" % (sys.argv[0],))
    #     sys.exit()

    arg = options.get_parameters()

    # Promt for user permission
    token = util.prompt_for_user_token(arg.username, scope)

    if token:
        if(arg.verbose):
            print("Token succesfull generated")
        # To find how many tracks are stpred
        cantidad_x_pag = 50 # Max Value accepted formo API
        cantidad_pag = 0
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks(1)

        # Print data in jason format. Transform Unicode to string FOR TEST
        if(arg.verbose):
            print("{} result to get".format(results["total"])
        # Save data in jason format. Transform Unicode to string FOR TEST
        # print(json.dumps(results))

        total =  results["total"]
        cantidad_pag = int(math.ceil(total / (cantidad_x_pag *1.0)))
        f = open('lista_musica.txt', 'w')

        # TODO: User can select if they wannt these output
        fjson = open('lista_musica_json.txt', 'w')
        merged_dict = []

        # Parse the pages to get the tracks
        for x in range(0, cantidad_pag):
            results = sp.current_user_saved_tracks(cantidad_x_pag, x)
            data = results['items']
            i=0
            while i < len(data):
                merged_dict.append(data[i])
                i += 1

            for item in results['items']:
                track = item['track']
                if(arg.verbose):
                    print("["+ CGREEN + "+" + CEND + "]" + track['name'].encode('utf-8') + ' - ' + track['artists'][0]['name'].encode('utf-8'))
                f.write(track['name'].encode('utf-8') + ' - ' + track['artists'][0]['name'].encode('utf-8') + '\n')


        fjson.write(json.dumps(merged_dict))
        fjson.close()
        f.close()
    else:
        print("Can't get token for", username)

if __name__ == '__main__':
    Main()
