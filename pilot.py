from client import Client
import os
import json
import time

TEAM_NAME = 'python starter'
configs = {
    'local' : { # for access to the simulator, change accordingly
        'TEAM_NAME' : TEAM_NAME,
        'ACCESS_CODE' : 'züwermepa',
        'RABBIT_HOST' : 'localhost'
        },
    'remote' : { # for access to the race track, change accordingly
        'TEAM_NAME' : TEAM_NAME,
        'ACCESS_CODE' : 'teifarseudo',
        'RABBIT_HOST' : '192.168.1.163'
        }
    }
# choose configuration
config = configs['local']

# client used for receiving messages and setting the power control
client = Client(config['TEAM_NAME'], config['ACCESS_CODE'])
RABBIT_HOST = config['RABBIT_HOST']

msgs = []
def receive(msg, event):
    """ utility function for logging incoming messages """
    msgs.append(msg)

def onRaceStart(msg):
    print('start')
    receive(msg)
    client.powerControl(powerValue)

def onVelocity(msg):
    receive(msg)
    client.powerControl(powerValue)

def onSensor(msg):
    receive(msg)
    client.powerControl(powerValue)

def onPenalty(msg):
    receive(msg)
    client.powerControl(powerValue)

def onRoundPassed(msg):
    receive(msg)
    client.powerControl(powerValue)

def onRaceStop(msg):
    receive(msg)
    client.disconnect()
    with open(os.path.join('data','{}.json'.format(time.strftime('%Y-%m-%d-%H-%M'))), 'w') as f:
        json.dump(self.msgs, f)

client.onRaceStart(onRaceStart)
client.onVelocity(onVelocity)
client.onSensor(onSensor)
client.onPenalty(onPenalty)
client.onRoundPassed(onRoundPassed)
client.onRaceStop(onRaceStop)

client.connect(RABBIT_HOST)
client.announce()
