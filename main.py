#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse 
import utils.color_print as color_print

from scan.JavaScan import JavaScan
from utils.check import checkEnv,checkDB, checkQL


print('''Welcome to 
_______________.___. _________            .___     ________  .____     
\______   \__  |   | \_   ___ \  ____   __| _/____ \_____  \ |    |    
 |     ___//   |   | /    \  \/ /  _ \ / __ |/ __ \ /  / \  \|    |    
 |    |    \____   | \     \___(  <_> ) /_/ \  ___//   \_/.  \    |___ 
 |____|    / ______|  \______  /\____/\____ |\___  >_____\ \_/_______ \
           \/                \/            \/    \/       \__>       \/
''')


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('-d', '--database', type=str, help='CodeQL database dir of target project')
    args.add_argument('-s', '--skip', action="store_true", help='Skip checking environment')

    parse_args = args.parse_args()

    if not parse_args.database:
        args.print_help()
        sys.exit()

    # 跳过环境检测，第一次不建议跳过，后续跳过节省时间
    if not parse_args.skip:
        if not checkEnv() or not checkDB(parse_args.database):
            color_print.error("Environment Error")
            sys.exit()

        if not checkQL(parse_args.database):
            color_print.error("qlpath error,check it at config/config.ini")
            sys.exit()

        color_print.info("Environment Check Success, start to scan database.")

    JavaScan().run(parse_args.database)

