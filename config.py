"""Configuration settings for FLL Pit Display."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'fllipit.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = False
EVENT_NAME = 'Littleton FLL Qualifier'
TEST_DB = False
DB_FILE = 'E:\\users\\m172108\\github\\database\\FLL 2018 INTO ORBIT blank as of 100918.accdb'

# The number of qualifying rounds, minimum is 
USE_5_QUAL_ROUNDS = True