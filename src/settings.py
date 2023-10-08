from decouple import config


DATABASE_URI = config("DATABASE_URI", default="localhost")
