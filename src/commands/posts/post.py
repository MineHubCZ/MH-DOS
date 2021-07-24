import requests
from exceptions import InternalError, NotFoundError
# I officially hate python oop.

class Post:
    
    """
    A class for representing Post

    Attributes
    ==========
    id: int
        Id of Post to get

    Methods
    =======
    static all():
        returns basic data about all posts
    
    static find():
        returns data about Post

    """ 
    @staticmethod
    def all():
        """
        Returns basic data about all posts

        Returns
        =======
        list
        """ 
        res = requests.get("https://minehub.cz/api/posts/")
        return res.json()
    
    @staticmethod
    def find(id: int):
        """
        Returns data about specific post

        Attributes
        ==========
        id: int
            Id of post to get

        Returns
        =======
        Post
        """ 
        return Post(id)

    id = 0
    title = ""
    slug = ""
    author = ""
    content = ""
    created_at = ""

    def __init__(self, id:int):
        res = requests.get(f"https://minehub.cz/api/posts/{id}")
        if res.status_code == 404:
            raise (NotFoundError.NotFoundError(id))

        if res.status_code == 500:
            raise (InternalError.NotFoundError)

        data = res.json()
        
        self.id = data["id"]
        self.title = data["title"]
        self.slug = data["slug"]
        self.author = data["author"]
        self.content = data["content"]
        self.created_at = data["created_at"]
       

