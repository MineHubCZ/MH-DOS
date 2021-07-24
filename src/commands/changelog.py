import requests
from helpers.rich import printr
from datetime import datetime

def changelog(arguments):
    data = requests.get("https://minehub.cz/api/changelog").json()
    
    for update in data:
        date = datetime.strptime(update["created_at"], "%Y-%m-%d %H:%M:%S").strftime("%d. %m. %Y") 
        printr(
f"""<blue>{update["server"]}<end>->
{update["text"]}
{date}
""")
