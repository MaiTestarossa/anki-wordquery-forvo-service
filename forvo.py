# -*- coding:utf-8 -*-#

import urllib2


from aqt.utils import showInfo, showText
from .base import WebService, export, with_styles, register

import json


@register(u'forvo')
class forvo(WebService):
    def __init__(self):
        super(forvo, self).__init__()

    @export(u'mp3', 0)
    def fld_mp3(self):
	
	
		# add your forvo api here,more visit https://api.forvo.com/
        self.API = ''
		# custuom language
		self.language = 'ja'
		
        self.action = 'word-pronunciations'
        url = 'https://apifree.forvo.com/key/' + self.API + '/format/json/action/' + self.action + '/word/' + self.word + '/language/' + self.language
        try:
            request = urllib2.urlopen(url)                                     # get the url, open the url
            get_json_file = json.load(request)
            items_ = get_json_file["items"]
            # 如果里面有多条发音，排序json，排序优先高分，高点击
            # if items has more than 1 ,sort json,high rate first, hits secound
            proc_count = len(items_)
            if proc_count > 1:
                # for i in range(proc_count):
                items_ = sorted(items_,key=lambda k: (-int(k['rate']), -int(k["hits"])))

            # lady first
            # 女性优先（这样做似乎分数就没意义了，万一唯一一个女的声音效果很差）
            # sorted_items = sorted(items_, key=lambda k: (-int(k['rate']), -int(k["hits"]), k["sex"]), reverse=True)

            #
            result_ogg_link = items_[0]['pathogg']             # get the result, load as JSON
            filename = u'_forvo_{}.ogg'.format(self.word)

            #here ignore system proxy
            # (in my windows system if env add http_proxy and https_proxy,urllib2 can't open through https links,i dont know why)
            proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy_handler)
            response = opener.open(result_ogg_link)
            with open(filename, 'wb') as f:
                f.write(response.read())
                f.close()
            return self.get_anki_label(filename, 'audio')
        except:                                                                # url error
            print "Check url path"
            return url