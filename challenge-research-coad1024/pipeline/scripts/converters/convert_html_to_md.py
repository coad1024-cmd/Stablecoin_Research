
import os
import sys
from html.parser import HTMLParser

class MarkdownConverter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.markdown = ""
        self.tags = []
        self.href = ""

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.markdown += '#' * level + ' '
        elif tag == 'p':
            self.markdown += '\n'
        elif tag == 'ul' or tag == 'ol':
            self.markdown += '\n'
        elif tag == 'li':
            self.markdown += '- '
        elif tag == 'blockquote':
            self.markdown += '> '
        elif tag == 'pre':
            self.markdown += '\n```\n'
        elif tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.href = attr[1]
                    self.markdown += '['

    def handle_endtag(self, tag):
        if self.tags:
            self.tags.pop()
        
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.markdown += '\n\n'
        elif tag == 'p':
            self.markdown += '\n'
        elif tag == 'ul' or tag == 'ol':
            self.markdown += '\n'
        elif tag == 'pre':
            self.markdown += '```\n\n'
        elif tag == 'a':
            self.markdown += f']({self.href})'
            self.href = ""

    def handle_data(self, data):
        if not self.tags:
            return
            
        current_tag = self.tags[-1]
        text = data.strip()
        
        if not text and current_tag not in ['pre']:
            return
            
        if current_tag in ['p', 'b', 'strong', 'i', 'em', 'span', 'li', 'a']:
            # For inline elements, give exactly one space if preceding implies it
            # But simple appending is usually "good enough" for basic scraping
            self.markdown += data.replace('\n', ' ').strip() + ' '
        elif current_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
             self.markdown += text
        elif current_tag == 'pre':
             self.markdown += data
        elif current_tag == 'blockquote':
             self.markdown += text

def html_to_md(html_content):
    parser = MarkdownConverter()
    parser.feed(html_content)
    return parser.markdown

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_html_to_md.py <input_file> [output_file]")
        return

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"Error: File {input_path} not found.")
        return

    # Determine output path
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = os.path.splitext(input_path)[0] + ".md"

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        md_content = html_to_md(html_content)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        print(f"Successfully converted {input_path} to {output_path}")
        
    except Exception as e:
        print(f"Conversion failed: {e}")

if __name__ == "__main__":
    main()
