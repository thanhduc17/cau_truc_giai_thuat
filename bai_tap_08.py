# https://blog.luyencode.net/ngan-xep-stack/
# https://vi.wikipedia.org/wiki/Ng%C4%83n_x%E1%BA%BFp
# code tham khảo từ chat gpt và https://www.geeksforgeeks.org/stack-in-python/
#   ngăn xếp (còn gọi là bộ xếp chồng, tiếng Anh: Stack) là một cấu trúc dữ liệu trừu tượng hoạt động theo nguyên lý “vào sau ra trước” (Last In First Out (LIFO). Tức là, phần tử cuối cùng được chèn vào ngăn xếp sẽ là phần tử đầu tiên được lấy ra khỏi ngăn xếp.
#các thuật ngữ 
#•	Push: Thêm một phần tử vào đỉnh của ngăn xếp, số phần tử của ngăn xếp tăng lên 1.
#•	Pop: Xóa bỏ phần tử đầu tiên ở đỉnh của ngăn xếp, số phần tử của ngăn xếp giảm đi 1.
#•	Top: Lấy giá trị của phần tử đầu tiên ở đỉnh của ngăn xếp, số phần tử của ngăn xếp không thay đổi.
#•	IsEmpty: Kiểm tra ngăn xếp trống hay không. Ngăn xếp trống là ngăn xếp không có phần tử nào.
#•	IsFull: Kiểm tra ngăn xếp đã đầy hay chưa. Thao tác này không phải lúc nào cũng có.
#•	Size: Lấy số lượng phần tử stack đang có.



class Stack:
    def __init__(self):     # đây là cách thức khởi tạo của lớp Stack để tạo ra một đối tượng mới trong lớp đó
        self.items = []     # sử dụng một danh sách (items) để lưu trữ các phần tử trong ngăn xếp
                                # danh sách ban đầu là trống 

# Push: Thêm một phần tử vào đỉnh của ngăn xếp, số phần tử của ngăn xếp tăng lên 1.
    def push(self, item):
        self.items.append(item) # sử dụng hàm append() của danh sách items để thêm phần tử mới vào ngăn xếp 

#Pop: Xóa bỏ phần tử đầu tiên ở đỉnh của ngăn xếp, số phần tử của ngăn xếp giảm đi 1.        
    def pop(self):
        return self.items.pop()  # sử dụng hàm pop() của danh sách items để xóa bỏ phần tử đầu tiên của ngăn xếp
 
  
#IsEmpty: Kiểm tra ngăn xếp trống hay không. Ngăn xếp trống là ngăn xếp không có phần tử nào.      
    def is_empty(self):
        return not bool(self.items) # sử dụng câu lệnh bool để kiểm tra danh sách items có rỗng hay không 
                                        # nếu rỗng sẽ trả về TRUE
                                        # nếu lẽ sẽ trả về FALSE


#Top hoặc peek: Lấy giá trị của phần tử đầu tiên ở đỉnh của ngăn xếp, số phần tử của ngăn xếp không thay đổi.
    def peek(self): #  phần tử ở đầu ngăn xếp (phần tử cuối cùng của danh sách)
        return self.items[-1]  #ta truy cập vào phần tử cuối cùng của danh sách items bằng cách sử dụng chỉ số -1
    
#IsFull: Kiểm tra ngăn xếp đã đầy hay chưa. Thao tác này không phải lúc nào cũng có.

#Size: Lấy số lượng phần tử stack đang có trong ngăn xếp
    def size(self):
        return len(self.items) # sử dụng hàm len() để đếm số lượng phần tử trong danh sách items
    
class Node:  # Lớp Node đại diện cho một node trong danh sách liên kết hay được sử dụng để tạo nút (node) mới
    def __init__(self, data):
        self.data = data   # đối tượng data dùng để chứa dữ liệu (data)
        self.next = None    # đối tượng next (hây con trỏ) để di chuyển từ từ node này sang node mới của ngăn xếp hiện tại 

class Stack:   # khởi tạo ngăn xếp
    def __init__(self):
        self.head = None        # đối tượng  head là None và size là 0.
        self.size = 0
    #push(data) sẽ thêm một node mới vào đầu stack 
    def push(self, data):
            new_node = Node(data)   # tạo một nút mới với dữ liệu là data
            new_node.next = self.head   # con trỏ của nút mới này trỏ đến head của ngăn xếp hiện tại
            self.head = new_node  # gán node mới này vào head của stack
            self.size += 1      # tăng kích thước size của stack lên 1
    # pop() sẽ lấy ra và trả về giá trị của node đầu tiên trong stack, sau đó xóa node này khỏi stack
    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data
    #  is_empty() sẽ trả về True nếu stack rỗng và False nếu stack không rỗng.
    def is_empty(self):
            return self.size == 0  
        
    # peek() sẽ trả về giá trị của node đầu tiên trong stack mà không xóa node đó khỏi stack
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
    # size() sẽ trả về số lượng các node trong stack
    def size(self):
        return self.size
   






