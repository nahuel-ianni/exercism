import re


RULES = {
    'h1': r'^\s*# (.*)$',
    'h2': r'^\s*## (.*)$',
    'h3': r'^\s*### (.*)$',
    'h4': r'^\s*#### (.*)$',
    'h5': r'^\s*##### (.*)$',
    'h6': r'^\s*###### (.*)$',
    'li': r'^\* (.*)',
    'ul': r'(<li>.*?</li>)(?![\n]*<li>)',
    'p': r'^([^<\n].*)',
    'strong': r'__(.*)__',
    'em': r'_(.*)_'
}

SPECIAL_FLAGS = {
    'ul': re.DOTALL
}

def parse(markdown):
    for tag, pattern in RULES.items():
        markdown = re.sub(
            pattern, 
            tag_content(r'\1', tag),
            markdown, 
            flags=re.MULTILINE | SPECIAL_FLAGS.get(tag, 0))

    return markdown.replace('\n', '')


def tag_content(content, html_tag):
    return f'<{html_tag}>{content}</{html_tag}>'
