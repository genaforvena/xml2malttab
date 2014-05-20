# -*- coding: utf8 -*-
__author__ = 'imozerov'
from collections import namedtuple

selected_feat = {'m', 'f', 'n', 'sg', 'pl', '1p', '2p', '3p', 'nom', 'gen', 'gen2', 'dat', 'acc', 'ins', 'prep', 'loc',
                 'real', 'imp', 'pass', 'comp', 'shrt'}

word_t = namedtuple('word_t', ['lemma', 'pos', 'feat', 'id', 'dom', 'link'])
feat_ru_en = {
    'ЕД': 'sg',
    'МН': 'pl',
    'ЖЕН': 'f',
    'МУЖ': 'm',
    'СРЕД': 'n',
    'ИМ': 'nom',
    'РОД': 'gen',
    'ДАТ': 'dat',
    'ВИН': 'acc',
    'ТВОР': 'ins',
    'ПР': 'prep',
    'ПАРТ': 'gen2',
    'МЕСТН': 'loc',
    'ОД': 'anim',
    'НЕОД': 'inan',
    'ИНФ': 'inf',
    'ПРИЧ': 'adjp',
    'ДЕЕПР': 'advp',
    'ПРОШ': 'pst',
    'НЕПРОШ': 'npst',
    'НАСТ': 'prs',
    '1-Л': '1p',
    '2-Л': '2p',
    '3-Л': '3p',
    'ИЗЪЯВ': 'real',
    'ПОВ': 'imp',
    'КР': 'shrt',
    'НЕСОВ': 'imperf',
    'СОВ': 'perf',
    'СТРАД': 'pass',
    'СЛ': 'compl',
    'СМЯГ': 'soft',
    'СРАВ': 'comp',
    'ПРЕВ': 'supl',
}

link_ru_en = {
    'предик': 'subj',
    '1-компл': 'obj',
    '2-компл': 'obj',
    '3-компл': 'obj',
    '4-компл': 'obj',
    '5-компл': 'obj',
    'опред': 'amod',
    'предл': 'prep',
    'обст': 'pobj',
}