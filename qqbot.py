import json
import requests
import re
from pprint import pprint
from cqhttp import CQHttp
# from selenium import webdriver#导入库
from weibo import top, toplist

# driver = webdriver.Chrome(executable_path = "C:\\Users\\laptop\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")
bot = CQHttp(api_root='http://127.0.0.1:5700')

BOT = "OwnThink"
dialogue = []
OWNTHINK = False

def enableOwnThink():
    global OWNTHINK
    OWNTHINK = True

@bot.on_message('private')
def handle_msg(context):
    pprint(context)
    msg_input = context['message']
    nickname = context['sender']['nickname']
    dialogue.append(nickname + ": " + msg_input)
    if OWNTHINK == False and msg_input == "我好无聊":
        enableOwnThink()
        bot.send(context, "啊哈，一起来尬聊吧!")
        dialogue.append("OwnThink: 啊哈，一起来尬聊吧!")
        msg_output = "你先说"
    # elif BOT == "Turing":
    #     # msg_output = answerMessage(msg_input)
    #     msg_output = "Turing is disabled"
    elif BOT == "OwnThink" and OWNTHINK == True:
        url_question = 'https://api.ownthink.com/bot?spoken=' + msg_input
        sess = requests.get(url_question)
        answer = sess.text
        msg_output = json.loads(answer)
        msg_output = msg_output['data']['info']['text']
        # log = msg_output
        # pprint(log)
        print(123)
    # elif msg_input == "你好":
    #     bot.send(context, "你好呀")
    elif msg_input == "微博热搜":
        bot.send(context, "好滴，我这就去看看沙雕在微博上热议什么！")
        # msg_output = genWeiboTopMsg()
    else:
        msg_output = "我在等待一个无聊的灵魂"
    dialogue.append("OwnThink: " + msg_output)
    bot.send(context, msg_output)
    pprint(dialogue)

def answerMessage(ask_message):
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    body = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": ""
            },
        },
        "userInfo": {
            "apiKey": "4d36f8eb68e54d5d9809a21c3beaa2f0",
            "userId": "552970"
        }
        
    }
    body['perception']['inputText']['text'] = ask_message
    data = json.dumps(body)
    
    response = requests.post(url, data = data)
    retext = response.text
    
    pprint(retext)
    
    answ_text = re.findall((re.compile('{.*?results":.*?values.*?text":"(.*?)"}', re.S)), retext)
    text = str(answ_text[0])
    try:
        answ_shows = re.findall((re.compile('{.*?showtext":"(.*?)",', re.S)), retext)
        return str(answ_shows[0])
    except IndexError:
        answ_names = re.findall((re.compile('{.*?name":"(.*?)",', re.S)), retext)
        answ_urls = re.findall((re.compile('{.*?detailurl":"(.*?)"}', re.S)), retext)
        try:
            for index in range(3):
                text = text+"\n原标题"+str(index+1)+":"+str(answ_names[index])+"\n链接地址："+str(answ_urls[index])
            return (text)
        except IndexError:
            return (str(answ_text[0]))

# def genWeiboTopMsg():
#     browser = webdriver.Chrome()#声明浏览器
#     url_WeiboTop = 'https://s.weibo.com/top/summary?Refer=top_hot'
#     browser.get(url_WeiboTop)
#     Tops = browser.find_elements_by_class_name('td-02')

#     toplist = []
#     for i in range(0, len(Tops)):
#         index_buf = i
#         text_buf = Tops[i].text
#         # # 暴力去数字
#         # for digit in range(10):
#         #     text_buf = text_buf.replace(str(digit),'')
#         url_buf = 'https://s.weibo.com/weibo?q=%23' + text_buf + '%23&Refer=top'
#         top_buf = top(index_buf, text_buf, url_buf)
#         toplist.append(top_buf)
#     browser.close()

#     msg_weibo = ""
#     for i in range(5):
#         index = toplist[i].index
#         text = toplist[i].text
#         url = toplist[i].url
#         msg_buf = str(index)
#         msg_buf += ', ' + text 
#         # msg_buf += ', ' + url 
#         msg_buf += '\n'
#         msg_weibo += msg_buf
#     print(msg_weibo)
#     return msg_weibo

bot.run('127.0.0.1', 8080)