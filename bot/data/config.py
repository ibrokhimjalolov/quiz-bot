from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
DEVELOPERS = env.list("DEVELOPERS")
IP = env.str("IP")

PG_DATABASE = env.str("PG_DATABASE")
PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
PG_HOST = env.str("PG_HOST")
PG_PORT = env.str("PG_PORT")



