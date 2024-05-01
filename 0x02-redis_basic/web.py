#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker"""

from functools import wraps
import redis
import requests
from typing import Callable

redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decortator for counting """
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        redis_.incr(f"count:{url}")
        cache_html = redis_.get(f"cached:{url}")
        if cache_html:
            return cache_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Rerieve the HTML content from URL """
    result = requests.get(url)
    return result.text
