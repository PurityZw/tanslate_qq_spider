# -*- coding:utf-8 -*-
from utlis.utlis import SpiderVarible
import json
import urllib
import urllib2
import time


def translate_spider(search_str):
    proxy_addr = SpiderVarible().get_random_proxy_addr()
    user_agent = SpiderVarible().get_random_user_agent()

    # 请求头
    time_str = str(int(time.time() * 1000))
    print time_str

    # form表单数据
    form_data = {
        "source": "auto",
        "target": "en",  # 此参数用于修改翻译方式, en表示英语
        "sourceText": search_str,
        "sessionUuid": "translate_uuid%s" % time_str,
    }

    # 将form数据进行url编码
    form_str = urllib.urlencode(form_data)

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(form_str),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "pgv_pvi=5313092608; pt2gguin=o0460683120; RK=BVRg0BF1eb; ptcz=9a13a6a951bfa53755d83914e9f320ea227c7dfe168d414e5f8d3c4b7420f2d3; fy_guid=4e181ea5-ccc0-486c-b045-c5b51f06c90f; pgv_info=ssid=s8530225160; ts_last=fanyi.qq.com/; pgv_pvid=9519925092; ts_uid=4263153620; qtv=b589f59552eb15c8; qtk=sTm6qSNbUEey7eXuh2fJn2BnFl6ZaVAh2K+dlZwS0Z3/sPFcTWAKFqbABbJ5+tlHNtYjY9+IrQHrn3j2ljo6VWnQ7VYvss0qXNFbioCpXh83hzh+fNIDO/OfEAoG5V3fViHy1imqTvue/Qen/BOrLg==; openCount=3",
        "Host": "fanyi.qq.com",
        "Origin": "http://fanyi.qq.com",
        "Referer": "http://fanyi.qq.com/",
        "User-Agent": user_agent,
        "X-Requested-With": "XMLHttpRequest",
    }

    # 使用代理
    proxy_handler = urllib2.ProxyHandler({'http': proxy_addr})
    # post请求
    request = urllib2.Request('http://fanyi.qq.com/api/translate', form_str, headers=headers)
    opener = urllib2.build_opener(proxy_handler)
    response = opener.open(request)
    # 返回结果为str, 需要转为json数据
    r = response.read()
    result = json.loads(r)
    # # 在pycharm中python2解释器默认为ASCII, 需要转码
    print '查询结果:%s' % (result['translate']['records'][0]['targetText']).encode()


if __name__ == '__main__':
    search_str = raw_input('查询内容:')
    translate_spider(search_str)
