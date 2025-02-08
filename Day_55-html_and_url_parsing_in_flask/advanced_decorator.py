class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticated(func):
    def wrapper(*args, **kwargs):
        if (args[0].is_logged_in == True):
            func(args[0])
    return wrapper

@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s blog post")


if __name__=='__main__':
    user = User('Bola')

    create_blog_post(user)
