__author__ = 'imozerov'

import os
import sqlite3
import xml.parsers.expat
import glob
from optparse import OptionParser
from rus_dicts import *

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

            lemma = lemma=attr['LEMMA'].lower() if 'LEMMA' in attr else ''
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
        f = open(filename, encoding='windows-1251')
        content = f.read()
        f.close()
        content = content.replace('encoding="windows-1251"', 'encoding="utf-8"')

        self._sentences = []
        self._sentence = []
        self._cdata = ''
        self._info = ''

        self._parser.Parse(content)

        return self._sentences

class Lexicon(object):
    def __init__(self, dbname):
        self.dbname = dbname
        db_exists = os.path.isfile(dbname)
        self.con = sqlite3.connect(dbname)
        self.cur = self.con.cursor()

        if not db_exists:
            self.create_db()

    def create_db(self):
        sql = '''
        create table words(
            id integer primary key autoincrement,
            lemma text,
            pos text,
            form text,
            info text,
            freq integer
        );
        create index words_lemma_form_info on words(lemma, form, info);
        '''
        [self.cur.execute(st) for st in sql.split(';') if len(st.strip())]

    def index(self, filename):
        sentences = Reader().read(filename)
        for sentence in sentences:
            for word in sentence:
                feat = ' '.join(word[1].feat)
                self.cur.execute('select id from words where lemma = ? and form = ? and pos = ? and info = ?', (word[1].lemma, word[0], word[1].pos, feat))
                row = self.cur.fetchone()
                if row is None:
                    self.cur.execute('insert into words (lemma, pos, form, info, freq) values (?, ?, ?, ?, 1)', (word[1].lemma, word[1].pos, word[0], feat))
                else:
                    self.cur.execute('update words set freq = freq + 1 where id = ?', row)

    def close(self):
        self.con.commit()
        self.con.close()

if __name__ == '__main__':
    parser = OptionParser()
    parser.usage = '%prog [options] inputfile'
    parser.add_option('-L', '--construct-lexicon', action = 'store_const', const = True	, dest = 'lexicon', help = 'construct lexicon')

    (options, args) = parser.parse_args()

    if options.lexicon:
        l = Lexicon('tmp/lexicon')
        files = glob.glob('res/*/*/*.tgt')
        for file in files:
            l.index(file)

        l.close()

