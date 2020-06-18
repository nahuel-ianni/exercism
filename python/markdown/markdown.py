import re


_headerSymbol = '#'

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for i in lines:
        if i.startswith(_headerSymbol):
            i = _handleHeaders(i)

        m = re.match(r'\* (.*)', i)
        if m:
            i = f'<li>{TEMPMETHOD(m.group(1))}</li>'

            if not in_list:
                i = f'<ul>{i}'
                in_list = True

        else:
            if in_list:
                in_list_append = True
                in_list = False

        i = _handleParagraphs(i)

        i = TEMPMETHOD(i)

        if in_list_append:
            i = '</ul>' + i
            in_list_append = False

        res += i

    if in_list:
        res += '</ul>'

    return res

def TEMPMETHOD(markdown):
    curr = markdown

    m1 = re.match('(.*)__(.*)__(.*)', curr)
    if m1:
        curr = m1.group(1) + '<strong>' + m1.group(2) + '</strong>' + m1.group(3)

    m1 = re.match('(.*)_(.*)_(.*)', curr)
    if m1:
        curr = m1.group(1) + '<em>' + m1.group(2) + '</em>' + m1.group(3)
    
    return curr



def _handleHeaders(markdown):
    exp_format = ' (.*)'

    for x in range(1, 7):
        regex = exp_format.rjust(x + len(exp_format), _headerSymbol)

        if re.match(regex, markdown):
            markdown = f'<h{x}>{markdown[x + 1:]}</h{x}>'
            break

    return markdown


def _handleParagraphs(markdown):
    return markdown if re.match('<h|<ul|<p|<li', markdown) else f'<p>{markdown}</p>'
