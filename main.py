from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("Ejemplo de Interfaz con PyQt6")
        self.setGeometry(100, 100, 800, 600)

        # Crear un widget central para la ventana principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crear un layout principal para organizar las 4 partes
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Parte 1: Layout vertical
        self.part1 = self.create_vertical_layout()
        main_layout.addWidget(self.part1)

        # Parte 2: Layout horizontal
        self.part2 = self.create_horizontal_layout()
        main_layout.addWidget(self.part2)

        # Parte 3: Layout de cuadrícula
        self.part3 = self.create_grid_layout()
        main_layout.addWidget(self.part3)

        # Parte 4: Tabla
        self.part4 = self.create_table()
        main_layout.addWidget(self.part4)

    def create_vertical_layout(self):
        # Crear un widget con un layout vertical
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Añadir elementos al layout vertical
        layout.addWidget(QLabel("Parte 1: Layout Vertical"))
        layout.addWidget(QPushButton("Botón 1"))
        layout.addWidget(QPushButton("Botón 2"))
        layout.addWidget(QPushButton("Botón 3"))

        return widget

    def create_horizontal_layout(self):
        # Crear un widget con un layout horizontal
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)

        # Añadir elementos al layout horizontal
        layout.addWidget(QLabel("Parte 2: Layout Horizontal"))
        layout.addWidget(QPushButton("Botón A"))
        layout.addWidget(QPushButton("Botón B"))
        layout.addWidget(QPushButton("Botón C"))

        return widget

    def create_grid_layout(self):
        # Crear un widget con un layout de cuadrícula
        widget = QWidget()
        layout = QGridLayout()
        widget.setLayout(layout)

        # Añadir elementos al layout de cuadrícula
        layout.addWidget(QLabel("Parte 3: Layout de Cuadrícula"), 0, 0, 1, 2)
        layout.addWidget(QPushButton("1, 0"), 1, 0)
        layout.addWidget(QPushButton("1, 1"), 1, 1)
        layout.addWidget(QPushButton("2, 0"), 2, 0)
        layout.addWidget(QPushButton("2, 1"), 2, 1)

        return widget

    def create_table(self):
        # Crear un widget de tabla
        table = QTableWidget()

        # Configurar la tabla (3 filas, 3 columnas)
        table.setRowCount(3)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Columna 1", "Columna 2", "Columna 3"])
        table.setVerticalHeaderLabels(["Fila 1", "Fila 2", "Fila 3"])

        # Rellenar la tabla con algunos datos
        table.setItem(0, 0, QTableWidgetItem("Dato 1"))
        table.setItem(0, 1, QTableWidgetItem("Dato 2"))
        table.setItem(0, 2, QTableWidgetItem("Dato 3"))
        table.setItem(1, 0, QTableWidgetItem("Dato 4"))
        table.setItem(1, 1, QTableWidgetItem("Dato 5"))
        table.setItem(1, 2, QTableWidgetItem("Dato 6"))
        table.setItem(2, 0, QTableWidgetItem("Dato 7"))
        table.setItem(2, 1, QTableWidgetItem("Dato 8"))
        table.setItem(2, 2, QTableWidgetItem("Dato 9"))

        return table


if __name__ == "__main__":
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Ejecutar el bucle principal de la aplicación
    sys.exit(app.exec())
