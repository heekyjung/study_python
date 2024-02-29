import hashlib  # 문자열 해싱 모듈

members = []
posts = []
username_list = []


class Member():
    def __init__(self, name, username, password):
        # 비밀번호 해싱
        password = password.encode('utf-8')  # 인코딩
        password = hashlib.sha256(password).hexdigest()  # 해시함수 적용

        self.member = {
            'name': name,
            'username': username,
            'password': password
        }
        username_list.append(username)

    def display(self):
        print(
            f"[name] {self.member['name']}\n[username] {self.member['username']}\n")


class Post():
    def __init__(self, title, content, author, password):
        # 비밀번호 해싱
        password = hashlib.sha256(password.encode('utf-8'))

        self.post = {
            'title': title,
            'content': content,
            'author': author,
            'password': password
        }

    # 제목, 작성자, 내용 모두 출력
    def display(self):
        print(
            f"[title] {self.post['title']}\n[author] {self.post['author']}\n{self.post['content']}\n")

    # 제목만 출력
    def display_title(self):
        print(self.post['title'])


# 회원 인스턴스 만들기
members.append(Member("Jennie Kim", "jennie", "1234"))
members.append(Member("Jisoo Kim", 'soovely', "5678"))
members.append(Member("Roseanne Park", 'rosie', "thorn"))
members.append(Member("Lisa Manobal", 'lalisa', "money"))

# 게시물 인스턴스 만들기
posts.append(Post("휘파람", "이대로 지나치지 마요~", "rosie", "thorn"))
posts.append(Post("붐바야", "네가 말로만 듣던 걔가 나야 Jennie", "jennie", "1234"))
posts.append(Post("불장난", "멈출 수 없는 이 떨림은 On and on and on", "rosie", "thorn"))
posts.append(Post("마지막처럼", "Baby 날 터질 것처럼 안아줘", "jennie", "1234"))
posts.append(Post("뚜두뚜두", "아직은 잘 모르겠지 굳이 원하면 test me", "soovely", "5678"))
posts.append(
    Post("Kill This Love", "BLACKPINK IN YOUR AREA!", "lalisa", "money"))
posts.append(Post("How You Like That", "보란 듯이 무너졌어", "jennie", "1234"))
posts.append(Post("Lovesick Girls", "아마 다 잠깐일지도 몰라", "soovely", "5678"))
posts.append(Post("Pink Venom", "내 손끝 툭 하나에 다 무너지는 중", "lalisa", "money"))
posts.append(Post("Shut Down", "게임이 아냐 진 적이 없으니까", "lalisa", "money"))
posts.append(Post("Yeah Yeah Yeah", "말도 안 돼 난 너에게 끌려 버렸어", "soovely", "5678"))


def create_member():  # 회원 생성 함수
    while True:
        reply = input(
            "Please enter NAME / USERNAME / PASSWORD (seperated by /): ").lower().split("/")
        if len(reply) == 3:
            name, username, password = reply
            members.append(Member(name, username, password))
            for member in members:
                member.display()
            return


def create_post():  # 게시물 생성 함수
    while True:
        reply = input(
            "Please enter TITLE, CONTENT, AUTHOR, PASSWORD (seperated by /): ").split("/")
        if len(reply) == 4:
            title, content, author, password = reply
            for member in members:
                if (member.member['username'] == author) and (member.member['password'] == hashlib.sha256(password.encode('UTF-8')).hexdigest()):
                    new_post = Post(title, content, author, password)
                    posts.append(new_post)
                    for post in posts:
                        if post.post['author'] == new_post.post['author']:
                            post.display_title()
                    return
            print("Invalid username or password")


def search():  # 검색 함수
    while True:
        reply = input("Select search category (Author, Content): ").lower()
        if reply == "author":
            while True:
                author_reply = input("Please enter author: ")
                if author_reply in username_list:
                    for post in posts:
                        if post.post['author'] == author_reply:
                            post.display_title()
                    break
            print("--- End of result ---")
            break
        elif reply == "content":
            while True:
                content_reply = input("Please enter search word: ")
                for post in posts:
                    if content_reply in post.post['content']:
                        post.display_title()
                break
            print('--- End of result ---')
        break


def start():  # 프로그램 실행 함수
    while True:
        reply = input(
            "Choose one from below.\n1. Create Member\n2. Create Post\n3. Search\n4. Exit program\nYour answer: ")
        if reply == "1":
            create_member()
        elif reply == "2":
            create_post()
        elif reply == "3":
            search()
        elif reply == "4":
            print("Exit the program.")
            return
        else:
            print("Just enter a number.")


# 프로그램 실행!
start()
