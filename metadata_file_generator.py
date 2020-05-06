# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'metadata_file_generator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
import pandas

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_metadata_editor(object):
    def setupUi(self, metadata_editor):
        metadata_editor.setObjectName(_fromUtf8("metadata_editor"))
        metadata_editor.resize(800, 600)
        self.centralwidget = QtGui.QWidget(metadata_editor)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 10, 781, 511))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(1)
        self.table.setRowCount(0)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        self.add_attribute = QtGui.QPushButton(self.centralwidget)
        self.add_attribute.setGeometry(QtCore.QRect(10, 530, 381, 23))
        self.add_attribute.setObjectName(_fromUtf8("add_attribute"))
        self.set_attribute = QtGui.QPushButton(self.centralwidget)
        self.set_attribute.setGeometry(QtCore.QRect(410, 530, 381, 23))
        self.set_attribute.setObjectName(_fromUtf8("set_attribute"))
        metadata_editor.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(metadata_editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        metadata_editor.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(metadata_editor)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        metadata_editor.setStatusBar(self.statusbar)
        self.actionAdd_Files = QtGui.QAction(metadata_editor)
        self.actionAdd_Files.setObjectName(_fromUtf8("actionAdd_Files"))
        self.actionClear_Table = QtGui.QAction(metadata_editor)
        self.actionClear_Table.setObjectName(_fromUtf8("actionClear_Table"))
        self.actionSave_to_csv = QtGui.QAction(metadata_editor)
        self.actionSave_to_csv.setObjectName(_fromUtf8("actionSave_to_csv"))
        self.actionOpen_csv_file = QtGui.QAction(metadata_editor)
        self.actionOpen_csv_file.setObjectName(_fromUtf8("actionOpen_csv_file"))
        self.menuFile.addAction(self.actionAdd_Files)
        self.menuFile.addAction(self.actionClear_Table)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_to_csv)
        self.menuFile.addAction(self.actionOpen_csv_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(metadata_editor)

        QtCore.QObject.connect(self.actionAdd_Files, QtCore.SIGNAL('triggered()'), self.get_files)
        QtCore.QObject.connect(self.actionClear_Table, QtCore.SIGNAL('triggered()'), self.clear_table)
        QtCore.QObject.connect(self.actionSave_to_csv, QtCore.SIGNAL('triggered()'), self.save_csv)
        QtCore.QObject.connect(self.actionOpen_csv_file, QtCore.SIGNAL('triggered()'), self.open_csv)
        QtCore.QObject.connect(self.add_attribute, QtCore.SIGNAL('clicked()'), self.add_attribute_column)
        QtCore.QObject.connect(self.set_attribute, QtCore.SIGNAL('clicked()'), self.set_attributes)

        QtCore.QMetaObject.connectSlotsByName(metadata_editor)

    def get_files(self):
        files = QtGui.QFileDialog.getOpenFileNames(None, 'Select File(s)', 'C:\\')
        files = [str(i).replace('/', '\\') for i in files]
        for i in range(0, len(files)):
            num_rows = self.table.rowCount()
            self.table.insertRow(num_rows)
            self.table.setItem(i, 0, QtGui.QTableWidgetItem(os.path.basename(files[i])))

    def clear_table(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(1)

    def save_csv(self):
        output = QtGui.QFileDialog.getSaveFileName(None, 'Save File', 'C:\\')
        output = str(output).replace('/', '\\')
        headers = [str(self.table.horizontalHeaderItem(i).text())
                   for i in range(0, self.table.horizontalHeader().count())]
        headers = [headers[0].lower()] + ['ATTRIBUTE_' + i for i in headers[1:]]
        num_rows = self.table.rowCount()
        num_cols = self.table.columnCount()
        data = []
        for i in range(0, num_rows):
            row = []
            for j in range(0, num_cols):
                row.append(str(self.table.item(i, j).text()))
            data.append(row)
        df = pandas.DataFrame(data, columns=headers)
        df.to_csv(path_or_buf=output + '.csv', index=False)

    def open_csv(self):
        input_file = QtGui.QFileDialog.getOpenFileName(None, 'Open File', 'C:\\')
        input_file = str(input_file).replace('/', '\\')
        self.clear_table()
        df = pandas.read_csv(input_file)
        if not df.empty:
            data = df.values.tolist()
            headers = list(df.columns)
            headers = [headers[0].capitalize()] + [i.split('ATTRIBUTE_')[1] for i in headers[1:]]
            self.table.setRowCount(len(data))
            self.table.setColumnCount(len(headers))
            self.table.setHorizontalHeaderLabels(headers)
            for row in data:
                for value in row:
                    self.table.setItem(data.index(row), row.index(value), QtGui.QTableWidgetItem(str(value)))

    def add_attribute_column(self):
        attribute, ok = QtGui.QInputDialog.getText(None, 'Add Attribute', 'Enter attribute:')
        headers = [str(self.table.horizontalHeaderItem(i).text())
                   for i in range(0, self.table.horizontalHeader().count())]
        self.table.setColumnCount(len(headers) + 1)
        self.table.setHorizontalHeaderLabels(headers + [str(attribute)])

    def set_attributes(self):
        attributes = [str(self.table.horizontalHeaderItem(i).text())
                      for i in range(0, self.table.horizontalHeader().count())]
        rows = [int(i.row()) for i in self.table.selectionModel().selectedRows()]
        headers = [str(self.table.horizontalHeaderItem(i).text())
                   for i in range(0, self.table.horizontalHeader().count())]
        attribute, ok = QtGui.QInputDialog.getItem(None, 'Choose Attribute', '', tuple(attributes[1:]))
        spec_attr, ok = QtGui.QInputDialog.getText(None, 'Add Specific Attribute', 'Enter specific attribute:')
        for i in rows:
            self.table.setItem(i, headers.index(str(attribute)), QtGui.QTableWidgetItem(str(spec_attr)))

    def retranslateUi(self, metadata_editor):
        metadata_editor.setWindowTitle(_translate("metadata_editor", "GNPS FBMN Metadata Editor", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("metadata_editor", "Filename", None))
        self.add_attribute.setText(_translate("metadata_editor", "Add Attribute", None))
        self.set_attribute.setText(_translate("metadata_editor", "Set Attribute", None))
        self.menuFile.setTitle(_translate("metadata_editor", "File", None))
        self.actionAdd_Files.setText(_translate("metadata_editor", "Add Files...", None))
        self.actionClear_Table.setText(_translate("metadata_editor", "Clear Table...", None))
        self.actionSave_to_csv.setText(_translate("metadata_editor", "Save to .csv...", None))
        self.actionOpen_csv_file.setText(_translate("metadata_editor", "Open .csv file...", None))


def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_metadata_editor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()