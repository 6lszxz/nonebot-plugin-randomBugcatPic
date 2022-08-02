from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.params import Arg, CommandArg, ArgPlainText
import random

getBC = on_command(cmd="随机猫猫虫",priority=5)

@getBC.handle()
async def sendPic(matcher : getBC ):
    num = random.randint(1, 79)
    link = 'http://43.142.78.228:8000/' + str(num) +'.gif'
    await getBC.send(MessageSegment(type = 'image',data={'file':link}))



