meaningless_words = [
    'in', 'on', 'at', 'from', 'to',
    'could', 'can', 'may',
    'please'
]

youtube_filter = ['play', 'youtube']

def filter_words(str):
    return ' '.join(filter(lambda x: x not in meaningless_words, str.lower().split(' ')))

def filter_youtube(str):
    str = filter_words(str)
    return ' '.join(filter(lambda x: x not in youtube_filter, str.split(' ')))
