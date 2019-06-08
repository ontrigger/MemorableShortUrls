import functools
import operator
import hashlib

from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse

from .words import a, a_1, n


# for some reason .title() de-capitalized some words
def capword(w):
    return w[0].upper() + w[1:]


def urldigest(url):
    return hashlib.sha1(url.encode('utf-8')).hexdigest()


def gen_shortlink(url):
    h = urldigest(url)

    hex_bytes = list(map(lambda x: int(x, 32),
                         map(''.join, zip(h[::2], h[1::2]))))

    length = len(hex_bytes)

    seg_size = length // 3

    segments = [hex_bytes[i * seg_size:(i + 1) * seg_size]
                for i in range(3)]

    segments[-1].extend(hex_bytes[3 * seg_size:])

    def checksum(w_bytes): return functools.reduce(operator.xor, w_bytes, 0)

    b1, b2, b3 = tuple(map(checksum, segments))

    return ''.join(capword(w) for w in [a[b1], a_1[b2], n[b3]])


def gen_absolute_link(request: WSGIRequest, slug):
    return request.build_absolute_uri(
        reverse('shortlink', args=(slug,))
    )
