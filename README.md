# FNF Python
Python based client framework version of the Fast and Furious challenge.

## How-To
1. You need a `python 3.5` installation.
2. You have to install the ```pika``` module: ```sudo pip install pika``` (if you don't have pip you can download it via your package manager).
3. Just follow the instructions in the [AkkaStarterKit] (https://github.com/FastAndFurious/AkkaStarterKit), and then use one of the following options:
4. If you plan to use the simulator, make sure to use the team name corresponding to the simulator configuration
5. Start the pilot using `python pilot.py`
6. Examine the generated data in `data/`

This client will just go at constant speed and disconnect on stop.

### Remote Simulator
1. Same as "Local Simulator" but you don't have to use the starter kit, instead provide your Team-ID and Access-Code to ```Client```:
2. Check the [pilot.py] (pilot.py) file for a basic overview on how-to use the client
