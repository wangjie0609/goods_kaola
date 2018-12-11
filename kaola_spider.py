import requests
import re
import json
class GoodsKaola():

    def __init__(self):
        self.url1 = 'https://m-goods.kaola.com/product/2048875.html'
        self.url2 = 'https://m-goods.kaola.com/product/getWapGoodsDetailDynamic.json?goodsId=2048875'

        self.headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
    def crawl(self):

        item = {}

        response1 = requests.get(self.url1,headers = self.headers)

        item['title'] = re.findall(r'title:(.+?)\ngoodsImageList', response1.text)[0]

        carousel_map = re.findall(r'goodsImageList:(.+]\n})',response1.text)[0]
        item['carousel_map_list'] = re.findall('(http.+?)"',carousel_map)

        detail_img = re.findall(r'</ul><p>(<img src=.+?),',response1.text)[0]
        item['detail_img_list'] = re.findall(r'http.+?jpg',detail_img)

        # print(title)
        # print(carousel_map)
        # print(carousel_map_list)
        # print(detail_img)
        # print(detail_img_list)
        response2 = requests.get(self.url2,headers = self.headers)
        json_dict = json.loads(response2.text)

        item['price'] = json_dict['data']['skuPrice']['currentPrice']
        # print(price)
        print(item)

goods = GoodsKaola()
goods.crawl()



