# -*- coding: utf-8 -*-

import os

DEBUG = os.getenv("DEBUG", True)

IP_ADDRESS = os.getenv("IP_ADDRESS", "0.0.0.0")
PORT = os.getenv("PORT", 5000)

VERSION = os.getenv("VERSION", "0.0.1")
SECRET_KEY = os.getenv("SECRET_KEY", "KnowLedge")
