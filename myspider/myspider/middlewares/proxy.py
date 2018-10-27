# -*- coding: utf-8 -*-
from utils.utils import getProxy

class ProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta['proxy']=getProxy(protocol='https')
        print('-------------use proxy:'+str(request.meta['proxy']))
        return None
