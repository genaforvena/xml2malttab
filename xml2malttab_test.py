# -*- coding: utf8 -*-
from StringIO import StringIO

__author__ = 'imozerov'
from xml2malttab import *

import unittest
import mock
import os

class TranslatorTest(unittest.TestCase):
    filename = None

    def testTanslate(self):
        test_out_first_line = 'Кабинет\tS\t2\tпредик'
        test_in = '<S ID="8"><W DOM="2" FEAT="S ЕД МУЖ ИМ НЕОД" ID="1" LEMMA="КАБИНЕТ" LINK="предик">Кабинет</W><W DOM="_root" FEAT="V НЕСОВ ИЗЪЯВ ПРОШ ЕД МУЖ" ID="2" LEMMA="ОТЛИЧАТЬСЯ">отличался</W><W DOM="2" FEAT="S ЕД ЖЕН ТВОР НЕОД" ID="3" LEMMA="СКРОМНОСТЬ" LINK="2-компл">скромностью</W>,<W DOM="3" FEAT="A ЕД ЖЕН ТВОР" ID="4" LEMMA="ПРИСУЩИЙ" LINK="опред">присущей</W><W DOM="4" FEAT="S ЕД МУЖ ДАТ ОД" ID="5" LEMMA="СЕМЕН" LINK="1-компл">Семену</W><W DOM="5" FEAT="S ЕД МУЖ ДАТ ОД" ID="6" LEMMA="ЕРЕМЕЕВИЧ" LINK="аппоз">Еремеевичу</W>.</S>'

        with mock.patch('xml2malttab.Reader.open_file', mock.mock_open(read_data=test_in), create=True):
            translator = Translator("unittest")
            translator.translate([x for x in range(100)])
        self.filename = translator.print_train_set()
        with open(self.filename, "a+") as f:
            lines = f.readlines()
        self.assertEqual(test_out_first_line, lines[0])

    def tearDown(self):
        os.remove(self.filename)

