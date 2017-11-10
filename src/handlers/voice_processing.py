meaningless_words = [
    'in', 'on', 'at', 'from', 'to',
    'could', 'can', 'may',
    'please'
]

youtube_meaningless_words = ['play', 'search', 'youtube']
google_meaningless_words = ['search', 'google']

def filter_words(str):
    return ' '.join(filter(lambda x: x not in meaningless_words, str.lower().split(' ')))

def topic_filter(str, topic):
    return ' '.join(filter(lambda x: x not in meaningless_words and x not in topic, str.split(' ')))

def filter_youtube(str):
    return topic_filter(str, youtube_meaningless_words)

def filter_google(str):
    return topic_filter(str, google_meaningless_words)
