#!/usr/bin/env python3

import os.path

from dotenv import load_dotenv

from src.main import app

if os.path.isfile("../.env"):
    load_dotenv("../.env")

if __name__ == "__main__":
    app.run(debug=True)
