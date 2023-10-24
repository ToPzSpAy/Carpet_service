import os
import sys
import unittest

from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget
from main import Auth
from threading import Timer
app = QApplication(sys.argv)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.w = Auth()
        self.w.show()

    def close_msg(self):
        self.w.m.done(1)

    def close_msg1(self):
        self.w.w.w.m.done(1)

    def test_login(self):
        self.w.login_e.setText('43434')
        self.w.pass_e.setText('gawy34k')
        Timer(1.0, self.close_msg).start()
        self.w.try_enter()
        self.w.login_e.setText('admin')
        self.w.pass_e.setText('1234')
        self.w.try_enter()
        self.assertEqual(self.w.w.dostup_l.text(), 'Доступ: Администратор')

    def test_user(self):
        self.w.login_e.setText('admin')
        self.w.pass_e.setText('1234')
        self.w.try_enter()
        self.w.w.user_window()
        i = self.w.w.w.user_table.item(0,0).text()
        self.assertEqual(i,'0')

    def test_pricelist(self):
        self.w.login_e.setText('admin')
        self.w.pass_e.setText('1234')
        self.w.try_enter()
        self.w.w.pricelist_window()
        name = '1test1'
        self.w.w.w.name_e.setText(name)
        self.w.w.w.price_e.setText('100')
        self.w.w.w.add_serv()
        row = self.w.w.w.services_table.rowCount() - 1
        result = self.w.w.w.services_table.item(row,1).text()
        self.w.w.w.select_serv(row,'')
        self.w.w.w.delete_serv()
        self.assertEqual(result, name)

    def test_servicees(self):
        self.w.login_e.setText('admin')
        self.w.pass_e.setText('1234')
        self.w.try_enter()
        self.w.w.services_window()
        name = 'test_service'
        self.w.w.w.name_e.setText(name)
        self.w.w.w.price_e.setText('300')
        self.w.w.w.add_serv()
        row = self.w.w.w.services_table.rowCount() - 1
        result = self.w.w.w.services_table.item(row,1).text()
        self.w.w.w.select_serv(row,'')
        self.w.w.w.delete_serv()
        self.assertEqual(result, name)

    def test_extramenu(self):
        self.w.login_e.setText('admin')
        self.w.pass_e.setText('1234')
        if os.path.isfile('backup/export_Services.csv'):
            os.remove('backup/export_Services.csv')
        self.w.try_enter()
        self.w.w.extra_window()
        self.w.w.w.export_csv()
        Timer(1, self.close_msg1).start()
        self.w.w.w.export_csv_conf()
        result = os.path.isfile('backup/export_Services.csv')
        self.assertEqual(True, result)



if __name__ == '__main__':
    unittest.main()