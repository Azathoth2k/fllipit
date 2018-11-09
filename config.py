"""Configuration settings for FLL Pit Display."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'fllipit.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = False
EVENT_NAME = 'Maine FLL Championship'
TEST_DB = False
DB_FILE = 'C:\\path\\to\\access\\database.accdb'

# The number of qualifying rounds, minimum is 
USE_5_QUAL_ROUNDS = False