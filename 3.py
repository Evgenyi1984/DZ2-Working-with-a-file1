filenames = ['1.txt', '2.txt', '3.txt']
file_contents = []
for filename in filenames:
    with open(filename, 'r') as f:
        content = f.read()
        lines = content.split('\n')
        lines = list(filter(lambda x: x if x else False ,lines))
        file_contents.append((filename, len(lines), content))
sorted_contents = sorted(file_contents, key=lambda x: x[1])
with open('result_3_file.txt', 'w') as result_file:
    for content in sorted_contents:
        file_name, line_count, content_text = content
        result_file.write(file_name + '\n')
        result_file.write(str(line_count) + '\n')
        result_file.write(content_text + '\n')
