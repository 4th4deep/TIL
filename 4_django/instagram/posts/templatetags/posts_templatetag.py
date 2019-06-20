from django import template

register = template.Library()

@register.filter
def hashtag_link(post):
    #   #멀캠
    #   <a>#멀캠</a>


    #   #멀캠 #4차 하이 #역삼
    content = post.content
    #   [H obj (1), H obj (3), H obj (6)]
    hashtags = post.hashtags.all()

    for hashtag in hashtags:
        content = content.replace(
            f'{hashtag.content}',
            f'<a href="/posts/hashtags/{hashtag.id}/">{hashtag.content}</a>'
        )

    return content
