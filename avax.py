
import urllib2

url='http://avxhome.se/pages/1/'
down=[]
for a in range(1,100):
	seed = urllib2.urlopen(url[:24]+str(a)+'/')
	avax = seed.read()
	for i in range(0,len(avax.split('Details</a>'))-1):
		print url[:17]+avax.split('Details</a>')[i].split('<a href=')[-1].split('>')[0].split('"')[1]
		con = urllib2.urlopen(url[:17]+avax.split('Details</a>')[i].split('<a href=')[-1].split('>')[0].split('"')[1])
		res=con.read()
		if 'nitroflare' in res:
			for j in range(1,len(res.split('nitroflare'))):
				print 'http://www.nitroflare.'+res.split('nitroflare')[j].split('target')[0].split('"')[0][1:].split('<')[0]
				if len(res.split('nitroflare')[j].split('target')[0].split('"')[0][1:].split('<')[0])>9: 
					down.append('http://www.nitroflare.'+res.split('nitroflare')[j].split('target')[0].split('"')[0][1:].split('<')[0]+'\n')
		else:
			print '---'
t =sorted(set(down))
file1 = open('workfile.txt', 'w')
for i in t:
	file1.write(i)
file1.close()
print t

