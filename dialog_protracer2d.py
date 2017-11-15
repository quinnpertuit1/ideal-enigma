from PyQt5 import QtCore, QtGui, QtWidgets

import os
import pandas as pd
import pt_data


class ProTracer2DDialog(object):
    def __init__(self):
        self.shots = []

    def setupUi(self, dlg2D):
        self.dialog = dlg2D

        dlg2D.setObjectName("dlg2D")
        dlg2D.resize(800, 600)
        dlg2D.setSizeGripEnabled(False)
        dlg2D.setModal(True)

        self.groupBox = QtWidgets.QGroupBox(dlg2D)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 141))
        self.groupBox.setObjectName("groupBox")
        self.tabWidget = QtWidgets.QTabWidget(dlg2D)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 781, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 771, 401))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(dlg2D)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlg2D)

        # Wire up event handlers

    def retranslateUi(self, dlg2D):
        _translate = QtCore.QCoreApplication.translate
        dlg2D.setWindowTitle(_translate("dlg2D", "PyProTracer 2D"))
        self.groupBox.setTitle(_translate("dlg2D", "Legend"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("dlg2D", "ProTracer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("dlg2D", "Shot Stats"))

    def set_shot_data(self, data):
        self.shots = data

    def initialize(self):
        if len(self.shots) > 0:
            # do work
            QtWidgets.QMessageBox.information(QtWidgets.QWidget(), 'Chosen Shots', str(self.shots))
        else:
            QtWidgets.QMessageBox.information(
                QtWidgets.QWidget(), 'Error Displaying ProTracer', 'There are no shots selected to show.')
            self.dialog.done(0)
