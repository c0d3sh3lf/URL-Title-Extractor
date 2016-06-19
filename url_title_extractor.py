#!/usr/bin/python

###
#   Author: Sumit Shrivastava (@invad3rsam)
#   Version: v1.0.0
#   Description: This script is used to extract the title from the provided URL
###

import httplib, re

title_re = re.compile(r".*?<title>(.*?)</title>.*?")
http_re = re.compile(r"^http")
url_protocol_format = re.compile(r".*?://.*?")


def http_connection(url, parameters):
    conn = httplib.HTTPConnection(url)
    conn.request("GET", parameters)
    response = conn.getresponse()
    if response.status == 200:
        html_data = response.read()
        title = title_re.search(html_data).group(1)
    else:
        title = str(response.status) + " " + str(response.reason)
    return title


def https_connection(url, parameters):
    conn = httplib.HTTPSConnection(url)
    conn.request("GET", parameters)
    response = conn.getresponse()
    if response.status == 200:
        html_data = response.read()
        title = title_re.search(html_data).group(1)
    else:
        title = str(response.status) + " " + str(response.reason)
    return title


def main():
    url = raw_input("Enter the URL: ")
    url_split = url.split("/")
    parameters = ""
    if url_protocol_format.match(url):
        if http_re.match(url):
            if url_split[0] == "http:":
                url = url_split[2]
                for i in range(3, len(url_split)):
                    parameters += "/" + url_split[i]
                parameters = parameters.strip()
                print http_connection(url, parameters)
            else:
                url = url_split[2]
                for i in range(3, len(url_split)):
                    parameters += "/" + url_split[i]
                parameters = parameters.strip()
                print https_connection(url, parameters)
        else:
            print "Only HTTP / HTTPS URLs supported"
    else:
        url = url_split[0]
        for i in range(1, len(url_split)):
            parameters += "/" + url_split[i]
        parameters = parameters.strip()
        print http_connection(url, parameters)


if __name__ == "__main__":
    main()