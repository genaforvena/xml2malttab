# -*- coding: utf8 -*-
__author__ = 'imozerov'
from collections import namedtuple

selected_feat = set(['m', 'f', 'n', 'sg', 'pl', '1p', '2p', '3p', 'nom', 'gen', 'gen2', 'dat', 'acc', 'ins', 'prep', 'loc',
                 'real', 'imp', 'pass', 'comp', 'shrt'])

word_t = namedtuple('word_t', ['lemma', 'pos', 'feat', 'id', 'dom', 'link'])
feat_ru_en = {
    u'ЕД': 'sg',
    u'МН': 'pl',
    u'ЖЕН': 'f',
    u'МУЖ': 'm',
    u'СРЕД': 'n',
    u'ИМ': 'nom',
    u'РОД': 'gen',
    u'ДАТ': 'dat',
    u'ВИН': 'acc',
    u'ТВОР': 'ins',
    u'ПР': 'prep',
    u'ПАРТ': 'gen2',
    u'МЕСТН': 'loc',
    u'ОД': 'anim',
    u'НЕОД': 'inan',
    u'ИНФ': 'inf',
    u'ПРИЧ': 'adjp',
    u'ДЕЕПР': 'advp',
    u'ПРОШ': 'pst',
    u'НЕПРОШ': 'npst',
    u'НАСТ': 'prs',
    u'1-Л': '1p',
    u'2-Л': '2p',
    u'3-Л': '3p',
    u'ИЗЪЯВ': 'real',
    u'ПОВ': 'imp',
    u'КР': 'shrt',
    u'НЕСОВ': 'imperf',
    u'СОВ': 'perf',
    u'СТРАД': 'pass',
    u'СЛ': 'compl',
    u'СМЯГ': 'soft',
    u'СРАВ': 'comp',
    u'ПРЕВ': 'supl',
}

link_ru_en = {
    u'предик': 'subj',
    u'1-компл': 'obj',
    u'2-компл': 'obj',
    u'3-компл': 'obj',
    u'4-компл': 'obj',
    u'5-компл': 'obj',
    u'опред': 'amod',
    u'предл': 'prep',
    u'обст': 'pobj',
}