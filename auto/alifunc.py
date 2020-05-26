# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：alifunc
   Description :
   Author : zhang
   date：2020/5/14
-------------------------------------------------
   Change Activity: 2020/5/14:
-------------------------------------------------
"""
from retrying import retry
import time, asyncio, random


def retry_if_result_none(result):
    return result is None


@retry(retry_on_result=retry_if_result_none, )
async def mouse_slide(page=None, num=5):
    await asyncio.sleep(1)
    if num < 0:
        return -1
    try:

        await page.hover('#nc_1_n1z')
        await page.mouse.down()

        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        await page.mouse.up()
    except Exception as e:
        print(e, '     :slide login False')
        await page.evaluate('''document.getElementsByClassName("fm-submit")[0].click()''')
        num -= 1
        return await mouse_slide(page=page, num=num)
    else:
        await asyncio.sleep(2)
        slider_again = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
        print('验证情况', slider_again)
        if slider_again != '验证通过':
            await page.evaluate('''document.getElementsByClassName("fm-submit")[0].click()''')
            num -= 1
            return await mouse_slide(page=page, num=num)
        else:
            #await page.screenshot({'path': './headless-slide-result.png'})
            print('验证通过')
            await page.evaluate('''document.getElementsByClassName("fm-submit")[0].click()''')
            time.sleep(2)
            # await asyncio.gather(
            #     page.waitForNavigation(),
            #     page.evaluate('''document.getElementsByClassName("fm-submit")[0].click()'''),
            #
            # )
            return 1


def input_time_random():
    return random.randint(100, 151)