TORTOISE_ORM = {
    "connections": {"default": "mysql://root:123456789@127.0.0.1:3306/tortoise"},
    "apps": {
        "models": {
            "models": ["model.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}