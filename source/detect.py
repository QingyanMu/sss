import Levenshtein_model
import data_utils
import vector
import argparse
import logging
import os

logger = logging.getLogger(__name__)
local_file = os.path.split(__file__)[-1]
logging.basicConfig(
    format='%(asctime)s : %(filename)s : %(funcName)s : %(levelname)s : %(message)s',
    level=logging.INFO)



def run(word):
    file_path='../temp/input_word2.txt'
    f=open(file_path, 'w', encoding='utf8')
    word = '1|'+word
    f.write(word) 
    f.close()   
    stop_word_path = '../input/stop_words.txt'
    corpus_path = '../input/item.txt'
    input_word_path = '../temp/input_word2.txt'
    process_number = 30
    pinyin_weight = 0.0
    top_k = 5
    win_len = 5

    word2id, word_list, id2word, input_word_code_dict, input_word_id = \
        data_utils.preprocess_file(corpus_path, input_word_path, stop_word_path)
    vector.synonym_detect(input_word_code_dict, top_k)
    return input_word_code_dict

