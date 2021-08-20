# 讀取對話紀錄
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

# 轉換
def convert(lines):
    new = []
    person = None # 把預設值設成無，其他語言叫null。
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: # 如果person有值的話，才執行下一行
            new.append(person + '： ' + line)
    return new

# 寫入檔案
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

# main function
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

# 進入點：最早開始被”執行“的地方
main()