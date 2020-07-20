def merge_the_tools(string, k):
    start = 0
    stop = k
    sample = []
    for i in range(len(string)//k):
        sample.append(string[start:stop])
        start += k
        stop += k

    if len(string) % k != 0:
        sample.append(string[-(len(string) % k):])
    
    for part in sample:
        part_list = list(part)
        part_unique = list(dict.fromkeys(part_list))               
        new_part = ''
        for j in range(len(part_unique)):
            new_part += part_unique[j]
        print(new_part)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
