'''
Created on Jul 14, 2012

@author: jon
'''

from struct import unpack


def parse(data):
    while 1:
        # Parse payload length
        length_bytes = data.read(2)
        if not length_bytes:
            break
        packet_length = unpack('>H', length_bytes)[0]

        # Parse payload (rest of packet)
        packet_payload = data.read(packet_length)
        if not packet_payload:
            break

        yield packet_payload
