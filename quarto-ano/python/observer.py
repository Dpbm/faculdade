from abc import ABC, abstractmethod
from time import ctime

class Post:
    def __init__(self,body):
        self.body = body
        self.time = ctime()
    
    def __str__(self):
        return f"""
                    Data: {self.time}

                    {self.body}
                """

class Observer(ABC):
    @abstractmethod
    def update(self, post):
        pass
    
    @abstractmethod
    def follow(self, user):
        pass

class Subject(ABC):
    @abstractmethod
    def add_follower(self,follower):
        pass

    @abstractmethod
    def remove_follower(self,follower):
        pass

    @abstractmethod
    def notify(self,post):
        pass

class User(Subject):
    def __init__(self):
        self.followers = []

    def add_follower(self, follower):
        self.followers.append(follower)

    def remove_follower(self, follower):
        self.followers.remove(follower)

    def notify(self, post):
        print("Adicionado novo post\n")
        for follower in self.followers:
            follower.update(post)

class Follower(Observer):
    def __init__(self, name):
        self.name = name
        self.following = []

    def update(self, post):
        print(f"{self.name} recebeu o novo post")
        print(f"{post}\n")

    def follow(self, user):
        user.add_follower(self)
        self.following.append(user)

    def unfollow(self, user):
        user.remove_follower(self)
        self.following.remove(user)

if __name__ == "__main__":

    print("--------PRIMEIRA VERSAO----------")
    user = User()

    follower1 = Follower("Jorge")
    follower2 = Follower("Robert")
    follower3 = Follower("Claudiney")

    user.add_follower(follower1)
    user.add_follower(follower2)
    user.add_follower(follower3)

    # testando a funcao de remover um follower
    user.remove_follower(follower2)

    user.notify("Post sobre flyweight")


    print("--------DESAFIO EXTRA----------")
    user1 = User()
    user2 = User()
    user3 = User()

    follower1 = Follower("Jorge")
    follower2 = Follower("Robert")
    follower3 = Follower("Claudiney")

    follower1.follow(user1)
    follower1.follow(user2)
    follower1.follow(user3)
    
    follower2.follow(user1)
    follower2.follow(user2)
    follower2.follow(user3)
    
    follower3.follow(user1)
    follower3.follow(user2)
    follower3.follow(user3)

    # testando a funcao de unfollow
    follower1.unfollow(user1)
    follower2.unfollow(user2)
    follower3.unfollow(user3)
    
    user1.notify(Post("novo post user 1"))
    user2.notify(Post("novo post user 2"))
    user3.notify(Post("novo post user 3"))

