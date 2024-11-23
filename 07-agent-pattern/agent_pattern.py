"""
代理模式

分类:
   远程代理
   虚代理
   保护代理

"""
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def get_content(self, user=None):
        pass

    @abstractmethod
    def set_content(self, content, user=None):
        pass


class RealSubject(Subject):
    def __init__(self, file_name):
        self.file_name = file_name
        print("正在读取文件内容...")
        with open(self.file_name, mode='r', encoding="utf-8") as file:
            self.content = file.read()
            print("已经读取到内容了")

    def get_content(self, user=None):
        return self.content

    def set_content(self, content, user=None):
        self.content = content
        with open(self.file_name, mode="w", encoding="utf-8") as file:
            file.write(content)


class VirtualProxy(Subject):
    def __init__(self, file_name):
        self.file_name = file_name
        self.subject = None

    def get_content(self, user=None):
        if not self.subject:
            self.subject = RealSubject(self.file_name)
        return self.subject.get_content()

    def set_content(self, content, user=None):
        if not self.subject:
            self.subject = RealSubject(self.file_name)
        self.subject.set_content(content)


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProtectedProxy(Subject):
    def __init__(self, file_name):
        self.identify_user = {}
        self.subject = VirtualProxy(file_name)

    def get_content(self, user=None):
        if user and user.id in self.identify_user:
            return self.subject.get_content()
        else:
            print("身份验证失败！！无法读取该文件！！")

    def set_content(self, content, user=None):
        if user and user.id in self.identify_user:
            self.subject.set_content(content)
        else:
            print("数据保存失败， 请进行身份验证后重试！")

    def login(self, user: User):
        self.identify_user[user.id] = user


if __name__ == '__main__':
    # r = RealSubject('test.txt')

    # subject = VirtualProxy('test.txt')
    # print(subject.get_content())

    p = ProtectedProxy("test.txt")
    print(p.get_content())

    u = User("uid1", "wang_shao")
    p.login(u)
    print(p.get_content(u))
