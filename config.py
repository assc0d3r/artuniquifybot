import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5897885316:AAEchiE7Kpm_EObAW_6PHaTXWZuTiiGQW88")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "10038985"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b13a9434d5f59fdb592bf3cd0f457eff")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1187675214").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "arttgcf")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "1BJWap1wBu7jiwHW_Y_WzZSyn0WrFwrdBDvr2bNeYNgJz9GDFdQxq571rrLYi1jCFDR4mU0v2Zmqr6O9tHnjzuAAlXtpSeebTikVyUredDVpNmTQaiAYnnvUJTU-wLOOC76WOQe5Ub714b3TEAfEUWz_U6pLnkNOuJ-zzU40YPXqZ9yLADy975Ei7ek_mP8cM3alxCh1hBihfK_sn4MRi5E8axvB0q5IZYzuH_F-Wvp4_dVU_i5JaUpD-a1NjLIyTdTl5Ee5ASQG27Z35H-lW2d--ee6jv4wDsp-0P7SxMRCuPg_trFyQbE7n1SLkxPZGwz222rgZ4tuhy-kyJjN9fWBCwKFKH6g=")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
