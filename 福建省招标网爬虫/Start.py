#  coding=utf-8
from Reptile import zbw_xinxi
import os
import sys

url_new = []


def fuzhou_url(a):
    for i in range(1, a):
        url = 'http://zfcg.fuzhou.gov.cn/350100/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&fromtime=2015-01-01&endtime=2020-12-31&notice_type=b716da75fe8d4e4387f5a8c72ac2a937'
        url_new.append(url)
    return


def putian_url(a):
    for i in range(1, a):
        url = 'http://110.89.45.47/350300/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&fromtime=2015-01-01&endtime=2020-12-31'
        url_new.append(url)
    return


def quanzhou_url(a):
    for i in range(1, a):
        url = 'http://120.35.30.176/3500/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&fromtime=2015-01-01&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&endtime=2020-12-31'
        url_new.append(url)
    return


def xiamen_url(a):
    for i in range(1, a):
        url = 'http://120.41.36.6/350200/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(i) + '&endtime=2020-12-31&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&fromtime=2015-01-01'
        url_new.append(url)
    return


def zhangzhou_url(a):
    for i in range(1, a):
        url = 'http://140.237.73.6/350600/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&fromtime=2015-01-01&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&endtime=2020-12-31'
        url_new.append(url)
    return


def longyan_url(a):
    for i in range(1, a):
        url = 'http://zfcg.longyan.gov.cn/350800/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&fromtime=2015-01-01&endtime=2020-12-31&notice_type=b716da75fe8d4e4387f5a8c72ac2a937'
        url_new.append(url)
    return


def sanming_url(a):
    for i in range(1, a):
        url = 'http://zfcg.cz.sm.gov.cn/350400/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&fromtime=2015-01-01&endtime=2020-12-31&notice_type=b716da75fe8d4e4387f5a8c72ac2a937'
        url_new.append(url)
    return


def nanping_url(a):
    for i in range(1, a):
        url = 'http://27.155.99.31/350700/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&endtime=2015-12-31&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&fromtime=2020-01-01'
        url_new.append(url)
    return


def ningde_url(a):
    for i in range(1, a):
        url = 'http://218.5.222.40/350900/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page=' + str(
            i) + '&endtime=2020-12-31&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&fromtime=2015-01-01'
        url_new.append(url)
    return


def shengji_url(a):
    for i in range(1, a):
        url = 'http://120.35.30.176/3500/noticelist/e8d2cd51915e4c338dc1c6ee2f02b127/?page='+str(i)+'&fromtime=2015-01-01&notice_type=b716da75fe8d4e4387f5a8c72ac2a937&endtime=2020-12-31'
        url_new.append(url)
    return


def url_del(name):
    # print(url_li[0])
    del name[0]
    return


def title():
    print(' -------------------------------\n'
          '    福建省招标网中标信息爬虫系统\n'
          ' -------------------------------\n'
          '丨           1. 福州            丨\n'
          '丨           2. 莆田            丨\n'
          '丨           3. 泉州            丨\n'
          '丨           4. 厦门            丨\n'
          '丨           5. 漳州            丨\n'
          '丨           6. 龙岩            丨\n'
          '丨           7. 三明            丨\n'
          '丨           8. 南平            丨\n'
          '丨           9. 宁德            丨\n'
          '丨           0. 省级            丨\n'
          ' -------------------------------')


def diqu(diqu, yema):
    if diqu == 1:
        fuzhou_url(yema)
        text = 'http://zfcg.fuzhou.gov.cn'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 2:
        putian_url(yema)
        text = 'http://110.89.45.47'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 3:
        quanzhou_url(yema)
        text = 'http://61.131.58.48'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 4:
        xiamen_url(yema)
        text = 'http://120.41.36.6'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 5:
        zhangzhou_url(yema)
        text = 'http://140.237.73.6'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 6:
        longyan_url(yema)
        text = 'http://zfcg.longyan.gov.cn'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 7:
        sanming_url(yema)
        text = 'http://zfcg.cz.sm.gov.cn'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 8:
        nanping_url(yema)
        text = 'http://27.155.99.31'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 9:
        ningde_url(yema)
        text = 'http://218.5.222.40/'
        zbw_xinxi(text, url_new, yema)
    elif diqu == 0:
        shengji_url(yema)
        text = 'http://120.35.30.176'
        zbw_xinxi(text, url_new, yema)
    else:
        print('请输入正确的地区编号')


if __name__ == '__main__':
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')
    title()
    serial_number = int(input("请输入需要爬取的地区\n"))
    page_number = int(input("请输入最后一页页码\n"))
    diqu(serial_number, page_number)
