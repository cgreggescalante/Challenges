import json
import os

from mdutils.mdutils import MdUtils


mdFile = MdUtils(file_name="README", title="Challenges")

mdFile.new_paragraph("All my coding challenge progress for the following websites.")
mdFile.write("\n")

excluded_dirs = {'.\\.git', '.\\.idea', '.\\python'}
sub_dirs = [f.path for f in os.scandir('.') if f.is_dir() and f.path not in excluded_dirs]

data = []
elements = []
for dir in sub_dirs:
    with open(dir + "\\info.json") as file:
        info = json.loads(file.read())
        data.append((info, dir))
        elements.append(mdFile.new_inline_link(info['link'], info['name']))

mdFile.new_list(elements)
mdFile.write("\n")

for site, dir in data:
    complete_dirs = [x[0] for x in os.walk(dir) if x[0].endswith("\\Complete") and "cmake-build-debug" not in x[0]]
    count_complete = 0
    for sd in complete_dirs:
        for a in os.walk(sd):
            count_complete += len(a[2])
    incomplete_dirs = [x[0] for x in os.walk(dir) if x[0].endswith("\\Incomplete") and "cmake-build-debug" not in x[0]]
    count_incomplete = 0
    for sd in incomplete_dirs:
        for a in os.walk(sd):
            count_incomplete += len(a[2])
    mdFile.new_line(f"## {site['name']}\n")
    mdFile.new_line(f"Completed: {count_complete}")
    mdFile.new_line(f"Attempted: {count_complete + count_incomplete}")

mdFile.create_md_file()

