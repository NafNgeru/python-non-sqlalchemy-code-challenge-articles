class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []
        print(f"New Author created: {self._name}")

    @property # Getter for name using in-built property decorator
    def name(self):
        return self._name
    def articles(self): # Getter for articles using in-built property decorator
        return self._articles

    def magazines(self): # Getter for magazines using in-built property decorator
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title): # To add article to author's list of articles
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self): # Return list of an author's categories
        categories = list(set(mag.category for mag in self.magazines()))
        return categories if categories else None
        

class Magazine:
    magazines = [] #Initializing magazine list for storing all magazine objects
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a non-empty string")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = [] # initializing articles list for storing those published by magazine

        Magazine.magazines.append(self) # adding new magazine to magazine list
        print(f"New Magazine created: {self._name} in category: {self._category}")
    
    @property
    def name(self):
        return self._name
    
    @name.setter # Setter for name using in-built property decorator
    def name(self, newname):
        if isinstance(newname, str) and (2 <= len(newname) <= 16):
            print(f"Changing magazine name from {self._name} to {newname}")
            self._name = newname
        else:
            raise ValueError("Magazine name must be a non-empty string between 2 and 16 characters")

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, newcategory):
        if isinstance(newcategory, str) and len(newcategory) > 0:
            print(f"Changing magazine category from {self._category} to {newcategory}")
            self._category = newcategory
        else:
            raise ValueError("Magazine category must be a non-empty string")

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        titles = [article.title for article in self._articles]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.magazine == self:
                author_counts[article.author] = author_counts.get(article.author, 0) + 1
        frequent_authors = [author for author, count in author_counts.items() if count >= 2]
        return frequent_authors if frequent_authors else None
    
    @classmethod # Class method to return the magazine with the most articles
    def top_contributor(cls):
        if not Article.articles:
            return None
        magazine_counts = {}
        for article in Article.articles:
            magazine_counts[article.magazine] = magazine_counts.get(article.magazine, 0) + 1
        
        return max(magazine_counts, key=magazine_counts.get)

class Article:
    all = [] # Initializing article list for storing all articles
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine class")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters long")
        
        self._author = author
        self._magazine = magazine
        self._title = title

        author.articles().append(self)
        magazine.articles().append(self) # adding new article to both author and magazine's list of articles
        
        print(f"New Article created: {self.title} by {self.author.name} in {self.magazine.name}")
        
        Article.all.append(self) # adding new article to article list
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @author.setter # Setter for author using in-built property decorator
    def author(self, newauthor):
        if isinstance(newauthor, Author):
            print(f"Changing author from {self._author.name} to {newauthor.name}")
            self._author = newauthor
            # self._author.articles().append(self)
        else:
            raise ValueError("Author must be an instance of Author class")
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter    # Setter for magazine using in-built property decorator
    def magazine(self, newmagazine):
        if isinstance(newmagazine, Magazine):
            print(f"Changing magazine from {self._magazine.name} to {newmagazine.name}")
            self._magazine = newmagazine
            # self._magazine.articles().append(self)
        else:
            raise ValueError("Magazine must be an instance of Magazine class")
    