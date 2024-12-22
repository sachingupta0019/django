from .models import BlogPost


def get_excerpt(description, word_count=30):
    words = description.split()
    return ' '.join(words[:word_count]) + '...' if len(words) > word_count else description
