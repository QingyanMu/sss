import struct

# 读取原始词汇表和词向量矩阵
with open('../temp/w2v_embed_300.bin', 'rb') as f:
    header_line = f.readline().rstrip().decode('utf-8')
    vocab_size, embedding_dim = map(int, header_line.split())

    vocab = [] 
    embeddings = []
    for i in range(vocab_size):
        # 读取单词和词向量数据
        word = b''
        while True:
            ch = f.read(1)
            if ch == b' ':
                break
            word += ch
        word = word.decode('utf-8','ignore')
        vec = struct.unpack('f' * embedding_dim, f.read(embedding_dim * 4))

        # 保存单词和词向量数据
        vocab.append(word)
        embeddings.append(vec)

# 读取句子数据，将其转换为单词和向量形式并存储到新的词汇表和词向量矩阵中
with open('../../../item.txt', 'r', encoding='utf-8') as f:
    new_vocab = vocab.copy()
    new_embeddings = embeddings.copy()

    for line in f:
        # 将句子分割为单词
        words = line.strip().split()

        # 计算句子的平均向量
        vec_sum = [0] * embedding_dim
        for word in words:
            if word in vocab:
                vec_sum = [vec_sum[j] + embeddings[vocab.index(word)][j] for j in range(embedding_dim)]
        vec_avg = [x / len(words) for x in vec_sum]

        # 如果句子中至少有一个单词在原来的词汇表中出现，则将句子的向量替换为平均向>量
        if any(word in vocab for word in words):
            new_embeddings.append(vec_avg)
            new_vocab.append(' '.join(words))

# 将新的词汇表和词向量矩阵存储到文件中
with open('w2v_embed_300_with_data.bin', 'wb') as f:
    # 写入头部信息
    header = f'{len(new_vocab)} {embedding_dim}\n'.encode('utf-8')
    f.write(header)

    # 写入词汇表和词向量数据
    for i in range(len(new_vocab)):
        word = new_vocab[i].encode('utf-8')
        f.write(word)
        f.write(b' ')

        vec = new_embeddings[i]
        for j in range(embedding_dim):
            data = struct.pack('f', vec[j])
            f.write(data)                                            
