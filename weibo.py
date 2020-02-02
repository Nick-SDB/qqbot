class top:
    index = 0
    text = ""
    url = ""
    msg = ""

    def __init__(self, index, text, url):
        self.index = index
        self.text = text
        self.url = url

class toplist(list):
    def __init__(self):
        self = list()
