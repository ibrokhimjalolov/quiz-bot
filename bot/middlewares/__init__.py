from loader import dp
from .throttling import ThrottlingMiddleware
from .auth import AuthMiddleware


if __name__ == "bot.middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(AuthMiddleware())
