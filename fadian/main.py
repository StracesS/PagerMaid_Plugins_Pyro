# 小作文生成，就算访问不了后端也可以使用。
# 适度发电促进感情，过度发电鱼塘爆炸
# 请注意不要刷屏

from secrets import choice

from pagermaid import log, Config
from pagermaid.listener import listener
from pagermaid.enums import Message
from pagermaid.services import client as request, scheduler
from pagermaid.hook import Hook


class FaDian:
    def __init__(self):
        self.data = {
            "data": [
                "-亲爱的{name}姐姐：近来寒暑不常，希自珍慰。在你那双又大又亮的眼睛里，我总能捕捉到你的宁静，你的热烈，你的聪颖，你的敏感。"
                "认识你以后我脑海里挂着的一切图画都消失得无影无踪，取而代之的是我俩在一起的欢乐时光。轻轻地爱你，让爱恋滋润你的心房；"
                "轻轻的想你，让思念充满我的内心；轻轻的感觉你，让温柔吹拂我的心灵；轻轻地爱你，直到永远。你身着一件紫红色旗袍，远远看去，"
                "真像一只小蝴蝶飞过一样，既美丽称身，又色彩柔和。海可以枯，石可以烂，我对你的爱，永不会变。我和你在这样茫茫的网海相遇，"
                "也许是我俩的缘吧！多少次和今天一样的夜晚，我透过黑色的天空追忆着你，那分明不在的事实显得如此美丽。似乎万物没有了生命，"
                "异常冰冷，此刻能感到温度和生命的，只有我唯一的心。我知道，我爱之所系在水之湄，情感的指向，注定我要在源头作长久的伫望。"
                "梦中的你，在眺望的下游，在情感河流的那边。也许可以重新将段段往事，牢牢捆扎成筏，在结束一段迷惘的眺望之后，沐着此时的雨雾，"
                "破釜沉舟般乘槎而来，在某个夜晚闯入你长夜孤灯的世界。一分钟就能让一个人心碎，一小时就能喜欢上一个人，一天就能爱上一个人。"
                "但是，要用一生的时间才能去忘掉一个人。",
                "-{name}最近有很多人喜欢，这个现象不得不说惹人深思。在这个信息化的时代，人们想当然的认为媒体平台的发展能够得到更加丰富的信息量，"
                "这也意味着可以有更加全面和客观的认知，即便是隔着冰冷屏幕。但这条论断忽视了人性的因素，因为人是很容易受欲望支配的动物。"
                "举个例子，大家以为通过她的动态可以触及到她内心最为柔软的角落，全方位了解这个人。其实不然，大部分人是无法了解事物的全部的，"
                "就如同她现在对着屏幕笑，但屏幕那端的观众却无法看到躲在她桌子下面戴着项圈的我。",
                "-{name}姐姐，我试图用那些漂亮的句子来形容你，我字字推敲写出长长的话，我总觉得不行。文字写不出你眼里的星辰，写不出你唇角的春风，"
                "无论哪个词，都及不上你的半分。",
                "-5岁的时候，我的梦想是成为一个能够保护世界于危难之中的超人，让世人皆能安稳快乐。10岁的时候，我的梦想是成为一个像莫奈一样的大画家，"
                "用我的双手绘画出大家平时无暇顾及且暂未发觉的美丽。15岁的时候，我的梦想是成为一个大作家，用我的大脑构建的天马行空的世界或故事，"
                "让人们能够通过我所构建的世界或者故事能够短暂抽离现实，享受体验到不一样的人生。而20岁的时候，我的梦想只想成为{name}姐姐的钟爱之人！"
                "而40岁的时候，我的梦想只想成为{name}姐姐一直钟爱之人！而60岁的时候，我的梦想只想成为{name}姐姐一直钟爱之人！而80岁的时候，"
                "我的梦想只想成为{name}姐姐一直钟爱之人！而100岁的时候，我的梦想只想成为{name}姐姐一直钟爱之人！而128岁的时候，"
                "我的梦想只想成为{name}姐姐一直钟爱之人！130岁的时候，我什么都不想了 因为这个世界已经没有你了",
                "-我曾经被和一个旅游团被困在了一片原始森林里，那里没有信号，电话打不出去，只能自己寻找出路。在走了几天之后我们的干粮也耗尽了，"
                "大家都有了放弃的念头，这时与我们同行的一位老人掏出了一个水晶球对我们说到，据说这个水晶球能让人在绝境时看见希望，要不试试吧。"
                "随后我将手放在了水晶球上，而我只看见了两个字：{name}",
                "-有人问我：“{name}是谁？”我想了想，该如何形容{name}呢？莎士比亚的语言实在华丽，用在{name}身上却有些纷繁了；"
                "徐志摩的风格热情似火，可我不忍将如此盛情强加于{name}；川端康城？虽优美含蓄，但{name}的可爱我是藏不住的。"
                "我不知道该如何形容{name}姐姐了。但是我知道的。{name}是我所面对的黑暗中的一点萤火；是我即将冻僵的心脏里尚存的余温。"
                "是我在残酷无情的现实里的避难所啊",
                "-有一天，有人问我：“如果{name}不爱你的话，你会是什么感受？”“就像水失去了鱼。”“不是鱼失去了水？看来{name}对你也没有那么重要嘛。”"
                "“是像水失去了鱼。水还是那谭水，它变得更平静，更清澈了，阳光洒下来，也能清晰的看到水底被照亮的石子。只是，"
                "水中再也没有鱼游动时卷起的水流，晴天时，也不再有鱼的影子，它变得有一些不一样了。之后，它遇上了干旱。在生命的尽头，"
                "它想着有鱼的那些日子。曾有条鱼在水里欢快的飘游，搅动着它的内心。”“再后来呢？”“再后来？一潭水干涸成了一滩水，"
                "路过的旅人借着它解渴，却惊诧地发现这一谭水有着淡淡的咸味。只有水知道这是他对某人的思念”。{name}我的{name}",
                "-我在床上哭了一晚上 崩溃了100次 撞了30次墙 幻觉出现3次 出现濒死感一次 刚昏过去了现在才醒 "
                "看到外面天黑了我又崩溃了因为我怎么想都想不明白 {name}为什么这么可爱",
                "-{name}姐姐！！！！啊啊啊啊啊啊啊姐姐！！！！！！！（怒吼）（变成猩猩）（飞进原始森林）（荡树藤）（创飞路过吃香蕉的猴子）"
                "（荡树藤）（摘一个榴莲）（砸死猴王）（称霸猴群）（掌握热武器技术）（入侵人类）（猩球崛起）（称霸天下）（迎娶{name}姐姐🤤）",
                "-感觉要为{name}姐姐守身如玉一辈子了，除了{name}姐姐其他的我都不嫁！",
                "-我英语不好，一次英语课老师问我wife是什么意思，我向隔壁的{name}求助，她指了指自己，我愣了许久，轻轻的说：主人",
                "-{name}姐姐的声音就像一瓶汽水。”“你指{name}的声音就是天籁之音？”“不，我的意思是，听了姐姐的声音就像夏天里的饮料机，"
                "脸贴在玻璃上许久才选到心怡的汽水，想把仔仔细细选中的汽水打开时盖子却不小心松掉了。”“然后汽水喷涌而出？”“"
                "然后我的心就扑通扑通的涌了出去，我想把我的心送给她。”"
            ],
            "date": 0
        }
        self.api = f"{Config.GIT_SOURCE}fadian/fadian.json"

    async def fetch(self):
        try:
            req = await request.get(self.api, follow_redirects=True)
            assert req.status_code == 200
            self.data = req.json()
        except Exception as e:
            await log(f"Warning: plugin fadian failed to refresh data. {e}")


fa_dian = FaDian()


@Hook.on_startup()
async def init_data():
    await fa_dian.fetch()


@scheduler.scheduled_job("cron", hour="2", id="plugins.fa_dian.refresh")
async def fa_dian_refresher_data():
    await fa_dian.fetch()


@listener(command="fadian",
          description="快速对着指定人物发电",
          parameters="<query>")
async def fa_dian_process(message: Message):
    if fa_dian.data.get("date") == 0:
        await fa_dian.fetch()
    if not (query := message.arguments):
        if user := message.from_user:
            query = "死号" if user.is_deleted else user.first_name
        elif channel := message.sender_chat:
            query = channel.title
        else:
            return await message.edit("请指定发电对象")
    if not query:
        return await message.edit("请指定发电对象")
    if data := fa_dian.data.get("data"):
        return await message.edit(choice(data).format(name=query))
    else:
        return await message.edit("发电数据为空")
