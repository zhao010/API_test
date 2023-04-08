
import time

import os


def ENV(keyname):
    values = os.environ.get(keyname,"")
    return values

def sleep(n_secs):
    time.sleep(n_secs)