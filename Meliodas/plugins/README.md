## Meliodas bot example plugin format here :
You can create your own custom plugin useing this format or use any [pyrogram](http://pyrogram.org) method !


```
from Meliodas import app
from Meliodas.utils.commands import *

@app.on_message(command("test"))
async def plug(_, message):
    OfficiallMeliodas = await message.reply_text(text="Hello I am Meliodas"
    )
    Denz = """
I'm a group management bot with some useful features.
@MeliodasRobot    
    """
    await OfficiallMeliodas.edit_text(denz)

__MODULE__ = "test"
__HELP__ = """  
/test - test cmd here
"""
```

