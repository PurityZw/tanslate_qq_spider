# tanslate_qq_spider
基于Python2.7 爬取某翻译接口demo.

***
### 2018.4.14 接口测试ok
form_data中的session_uuid需要通过时间戳生成 str(int(time.time) * 1000)

root_url, 需要向该url发送post请求
http://fanyi.qq.com/api/translate

```
headers = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Connection": "keep-alive",
	"Content-Length": post数据的长度,
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie": "pgv_pvi=5313092608; pt2gguin=o0460683120; RK=BVRg0BF1eb; ptcz=9a13a6a951bfa53755d83914e9f320ea227c7dfe168d414e5f8d3c4b7420f2d3; fy_guid=4e181ea5-ccc0-486c-b045-c5b51f06c90f; pgv_info=ssid=s8530225160; ts_last=fanyi.qq.com/; pgv_pvid=9519925092; ts_uid=4263153620; qtv=b589f59552eb15c8; qtk=sTm6qSNbUEey7eXuh2fJn2BnFl6ZaVAh2K+dlZwS0Z3/sPFcTWAKFqbABbJ5+tlHNtYjY9+IrQHrn3j2ljo6VWnQ7VYvss0qXNFbioCpXh83hzh+fNIDO/OfEAoG5V3fViHy1imqTvue/Qen/BOrLg==; openCount=3",
	"Host": "fanyi.qq.com",
	"Origin": "http://fanyi.qq.com",
	"Referer": "http://fanyi.qq.com/",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
}

form_data = {
    "source": "auto",
    "target": "en",
    "sourceText": 查找的内容,
    "sessionUuid": "translate_uuid1523623924692",
}
```
