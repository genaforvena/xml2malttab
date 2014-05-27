# -*- coding: utf8 -*-
from StringIO import StringIO

__author__ = 'imozerov'
from xml2malttab import *

import unittest
import mock
import os
import sys

class TranslatorTest(unittest.TestCase):
    filename = None
    test_in = '<S ID="8"><W DOM="2" FEAT="S ЕД МУЖ ИМ НЕОД" ID="1" LEMMA="КАБИНЕТ" LINK="предик">Кабинет</W><W DOM="_root" FEAT="V НЕСОВ ИЗЪЯВ ПРОШ ЕД МУЖ" ID="2" LEMMA="ОТЛИЧАТЬСЯ">отличался</W><W DOM="2" FEAT="S ЕД ЖЕН ТВОР НЕОД" ID="3" LEMMA="СКРОМНОСТЬ" LINK="2-компл">скромностью</W>,<W DOM="3" FEAT="A ЕД ЖЕН ТВОР" ID="4" LEMMA="ПРИСУЩИЙ" LINK="опред">присущей</W><W DOM="4" FEAT="S ЕД МУЖ ДАТ ОД" ID="5" LEMMA="СЕМЕН" LINK="1-компл">Семену</W><W DOM="5" FEAT="S ЕД МУЖ ДАТ ОД" ID="6" LEMMA="ЕРЕМЕЕВИЧ" LINK="аппоз">Еремеевичу</W>.</S>'

    def setUp_transaltor(self):
        with mock.patch('xml2malttab.Reader.open_file', mock.mock_open(read_data=self.test_in), create=True):
            translator = Translator("unittest")
            translator.translate([x for x in range(100)])
        self.filename = translator.print_train_set()
        with open(self.filename, "a+") as f:
            self.lines = f.readlines()

    def test_translate_validInput_shouldOutputValidLines(self):
        self.setUp_transaltor()
        test_out_first_line = 'Кабинет\tS.m.nom.sg\t2\tпредик\n'
        self.assertEqual(test_out_first_line, self.lines[0])

    def test_translate_validInput_shouldContainNewLineBetweenSentences(self):
        self.setUp_transaltor()
        self.assertIn("\n", self.lines)

    # def test_in_english_russianSetInput_shouldReturnEnglishSet(self):
    #     set_should_be = set(["m", "nom", "sg", "inan"])
    #     translator = Translator()
    #     translated_set = translator.in_english(set(["ЕД", "МУЖ", "ИМ", "НЕОД"]))
    #
    #     self.assertEqual(set_should_be, translated_set)

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            print "Cant delete file!"

