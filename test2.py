import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading

class ImageUploaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图片提交任务 UI")
        self.root.geometry("500x400")

        self.images1 = []
        self.images2 = []

        # 设置自定义tkinter主题
        ctk.set_appearance_mode("System")  # 可以选择 "Light" 或 "Dark"
        ctk.set_default_color_theme("blue")  # 设置主题色

        # 第一组图片选择
        self.label1 = ctk.CTkLabel(root, text="图片输入框 1:")
        self.label1.pack(pady=10)
        self.select_button1 = ctk.CTkButton(root, text="选择图片组1", command=self.select_images1)
        self.select_button1.pack(pady=5)
        self.files_label1 = ctk.CTkLabel(root, text="", wraplength=400, fg="gray")
        self.files_label1.pack()

        # 第二组图片选择
        self.label2 = ctk.CTkLabel(root, text="图片输入框 2:")
        self.label2.pack(pady=10)
        self.select_button2 = ctk.CTkButton(root, text="选择图片组2", command=self.select_images2)
        self.select_button2.pack(pady=5)
        self.files_label2 = ctk.CTkLabel(root, text="", wraplength=400, fg="gray")
        self.files_label2.pack()

        # 提交按钮
        self.submit_button = ctk.CTkButton(root, text="提交任务", command=self.submit_task)
        self.submit_button.pack(pady=20)

    def select_images1(self):
        files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
        self.images1 = files
        self.files_label1.config(text="\n".join(files))

    def select_images2(self):
        files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
        self.images2 = files
        self.files_label2.config(text="\n".join(files))

    def submit_task(self):
        if not self.images1 or not self.images2:
            messagebox.showwarning("提示", "请先选择两组图片！")
            return
        self.submit_button.config(state=ctk.DISABLED)
        threading.Thread(target=self.background_task).start()

    def background_task(self):
        print("开始处理图片组1:", self.images1)
        print("开始处理图片组2:", self.images2)
        # 模拟耗时任务
        import time
        time.sleep(3)
        print("处理完成")
        messagebox.showinfo("完成", "后台任务已完成！")
        self.submit_button.config(state=ctk.NORMAL)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ImageUploaderApp(root)
    root.mainloop()