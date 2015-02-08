import http.client
import json
import random
import sys
import time
import logging

log = logging.getLogger('grot-client')

SERVER = 'grot-lukaszjagodzinski.c9.io'

if __name__ == '__main__':
    token = sys.argv[1]  # your Access Token
    game = sys.argv[2]  # 0 (development mode), 1 (duel), 2 (contest)

    time.sleep(random.random())

    # connect to the game server
    client = http.client.HTTPConnection(SERVER, 80)
    client.connect()

    # block until the game starts
    client.request('GET', '/games/{}/board?token={}'.format(game, token))

    response = client.getresponse()
    '''
    {
        "score": 0,  # obtained points
        "moves": 5,  # available moves
        "moved": [None, None],  # your last choice [x, y]
        "board": [
            [
                {
                    "points": 1,
                    "direction": "up",
                    "x": 0,
                    "y": 0,
                },
                {
                    "points": 0,
                    "direction": "down",
                    "x": 1,
                    "y": 0,
                }
            ],
            [
                {
                    "points": 5,
                    "direction": "right",
                    "x": 0,
                    "y": 1,
                },
                {
                    "points": 0,
                    "direction": "left",
                    "x": 1,
                    "y": 1,
                }
            ]
        ]
    }
    '''

    while response.status == 200:
        data = json.loads(response.read().decode())
        moves = str(data['moves'])
        score = '';
        if('score' in data.keys()):
            score = str(data['score'])
        print('Moves: ' + moves + ' Score: ' + score)
        #data['board'][0][0]['direction'];
        #here
        xpos_tmp = 3
        ypos_tmp = 3
        max_score = 0;
        for xpos in range(2,5):
            for ypos in range(2,5):
                if (data['board'][ypos][xpos]['points']>max_score):
                    ypos_tmp = ypos
                    xpos_tmp = xpos
                    #print(str(ypos_tmp) + ' ' + str(xpos_tmp))
                    # print(max_score)
                    max_score = data['board'][ypos][xpos]['points']
        
        xpos = ypos_tmp            
        xpos = xpos_tmp            
        print(str(ypos) + ' ' + str(xpos))
        #xpos = random.randint(0, 4)
        #ypos = random.randint(0, 4)

        time.sleep(random.random() * 3 + 1)

        # make your move and wait for a new round
        client.request(
            'POST', '/games/{}/board?token={}'.format(game, token),
            json.dumps({
                'x': xpos,
                'y': ypos,
            })
        )

        response = client.getresponse()