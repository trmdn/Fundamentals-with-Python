class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes


comments = Comment("user1", "I like this book")
print(comments.username)
print(comments.content)
print(comments.likes)