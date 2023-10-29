# importing requried libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

# Main class


class Window(QMainWindow):
    # Constructor method
    def __init__(self):
        # inheriting methods and properties from superclass QMaindWindow
        super().__init__()
        # Setting the title
        self.setWindowTitle("Loan Calculator")
        # Setting the geometry of the app
        self.width = 400
        self.height = 500
        self.setGeometry(100, 100, self.width, self.height)
        self.UiComponents()
        # showing the window
        self.show()

    # Function to add widgets
    def UiComponents(self):
        head = QLabel("Loan Calculator \n XYZ Bank", self)
        head.setGeometry(0, 10, 400, 60)
        font = QFont('Times', 15)
        font.setBold(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter)
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkBlue)
        head.setGraphicsEffect(color)

        # Interest Label
        i_label = QLabel("Annual Interest", self)
        # properties
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setGeometry(20, 100, 170, 40)
        i_label.setStyleSheet("QLabel" "{"
                              "border : 2px solid black;"
                              "background: rgba(70, 70, 70, 35);"
                              "}")
        i_label.setFont(QFont('Times', 9))

        # Input field for interest rate (QLineEdit)
        self.rate = QLineEdit(self)
        # Only integers
        onlyInt = QIntValidator()
        self.rate.setValidator(onlyInt)
        # setting properties for input field
        self.rate.setGeometry(200, 100, 180, 40)
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFont(QFont('Times', 9))

        # Number of years
        n_label = QLabel("Years", self)
        # properties
        n_label.setAlignment(Qt.AlignCenter)
        n_label.setGeometry(20, 150, 170, 40)
        n_label.setStyleSheet("QLabel" "{"
                              "border : 2px solid black;"
                              "background: rgba(70, 70, 70, 35);"
                              "}")
        n_label.setFont(QFont('Times', 9))

      # Input field for number of years (QLineEdit)
        self.years = QLineEdit(self)
        # Only integers
        onlyInt = QIntValidator()
        self.years.setValidator(onlyInt)
        # setting properties for input field
        self.years.setGeometry(200, 150, 180, 40)
        self.years.setAlignment(Qt.AlignCenter)
        self.years.setFont(QFont('Times', 9))

      # Create the loan amount label
        a_label = QLabel("Amount", self)
        a_label.setAlignment(Qt.AlignCenter)
        a_label.setGeometry(20, 200, 170, 40)
        a_label.setStyleSheet("QLabel" "{"
                              "border : 2px solid black;"
                              "background: rgba(70, 70, 70, 35);"
                              "}")
        a_label.setFont(QFont('Times', 9))

      # Input field for number of years (QLineEdit)
        self.amount = QLineEdit(self)
        # Only integers
        onlyInt = QIntValidator()
        self.amount.setValidator(onlyInt)
        # setting properties for input field
        self.amount.setGeometry(200, 200, 180, 40)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setFont(QFont('Times', 9))

      # ////////////////////////Compute Payment ///////////////////////////
        # Creating the compute button
        calculate = QPushButton("Compute Payment", self)
        # set geometry
        calculate.setGeometry(125, 270, 150, 40)
        # Add action to the calculate button
        calculate.clicked.connect(self.calculate_action)

        # ////////////////////Output Widgets ///////////////////////////////
        # Monthly payment label
        self.m_payment = QLabel(self)
        self.m_payment.setAlignment(Qt.AlignCenter)
        self.m_payment.setGeometry(50, 340, 300, 60)
        self.m_payment.setStyleSheet("QLabel" "{"
                                     "border : 3px solid black;"
                                     "background: white"
                                     "}")
        self.m_payment.setFont(QFont('Times', 11))

        # Total payment label
        self.t_payment = QLabel(self)
        self.t_payment.setAlignment(Qt.AlignCenter)
        self.t_payment.setGeometry(50, 410, 300, 60)
        self.t_payment.setStyleSheet("QLabel" "{"
                                     "border : 3px solid black;"
                                     "background: white"
                                     "}")
        self.t_payment.setFont(QFont('Times', 11))

    def calculate_action(self):
        # Getting annual interest rate
        annualInterestRate = self.rate.text()
        # To check if fields are empty
        if len(annualInterestRate) == 0 or annualInterestRate == '0':
            # QMessageBox.critical(self, "Alert!", "Fill the blanks!")
            return

        # Getting number of years
        numberOfYears = self.years.text()
        # To check if fields are empty
        if len(numberOfYears) == 0 or numberOfYears == '0':
            # QMessageBox.critical(self, "Alert!", "Fill the blanks!")
            return

        # Getting loan amount
        loanAmount = self.amount.text()
        # To check if fields are empty
        if len(loanAmount) == 0 or loanAmount == '0':
            # QMessageBox.critical(self, "Alert!", "Fill the blanks!")
            return

        # Get Calculations
        # ////////////////
        # Convert text into integer
        annualInterestRate = int(annualInterestRate)
        numberOfYears = int(numberOfYears)
        loanAmount = int(loanAmount)

        # Monthly interest rate calculation [12 X 100%]
        monthlyInterestRate = annualInterestRate / 1200
        #  calculate monthly payment
        monthlyPayment = loanAmount * monthlyInterestRate / \
            (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        # Set the format for monthly payment for 2 decimal points float
        monthlyPayment = "{:.2f}".format(monthlyPayment)
        # Add text to monthly payment calculation
        self.m_payment.setText("Monthly Payment : " + str(monthlyPayment))
        # Getting total payment
        totalPayment = float(monthlyPayment) * 12 * numberOfYears
        totalPayment = "{:.2f}".format(totalPayment)
        # Add text to total payment calculation
        self.t_payment.setText("Total Payment : " + str(totalPayment))


# Create app object
App = QApplication(sys.argv)

# Instantiate Window class
window = Window()

# Start the app
sys.exit(App.exec())