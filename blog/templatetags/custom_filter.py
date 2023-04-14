from django import template

register = template.Library()


@register.simple_tag
def calculate_percentage(post):
    total_votes = post.number_of_likes() + post.number_of_dislikes()
    if total_votes > 0:
        percentage = (post.number_of_likes() / total_votes) * 100
        return "{:.0f}%".format(percentage)
    else:
        return "0%"
