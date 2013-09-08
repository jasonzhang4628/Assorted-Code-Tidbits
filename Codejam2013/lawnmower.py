input_file = open('test.txt', 'r')
text = input_file.read().split()

cases = int(text[0])

def separator(textlist):
    count = 0
    position = 1
    output = []
    for _ in range(cases):
        output.append([])
    while count < cases:
        n, m = int(textlist[position]), int(textlist[position + 1])
        output[count].append([n, m])
        output[count].append([])
        position += 2
        cap = position + n * m
        while position < cap:
            output[count][1].append(int(textlist[position]))
            position += 1
        count += 1
    return output
   

 
print(separator(text))
