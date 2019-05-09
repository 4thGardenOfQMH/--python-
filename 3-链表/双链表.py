#__Author__: 42902
#__Date__: 2019/5/9
class LNode(object):

    def __init__(self,elem=None,next=None):
        self.elem=elem
        self.next=next
'''
基本的链表操作
    创建空列表
    初始化（参数为列表）
    删除链表
    判断表是否为空
    获取表的长度
加入结点操作
    表首端插入
    表后端插入
    一般情况的元素插入（指定位置插入）
删除元素
    删除表首元素
    删除表尾元素
    一般情况的元素删除（指定位置删除）
扫描、定位和遍历
    按下标定位
    按元素定位
求表的长度
'''
class LinkedList(object):

    # 创建空列表
    def __init__(self, maxsize=None):
        self.maxsize=maxsize
        self._head=None
    def __str__(self):
        p=self._head
        result=''
        while p!=None:
            result+=str(p.elem)+' '
            p=p.next
        return result

    #初始化
    def initList(self,list):
        for elem in list:
            self.append(elem)

    #删除链表
    def delete(self):
        self._head=None

    # 判断表是否为空
    def is_empty(self):
        return self._head == None

    #获取表的长度
    def getLength(self):
        p=self._head
        n=0
        while p!=None:
            n+=1
            p=p.next
        return n

    #表首端插入
    def prepend(self,elem):
        node=LNode(elem)
        if self._head==None:
            self._head=node
            return
        node.next=self._head
        self._head=node


    #表后端插入
    def append(self,elem):
        node=LNode(elem)
        if self._head==None:
            self._head=node
        else:
            p=self._head
            while p.next !=None:
                p=p.next
            p.next=node

    #表中任意位置的插入 index从1开始
    def insert(self,index,elem):
        len=self.getLength()
        if len==0 or index<-1 or index>len:
            raise linkedListUnderFlow('in insert')
        node=LNode(elem)
        if index==1:
            self.prepend(elem)
            return
        i=1
        p=self._head
        while i != index-1:
            p=p.next
            i+=1
        node.next=p.next
        p.next=node


    #删除表首元素
    def pop(self):
        if self.is_empty():
            raise linkedListUnderFlow('in pop')
        e=self._head.elem
        self._head=self._head.next
        return e


    #删除表尾元素
    def pop_last(self):
        if self._head==None:
            raise linkedListUnderFlow('in pop_last')
        p=self._head
        if p.next==None:
            e=p.elem
            self._head=None
            return e
        while p.next.next!=None:
            p=p.next
        e=p.next.elem
        p.next=None
        return e

    # 删除表中任意位置的元素 index从1开始
    def remove(self,index):
        len=self.getLength()
        if len==0 or index<-1 or index>len:
            raise linkedListUnderFlow('in remove')
        if index==1:
            return self.pop()
        i=1
        p=self._head
        while i != index-1:
            p=p.next
            i+=1
        e=p.next.elem
        p.next=p.next.next
        return e

    #按下标定位
    def find(self,index):
        len=self.getLength()
        if len==0 or index<-1 or index>len:
            raise linkedListUnderFlow('in find')
        i=1
        p=self._head
        while i!=index:
            p=p.next
            i+=1
        return p.elem

    #按元素定位
    def index(self,elem):
        if self.getLength()==0:
            raise linkedListUnderFlow('in index')
        p=self._head
        e=p.elem
        i=1
        while e!= elem:
            p=p.next
            e=p.elem
            i+=1
        return i

    #将方法作用在表中的每一个元素上


#定义异常类
class linkedListUnderFlow(ValueError):
    pass

if __name__=='__main__':
    l=LinkedList()
    # 初始化
    print('========测试initList方法======')
    l.initList([1,2,3,4,5,6,7,8,9])
    print(l)
    print('========测试is_empty方法======')
    print(l.is_empty())
    print('========测试getLength方法======')
    print(l.getLength())
    # 表首端插入
    print('========测试prepend方法======')
    l.prepend(100)
    print(l)
    # 表后端插入
    print('========测试append方法======')
    l.append('1000')
    print(l)
    # 表中任意位置的插入 index从1开始
    print('========测试insert方法======')
    l.insert(1,0)
    print(l)
    l.insert(11,11)
    print(l)
    l.insert(5,90)
    print(l)

    # # 删除表首元素
    print('========测试pop方法======')
    print(l.pop())
    print(l)

    # # 删除表尾元素
    print('========测试pop_last方法======')
    print(l.pop_last())
    print(l)

    # # 删除表中任意位置的元素 index从1开始
    print('========测试remove方法======')
    print(l.remove(1))
    print(l)
    print(l.remove(11))
    print(l)
    print(l.remove(3))
    print(l)

    # # 按下标定位
    print('========测试find方法======')
    print(l.find(1))
    print(l.find(3))
    print(l.find(9))

    # 按元素定位
    print('========测试index方法======')
    print(l.index(1))
    print(l.index(8))
    print(l.index(11))

    # # 删除链表
    print('========测试delete方法======')
    l.delete()
    if  l.is_empty():
        print('链表为空')
