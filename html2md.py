import os
import html2text
from pathlib import Path

def convert_html_to_md(html_path, output_dir):
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 使用 html2text 转换为 Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False  # 保留链接
    markdown_content = h.handle(html_content)

    # 生成输出文件路径
    output_file = output_dir / (html_path.stem + ".md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"✅ 转换完成: {html_path} -> {output_file}")

def batch_convert_all_html(root_path):
    root_path = Path(root_path).resolve()
    output_dir = root_path / "python_output"
    output_dir.mkdir(exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(root_path):
        for file in filenames:
            if file.lower().endswith((".html", ".htm")):
                html_file_path = Path(dirpath) / file
                convert_html_to_md(html_file_path, output_dir)

if __name__ == "__main__":
    current_directory = Path(__file__).parent
    batch_convert_all_html(current_directory)
