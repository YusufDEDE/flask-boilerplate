"""Flask configuration variables."""
from os import path, getenv
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    # General Config
    SECRET_KEY = getenv("SECRET_KEY")
    HOST = getenv('HOST', '127.0.0.1')
    PORT = getenv('PORT', 5000)
    DEBUG = True if getenv('DEBUG') == 'True' else False
