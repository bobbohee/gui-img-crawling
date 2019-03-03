# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from lib.extractWordLayout import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import urllib.request as request
import urllib.error as err
import urllib.parse as parse
import datetime
import codecs
import time
import sys
import io
import os
import img_crawling

# 아래 코드는 Atom 에디터에서 실행시에 한글 검색 결과가 있는 삽입해야 함.
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 초기화
        self.setupUi(self)
        # 시그널 초기화
        self.initSignal()
        # 초기 셋팅
        self.initSetting()

    # 초기 셋팅
    def initSetting(self):
        self.swordEdit.setFocus(True)

    # 시그널 초기화
    def initSignal(self):
        # 시작 버튼 클릭 시
        self.startSearchWordButton.clicked.connect(self.extractWordStart)
        # 초기화 버튼 클릭 시
        self.initButton.clicked.connect(self.initAllComponent)
        # 종료 버튼 클릭 시
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # 엔터키 입력 시
        self.swordEdit.returnPressed.connect(self.extractWordStart)
        # 검색어 리스트 클릭 시
        self.listWidget_3.itemClicked.connect(self.setTextFotWord)
        # 검색어 리스트 더블 클릭 시
        self.listWidget_3.itemDoubleClicked.connect(self.extractWordStart)

    # 추출 시작
    def extractWordStart(self):
        word = self.swordEdit.text().strip()

        url = 'https://www.google.co.kr/search?q=' + word + '&tbm=isch&source=lnt&tbs=qdr:y'

        # 웹뷰 미리보기 로드
        self.webView.load(QUrl(url))
        self.listWidget_3.addItem(word)

        img_crawling.neg_img(word)

        # 재 요청 시 초기화 작업
        self.swordEdit.clear()
        self.swordEdit.setFocus(True)

    # 초기화 버튼 클릭 시
    def initAllComponent(self):
        self.swordEdit.clear()
        self.listWidget_3.clear()
        self.webView.load(QUrl('about:blank'))
        self.swordEdit.setFocus(True)

    # 검색어 리스트 텍스트 클릭 시
    def setTextFotWord(self):
        self.swordEdit.setFocus(True)
        self.swordEdit.setText(self.listWidget_3.currentItem().text().strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    extractWord = Main()
    extractWord.show()
    app.exec_()
