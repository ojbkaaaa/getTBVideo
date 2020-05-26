# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：main
   Description :
   Author : zhang
   date：2020/5/14
-------------------------------------------------
   Change Activity: 2020/5/14:
-------------------------------------------------
"""
import asyncio
import time
import time, os, signal, psutil
from pyppeteer.launcher import launch

async def slideMain(url):
    try:
        # url = 'https://market.m.taobao.com/app/tb-source-app/video-fullpage/pages/index?ut_sk=1.XKBH3PVxDsQDACpYS6LvyMSY_21380790_1590391224810.Copy.tblive-video&id=266189251406&wx_navbar_hidden=true&spm=a2141.7631549&coverImage=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi3%2F2201521814157%2FO1CN019O1oIE1gZx31mdWfS_%21%212201521814157-0-beehive-scenes.jpg&wh_weex=true&videoUrl=https%3A%2F%2Fcloud.video.taobao.com%2Fplay%2Fu%2F2201521814157%2Fp%2F1%2Fe%2F6%2Ft%2F1%2F266189251406.mp4&business_spm=a1z2l.12141986&sourceType=other&suid=5867D428-EE2D-4055-9F7C-1E671143CD34&source=WEITAO&type=WEITAO&contentId=266189251406&accountId=2201521814157&origin=VideoInteract%7Ca310p.13800399.0.0%7C%7B%22contentId%22%3A%22266189251406%22%7D&un=b570a64d6552cdf845426828bb998f85&share_crt_v=1&sp_tk=77+lUEtzUDFKSjJHR2Tvv6U=&cpp=1&shareurl=true&short_name=h.VlpvzkQ&sm=196de2&app=chrome'
        browser = await launch({'headless': True, 'args': ['--no-sandbox'], 'userDataDir': 'userData', 'dumpio': True})
        page = await browser.newPage()
        await page.setUserAgent(
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

        await page.goto(url)

        # time.sleep(2)
        await page.evaluate("document.getElementsByClassName('play-btn-wrap')[0].getElementsByTagName('img')")
        time.sleep(1)
        await page.evaluate(
                '''document.getElementsByClassName('play-btn-wrap')[0].getElementsByTagName('img')[0].click()''')
        time.sleep(2)
        src = await page.Jeval('.dwplayerVideo', "node => node.src")

        print(src)
        try:
            pid = browser.process.pid
            pgid = os.getpgid(pid)
            print('pid:', pid, pgid)
            # 强制结束
            os.kill(pid, signal.SIGKILL)
            print("结束进程：%d" % pid)
            print("父进程是：%d" % pgid)
            print("等待结果：%d" % browser.process.wait())
        except BaseException as err:
            print("close: {0}".format(err))
        return src

    except Exception as e:
        print('代码异常：', e)
        return {'code': 4, 'msg': '代码异常'}



if __name__ == '__main__':
    url = 'https://m.tb.cn/h.VOOBQTq?sm=5a667f'
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(slideMain(url))
    print(res)
