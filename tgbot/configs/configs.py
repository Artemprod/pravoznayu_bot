from tgbot.enteties import TgBot
from environs import Env


def load_config(path: str) -> TgBot:
    env = Env()
    env.read_env(path)
    return TgBot(
        token=env("BOT_TOKEN"),
    )
