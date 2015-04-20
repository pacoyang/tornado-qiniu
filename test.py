#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
测试tornaqiniu

@file:test.py
@modul:test
@author:xiaolin@idealsee.cn
@date:2015-04-20
"""
import os
import tornado.ioloop
import tornado.gen

from tornalet import asyncify
from tornado.httpclient import AsyncHTTPClient

import tornaqiniu

from tornaqiniu import BucketManager

access_key = os.getenv('QINIU_ACCESS_KEY',"A7vB3qbo79ZmA7dWNJTbMjjt1UVtjjTYbQ8jeyee")
secret_key = os.getenv('QINIU_SECRET_KEY',"_4JSKT44vZYyM1RS9KXobTZWpNqLy1sOKPb2wus_")
bucket_name = os.getenv('QINIU_TEST_BUCKET',"simlens")

@tornado.gen.engine
def test_qiniu(callback=None):
    q = tornaqiniu.Auth(access_key,secret_key)
    bucket = BucketManager(q)
    ret,eof,info = yield tornado.gen.Task(bucket.list,bucket_name,limit=4)
    assert len(ret.get('items'))
    callback()

def qiniu_callback(a=None):
    tornado.ioloop.IOLoop.instance().stop()
    exit(0)
@tornado.gen.engine
def test_asyncify(callback=None):
    http_client = AsyncHTTPClient()
    # This where the magic happens, tornalet.asyncify wraps the parent
    # call in a greenlet that can be swapped out the same as any
    # aync tornado IO handler call.
    resp = asyncify(http_client.fetch)(request="http://localhost/",callback=callback)
def main():
    test_qiniu(qiniu_callback)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()