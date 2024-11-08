import re
from typing import Union

import httpx
from nonebot import logger

from ...utils_.travel_cycle import NormalTravel
from ...utils_ import time_no_more, parse_img_url


class Travelling:
    """国服复刻类"""

    def __init__(self):
        self.url = 'https://weibo.com/ajax/statuses/mymblog?uid=5539106873&feature=0'
        self.longtext = 'https://weibo.com/ajax/statuses/longtext?id='
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                          '/62.0.3202.9 Safari/537.36',
            'cookie': 'SUB=_2AkMUd3SHf8NxqwFRmP8Ty2Pna4VwywzEieKiK4VcJRMxHRl'
                      '-yT9jqnAOtRB6P_daaLXfdvYkPfvZhXy3bTeuLdBjWXF9;'  # 未登录时的cookie直接写死 目前
        }
        self.copyright_ = ('------------'
                           '\r【数据来源：微博@陈陈爱吃小兔包】\n'
                           '--本插件仅做数据展示之用，著作权归原文作者所有。'
                           '转载或转发请附文章作者微博--')

    async def get_mblog(self, max_page) -> Union[str, dict, None]:
        """获取微博 @光遇陈陈和包包 复刻先祖详情"""

        for page in range(1, max_page + 1):
            param = {
                'page': str(page)
            }
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    url=self.url,
                    headers=self.headers,
                    params=param
                )
                overhead = response.json().get('data')
                if overhead:
                    overhead = overhead.get('list')
                    for log in overhead:
                        if (
                                log.get('pic_infos') and
                                re.findall(
                                    r'#(光遇复刻)*([\u4e00-\u9fa5])*(先祖复刻)*([\u4e00-\u9fa5])*#',
                                    log['text_raw']
                                ) and time_no_more(log.get('created_at'), 12, 30)
                                # 为了包包我已经放弃了优雅。
                        ):
                            return log
                else:
                    return 'invalid'
        return None

    async def get_data(self) -> Union[str, None]:
        """获取复刻数据"""
        travel = NormalTravel()
        status = travel.national()
        results = ''
        overhead = await self.get_mblog(2)
        if overhead == 'invalid':
            return '超过未登录能获取页数的最大值：2'
        if overhead:
            pic_infos = overhead.get('pic_infos')
            if pic_infos:
                for pic in pic_infos:
                    large_url = pic_infos[pic]['largest']['url']
                    release_time = status.get('current_release').replace(' 12:00:00', '')
                    path = await parse_img_url(large_url, release_time)
                    results = path
            else:
                results = None
        else:
            notice = '没有找到国服复刻先祖的数据'
            logger.warning(notice)
            results = None
        return results
