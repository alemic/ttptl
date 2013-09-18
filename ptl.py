URL = 'http://open.t.qq.com/api/statuses/public_timeline?format=%(format)s&pos=%(pos)d&reqnum=%(reqnum)d'
PARAM = {'format' : 'xml', 'pos' : 0, 'reqnum' : 50}

def doc_from_url(url, encoding='utf8'):
    import lxml.html as x
    import urllib2
    raw = urllib2.urlopen(url).read()
    if encoding:
        raw = raw.decode(encoding)
    return x.document_fromstring(raw)
    #return x.parse(url)

def follow():
    seen = []
    while True:
        doc = doc_from_url(URL % PARAM)
        ts = doc.xpath('//root/data/info')
        for t in ts:
            try:
                t_id = eval(t.xpath('id')[0].text)
                t_nick = t.xpath('nick')[0].text
                t_text = t.xpath('origtext')[0].text
            except IndexError:
                continue
            if t_id not in seen:
                seen.append(t_id)
                if len(seen) > 1000:
                    del seen[0]
                print '[[%s]]' % t_nick
                print t_text

if __name__ == '__main__':
    follow()
