
# Guía General de Componentes y Funcionalidades de PyQt6

Esta guía proporciona una introducción general a los componentes más utilizados en PyQt6. Incluye ejemplos prácticos y explicaciones sobre layouts, botones, tablas, comboboxes y otros elementos básicos para desarrollar interfaces gráficas.

---

## **1. Layouts en PyQt6**

Los layouts controlan cómo se organizan los widgets dentro de una ventana.

### **1.1 QVBoxLayout**
Organiza los widgets en una columna vertical.

```python
layout = QVBoxLayout()
layout.addWidget(QPushButton("Botón 1"))
layout.addWidget(QPushButton("Botón 2"))
```

### **1.2 QHBoxLayout**
Organiza los widgets en una fila horizontal.

```python
layout = QHBoxLayout()
layout.addWidget(QPushButton("Botón 1"))
layout.addWidget(QPushButton("Botón 2"))
```

### **1.3 QGridLayout**
Organiza los widgets en una cuadrícula (similar a una tabla).

```python
layout = QGridLayout()
layout.addWidget(QPushButton("Botón 1"), 0, 0)
layout.addWidget(QPushButton("Botón 2"), 0, 1)
layout.addWidget(QPushButton("Botón 3"), 1, 0, 1, 2)  # Ocupa 2 columnas
```

### **1.4 QStackedLayout**
Permite apilar varios widgets y mostrar uno a la vez.

```python
layout = QStackedLayout()
layout.addWidget(QLabel("Vista 1"))
layout.addWidget(QLabel("Vista 2"))
layout.setCurrentIndex(0)  # Mostrar la primera vista
```

---

## **2. Botones y Eventos**

### **2.1 Botones básicos**
El `QPushButton` se utiliza para crear botones y conectar eventos.

```python
button = QPushButton("Hacer algo")
button.clicked.connect(lambda: print("¡Botón clicado!"))
```

### **2.2 Checkbox**
El `QCheckBox` permite opciones de activación/desactivación.

```python
checkbox = QCheckBox("Activar opción")
checkbox.stateChanged.connect(lambda state: print(f"Estado: {state}"))
```

### **2.3 Radio Buttons**
Los `QRadioButton` permiten seleccionar una opción dentro de un grupo.

```python
radio1 = QRadioButton("Opción 1")
radio2 = QRadioButton("Opción 2")
radio1.toggled.connect(lambda checked: print(f"Opción 1: {checked}"))
```

---

## **3. Entradas de Texto**

### **3.1 QLineEdit**
Crea una entrada de texto para datos cortos.

```python
line_edit = QLineEdit()
line_edit.setPlaceholderText("Introduce tu texto aquí")
line_edit.textChanged.connect(lambda text: print(f"Texto: {text}"))
```

### **3.2 QTextEdit**
Crea un editor de texto multilínea.

```python
text_edit = QTextEdit()
text_edit.setPlainText("Texto inicial")
```

---

## **4. Combobox (Lista Desplegable)**

El `QComboBox` muestra una lista de opciones desplegables.

```python
combo_box = QComboBox()
combo_box.addItems(["Opción 1", "Opción 2", "Opción 3"])
combo_box.currentTextChanged.connect(lambda text: print(f"Seleccionado: {text}"))
```

---

## **5. Tablas (QTableWidget)**

El `QTableWidget` se utiliza para mostrar datos en formato tabular.

```python
table = QTableWidget()
table.setRowCount(3)
table.setColumnCount(3)
table.setHorizontalHeaderLabels(["Columna 1", "Columna 2", "Columna 3"])

# Insertar datos
table.setItem(0, 0, QTableWidgetItem("Dato 1"))
table.setItem(0, 1, QTableWidgetItem("Dato 2"))
table.setItem(0, 2, QTableWidgetItem("Dato 3"))
```

---

## **6. Diálogos y Ventanas Emergentes**

### **6.1 QMessageBox**
Crea un cuadro de diálogo para mostrar mensajes.

```python
msg = QMessageBox()
msg.setText("Este es un mensaje.")
msg.exec()
```

### **6.2 QFileDialog**
Abre un cuadro de diálogo para seleccionar archivos.

```python
file_dialog = QFileDialog()
file_path = file_dialog.getOpenFileName()[0]
print(f"Archivo seleccionado: {file_path}")
```

---

## **7. Eventos Personalizados**

Puedes conectar eventos a cualquier widget utilizando `signal` y `slot`.

```python
button = QPushButton("Clic aquí")
button.clicked.connect(lambda: print("Botón presionado"))
```

---

## **8. Ejemplo Completo**

Aquí tienes un ejemplo que combina varios componentes:

```python
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem, QComboBox
)
import sys

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo Completo")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Tabla
        self.table = QTableWidget(3, 3)
        self.table.setHorizontalHeaderLabels(["Columna 1", "Columna 2", "Columna 3"])
        layout.addWidget(self.table)

        # Entrada de texto
        self.input = QLineEdit()
        self.input.setPlaceholderText("Introduce algo")
        layout.addWidget(self.input)

        # Botón para añadir a la tabla
        add_button = QPushButton("Añadir a la tabla")
        add_button.clicked.connect(self.add_to_table)
        layout.addWidget(add_button)

        # ComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Item 1", "Item 2", "Item 3"])
        layout.addWidget(self.combo_box)

    def add_to_table(self):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.input.text()))
        self.input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
```

---

## **Conclusión**
Esta guía cubre los aspectos básicos de PyQt6, como layouts, botones, entradas de texto, tablas y eventos. Con estos componentes, puedes construir aplicaciones gráficas interactivas y funcionales.

Ver más: [Guía avanzada](guia_avanzada.md)