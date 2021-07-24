from commands.posts.post import Post
from helpers.rich import printr
from exceptions import NotFoundError, InternalError
from datetime import datetime

def show(id:int):
    try:
        post = Post.find(id)
        line = "="*len(post.title)    
        date = datetime.strptime(post.created_at, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d. %m. %Y")
        printr(
    f"""
    <blue>{post.title}<end>
    By <blue>{post.author}<end>
    {line}
    {post.content}

    {date}
    """)
    except NotFoundError.NotFoundError:
        printr("<red>Not found!<end>")
    except InternalError.InternalError:
        printr("Klasicky webdev... <red>Internal Server Error!<end>")


