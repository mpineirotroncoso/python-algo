import sys
from multiprocessing.resource_tracker import register
from tkinter.constants import CENTER

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton
)
from PyQt6.QtCore import Qt

from Login import Login
from Register import Register


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("Design Preview")
        self.setGeometry(100, 100, 800, 600) # posicion 100,100 y tamaño 800x600

        principal_widget = QWidget() # widget principal donde va a estar todo
        self.setCentralWidget(principal_widget) # mostrar el widget principal

        # establecemos el layout principal
        principal_layout = QVBoxLayout() # layout principal
        principal_widget.setLayout(principal_layout) # el layout principal es vertical

        # botones superiores
        botones_superiores = QHBoxLayout()


        botonsup1 = QPushButton("Data Vault")
        botonsup1.setFixedSize(150, 100)
        botonsup2 = QPushButton("Settings")
        botonsup1.setEnabled(False)
        botonsup2.setFixedSize(150, 100)
        botonsup2.setEnabled(False)
        botonsup3 = QPushButton("Help")
        botonsup3.clicked.connect(self.botonsup3_click)
        botonsup3.setFixedSize(150, 100)
        botonsup4 = QPushButton("Close")
        botonsup4.clicked.connect(self.close)
        botonsup4.setFixedSize(150, 100)

        botones_superiores.addWidget(botonsup1)
        botones_superiores.addWidget(botonsup2)
        botones_superiores.addWidget(botonsup3)
        botones_superiores.addWidget(botonsup4)

        principal_layout.addLayout(botones_superiores)

        titulolyt = QHBoxLayout()
        principal_layout.addLayout(titulolyt)

        titulo = QLabel("SPARTAN PASSWORD PROTECTOR")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont() # fuente para poder cambiarle el tamaaño
        font.setPointSize(20)
        titulo.setFont(font) # asignarle la fuente al titulo
        titulolyt.addWidget(titulo)


        sublayout = QHBoxLayout()
        principal_layout.addLayout(sublayout)

        # Layout de la izquierda
        layout_login_about = QVBoxLayout()
        sublayout.addLayout(layout_login_about)
        login = Login() # hay que inicializar el login
        layout_login_about.addWidget(login.get_frame())

        # Layout de la derecha
        layout_registro_password = QVBoxLayout()
        sublayout.addLayout(layout_registro_password)
        register = Register()
        layout_registro_password.addWidget(register.get_frame())

    def botonsup3_click(self):
        print("help")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())