import webbrowser
import os

def open_html_file(html_file_path):
    if os.path.exists(html_file_path):
        # 获取文件的绝对路径
        absolute_path = os.path.abspath(html_file_path)
        # 使用默认浏览器打开 HTML 文件
        webbrowser.open(f'file://{absolute_path}')
    else:
        print(f"错误：文件 {html_file_path} 不存在。")

if __name__ == "__main__":
    # 指定要打开的 HTML 文件路径
    html_file = 'example.html'
    open_html_file(html_file)    