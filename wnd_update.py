# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_update.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import update_image_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(510, 301)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(65, 64))
        self.label.setPixmap(QPixmap(u":/images/icon_128x128.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_bbh = QLabel(Form)
        self.label_bbh.setObjectName(u"label_bbh")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_bbh.setFont(font1)

        self.verticalLayout.addWidget(self.label_bbh)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.textEdit)

        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.label_zt = QLabel(Form)
        self.label_zt.setObjectName(u"label_zt")
        self.label_zt.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.label_zt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_tgbb = QPushButton(Form)
        self.btn_tgbb.setObjectName(u"btn_tgbb")

        self.horizontalLayout.addWidget(self.btn_tgbb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_azgx = QPushButton(Form)
        self.btn_azgx.setObjectName(u"btn_azgx")
        self.btn_azgx.setCheckable(False)
        self.btn_azgx.setAutoDefault(True)
        self.btn_azgx.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_azgx)

        self.btn_ok = QPushButton(Form)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btn_ok)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.btn_azgx.setDefault(True)
        self.btn_ok.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u66f4\u65b0", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u53d1\u73b0\u65b0\u7248\u672c", None))
        self.label_bbh.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u7248\u672c:2.0    \u5f53\u524d\u7248\u672c:1.0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7248\u672c\u63cf\u8ff0", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_zt.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5927\u5c0f \u4e0b\u8f7d\u901f\u5ea6 \u5269\u4f59\u65f6\u95f4", None))
        self.btn_tgbb.setText(QCoreApplication.translate("Form", u"\u8df3\u8fc7\u7248\u672c", None))
        self.btn_azgx.setText(QCoreApplication.translate("Form", u"\u5b89\u88c5\u66f4\u65b0", None))
        self.btn_ok.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
    # retranslateUi

