import discord
import datetime 

class EmbedHandler(discord.Embed):
    COLOR = {
        "nor": 0x6ecc9,
        "err": 0xff0000,
        "exc": 0xff0000
    }

    def __init__(self, kind = "nor", fields: dict | None = None, **kwargs):
        super().__init__(color = self.COLOR.get(kind, self.COLOR["nor"]), **kwargs)
        for name, value in (fields or {}.items()):
            self.add_field(name = name, value = value)

    def add_fields(self, fields : dict, *, inline : bool = False):
        for name, value in fields.items():
            self.add_field(name = name, value = value, inline = inline)
        return self

