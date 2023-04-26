# Queue là một vùng chứa chứa dữ liệu. Dữ liệu được nhập trước sẽ bị xóa trước, và do đó một Queue còn được gọi 
# “Nhập trước xuất trước” (FIFO). Queue có hai đầu phía trước và phía sau. Các mục được nhập từ phía sau và loại bỏ 
# từ phía trước.
# put (item): Thao tác này sẽ đưa mặt hàng vào bên trong Queue.
# get (): Điều này sẽ trả lại cho bạn một mục từ Queue.
# void (): Nó sẽ trả về true nếu Queue trống và false nếu có các mục.
# qsize (): trả về kích thước của Queue.
# full (): trả về true nếu Queue đầy, ngược lại là false.

import queue

# Tạo một hàng đợi mới
q = queue.Queue()

# Thêm phần tử vào hàng đợi
q.put(7)
q.put(4)
q.put(5)

# Lấy phần tử ra khỏi hàng đợi
print(q.get())  
print(q.get())  
print(q.get())  

# empty() để kiểm tra xem hàng đợi có rỗng hay không:

if q.empty():
    print("Hàng đợi rỗng")
else:
    print("Hàng đợi không rỗng")
# lấy số lượng phần tử trong hàng đợi, chúng ta có thể sử dụng hàm qsize() như sau:

print(q.qsize())


# Danh sách liên kết