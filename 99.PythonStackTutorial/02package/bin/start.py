#__author:jack
#date 2019-12-26 12:55

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from module import main
from logs import log

main.main()

log.info("logging info")
