from decouple import config
from nanoleafapi import Nanoleaf, RED
import time

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('DeijAlert')

LOCAL_IP = config('LOCAL_IP')

def deijalert():
    """Set the nanoleaf wall on the local network to pulse red for 10 seconds."""
    nl = Nanoleaf(LOCAL_IP)
    is_on = nl.get_power()
    current_effect = nl.get_current_effect()
    
    nl.pulsate(RED) 
    logger.info('Pulsing Nanoleaf red for 10 seconds')
    time.sleep(10)
    
    logger.info('Setting Nanoleaf to previous state')
    if is_on:
        nl.set_effect(current_effect)
    else:
        nl.power_off()
    logger.info('Done')

if __name__ == "__main__":
    deijalert()
