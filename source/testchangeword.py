import detect
word='孩子'

def findsyn(word_):
    detect.run(word_)
    file_path='../output/w2v_synonym.txt'
    f=open(file_path, 'r', encoding='utf8')
    line = f.readline() 
    f.close()
    words = line.split('|')
    return words[-4]


print(findsyn(word))
