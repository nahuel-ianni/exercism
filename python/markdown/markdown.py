import re


_headerMdSymbol = '#'

def parse(markdown):
    res = ''
    in_list = False
    in_list_append = False

    for line in markdown.split('\n'):
        if line.startswith(_headerMdSymbol):
            line = _handleHeaders(line)

        m = re.match(r'\* (.*)', line)
        if m:
            line = f'<li>{m.group(1)}</li>'

            if not in_list:
                line = f'<ul>{line}'
                in_list = True

        else:
            if in_list:
                in_list_append = True
                in_list = False

        line = _handleParagraphs(line)

        line = _handleTextLabeling(line, '__', 'strong')
        line = _handleTextLabeling(line, '_', 'em')

        if in_list_append:
            line = '</ul>' + line
            in_list_append = False

        res += line

    if in_list:
        res += '</ul>'

    return res


def _handleHeaders(markdown):
    expression = ' (.*)'

    for x in range(1, 7):
        regex = expression.rjust(x + len(expression), _headerMdSymbol)

        if re.match(regex, markdown):
            markdown = f'<h{x}>{markdown[x + 1:]}</h{x}>'
            break

    return markdown


def _handleParagraphs(markdown):
    return markdown if re.match('<h|<ul|<p|<li', markdown) else f'<p>{markdown}</p>'


def _handleTextLabeling(markdown, mdLabel, htmlLabel):
    m = re.match(f'(.*){mdLabel}(.*){mdLabel}(.*)', markdown)
    return f'{m.group(1)}<{htmlLabel}>{m.group(2)}</{htmlLabel}>{m.group(3)}' if m else markdown
