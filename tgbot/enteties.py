from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class FrequencyTypes(Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'


@dataclass
class Options:
    subscription_status: bool | None  # Статус подписки на получение карточек (True - активно, False - неактивно).
    subscription_frequency: FrequencyTypes | None  # Частота подписки (Ежедневно, еженедельно, ежемесячно).
    custom_time: str | None




@dataclass
class Results:
    test_id: int
    date_taken:  datetime
    score: int
    attempt: int





@dataclass
class TgBot:
    token: str


@dataclass
class Picture:
    id: int
    link_to_picture: str
    article_name: str

@dataclass
class User:
    id: int
    first_name: str | None
    last_name: str | None
    username: str | None
    options: Options | None
    viewed_pictured: list[Picture] | None # Список картинок котрые уже были отправлены пользователю
    test_results: list[Results] | None  # Список результатов тестов(можно хранить в виде id тестов и полученных результатов).