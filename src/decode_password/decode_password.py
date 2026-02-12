
class FindPassword:
    def __init__(self, filename):
        self.filename = filename

    def find_char_in_chunk(self,coord_row, chunk_size):
        first_square_bracket = coord_row.find("[")
        second_square_bracket = coord_row.find("]")
        indexes_str = coord_row[first_square_bracket+1:second_square_bracket]
        new_y, x = [int(i.strip()) for i in indexes_str.split(",")]

        new_x = len(chunk_size)-1-x
        if new_x < 0 or new_x >= len(chunk_size):
            return None
        if new_y < 0 or new_y >= len(chunk_size[new_x]):
            return None

        return chunk_size[new_x][new_y]


    def parse_file(self):
        lines = []

        with open(self.filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    lines.append(line)

        i = 0
        while i < len(lines):
            if not lines[i]:
                i+=1
                continue
            index = None

            if lines[i].isdigit():
                index = int(lines[i])
                i+=1
                if i >= len(lines):
                    break

            coord_line = lines[i]
            i+=1
            if i >= len(lines):
                break

            chunk = []
            while i<len(lines):
                if lines[i].isdigit() or lines[i].startswith("["):
                    break
                if lines[i]:
                    chunk.append(lines[i])
                i += 1

            c = self.find_char_in_chunk(coord_line, chunk)
            if c is not None:
                yield {"index": index, "char": c}


fp = FindPassword("./decode_password.txt")

#part 1:
for block in fp.parse_file():
    print(block["char"])

#part 2:
char_map = {}
for block in fp.parse_file():
    char_map[block["index"]] = block["char"]
def print_password(char_map):
    result = []
    for key in sorted(char_map.keys()):
        result.append(char_map[key])
    print("".join(result))

print_password(char_map)


#part 3
char_map = {}
for block in fp.parse_file():
    if block["index"] in char_map:
        break
    char_map[block["index"]] = block["char"]
print_password(char_map)









