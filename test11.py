from dataclasses import dataclass



@dataclass
class DatabaseConfig:
    host: str  # URL-адрес базы данных
    user: str  # Username пользователя базы данных
    password: str  # Пароль к базе данных
    database: str  # Название базы данных


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    bot: TgBot
    db: DatabaseConfig


my_config = Config(
    bot=TgBot(token="mytoken", admin_ids=[123123123]),
    db=DatabaseConfig(
        host="https://db.my",
        user="admin",
        password="mysecretpass",
        database="MyDB"
    )
)

print(my_config.bot.token)
print(my_config.bot.admin_ids)

print(type(range(5)))