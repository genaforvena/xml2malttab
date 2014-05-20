# -*- coding: utf8 -*-
__author__ = 'imozerov'

import xml.parsers.expat
import glob
import argparse
from rus_dicts import *


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('output')
    return parser.parse_args()


class Reader(object):
    def __init__(self):
        self._parser = xml.parsers.expat.ParserCreate()
        self._parser.StartElementHandler = self.start_element
        self._parser.EndElementHandler = self.end_element
        self._parser.CharacterDataHandler = self.char_data

    def start_element(self, name, attr):
        if name == 'W':
            features = attr['FEAT'].split(' ') if 'FEAT' in attr else ['UNK']
            for i in range(0, len(features)):
                if features[i] in feat_ru_en:
                    features[i] = feat_ru_en[features[i]]

            lemma = lemma = attr['LEMMA'].lower() if 'LEMMA' in attr else ''
            link = attr['LINK'] if 'LINK' in attr else None

            dom = int(attr['DOM']) if attr['DOM'] != '_root' else 0
            pos = features[0]
            feat = set(features[1:])

            if 'adjp' in feat:
                pos = 'VADJ'
                feat -= {'adjp'}

            if 'advp' in feat:
                pos = 'VADV'
                feat -= {'advp'}

            if 'inf' in feat:
                pos = 'VINF'
                feat -= {'inf'}

            self._info = word_t(lemma=lemma, pos=pos, feat=feat, id=int(attr['ID']), dom=dom, link=link)
            self._cdata = ''

    def end_element(self, name):
        if name == 'S':
            self._sentences.append(self._sentence)
            self._sentence = []
        elif name == 'W':
            self._sentence.append((self._cdata, self._info))
            self._cdata = ''

    def char_data(self, content):
        self._cdata += content

    def read(self, filename):
        f = self.open_file(filename)
        content = f.read()
        f.close()
        content = content.replace('encoding="windows-1251"', 'encoding="utf-8"')

        self._sentences = []
        self._sentence = []
        self._cdata = ''
        self._info = ''

        self._parser.Parse(content)

        return self._sentences

    def open_file(self, filename):
        return open(filename)

class Translator(object):
    train_set_postfix = "_train"
    test_set_postfix = "_test"

    def __init__(self, output = "corpus"):
        self._output = output
        self._files_limit = 1000
        self._test_set = None
        self._train_set = None

    def translate(self, files):
        corpus = []
        for file in files[0:800]:
            R = Reader()
            sentences = R.read(file)
            corpus.extend(sentences)
            del (R)

        fold_size = int(round(len(corpus) / 10))

        self._train_set = corpus[0:-fold_size]
        self._test_set = corpus[-fold_size:]

    def print_train_set(self):
        return self._print_to_file(self._train_set, self.train_set_postfix)

    def print_test_set(self):
        return self._print_to_file(self._test_set, self.test_set_postfix)

    def _print_to_file(self, list_to_print, out_postfix):
        filename = self._output + out_postfix + ".conll"
        with open(filename, "w+") as f:
            for sentence in list_to_print:
                for word in sentence:
                    if len(word) < 2: continue
                    w = word[0] or 'FANTOM'
                    p = '.'.join([word[1].pos] + sorted(word[1].feat & selected_feat))
                    l = word[1].link if word[1].dom else 'ROOT'
                    d = str(word[1].dom)
                    f.write('\t'.join([w, p, d, l]).encode("utf-8"))
                    f.write('')
        return filename


if __name__ == '__main__':
    args = parse_command_line_arguments()
    files = glob.glob(args.path + '/*/*/*.tgt')
    translator = Translator(args.output)
    translator.translate(files)
    translator.print_train_set()
    translator.print_test_set()





