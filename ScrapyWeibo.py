from selenium import webdriver#导入库
from weibo import top, toplist

driver = webdriver.Chrome(executable_path = "C:\\Users\\laptop\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\selenium\\webdriver\\chrome\\chromedriver.exe")

def genWeiboTopMsg():
    browser = webdriver.Chrome()#声明浏览器
    url_WeiboTop = 'https://s.weibo.com/top/summary?Refer=top_hot'
    browser.get(url_WeiboTop)
    Tops = browser.find_elements_by_class_name('td-02')

    toplist = toplist()
    for i in range(0, len(Tops)):
        index_buf = i
        text_buf = Tops[i].text
        # # 暴力去数字
        # for digit in range(10):
        #     text_buf = text_buf.replace(str(digit),'')
        url_buf = 'https://s.weibo.com/weibo?q=%23' + text_buf + '%23&Refer=top'
        top_buf = top(index_buf, text_buf, url_buf)
        toplist.append(top_buf)
    
    msg = ""
    for i in range(len(toplist)):
        index = toplist[i].index
        text = toplist[i].text
        url = toplist[i].url
        msg_buf = str(index)
        msg_buf += ', ' + text 
        # msg_buf += ', ' + url 
        msg_buf += '\n'
        msg += msg_buf
    return msg

    print(msg_weibo)

# browser.close()

# browser = webdriver.Chrome()#声明浏览器
# url_WeiboTop = 'https://s.weibo.com/top/summary?Refer=top_hot'
# browser.get(url_WeiboTop)
# Tops = browser.find_elements_by_class_name('td-02')

# toplist = toplist()
# for i in range(0, len(Tops)):
#     index_buf = i
#     text_buf = Tops[i].text
#     # # 暴力去数字
#     # for digit in range(10):
#     #     text_buf = text_buf.replace(str(digit),'')
#     url_buf = 'https://s.weibo.com/weibo?q=%23' + text_buf + '%23&Refer=top'
#     top_buf = top(index_buf, text_buf, url_buf)
#     toplist.append(top_buf)


# msg_weibo = genWeiboTopMsg(toplist)

# print(msg_weibo)

# browser.close()