#  coding=utf-8
import requests
from lxml import etree
import pandas
from rich.progress import track


headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'WEB=63297385',
        # 'Host': 'zfcg.cz.sm.gov.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def get_html(url):  # 请求头，获取页面源码
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding
        if response.status_code == 200:
            # print('成功获取源代码')
            pass
    except Exception as e:
        print('获取源代码失败:%s' % e)
    return response.text


def parse_next_url(html):  # 拿到下个界面链接地址
    global href1
    html1 = etree.HTML(html)
    tables = html1.xpath("//div[@class='wrapTable']//table")
    for i in tables:
        href1 = i.xpath(".//tr[@class='gradeX']//a/@href")
    return href1


def parse_region(html):  # 拿到区域文本，并遍历
    # global href1
    html1 = etree.HTML(html)
    tables = html1.xpath("//div[@class='wrapTable']//table")
    for i in tables:
        href1 = i.xpath(".//tr[@class='gradeX']/td[1]/text()")
    return href1


def parse_time(html):  # 拿到时间文本，并遍历
    global href1
    html1 = etree.HTML(html)
    tables = html1.xpath("//div[@class='wrapTable']//table")
    for i in tables:
        href1 = i.xpath(".//tr[@class='gradeX']/td[5]/text()")
    return href1


def ergodic_next_url(url, href, a):  # 组合成下个页面链接
    global next_url
    next_url = url + href[a]
    return next_url


def ergodic_region(href, a):  # 遍历区域
    global next_url1
    next_url1 = href[a]
    return next_url1


def ergodic_time(href, a):  # 遍历时间
    global next_url1
    next_url1 = href[a]
    return next_url1


def parse_next_text(html1):  # 拿到下个界面信息
    html = etree.HTML(html1)
    tables = html.xpath(".//div[@class='customize_purchaseResult']//font/text()")
    try:
        zbr = html.xpath(".//span[@class='customize_cgr']/text()")[0]  # 招标人
        zbrdz = html.xpath(".//span[@class='customize_cgrdz']/text()")[0]  # 招标人地址
        zbmc = html.xpath(".//span[@class='customize__projectName']/text()")[0]  # 招标项目名称
        zbgs = tables[0]  # 中标公司名称
        zbgsdz = tables[1]  # 中标公司地址
        zbje = tables[2]  # 中标金额
    except IndexError:
        try:
            zbr = html.xpath(".//td[@colspan='1']/p/span/text()")[2]  # 招标人
            zbrdz = html.xpath(".//td[@colspan='1']/p/span/text()")[3]  # 招标人地址
            zbmc = html.xpath(".//td[@colspan='1']/p/span/text()")[0]  # 招标项目名称
            zbgs = html.xpath(".//td[@colspan='6']/font/text()")[0]  # 中标公司名称
            zbgsdz = html.xpath(".//td[@colspan='6']/font/text()")[1]  # 中标公司地址
            zbje = html.xpath(".//td[@colspan='6']/font/text()")[2]  # 中标金额
        except IndexError:
            try:
                zbr = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[3]/td[2]/p/span/text()")[0]  # 招标人
                zbrdz = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/td[2]/p/span/text()")[0]  # 招标人地址
                zbmc = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/p/span/text()")[0]  # 招标项目名称
                zbgs = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[15]/td/table/tbody/tr[4]/td[2]/font/text()")[0]  # 中标公司名称
                zbgsdz = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[15]/td/table/tbody/tr[5]/td[2]/font/text()")[0]  # 中标公司地址
                zbje = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/table/tbody/tr[15]/td/table/tbody/tr[6]/td[2]/font/text()")[0]  # 中标金额
            except IndexError:
                try:
                    zbr = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/span[2]/span[10]/text()")[2]  # 招标人
                    zbrdz = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/span[2]/span[11]/text()")[3]  # 招标人地址
                    zbmc = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/span[1]/span[3]/span/span/text()")[0]  # 招标项目名称
                    zbgs = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/span[2]/table/tbody/tr[2]/td[1]/font/text()")[0]  # 中标公司名称
                    zbgsdz = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/span[2]/table/tbody/tr[2]/td[2]/font/text()")[1]  # 中标公司地址
                    zbje = html.xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[2]/span[2]/table/tbody/tr[2]/td[3]/font/text()")[2]  # 中标金额
                except IndexError:
                    zbr = ''
                    zbrdz = ''
                    zbmc = ''
                    zbgs = ''
                    zbgsdz = ''
                    zbje = ''

    zbw = {'招标人': zbr, '招标人地址': zbrdz, '招标项目名称': zbmc, '中标供应商': zbgs, '中标供应商地址': zbgsdz, '中标金额': zbje.replace('元', '')}

    return zbw


def county(html):
    html1 = etree.HTML(html)
    tables = html1.xpath(".//div[@class='location']/button/text()")
    return tables


def zbw_xinxi(text, url, yema):
    zbwxx = []
    url_lis = url
    try:
        for i in track(range(yema)):
            url2 = url_lis[i]
            html = get_html(url2)
            href1 = parse_next_url(html)
            qy_1 = parse_region(html)
            time_1 = parse_time(html)
            for b in range(10):
                qy_2 = ergodic_region(qy_1, b)
                qy_3 = {'区域': qy_2}
                time_2 = ergodic_time(time_1, b)
                time_3 = {'招标日期': time_2}
                next_url = ergodic_next_url(text, href1, b)
                html = get_html(next_url)
                zbw = parse_next_text(html)
                url_1 = {'页面地址': next_url}
                qy_3.update(time_3)
                qy_3.update(zbw)
                qy_3.update(url_1)
                zbwxx.append(qy_3)
                print('成功爬取第 ' + str(i + 1) + ' 页，第 ' + str(b + 1) + ' 个  ' + zbw['招标项目名称'])
                zbwdata = pandas.DataFrame(zbwxx)
                zbwdata.to_csv('/Users/Tanmy/Documents/Python/Zhaobiao_Reptile/xlsx/'+str(county(html)[0])+'中标信息.csv')
    except KeyboardInterrupt:
        print("用户手动停止")
