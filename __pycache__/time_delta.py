# When users post an update on social media,such as a URL, image, status update etc., 
# other users in their network are able to view this new post on their news feed. Users can also see exactly when 
# the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. 
# You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

import math
import os
import random
import re
import sys
from datetime import datetime
def time_delta(t1, t2):
    time1=datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    time2=datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(int(abs(time1-time2).total_seconds()))
