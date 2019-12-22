periodic_table = {}
map_index_to_column = {}

csv_file = open("./data/table.csv", "r", encoding="utf-8")
text_lines = csv_file.read().splitlines()
header, body = text_lines[0], text_lines[1:]

index = 0
for column_name in header.split(','):
    periodic_table[column_name] = []
    map_index_to_column[index] = column_name
    index += 1
for line in body:
    contents = line.split(',')
    for position, content in enumerate(contents):
        column = map_index_to_column[position]
        periodic_table[column].append(content)
