#!/usr/bin/python
# -*- coding: utf-8 -*-

from tornado import gen
from tornado.httpclient import AsyncHTTPClient

@gen.coroutine
def fetch(url='', api_key=''):
    http_client = AsyncHTTPClient()
    headers = {'X-Graphiti-Rest-Api-Key': api_key}

    response = yield http_client.fetch(url, headers=headers)
    raise gen.Return(response)

