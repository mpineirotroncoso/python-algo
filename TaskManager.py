from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QGridLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton,
    QLineEdit, QTextEdit, QGroupBox, QComboBox, QCheckBox
)
import sys

class TaskManager(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.setWindowTitle("Gestor de Tareas")
        self.setGeometry(100, 100, 1000, 600)

        # Crear un widget central para la ventana principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Crear el layout principal
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Parte superior: barra de búsqueda
        self.search_bar = self.create_search_bar()
        main_layout.addWidget(self.search_bar)

        # Parte central: tabla de tareas y detalles
        central_area = QHBoxLayout()

        # Tabla de tareas
        self.task_table = self.create_task_table()
        central_area.addWidget(self.task_table)

        # Detalles de tarea
        self.task_details = self.create_task_details()
        central_area.addWidget(self.task_details)

        main_layout.addLayout(central_area)

        # Parte inferior: botones de acciones
        self.action_buttons = self.create_action_buttons()
        main_layout.addWidget(self.action_buttons)

    def create_search_bar(self):
        # Crear un grupo con un layout horizontal para la barra de búsqueda
        group = QGroupBox("Buscar Tareas")
        layout = QHBoxLayout()

        # Elementos de la barra de búsqueda
        layout.addWidget(QLabel("Buscar:"))
        search_input = QLineEdit()
        layout.addWidget(search_input)
        search_button = QPushButton("Buscar")
        layout.addWidget(search_button)

        group.setLayout(layout)
        return group

    def create_task_table(self):
        # Crear una tabla para listar tareas
        table = QTableWidget()

        # Configurar la tabla (5 filas, 4 columnas)
        table.setRowCount(5)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["ID", "Título", "Estado", "Prioridad"])

        # Añadir datos de ejemplo
        data = [
            [1, "Comprar alimentos", "Pendiente", "Alta"],
            [2, "Preparar reunión", "En progreso", "Media"],
            [3, "Enviar correos", "Completada", "Baja"],
            [4, "Revisar proyecto", "Pendiente", "Alta"],
            [5, "Llamar al cliente", "Pendiente", "Media"],
        ]
        for row, task in enumerate(data):
            for col, value in enumerate(task):
                table.setItem(row, col, QTableWidgetItem(str(value)))

        return table

    def create_task_details(self):
        # Crear un grupo con un layout vertical para detalles de tarea
        group = QGroupBox("Detalles de la Tarea")
        layout = QVBoxLayout()

        # Campos para mostrar detalles de la tarea
        layout.addWidget(QLabel("Título:"))
        title_input = QLineEdit()
        layout.addWidget(title_input)

        layout.addWidget(QLabel("Descripción:"))
        description_input = QTextEdit()
        layout.addWidget(description_input)

        layout.addWidget(QLabel("Estado:"))
        status_combo = QComboBox()
        status_combo.addItems(["Pendiente", "En progreso", "Completada"])
        layout.addWidget(status_combo)

        layout.addWidget(QLabel("Prioridad:"))
        priority_combo = QComboBox()
        priority_combo.addItems(["Alta", "Media", "Baja"])
        layout.addWidget(priority_combo)

        save_button = QPushButton("Guardar Cambios")
        layout.addWidget(save_button)

        group.setLayout(layout)
        return group

    def create_action_buttons(self):
        # Crear un grupo con un layout horizontal para botones de acciones
        group = QGroupBox("Acciones")
        layout = QHBoxLayout()

        # Botones para acciones generales
        add_task_button = QPushButton("Añadir Tarea")
        edit_task_button = QPushButton("Editar Tarea")
        delete_task_button = QPushButton("Eliminar Tarea")
        mark_complete_button = QPushButton("Marcar como Completada")

        # Añadir botones al layout
        layout.addWidget(add_task_button)
        layout.addWidget(edit_task_button)
        layout.addWidget(delete_task_button)
        layout.addWidget(mark_complete_button)

        group.setLayout(layout)
        return group

if __name__ == "__main__":
    # Crear la aplicación y la ventana principal
    app = QApplication(sys.argv)
    window = TaskManager()
    window.show()

    # Ejecutar el bucle principal de la aplicación
    sys.exit(app.exec())
