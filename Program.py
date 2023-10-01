# -*- coding: utf-8 -*-
import sys
from PyQt6.QtCore import Qt, QDate, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog, QMessageBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QDesktopServices
from Layout.Ui_Layout.Ui_main import Ui_MainWindow
from Layout.SubLayout.info.LongBusSumPage import LongBusSumPage
from Layout.SubLayout.info.CompanyOfficersPage import CompanyOfficerPage
from Layout.SubLayout.Techanalysis.TechanalysisPage import TechAnalysispage
from Layout.SubLayout.Techanalysis.OptimizationIndicatorTools import OptimizationIndicatorTool
from Layout.SubLayout.Mmanagement.MmanagementPage import Moneymanagepage
from Layout.SubLayout.Entrymanagement.OptEntmanagementPage import optEntrymanagepage
from Layout.SubLayout.Entrymanagement.EntmanagementPage import Entrymanagepage
from Layout.Method_Class.backtrade import cerebrosetup
from Layout.SubLayout.Search.SearchSymbol import Tickersearch
from Global.Value.UniversalValue import GlobalValue
from Global.Value.TechToolParam import TechValue
from Global.Value.MoneyManageParam import MoneyValue
from Layout.SubLayout.Ta.talib_lib import talib_list
import matplotlib.pyplot as plt
import mplfinance as mpf
import talib
import functools
import numpy as np
import yfinance as yf
import vectorbt as vbt
import pandas as pd
import webbrowser
import quantstats as qs
import pytz
import backtrader as bt


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # use the Ui_login_form
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)
        self.btn_click()
        self.side_meun_btn()

    # Base Setting
    # ...............................................................................

    def btn_click(self):

        self.ui.searchenter_btn.clicked.connect(self.searchpage)
        self.ui.LongBusinessSummary_btn.clicked.connect(self.longbussumpage)
        self.ui.CompanyOfficers_btn.clicked.connect(self.companyofficerspage)
        self.ui.Period_combo.currentTextChanged.connect(
            self.Period_combo_box_changed)
        self.ui.Interval_combo.currentTextChanged.connect(
            self.checkintervalis1m)
        self.ui.loading_btn.clicked.connect(self.tickerhistory)
        self.ui.clear_btn.clicked.connect(self.cleartickerhistory)
        self.ui.historydownload_btn.clicked.connect(
            self.historydownload)
        self.ui.new_tableview.clicked.connect(self.handleClicked)
        self.ui.techPeriod_combo.currentTextChanged.connect(
            self.techPeriod_combo_box_changed)
        self.ui.techInterval_combo.currentTextChanged.connect(
            self.techcheckintervalis1m)
        self.ui.techanalysis_tools_btn.clicked.connect(
            self.techanalysistoolpage)
        self.ui.Techenter_btn.clicked.connect(self.techanalysisenterdetail)
        self.ui.DownLoad_btn.clicked.connect(self.techanalysisenterdownloadcsv)
        self.ui.aa_techPeriod_combo.currentTextChanged.connect(
            self.aatechPeriod_combo_box_changed)
        self.ui.aa_techInterval_combo.currentTextChanged.connect(
            self.aatechcheckintervalis1m)
        self.ui.aa_Techenter_btn.clicked.connect(
            self.aatechanalysisenterdetail)
        self.ui.aa_techanalysis_tools_btn.clicked.connect(
            self.aatechanalysistoolpage)
        self.ui.aa_techanalysis_tools_mmbtn.clicked.connect(
            self.aamoneymanagepage)
        self.ui.aa_techanalysis_tools_entriesbtn.clicked.connect(
            self.aaentrymanagepage)
        self.ui.aa_DownLoad_btn.clicked.connect(
            self.techanalysisenterdownloadcsv)

        self.ui.ea_techPeriod_combo.currentTextChanged.connect(
            self.eatechPeriod_combo_box_changed)
        self.ui.ea_techInterval_combo.currentTextChanged.connect(
            self.eatechcheckintervalis1m)
        self.ui.ea_Techenter_btn.clicked.connect(
            self.eatechanalysisenterdetail)

        self.ui.ea_techanalysis_tools_btn.clicked.connect(
            self.OptimizationIndicatorToolspage)
        self.ui.ea_techanalysis_tools_mmbtn.clicked.connect(self.aamoneymanagepage)
        self.ui.ea_techanalysis_tools_entriesbtn.clicked.connect(self.Optentrymanagepage)

    def side_meun_btn(self):
        self.ui.Btn_Home.clicked.connect(self.showtkhome)
        self.ui.Btn_Search.clicked.connect(self.showtksearch)
        self.ui.Btn_Info.clicked.connect(self.infopage)
        self.ui.Btn_History.clicked.connect(self.historypage)
        self.ui.Btn_News.clicked.connect(self.newpage)
        self.ui.Btn_TA.clicked.connect(self.techanalysispage)
        self.ui.Btn_AA.clicked.connect(self.aatechanalysispage)
        self.ui.Btn_EAA.clicked.connect(self.eatechanalysispage)

    def showtkhome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page)

    def showtksearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.search_page)

    def showtkinfo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.info_page)

    def showhistory(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.history_metadata_page)

    def shownew(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.new_page)

    def showtechanalysis(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.techanalysis_page)

    def showaatechanalysis(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.aatechanalysis_page)

    def showeatechanalysis(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.eatechanalysis_page)

    # Base Setting
    # ...............................................................................
    # ///////////////////////////////////////////////////////////////////////////////
    # Search Page
    # ...............................................................................

    def searchpage(self):
        try:
            if (Tickersearch(self.ui.text_lineEdit.text().upper()).tickerchecking() == True):
                self.settersymbol(self.ui.text_lineEdit.text().upper())
                self.addsearchhistory(self.gettersymbol())
                self.ui.Sub_Tittle.setText(
                    'Ticker Symbol : ' + self.gettersymbol())
                self.clearlineedit()
                print('Ticker Symbol Loading')
            else:
                print('Error Ticker Symbol')
        except:
            print('Error Ticker Symbol')

    def longbussumpage(self):
        self.infodict = self.gettersymbolinfo()
        self.uishow = LongBusSumPage(self.infodict['longBusinessSummary'])
        self.uishow.show()

    def companyofficerspage(self):
        self.infodict = self.gettersymbolinfo()
        self.uishow = CompanyOfficerPage(self.infodict['companyOfficers'])
        self.uishow.show()

    def addsearchhistory(self, text):
        return self.ui.Search_listview.addItem(text)

    def clearlineedit(self):
        self.ui.text_lineEdit.clear()

    # Search Page
    # ...............................................................................
    # ///////////////////////////////////////////////////////////////////////////////
    # Info Page
    # ...............................................................................

    def infopage(self):
        try:
            if (self.gettersymbol() != ""):
                self.showtkinfo()
                self.tickerinfo()
            else:
                self.showtkhome()
        except:
            self.showtkhome()

    def tickerinfo(self):
        self.search = Tickersearch(self.gettersymbol())
        self.settersymbolinfo(self.search.tickerinfo())
        self.infodetail()

    def infodetail(self):
        self.infodict = self.gettersymbolinfo()
        self.ui.symbol_edit.setText(self.infodict['symbol'])
        self.ui.shortName_edit.setText(self.infodict['shortName'])
        self.ui.longName_edit.setText(self.infodict['longName'])
        self.ui.city_edit.setText(self.infodict['city'])
        self.ui.zip_edit.setText(self.infodict['zip'])
        self.ui.country_edit.setText(self.infodict['country'])
        self.ui.phone_edit.setText(self.infodict['phone'])
        self.ui.website_edit.setText(self.infodict['website'])
        self.ui.industry_edit.setText(self.infodict['industry'])
        self.ui.industrydisp_edit.setText(self.infodict['industryDisp'])
        self.ui.sector_edit.setText(self.infodict['sector'])
        self.ui.auditrisk_edit.setText("{}".format(self.infodict['auditRisk']))
        self.ui.boardrisk_edit.setText("{}".format(self.infodict['boardRisk']))
        self.ui.compensationrisk_edit.setText(
            "{}".format(self.infodict['compensationRisk']))
        self.ui.shareholderrightsrisk_edit.setText(
            "{}".format(self.infodict['shareHolderRightsRisk']))
        self.ui.overallrisk_edit.setText(
            "{}".format(self.infodict['overallRisk']))
        self.ui.fulltime_edit.setText(
            "{}".format(self.infodict['fullTimeEmployees']))
        self.ui.address_edit.setText(self.infodict['address1'])
        self.ui.state_edit.setText(self.infodict['state'])
        self.ui.currency_edit.setText(self.infodict['currency'])
        self.ui.enterprisevalue_edit.setText(
            "{}".format(self.infodict['enterpriseValue']))

    # Info Page
    # ...............................................................................
    # ///////////////////////////////////////////////////////////////////////////////
    # History Page
    # ...............................................................................

    def historypage(self):
        try:
            if (self.gettersymbol() != ""):
                self.showhistory()
                self.historydetail()

            else:
                self.showtkhome()
        except:
            self.showtkhome()

    def tickerhistory(self):
        try:
            self.search = Tickersearch(self.gettersymbol())
            self.kwargs = self.historytextmodel()
            self.pdtext = self.search.tickerhisory(self.kwargs)
            self.settersymbolhistory(self.pdtext)
            self.history_tableviewsetup(
                self.history_tableviewmodelsetup(self.gettersymbolhistory(), self.header()))
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def historydownload(self):
        try:
            self.tickerhistorydownload(self.gettersymbolhistory())
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def tickerhistorydownload(self, pdtext):
        try:
            if (pdtext is not None):
                # create and show the file dialog
                self.file_dialog = QFileDialog()
                self.file_path, _ = self.file_dialog.getSaveFileName(
                    filter='CSV files (*.csv);;All files (*.*)')
                # save the DataFrame to the CSV file
                if self.file_path:
                    pdtext.to_csv(self.file_path)
                    QMessageBox.information(
                        None, 'Save Completed', f'The file has been saved to:\n{self.file_path}')

        except:
            print("except ! Please select the option that requires history")
            QMessageBox.warning(None, 'Error Ticker History',
                                'Please select the option that requires history.')

    def historycomboclear(self):
        self.ui.Period_combo.clear()
        self.ui.Interval_combo.clear()

    def historydetail(self):
        self.historycomboclear()
        valid_periods = ['Option', '', '1d', '5d', '1mo',
                         '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.Valid_intervals = ['Option', '', '1m',
                                '30m', '1h', '1d', '5d', '1wk', '1mo']
        self.ui.historysymbol_edit.setText(self.gettersymbol())
        self.ui.Period_combo.addItems(valid_periods)
        self.ui.Interval_combo.addItems(self.Valid_intervals)
        self.ui.start_dateEdit.setDate(QDate.currentDate())
        self.ui.end_dateEdit.setDate(QDate.currentDate())
        self.ui.start_dateEdit.hide()
        self.ui.end_dateEdit.hide()

    def checkintervalis1m(self):
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.interval = self.ui.Interval_combo.currentText()
        if (self.interval == "1m"):
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(['Option', '1d', '5d'])
        elif (self.interval == "30m") or (self.interval == "1h"):
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(
                ['Option', '1d', '5d', '1mo', '3mo'])
        else:
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(self.valid_periods)

    def historytextmodel(self):
        history_params = {}
        interval = self.ui.Interval_combo.currentText()
        if interval not in ['Option', '']:
            history_params['interval'] = interval
        period = self.ui.Period_combo.currentText()
        if period not in ['Option', '']:
            history_params['period'] = period
        start = self.ui.start_dateEdit.text()
        if not self.ui.start_dateEdit.isHidden():
            history_params['start'] = start
        end = self.ui.end_dateEdit.text()
        if not self.ui.end_dateEdit.isHidden():
            history_params['end'] = end
        return history_params

    def Period_combo_box_changed(self):
        if self.ui.Period_combo.currentText() == '':
            self.ui.start_dateEdit.setEnabled(True)
            self.ui.end_dateEdit.setEnabled(True)
            self.ui.start_dateEdit.show()
            self.ui.end_dateEdit.show()
        else:
            self.ui.start_dateEdit.setEnabled(False)
            self.ui.end_dateEdit.setEnabled(False)
            self.ui.start_dateEdit.hide()
            self.ui.end_dateEdit.hide()

    def history_tableviewmodelsetup(self, pd, HeaderLabel):
        df = pd
        self.model = QStandardItemModel(df.shape[0], df.shape[1]+1)
        self.model.setHorizontalHeaderLabels(HeaderLabel)
        for i in range(df.shape[0]):
            # Set index value in the first column
            date = df.index[i].strftime("%Y-%m-%d %H:%M:%S")
            item = QStandardItem(date)
            # item = QStandardItem(str(df.index[i]))
            self.model.setItem(i, 0, item)
            # Set remaining column values 小數點後的2位數
            for j in range(df.shape[1]):
                item = QStandardItem(str("{:.2f}".format(df.iloc[i, j])))
                self.model.setItem(i, j+1, item)
        return self.model

    def header(self):
        header = ["Datetime", "Open", "High", "Low",
                  "Close", "Volume", "Dividends", "Stock Splits"]
        return header

    def history_tableviewsetup(self, model):
        self.ui.history_tableview.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive)
        self.ui.history_tableview.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.history_tableview.verticalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.history_tableview.setStyleSheet(
            "QTableCornerButton::section{background-color: rgb(40, 40, 40);}")
        self.ui.history_tableview.setModel(model)

    def cleartickerhistory(self):
        self.settersymbolhistory(None)
        self.clearhistory_tableview()

    def clearhistory_tableview(self):
        self.model = QStandardItemModel()
        self.model.clear()
        self.model.setHorizontalHeaderLabels([])
        self.ui.history_tableview.setModel(self.model)

    # History Page
    # ...............................................................................
    # ///////////////////////////////////////////////////////////////////////////////
    # New Page
    # ...............................................................................

    def newpage(self):
        try:
            if (self.gettersymbol() != ""):
                self.shownew()
                self.newdetail()
                self.tickernew()
                self.newstableviewsetup(self.newstableviewModelsetup(
                    self.newsheader(), self.newstabledata(self.gettersymbolnews())))

            else:
                self.showtkhome()
        except:
            self.showtkhome()

    def newdetail(self):
        self.ui.newsymbol_edit.setText(self.gettersymbol())

    def tickernew(self):
        try:
            self.search = Tickersearch(self.gettersymbol())
            self.text = self.search.tickernew()
            self.settersymbolnews(self.text)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def newstableviewModelsetup(self, HeaderLabel, data):
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(HeaderLabel)
        for officer in data:
            self.item_publisher = QStandardItem(officer['publisher'])
            self.item_title = QStandardItem(officer['title'])
            self.item_link = QStandardItem(str(officer['link']))
            self.model.appendRow(
                [self.item_publisher, self.item_title,  self.item_link])
        return self.model

    def newstableviewsetup(self, model):
        self.ui.new_tableview.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        self.ui.new_tableview.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.new_tableview.verticalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(40, 40, 40); color: rgb(255, 255, 255);}")
        self.ui.new_tableview.setStyleSheet(
            "QTableCornerButton::section{background-color: rgb(40, 40, 40);}")
        self.ui.new_tableview.setModel(model)

    def newscolumnCount(self):
        return len(self.newstabledata(self.gettersymbolnews()))

    def newsheader(self):
        header = ["Publisher", "Title",  "Link"]
        return header

    def newsheaderRow(self):
        return len(self.newsheader())

    def newstabledata(self, text):
        self.newstext = text
        new_list = [{'publisher': officer.get('publisher'), 'title': officer.get('title'),  'link': officer.get(
            'link')} for officer in self.newstext if 'title' in officer and 'link' in officer]
        return new_list

        """ Need Remake"""

    def handleClicked(self):
        try:
            url = self.ui.new_tableview.currentIndex().data()
            QDesktopServices.openUrl(QUrl(url))
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))
        """ Need Remake"""

    # News Page
    # ...............................................................................
    # ///////////////////////////////////////////////////////////////////////////////
    # Tech Analyis Page
    # ...............................................................................
    def techanalysispage(self):
        try:
            if (self.gettersymbol() != ""):
                self.showtechanalysis()
                self.clear_db_perm()
                self.techanalysispagesetup()
                self.techdetail()

            else:
                self.showtkhome()
        except:
            self.showtkhome()

    def techanalysispagesetup(self):
        self.ui.DownLoad_btn.hide()

    def techcomboclear(self):
        self.ui.techPeriod_combo.clear()
        self.ui.techInterval_combo.clear()

    def techdetail(self):
        self.techcomboclear()
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.Valid_intervals = ['Option', '', '1m',
                                '30m', '1h', '1d', '5d', '1wk', '1mo']
        self.ui.techanalysissymbol_edit.setText(self.gettersymbol())
        self.ui.techPeriod_combo.addItems(self.valid_periods)
        self.ui.techInterval_combo.addItems(self.Valid_intervals)
        self.ui.techstart_dateEdit.setDate(QDate.currentDate())
        self.ui.techend_dateEdit.setDate(QDate.currentDate())
        self.ui.techstart_dateEdit.hide()
        self.ui.techend_dateEdit.hide()

    def techcheckintervalis1m(self):
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.interval = self.ui.techInterval_combo.currentText()
        if (self.interval == "1m"):
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(['Option', '1d', '5d'])
        elif (self.interval == "30m") or (self.interval == "1h"):
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(
                ['Option', '1d', '5d', '1mo', '3mo'])
        else:
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(self.valid_periods)

    def techtextmodel(self):
        self.tech_params = {}
        interval = self.ui.techInterval_combo.currentText()
        if interval not in ['Option', '']:
            self.tech_params['interval'] = interval
        period = self.ui.techPeriod_combo.currentText()
        if period not in ['Option', '']:
            self.tech_params['period'] = period
        start = self.ui.techstart_dateEdit.text()
        if not self.ui.techstart_dateEdit.isHidden():
            self.tech_params['start'] = start
        end = self.ui.techend_dateEdit.text()
        if not self.ui.techend_dateEdit.isHidden():
            self.tech_params['end'] = end
        return self.tech_params

    def techPeriod_combo_box_changed(self):
        if self.ui.techPeriod_combo.currentText() == '':
            self.ui.techstart_dateEdit.setEnabled(True)
            self.ui.techend_dateEdit.setEnabled(True)
            self.ui.techstart_dateEdit.show()
            self.ui.techend_dateEdit.show()
        else:
            self.ui.techstart_dateEdit.setEnabled(False)
            self.ui.techend_dateEdit.setEnabled(False)
            self.ui.techstart_dateEdit.hide()
            self.ui.techend_dateEdit.hide()

    def techanalysistoolpage(self):
        self.uishow = TechAnalysispage()
        self.uishow.show()

    def toolhistorytextmodel(self):
        history_params = {}
        interval = self.ui.techInterval_combo.currentText()
        if interval not in ['Option', '']:
            history_params['interval'] = interval
        period = self.ui.techPeriod_combo.currentText()
        if period not in ['Option', '']:
            history_params['period'] = period
        start = self.ui.techstart_dateEdit.text()
        if not self.ui.techstart_dateEdit.isHidden():
            history_params['start'] = start
        end = self.ui.techend_dateEdit.text()
        if not self.ui.techend_dateEdit.isHidden():
            history_params['end'] = end
        return history_params

    def techanalysisenterdetail(self):
        try:
            if (self.techanalysisenter() == True):
                self.ui.DownLoad_btn.show()
            else:
                self.ui.DownLoad_btn.hide()
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def techanalysisenterdownloadcsv(self):
        try:
            self.tickerhistorydownload(self.gettertoolhistory())
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def techanalysisenterdownload(self, pdtext):
        try:
            if (pdtext is not None):
                # create and show the file dialog
                self.file_dialog = QFileDialog()
                self.file_path, _ = self.file_dialog.getSaveFileName(
                    filter='CSV files (*.csv);;All files (*.*)')
                # save the DataFrame to the CSV file
                if self.file_path:
                    pdtext.to_csv(self.file_path)
                    QMessageBox.information(
                        None, 'Save Completed', f'The file has been saved to:\n{self.file_path}')

        except:
            print("except ! Please select the option that requires history")
            QMessageBox.warning(None, 'Error Ticker History',
                                'Please select the option that requires history.')

    def techanalysisenter(self):
        if (self.clearLayout(self.ui.CanvasLayout) == True):
            self.search = Tickersearch(self.gettersymbol())
            self.kwargs = self.toolhistorytextmodel()
            self.pdtext = self.search.tickerhisory(self.kwargs)
            self.settertoolhistory(self.pdtext)
            self.calculateinter()
            self.drawPhoto()
            return True

    def drawPhoto(self):
        try:
            self.canvas = talib_list()
            self.canvas.matplotlib_main()
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def calculateinter(self):
        try:
            self.paramlist = self.getterTechValue()
            self.paramlistkey = list(self.paramlist.keys())
            for param in self.paramlistkey:
                self.pa = talib_list()
                self.pa.calculatereturn(param)
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        return True

    # Tech Analyis Page
    # ...............................................................................
    # ///////////////////////////////////////////////////////////////////////////////
    # Tech Auto Analyis Page
    # ...............................................................................
    def aatechanalysispage(self):
        try:
            if (self.gettersymbol() != ""):
                self.showaatechanalysis()
                self.clear_db_perm()
                self.aa_techanalysispagesetup()
                self.aatechdetail()

            else:
                self.showtkhome()
        except:
            self.showtkhome()

    def aatechcomboclear(self):
        self.ui.aa_techPeriod_combo.clear()
        self.ui.aa_techInterval_combo.clear()

    def aatechdetail(self):
        self.aatechcomboclear()
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.Valid_intervals = ['Option', '', '1m',
                                '30m', '1h', '1d', '5d', '1wk', '1mo']
        self.ui.aa_techanalysissymbol_edit.setText(self.gettersymbol())
        self.ui.aa_techPeriod_combo.addItems(self.valid_periods)
        self.ui.aa_techInterval_combo.addItems(self.Valid_intervals)
        self.ui.aa_techstart_dateEdit.setDate(QDate.currentDate())
        self.ui.aa_techend_dateEdit.setDate(QDate.currentDate())
        self.ui.aa_techstart_dateEdit.hide()
        self.ui.aa_techend_dateEdit.hide()

    def aatechcheckintervalis1m(self):
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.interval = self.ui.aa_techInterval_combo.currentText()
        if (self.interval == "1m"):
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(['Option', '1d', '5d'])
        elif (self.interval == "30m") or (self.interval == "1h"):
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(
                ['Option', '1d', '5d', '1mo', '3mo'])
        else:
            self.ui.aa_techPeriod_combo.clear()
            self.ui.aa_techPeriod_combo.addItems(self.valid_periods)

    def aatechPeriod_combo_box_changed(self):
        if self.ui.aa_techPeriod_combo.currentText() == '':
            self.ui.aa_techstart_dateEdit.setEnabled(True)
            self.ui.aa_techend_dateEdit.setEnabled(True)
            self.ui.aa_techstart_dateEdit.show()
            self.ui.aa_techend_dateEdit.show()
        else:
            self.ui.aa_techstart_dateEdit.setEnabled(False)
            self.ui.aa_techend_dateEdit.setEnabled(False)
            self.ui.aa_techstart_dateEdit.hide()
            self.ui.aa_techend_dateEdit.hide()

    def aatoolhistorytextmodel(self):
        history_params = {}
        interval = self.ui.aa_techInterval_combo.currentText()
        if interval not in ['Option', '']:
            history_params['interval'] = interval
        period = self.ui.aa_techPeriod_combo.currentText()
        if period not in ['Option', '']:
            history_params['period'] = period
        start = self.ui.aa_techstart_dateEdit.text()
        if not self.ui.aa_techstart_dateEdit.isHidden():
            history_params['start'] = start
        end = self.ui.aa_techend_dateEdit.text()
        if not self.ui.aa_techend_dateEdit.isHidden():
            history_params['end'] = end
        return history_params

    def _from_ticker(self):
        try:
            type = self.getterModeParamlValue()
            if (type == "From_Signals()"):
                self.calculateinter()
                cerebrosetup()
            return True
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))
            print(str(msg))
            return False

    def aatechanalysisenterdetail(self):
        try:
            if (self.aatechanalysisenter() == True):
                if (self._from_ticker() == True):
                    self.ui.aa_DownLoad_btn.show()
                else:
                    self.ui.aa_DownLoad_btn.hide()
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

    def aatechanalysisenter(self):
        self.search = Tickersearch(self.gettersymbol())
        self.kwargs = self.aatoolhistorytextmodel()
        self.pdtext = self.search.tickerhisory(self.kwargs)
        self.settertoolhistory(self.pdtext)
        return True

    def aa_techanalysispagesetup(self):
        self.ui.aa_DownLoad_btn.hide()

    def aatechanalysistoolpage(self):
        self.uishow = TechAnalysispage()
        self.uishow.show()

    def aamoneymanagepage(self):
        self.uishow = Moneymanagepage()
        self.uishow.show()

    def aaentrymanagepage(self):
        self.uishow = Entrymanagepage()
        self.uishow.show()

    def OptimizationIndicatorToolspage(self):
        self.uishow = OptimizationIndicatorTool()
        self.uishow.show()

    def Optentrymanagepage(self):
        self.uishow = optEntrymanagepage()
        self.uishow.show()

    # Tech Auto Analyis Page
    # ...............................................................................
    # EA Tech Auto Analyis Page

    def eatechanalysispage(self):
        try:
            if (self.gettersymbol() != ""):
                self.showeatechanalysis()
                self.clear_db_perm()
                self.ea_techanalysispagesetup()
                self.eatechdetail()

            else:
                self.showtkhome()
        except:
            self.showtkhome()

    def eatechcomboclear(self):
        self.ui.ea_techPeriod_combo.clear()
        self.ui.ea_techInterval_combo.clear()

    def eatechdetail(self):
        self.eatechcomboclear()
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.Valid_intervals = ['Option', '', '1m',
                                '30m', '1h', '1d', '5d', '1wk', '1mo']
        self.ui.ea_techanalysissymbol_edit.setText(self.gettersymbol())
        self.ui.ea_techPeriod_combo.addItems(self.valid_periods)
        self.ui.ea_techInterval_combo.addItems(self.Valid_intervals)
        self.ui.ea_techstart_dateEdit.setDate(QDate.currentDate())
        self.ui.ea_techend_dateEdit.setDate(QDate.currentDate())
        self.ui.ea_techstart_dateEdit.hide()
        self.ui.ea_techend_dateEdit.hide()

    def eatechcheckintervalis1m(self):
        self.valid_periods = ['Option', '', '1d', '5d', '1mo',
                              '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        self.interval = self.ui.ea_techInterval_combo.currentText()
        if (self.interval == "1m"):
            self.ui.ea_techPeriod_combo.clear()
            self.ui.ea_techPeriod_combo.addItems(['Option', '1d', '5d'])
        elif (self.interval == "30m") or (self.interval == "1h"):
            self.ui.ea_techPeriod_combo.clear()
            self.ui.ea_techPeriod_combo.addItems(
                ['Option', '1d', '5d', '1mo', '3mo'])
        else:
            self.ui.ea_techPeriod_combo.clear()
            self.ui.ea_techPeriod_combo.addItems(self.valid_periods)

    def eatechPeriod_combo_box_changed(self):
        if self.ui.ea_techPeriod_combo.currentText() == '':
            self.ui.ea_techstart_dateEdit.setEnabled(True)
            self.ui.ea_techend_dateEdit.setEnabled(True)
            self.ui.ea_techstart_dateEdit.show()
            self.ui.ea_techend_dateEdit.show()
        else:
            self.ui.ea_techstart_dateEdit.setEnabled(False)
            self.ui.ea_techend_dateEdit.setEnabled(False)
            self.ui.ea_techstart_dateEdit.hide()
            self.ui.ea_techend_dateEdit.hide()

    def ea_techanalysispagesetup(self):
        self.ui.ea_DownLoad_btn.hide()

    def eatoolhistorytextmodel(self):
        history_params = {}
        interval = self.ui.ea_techInterval_combo.currentText()
        if interval not in ['Option', '']:
            history_params['interval'] = interval
        period = self.ui.ea_techPeriod_combo.currentText()
        if period not in ['Option', '']:
            history_params['period'] = period
        start = self.ui.ea_techstart_dateEdit.text()
        if not self.ui.ea_techstart_dateEdit.isHidden():
            history_params['start'] = start
        end = self.ui.ea_techend_dateEdit.text()
        if not self.ui.ea_techend_dateEdit.isHidden():
            history_params['end'] = end
        return history_params

    def eatechanalysisenter(self):
        self.search = Tickersearch(self.gettersymbol())
        self.kwargs = self.eatoolhistorytextmodel()
        self.pdtext = self.search.tickerhisory(self.kwargs)
        self.settertoolhistory(self.pdtext)
        return True

    def eatechanalysisenterdetail(self):
        try:
            if (self.eatechanalysisenter() == True):
                pass
        except BaseException as msg:
            QMessageBox.warning(None, 'System Error',
                                'System Error !' + str(msg))

#####################
    def settersymbol(self, text):
        GlobalValue.set_Symbol_static_var(text)

    def gettersymbol(self):
        return GlobalValue.get_Symbol_static_var()

#####################
    def settersymbolhistory(self, text):
        GlobalValue.set_Symbol_history_var(text)

    def gettersymbolhistory(self):
        return GlobalValue.get_Symbol_history_var()
#####################

    def settersymbolinfo(self, text):
        GlobalValue.set_Symbol_info_var(text)

    def gettersymbolinfo(self):
        return GlobalValue.get_Symbol_info_var()
####################

    def settertoolhistory(self, text):
        GlobalValue.set_TechTool_history_var(text)

    def gettertoolhistory(self):
        return GlobalValue.get_TechTool_history_var()
####################

    def setterModelValue(self, text):
        MoneyValue.set_model_perm_var(text)

    def getterModelValue(self):
        return MoneyValue.get_model_perm_var()
####################

    def setterModeParamlValue(self, text):
        MoneyValue.set_model_name_var(text)

    def getterModeParamlValue(self):
        return MoneyValue.get_model_name_var()
#####################

    def setterEntryTechValue(self, text):
        TechValue.set_tech_Entry_var(text)

    def getterEntryTechValue(self):
        return TechValue.get_tech_Entry_var()

####################
    def getterTechValue(self):
        return TechValue.get_tech_toolperm_var()

    def setterTechValue(self, text):
        TechValue.set_tech_toolperm_var(text)

####################
    def settersymbolnews(self, text):
        GlobalValue.set_Symbol_new_var(text)

    def gettersymbolnews(self):
        return GlobalValue.get_Symbol_new_var()
####################

    def setterEntryRangeTechValue(self, text):
        TechValue.set_tech_range_perm(text)

    def getterEntryRangeTechValue(self):
        return TechValue.get_tech_range_perm()
##########################

    def setterEntryRangeValue(self, text):
        TechValue.set_entry_range_perm(text)

    def getterEntryRangeValue(self):
        return TechValue.get_entry_range_perm()
###########################
    def clear_db_perm(self):
        self.setterEntryRangeValue({})
        self.setterEntryRangeTechValue({})
        self.setterEntryTechValue({})
        self.setterTechValue({})
        self.setterModeParamlValue(None)
        self.setterModelValue({})
        print(f"Reset Perm Value")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
