import sys

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return f"文件 {file_path} 不存在。"
    except Exception as e:
        return f"发生错误：{e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        file_content = read_file(file_path)
        print(f"文件内容：\n{file_content}")
    else:
        print("请提供文件路径作为命令行参数。")