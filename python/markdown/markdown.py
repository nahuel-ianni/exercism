import re


_headerMdSymbol = '#'

def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False

    for i in lines:
        if i.startswith(_headerMdSymbol):
            i = _handleHeaders(i)

        m = re.match(r'\* (.*)', i)
        if m:
            i = f'<li>{m.group(1)}</li>'

            if not in_list:
                i = f'<ul>{i}'
                in_list = True

        else:
            if in_list:
                in_list_append = True
                in_list = False

        i = _handleParagraphs(i)

        i = _handleTextLabeling(i, '__', 'strong')
        i = _handleTextLabeling(i, '_', 'em')

        if in_list_append:
            i = '</ul>' + i
            in_list_append = False

        res += i

    if in_list:
        res += '</ul>'

    return res


def _handleHeaders(markdown):
    exp_format = ' (.*)'

    for x in range(1, 7):
        regex = exp_format.rjust(x + len(exp_format), _headerMdSymbol)

        if re.match(regex, markdown):
            markdown = f'<h{x}>{markdown[x + 1:]}</h{x}>'
            break

    return markdown


def _handleParagraphs(markdown):
    return markdown if re.match('<h|<ul|<p|<li', markdown) else f'<p>{markdown}</p>'


def _handleTextLabeling(markdown, mdLabel, htmlLabel):
    m = re.match(f'(.*){mdLabel}(.*){mdLabel}(.*)', markdown)
    return f'{m.group(1)}<{htmlLabel}>{m.group(2)}</{htmlLabel}>{m.group(3)}' if m else markdown
