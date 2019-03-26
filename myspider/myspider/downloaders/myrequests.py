#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

'''
用于替代scrapy原生下载器（过于简陋），在尽量不渲染css/js，不访问附带文件的情况下，高度模拟真实访问，反反爬。
'''


def my_requests_request(method, url, **kwargs):
    """
    :param method: method for the new :class:`Request` object.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary or bytes to be sent in the query string for the :class:`Request`.
    :param data: (optional) Dictionary, bytes, or file-like object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
    :param cookies: (optional) Dict or CookieJar object to send with the :class:`Request`.
    :param files: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
        ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
        or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
        defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
        to add for the file.
    :param auth: (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
    :param timeout: (optional) How long to wait for the server to send data
        before giving up, as a float, or a :ref:`(connect timeout, read
        timeout) <timeouts>` tuple.
    :type timeout: float or tuple
    :param allow_redirects: (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection.
    :type allow_redirects: bool
    :param proxies: (optional) Dictionary mapping protocol to the URL of the proxy.
    :param verify: (optional) whether the SSL cert will be verified. A CA_BUNDLE path can also be provided. Defaults to ``True``.
    :param stream: (optional) if ``False``, the response content will be immediately downloaded.
    :param cert: (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    return requests.request(method=method, url=url, timeout=10, **kwargs)


class MyRequestsSession(requests.Session):
    """
    #: A case-insensitive dictionary of headers to be sent on each
    #: :class:`Request <Request>` sent from this
    #: :class:`Session <Session>`.
    self.headers = default_headers()

    #: Default Authentication tuple or object to attach to
    #: :class:`Request <Request>`.
    self.auth = None

    #: Dictionary mapping protocol or protocol and host to the URL of the proxy
    #: (e.g. {'http': 'foo.bar:3128', 'http://host.name': 'foo.bar:4012'}) to
    #: be used on each :class:`Request <Request>`.
    self.proxies = {}

    #: Event-handling hooks.
    self.hooks = default_hooks()

    #: Dictionary of querystring data to attach to each
    #: :class:`Request <Request>`. The dictionary values may be lists for
    #: representing multivalued query parameters.
    self.params = {}

    #: Stream response content default.
    self.stream = False

    #: SSL Verification default.
    self.verify = True

    #: SSL client certificate default.
    self.cert = None

    #: Maximum number of redirects allowed. If the request exceeds this
    #: limit, a :class:`TooManyRedirects` exception is raised.
    #: This defaults to requests.models.DEFAULT_REDIRECT_LIMIT, which is
    #: 30.
    self.max_redirects = DEFAULT_REDIRECT_LIMIT

    #: Trust environment settings for proxy configuration, default
    #: authentication and similar.
    self.trust_env = True

    #: A CookieJar containing all currently outstanding cookies set on this
    #: session. By default it is a
    #: :class:`RequestsCookieJar <requests.cookies.RequestsCookieJar>`, but
    #: may be any other ``cookielib.CookieJar`` compatible object.
    self.cookies = cookiejar_from_dict({})

    # Default connection adapters.
    self.adapters = OrderedDict()
    self.mount('https://', HTTPAdapter())
    self.mount('http://', HTTPAdapter())

    # Only store 1000 redirects to prevent using infinite memory
    self.redirect_cache = RecentlyUsedContainer(REDIRECT_CACHE_SIZE)
    """
    def __init__(self):
        super(MyRequestsSession, self).__init__()
