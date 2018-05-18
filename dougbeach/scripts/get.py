#
# Download all pages from Dr. Doug Beach's Health and Wellness Guide
#

import urllib2

def go():
	page = 0
	max = 185

	for i in xrange(186):
		file('Page' + str(i) + '.html', 'w').write(urllib2.urlopen("http://members.shaw.ca/stevejobber/doug/Page" + str(i) + ".html").read())
		print str(i) + ": DONE"

	print "-----"
	print "All Finished"

go()