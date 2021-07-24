from commands.posts.post import Post
from commands.posts.show import show
from helpers.rich import printr
from datetime import datetime

exit_commands = ["quit", "exit", "q", "done", "hi", "x", "bye"]

def all():
    posts = Post.all()
    last_key = 0
    max_id = len(posts)
    while last_key < max_id:
        post = posts[last_key]
        date = datetime.strptime(post["created_at"], "%Y-%m-%d %H:%M:%S").strftime("%d. %m. %Y") 
        printr(
f"""{post["id"]} ->
<blue>{post["title"]}<end>
{date}
""")
       
        while True:
            command = input("")
            if command in exit_commands:
                return

            if command == "show":
                show(post["id"])
                continue

            last_key += 1
            break

