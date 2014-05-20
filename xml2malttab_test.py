# -*- coding: utf8 -*-
__author__ = 'imozerov'
from xml2malttab import *

import unittest
import mock
import os


test_out_first_line = 'Кабинет 		S      2       предик'
test_in = '<S ID="8"><W DOM="2" FEAT="S ЕД МУЖ ИМ НЕОД" ID="1" LEMMA="КАБИНЕТ" LINK="предик">Кабинет</W><W DOM="_root" FEAT="V НЕСОВ ИЗЪЯВ ПРОШ ЕД МУЖ" ID="2" LEMMA="ОТЛИЧАТЬСЯ">отличался</W><W DOM="2" FEAT="S ЕД ЖЕН ТВОР НЕОД" ID="3" LEMMA="СКРОМНОСТЬ" LINK="2-компл">скромностью</W>,<W DOM="3" FEAT="A ЕД ЖЕН ТВОР" ID="4" LEMMA="ПРИСУЩИЙ" LINK="опред">присущей</W><W DOM="4" FEAT="S ЕД МУЖ ДАТ ОД" ID="5" LEMMA="СЕМЕН" LINK="1-компл">Семену</W><W DOM="5" FEAT="S ЕД МУЖ ДАТ ОД" ID="6" LEMMA="ЕРЕМЕЕВИЧ" LINK="аппоз">Еремеевичу</W>.</S>'


class TranslatorTest(unittest.TestCase):
    filename = None
    def testTanslate(self):
        Reader.read = mock.Mock(return_value = test_in)
        translator = Translator("unittest")
        translator.translate([10])
        self.filename = translator.print_train_set()
        with open(self.filename, "r") as f:
            lines = f.readlines()
        self.assertEqual(test_out_first_line, lines[0])

    def tearDown(self):
        os.remove(self.filename)

