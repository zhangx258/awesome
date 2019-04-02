#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zhangx258'

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

async def index(request):
    return web.Response(body='<h1>AWesome</h1>'.encode('utf-8'),content_type='text/html')
async def hello(request):
    text = '<h1>hello,%s</h1>' % request.match_info['name']
    resp = web.Response(body=text.encode('utf-8'))
    #如果不添加content_type，某些严谨的浏览器会把网页当成文件下载，而不是直接显示
    resp.content_type = 'text/html;charset=utf-8'
    return resp
async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET','/hello/{name}',hello)
    server = await loop.create_server(app._make_handler(), host='127.0.0.1', port=9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return server
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()