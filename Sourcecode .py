import tkinter as tk
from tkinter import Entry, Button, filedialog
import os
import shutil

# Hàm để tạo thư mục mới
def create_directory():
    new_folder_name = folder_name_entry.get()
    if new_folder_name:
        try:
            os.mkdir(new_folder_name)
            result_label.config(text=f"Đã tạo thư mục '{new_folder_name}' thành công.")
        except FileExistsError:
            result_label.config(text=f"Thư mục '{new_folder_name}' đã tồn tại.")
    else:
        result_label.config(text="Vui lòng nhập tên thư mục.")

# Hàm để xoá thư mục
def delete_directory():
    folder_to_delete = folder_name_entry.get()
    if folder_to_delete:
        try:
            shutil.rmtree(folder_to_delete)
            result_label.config(text=f"Đã xoá thư mục '{folder_to_delete}' thành công.")
        except FileNotFoundError:
            result_label.config(text=f"Thư mục '{folder_to_delete}' không tồn tại.")
    else:
        result_label.config(text="Vui lòng nhập tên thư mục.")

# Hàm để đổi tên thư mục
def rename_directory():
    old_folder_name = folder_name_entry.get()
    new_folder_name = new_name_entry.get()
    if old_folder_name and new_folder_name:
        try:
            os.rename(old_folder_name, new_folder_name)
            result_label.config(text=f"Đã đổi tên thư mục thành công từ '{old_folder_name}' thành '{new_folder_name}'.")
        except FileNotFoundError:
            result_label.config(text=f"Thư mục '{old_folder_name}' không tồn tại.")
        except FileExistsError:
            result_label.config(text=f"Thư mục '{new_folder_name}' đã tồn tại.")
    else:
        result_label.config(text="Vui lòng nhập tên thư mục cũ và mới.")

# Hàm để di chuyển thư mục
def move_directory():
    folder_to_move = folder_name_entry.get()
    destination_folder = filedialog.askdirectory()
    if folder_to_move and destination_folder:
        try:
            shutil.move(folder_to_move, destination_folder)
            result_label.config(text=f"Đã di chuyển thư mục '{folder_to_move}' đến '{destination_folder}' thành công.")
        except FileNotFoundError:
            result_label.config(text=f"Thư mục '{folder_to_move}' không tồn tại.")
    else:
        result_label.config(text="Vui lòng nhập tên thư mục và chọn vị trí đích.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Quản Lý Thư Mục")
root.geometry("600x400")  # Đặt kích thước cửa sổ là 600x400 px

# Nhập tên thư mục
folder_name_label = tk.Label(root, text="Tên Thư Mục:")
folder_name_label.pack()

folder_name_entry = Entry(root)
folder_name_entry.pack()

# Nhập tên mới (đối với chức năng đổi tên thư mục)
new_name_label = tk.Label(root, text="Tên Mới:")
new_name_label.pack()

new_name_entry = Entry(root)
new_name_entry.pack()

# Tạo nút bấm "Tạo Thư Mục", "Xoá Thư Mục", "Đổi Tên Thư Mục", và "Di Chuyển Thư Mục"
create_button = Button(root, text="Tạo Thư Mục", command=create_directory, relief=tk.RAISED, borderwidth=3)
delete_button = Button(root, text="Xoá Thư Mục", command=delete_directory, relief=tk.RAISED, borderwidth=3)
rename_button = Button(root, text="Đổi Tên Thư Mục", command=rename_directory, relief=tk.RAISED, borderwidth=3)
move_button = Button(root, text="Di Chuyển Thư Mục", command=move_directory, relief=tk.RAISED, borderwidth=3)

create_button.pack(pady=10)
delete_button.pack()
rename_button.pack()
move_button.pack()

# Hiển thị kết quả
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack()

# Khởi động ứng dụng
root.mainloop()
