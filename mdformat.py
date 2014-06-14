def markdown():
    with open('Google IP new.txt', 'r', encoding='utf-8') as fr, open('newip.txt', 'w', encoding='utf-8') as fw:
        s = fr.readlines()
        for i in s:
            if not i.startswith('htt'):
                fw.write(i)
                fw.write('---')
            else:
                line = i.split()
                for j in line:
                    fw.write('['+j[7:]+']'+'('+j+')'+'\t')
            fw.write('\n')
