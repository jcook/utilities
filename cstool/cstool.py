#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, getopt
import requests

__VERSION__ = '0.0.1'

welcome = """
Checking Status from [http://202.109.79.211:8002/] (Shanghai) v%s

License: https://github.com/jcook/utilities/blob/master/LICENSE
""" % __VERSION__

def req_post(id=201625200000, step_forward=10):

	print 'Checking Status from [%d] to [%d]' % (id-step_forward, id)
	
	url = 'http://202.109.79.211:8002/TransFlowQueryResult.jsp'
	headers = {'Content-Type': 'application/x-www-form-urlencoded',
			   'Host': '202.109.79.211:8002',
			   'Connection': 'keep-alive',
			   'Content-Length': '58',
			   'Cache-Control': 'max-age=0',
			   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			   'Origin': 'http://202.109.79.211:8002',
			   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36',
			   'Referer': 'http://202.109.79.211:8002/',
			   'Accept-Encoding': 'gzip, deflate',
			   'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
			  }
 
	for i in range(id-step_forward, id+1):
		s = 'query=1&transactionid=%s' % str(i)
		s += '&button1=+%C8%B7+%B6%A8+'
		try:
			r = requests.post(url, data=s, headers=headers)
			ret = r.text
			idx1 = ret.find('<P>&nbsp;</P>') + len('<P>&nbsp;</P>')
			idx2 = ret.find('</BODY>')
			print ret[idx1:idx2-4]
		except:
			print 'Unexcepted error orrur. Checking network first.'
			sys.exit(1)

def Usage():
	print 'Usage:'
	print '	-h, --help: print help message'
	print '	-v, --version: Show version info'
	print '	-i, --id: Indicate id for checking'
	print '	-f, --forward: Indicate forward number for checking'
	print ''
	print 'Example:'
	print '	tool.exe -i 201625200020 -f 5'
	print 'Will check the result from 201625200015 to 201625200020.'
	
def Version():
    print welcome

def main(argv):
	id = 0
	forward = 10
	try:
		opts, args = getopt.getopt(argv[1:], 'hvi:f:', ['id=', 'forward='])
	except getopt.GetoptError, err:
		print str(err)
		Usage()
		sys.exit(2)
	for o, a in opts:
		if o in ('-h', '--help'):
			Usage()
			sys.exit(1)
		elif o in ('-v', '--version'):
			Version()
			sys.exit(1)
		elif o in ('-i', '--id'):
			id = int(a)
		elif o in ('-f', '--forward'):
			forward=int(a)
		else:
			print 'Invalid option(s)!'
			Usage()
			sys.exit(3)
	if id == 0:
		Usage()
		sys.exit(1)
	req_post(id, forward)	

if __name__ == '__main__':
	main(sys.argv)