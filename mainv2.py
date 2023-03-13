import tkinter as tk
from tkinter import filedialog
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 選擇按鈕
        self.select_button = tk.Button(self)
        self.select_button["text"] = "選擇檔案"
        self.select_button["command"] = self.select_file
        self.select_button.pack(side="top")

        # 左側輸入框
        self.input_label = tk.Label(self, text="輸入：")
        self.input_label.pack(side="left")

        self.input_text = tk.Text(self, height=20, width=50)
        self.input_text.pack(side="left")

        # 右側輸出框
        self.output_label = tk.Label(self, text="輸出：")
        self.output_label.pack(side="left")

        self.output_text = tk.Text(self, height=20, width=50)
        self.output_text.pack(side="left")

        # 執行按鈕
        self.run_button = tk.Button(self)
        self.run_button["text"] = "執行"
        self.run_button["command"] = self.run_file
        self.run_button.pack(side="bottom")

    def select_file(self):
        # 開啟文件選擇框
        filename = filedialog.askopenfilename()
        # 將選擇的文件名稱顯示在標籤中
        self.select_button["text"] = filename

    def run_file(self):
        # 從選擇的檔案中讀取UNIX執行檔
        filename = self.select_button["text"]
        if not filename:
            return
        # 從左側輸入框中讀取測試資料
        input_data = self.input_text.get("1.0", "end-1c")
        # 執行UNIX執行檔
        process = subprocess.Popen([filename], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # 將測試資料傳送到標準輸入
        output_data, _ = process.communicate(input=input_data.encode())
        # 將輸出顯示在右側輸出框中
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", output_data.decode())

root = tk.Tk()
app = Application(master=root)
app.mainloop()
