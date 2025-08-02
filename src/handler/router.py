from . import base, chat


def get_routers() -> list:
    return [
        base.router,
        chat.router,
    ]
