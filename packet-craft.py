#!/usr/bin/env python

# if you run into problems you may need to change the above line to
# the following:  #!/opt/miniconda/bin/python

# import all scapy, you should not need additional imports
from scapy.all import *

# craft your packet here
packet=IP()

# send your packet and store the response in a variable named response
response=sr(packet)

