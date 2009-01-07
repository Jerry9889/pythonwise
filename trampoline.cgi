#!/usr/bin/env python
'''A CGI "trampoline" to enable cross site AJAX (when JSONP is not possible)'''

__author__ = "Miki Tebeka &lt;miki.tebeka@gmail.com&gt;"

from os import environ
from sys import argv

def get_query():
    if len(argv) &gt; 1:
        return argv[1]

    return env.get("QUERY_STRING", "")


def main():
    from urllib import urlopen

    query = get_query()
    if query:
        query = "?" + query
    # Example search in citeseer
    url = "http://citeseer.ist.psu.edu/cis%s" % query

    o = urlopen(url)

    print "Content-type: %(content-type)s\n" % o.headers
    print o.read()

if __name__ == "__main__":
    main()