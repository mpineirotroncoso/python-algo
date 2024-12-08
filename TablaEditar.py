from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QGroupBox, QLabel
)
import sys

class TableEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("Editor de Tabla")
        self.setGeometry(100, 100, 600, 400)

        # Crear el widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Tabla
        self.table = QTableWidget()
        self.table.setColumnCount(3)  # Número de columnas
        self.table.setHorizontalHeaderLabels(["Columna 1", "Columna 2", "Columna 3"])
        main_layout.addWidget(self.table)

        # Área de entrada de datos
        self.input_area = self.create_input_area()
        main_layout.addWidget(self.input_area)

        # Botones de acciones
        self.action_buttons = self.create_action_buttons()
        main_layout.addWidget(self.action_buttons)

    def create_input_area(self):
        # Crear un grupo para la entrada de datos
        group = QGroupBox("Añadir Datos")
        layout = QHBoxLayout()

        # Campos de entrada
        self.input_1 = QLineEdit()
        self.input_1.setPlaceholderText("Dato 1")
        self.input_2 = QLineEdit()
        self.input_2.setPlaceholderText("Dato 2")
        self.input_3 = QLineEdit()
        self.input_3.setPlaceholderText("Dato 3")

        # Añadir campos al layout
        layout.addWidget(QLabel("Columna 1:"))
        layout.addWidget(self.input_1)
        layout.addWidget(QLabel("Columna 2:"))
        layout.addWidget(self.input_2)
        layout.addWidget(QLabel("Columna 3:"))
        layout.addWidget(self.input_3)

        group.setLayout(layout)
        return group

    def create_action_buttons(self):
        # Crear un grupo para los botones de acción
        group = QGroupBox("Acciones")
        layout = QHBoxLayout()

        # Botón para añadir datos
        add_button = QPushButton("Añadir")
        add_button.clicked.connect(self.add_row)  # Conectar con el método para añadir filas
        layout.addWidget(add_button)

        # Botón para eliminar datos
        delete_button = QPushButton("Eliminar")
        delete_button.clicked.connect(self.delete_row)  # Conectar con el método para eliminar filas
        layout.addWidget(delete_button)

        group.setLayout(layout)
        return group

    def add_row(self):
        """Añadir una nueva fila a la tabla con los datos introducidos."""
        # Obtener datos de los campos de entrada
        data1 = self.input_1.text()
        data2 = self.input_2.text()
        data3 = self.input_3.text()

        # Validar que no estén vacíos
        if data1.strip() == "" or data2.strip() == "" or data3.strip() == "":
            return  # No hacer nada si algún campo está vacío

        # Añadir una nueva fila
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)

        # Insertar los datos en la nueva fila
        self.table.setItem(row_count, 0, QTableWidgetItem(data1))
        self.table.setItem(row_count, 1, QTableWidgetItem(data2))
        self.table.setItem(row_count, 2, QTableWidgetItem(data3))

        # Limpiar los campos de entrada
        self.input_1.clear()
        self.input_2.clear()
        self.input_3.clear()

    def delete_row(self):
        """Eliminar la fila seleccionada de la tabla."""
        selected_rows = self.table.selectionModel().selectedRows()  # Obtener filas seleccionadas

        # Eliminar filas seleccionadas en orden inverso para evitar problemas de índice
        for index in sorted(selected_rows, key=lambda x: x.row(), reverse=True):
            self.table.removeRow(index.row())

if __name__ == "__main__":
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    window = TableEditor()
    window.show()

    # Ejecutar el bucle principal de la aplicación
    sys.exit(app.exec())
