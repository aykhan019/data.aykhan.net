import os
import time

# HTML template for the index.html file, with a signature comment
INDEX_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon"
        href="https://res.cloudinary.com/dbriqxpaa/image/upload/v1680096853/Logo/logo-xl-ico_qzbf7d.ico" />
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            font-weight: 400;
            transition: background-color 0.3s, color 0.3s;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 8px 13px;  /* Increased padding by 10% */
            border: 1px solid #ccc;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        td.icon-col {{
            width: 44px;  /* Increased width by 10% */
            text-align: center;
        }}
        a {{
            text-decoration: none;
            color: #007BFF;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        .go-back {{
            margin-bottom: 22px;  /* Increased margin-bottom by 10% */
            margin-left: 11px;  /* Increased margin-left by 10% */
            display: inline-block;
        }}
        h1 {{
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            font-size: 1.65em;  /* Increased font-size by 10% */
            margin: 0;
            padding: 11px;  /* Increased padding by 10% */
        }}
        /* Dark mode styles */
        body.dark-mode {{
            background-color: #333;
            color: #f1f1f1;
        }}
        body.dark-mode th {{
            background-color: #555;
        }}
        body.dark-mode a {{
            color: #1e90ff;
        }}
        /* Dark mode button styles */
        .dark-mode-toggle {{
            position: fixed;
            bottom: 22px;  /* Increased bottom by 10% */
            right: 22px;  /* Increased right by 10% */
            background-color: #007BFF;
            color: #fff;
            border: none;
            padding: 11px 22px;  /* Increased padding by 10% */
            cursor: pointer;
            border-radius: 5.5px;  /* Increased border-radius by 10% */
            z-index: 1000;
        }}
        .dark-mode-toggle:hover {{
            background-color: #0056b3;
        }}
    </style>
</head>
<body>
    <h1>{header_text}</h1>
    {go_back_link}
    <table>
        <thead>
            <tr>
                <th class="icon-col">Icon</th>
                <th>Name</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
        {table_rows}
        </tbody>
    </table>
    
    <!-- Auto-generated by Python script -->
    <button class="dark-mode-toggle" onclick="toggleDarkMode()">🌙 Dark Mode</button>
    <script>
        function toggleDarkMode() {{
            const body = document.body;
            const button = document.querySelector('.dark-mode-toggle');
            body.classList.toggle('dark-mode');
            const isDarkMode = body.classList.contains('dark-mode');
            localStorage.setItem('darkMode', isDarkMode);

            // Update button text based on current mode
            button.textContent = isDarkMode ? '🌞 Light Mode' : '🌙 Dark Mode';
        }}

        // Load dark mode setting from localStorage
        document.addEventListener('DOMContentLoaded', () => {{
            const isDarkMode = localStorage.getItem('darkMode') === 'true';
            const button = document.querySelector('.dark-mode-toggle');

            if (isDarkMode) {{
                document.body.classList.add('dark-mode');
                button.textContent = '🌞 Light Mode';
            }} else {{
                button.textContent = '🌙 Dark Mode';
            }}
        }});
    </script>
</body>
</html>
"""

EXCLUDED_DIRS = ['.git', '.github', '__pycache__']  # Exclude certain directories

def is_auto_generated(file_path):
    """Check if the file contains the auto-generated signature"""
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return '<!-- Auto-generated by Python script -->' in content

def format_size(size):
    """Convert bytes to a human-readable string"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0

def format_date(timestamp):
    """Convert a timestamp to a readable date format"""
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(timestamp))

def get_full_url(root, folder_path):
    """Generate a full URL based on the directory path relative to the root"""
    relative_path = os.path.relpath(root, folder_path)
    if relative_path == ".":
        return "data.aykhan.net"
    return f"data.aykhan.net/{relative_path.replace(os.sep, '/')}"

def to_title_case(s):
    """Convert a string to title case."""
    return s.replace('/', ' ').title().replace(' ', ' | ')

def generate_index_html(folder_path):
    """
    Recursively generates or updates index.html files in each folder and subfolder,
    but skips files not auto-generated by this script and excludes certain folders.
    """
    for root, dirs, files in os.walk(folder_path):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        index_file_path = os.path.join(root, 'index.html')

        # Skip updating if index.html exists but was not auto-generated
        if 'index.html' in files and not is_auto_generated(index_file_path):
            print(f'Skipping {index_file_path} (manually created)')
            continue

        # Determine if we're in the root directory (Home)
        if root == folder_path:
            header_text = "data.aykhan.net"
            title = "data.aykhan.net"
            go_back_link = ""  # No go-back link on home
        else:
            full_url = get_full_url(root, folder_path)  # Generate full URL for the directory
            header_text = full_url
            title = to_title_case(full_url)
            go_back_link = '<a href="../index.html" class="go-back">⬅️ Go Back</a>'

        # Create list of items (folders and files) for the current folder
        table_rows = []

        # Add directories to the table
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            last_modified = format_date(os.path.getmtime(dir_path))
            table_rows.append(
                f'<tr>'
                f'<td class="icon-col">📁</td>'
                f'<td><a href="{dir_name}/index.html">{dir_name}/</a></td>'
                f'<td>-</td>'
                f'<td>{last_modified}</td>'
                f'</tr>'
            )

        # Add files to the table (skip the index.html file)
        for file_name in files:
            if file_name == "index.html":
                continue
            file_path = os.path.join(root, file_name)
            file_size = format_size(os.path.getsize(file_path))
            last_modified = format_date(os.path.getmtime(file_path))
            table_rows.append(
                f'<tr>'
                f'<td class="icon-col">📄</td>'
                f'<td><a href="{file_name}">{file_name}</a></td>'
                f'<td>{file_size}</td>'
                f'<td>{last_modified}</td>'
                f'</tr>'
            )

        # Join the table rows as HTML
        table_rows_html = "\n        ".join(table_rows)

        # Render the final HTML for the index.html file
        index_html_content = INDEX_HTML_TEMPLATE.format(
            title=title,
            header_text=header_text,
            table_rows=table_rows_html,
            go_back_link=go_back_link
        )

        # Write or overwrite index.html in the current folder with utf-8 encoding
        with open(index_file_path, 'w', encoding='utf-8') as index_file:
            index_file.write(index_html_content)

        print(f'Updated {index_file_path}')

if __name__ == "__main__":
    root_folder = '.'
    generate_index_html(root_folder)