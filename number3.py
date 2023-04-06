import os

project = os.getcwd()
container = os.path.join(project, 'files')

files_dict = {}

for filename in os.listdir('files'):
    if filename.endswith('.txt'):
        file = os.path.join(container, filename)
        with open(file, 'rt', encoding='utf-8') as f:
            line_count = 0
            content = []
            for line in f:
                content.append(line.strip('\n'))
                line_count += 1
            files_dict[filename] = {
                'line_count': line_count,
                'content': content
            }


files_dict_sorted = dict(sorted(files_dict.items(), key=lambda x: x[1].get('line_count')))


with open('container.txt', 'w', encoding='utf=8') as f:
    for i in files_dict_sorted:
        f.write(i + '\n')
        f.write(str(files_dict_sorted[i]['line_count']) + '\n')
        f.write('\n'.join(files_dict_sorted[i]['content']) + '\n')

