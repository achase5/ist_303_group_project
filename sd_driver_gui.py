import os.path
import pickle
import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QButtonGroup, QCheckBox, QSlider, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMenuBar, qApp, QLineEdit, QTextEdit)
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from sd_gui_contents import *



class MenuBar(QMainWindow):

	def __init__(self):

		super().__init__()

		self.main_widget = Window()
		self.setCentralWidget(self.main_widget)

		self.init_ui()

	def init_ui(self):

		bar = self.menuBar()
		app_menu_btn1 = bar.addMenu('Handle Applications')
		app_menu_btn2 = bar.addMenu('Update Applications')
		app_menu_btn3 = bar.addMenu('Check-In Camper')
		app_menu_btn4 = bar.addMenu('Maintenance')
		app_menu_btn5 = bar.addMenu('Claremont Has Talent')

		new_action = QAction('New Application', self)
		new_action.setShortcut('Ctrl+N')
		app_menu_btn1.addAction(new_action)
		new_action.triggered.connect(self.create_new_app)

		search_action = QAction("Search Applicant", self)
		search_action.setShortcut('Ctrl+S')
		app_menu_btn1.addAction(search_action)
		search_action.triggered.connect(self.search_app)

		payment_action = QAction('Process Payment', self)
		payment_action.setShortcut('Ctrl+P')
		app_menu_btn2.addAction(payment_action)
		payment_action.triggered.connect(self.pay_app)

		decision_action = QAction('Make Decision', self)
		decision_action.setShortcut('Ctrl+D')
		app_menu_btn2.addAction(decision_action)
		decision_action.triggered.connect(self.make_decision_app)

		offical_check_in_action = QAction('Official Check-In', self)
		offical_check_in_action.setShortcut('Ctrl+O')
		app_menu_btn3.addAction(offical_check_in_action)
		offical_check_in_action.triggered.connect(self.check_in_app)

		check_in_search_action = QAction('Search Camper', self)
		check_in_search_action.setShortcut('Ctrl+X')
		app_menu_btn3.addAction(check_in_search_action)
		check_in_search_action.triggered.connect(self.check_in_search_app)

		emergency_form_action = QAction('Emergency Form', self)
		app_menu_btn3.addAction(emergency_form_action)
		emergency_form_action.triggered.connect(self.emerg_form_app)

		medical_form_action = QAction('Medical Form', self)
		app_menu_btn3.addAction(medical_form_action)
		medical_form_action.triggered.connect(self.med_form_app)

		legal_form_action = QAction('Legal Form', self)
		app_menu_btn3.addAction(legal_form_action)
		legal_form_action.triggered.connect(self.legal_form_app)

		maintenance_action = QAction('Enter Maintenance Mode', self)
		maintenance_action.setShortcut('Ctrl+M')
		app_menu_btn4.addAction(maintenance_action)
		maintenance_action.triggered.connect(self.maintenance_app)

		talent_show_action = QAction('Top Campers', self)
		app_menu_btn5.addAction(talent_show_action)
		talent_show_action.triggered.connect(self.talent_app)

		band_ranking_action = QAction('Band Rankings', self)
		app_menu_btn5.addAction(band_ranking_action)
		band_ranking_action.triggered.connect(self.band_rank_app)		


		oImage = QImage("concert-png.jpg")
		sImage = oImage.scaled(QtCore.QSize(1000,700))                   
		palette = QPalette()
		palette.setBrush(10, QBrush(sImage))                     
		self.setPalette(palette)

		self.setWindowTitle("FRoST Registration System")
		self.resize(800, 495)

		self.show()


	def create_new_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 400, 150)
		self.main_widget.new_app_ui()

	def search_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.search_app_ui()

	def pay_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.process_payment_ui()

	def make_decision_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.make_decision_ui()

	def emerg_form_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.emergency_form_ui()

	def med_form_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.medical_form_ui()

	def legal_form_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.legal_form_ui()

	def check_in_search_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.check_in_search_ui()

	def check_in_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.check_in_ui()

	def maintenance_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.maintenance_mode_ui()

	def talent_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.talent_show_ui()

	def band_rank_app(self):
		self.setPalette(self.style().standardPalette())
		self.setGeometry(100, 100, 900, 150)
		self.main_widget.band_ranking_ui()



	


# Run the Application..
app = QApplication(sys.argv)
window = MenuBar()
sys.exit(app.exec_())