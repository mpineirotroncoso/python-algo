# Guía Avanzada de Configuración de Widgets y Ventanas en PyQt6

Parámetros avanzados para personalizar widgets y ventanas en PyQt6, incluyendo cómo modificar colores, fuentes, tamaños y propiedades específicas de la ventana principal.

---

## **1. Configuración de la Ventana Principal**

### **1.1 Tamaño y Posición**
Puedes configurar el tamaño inicial, la posición y las restricciones de una ventana.

```python
# Tamaño inicial de la ventana
self.setGeometry(100, 100, 800, 600)  # x, y, ancho, alto

# Establecer un tamaño fijo (deshabilita redimensionar)
self.setFixedSize(800, 600)

# Restringir el tamaño máximo y mínimo
self.setMinimumSize(400, 300)
self.setMaximumSize(1200, 800)
```
### 1.2 Títulos y Iconos
```python
self.setWindowTitle("Mi Aplicación Avanzada")

# Establecer un ícono para la ventana
from PyQt6.QtGui import QIcon
self.setWindowIcon(QIcon("ruta/a/icono.png"))
```
### 1.3 Comportamiento de Redimensionamiento
Puedes deshabilitar la capacidad de maximizar, minimizar o redimensionar:

```python
self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.MSWindowsFixedSizeDialogHint)
```
## 2. Personalización de Widgets
### 2.1 Cambiar Colores
Usando estilosheets (setStyleSheet), puedes modificar colores de fondo, texto, bordes, etc.

**Botón Personalizado**
```python
button = QPushButton("Botón Personalizado")
button.setStyleSheet("""
    QPushButton {
        background-color: #4CAF50;  /* Fondo verde */
        color: white;              /* Texto blanco */
        border-radius: 8px;        /* Bordes redondeados */
        padding: 10px;             /* Espaciado interno */
    }
    QPushButton:hover {
        background-color: #45a049; /* Cambiar color al pasar el ratón */
    }
""")
```
**Tabla (QTableWidget)**

Puedes personalizar las celdas, encabezados y líneas:

```python
table.setStyleSheet("""
    QTableWidget::item {
        border: 1px solid #d3d3d3;
        padding: 5px;
    }
    QHeaderView::section {
        background-color: #f0f0f0;  /* Fondo de los encabezados */
        font-weight: bold;          /* Texto en negrita */
    }
""")
```
### 2.2 Modificar Fuente

```python
from PyQt6.QtGui import QFont

# Cambiar la fuente de un widget
label = QLabel("Texto con Fuente Personalizada")
label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
```
### 2.3 Tamaño de Widgets
Puedes controlar el tamaño mínimo, máximo y preferido de cualquier widget.

```python
widget.setMinimumSize(100, 50)  # Tamaño mínimo (ancho x alto)
widget.setMaximumSize(300, 100)  # Tamaño máximo
widget.setFixedSize(200, 75)  # Tamaño fijo
```

### 2.4 Placeholder y Tooltip
Algunos widgets permiten placeholders (texto de guía) y tooltips (información adicional al pasar el ratón).

```python
line_edit = QLineEdit()
line_edit.setPlaceholderText("Introduce tu nombre aquí")  # Placeholder
line_edit.setToolTip("Este campo es obligatorio")         # Tooltip
```
## 3. Propiedades de Interactividad
### 3.1 Habilitar o Deshabilitar Widgets

```python
button.setEnabled(False)  # Deshabilitar el botón
button.setEnabled(True)   # Habilitar el botón
```
### 3.2 Mostrar u Ocultar Widgets
```python
widget.hide()  # Ocultar
widget.show()  # Mostrar
```
### 3.3 Configuración de Focus
Controla qué widget recibe el foco cuando se inicia la ventana.

```python
widget.setFocus()  # Asignar foco inicial
widget.setFocusPolicy(Qt.FocusPolicy.ClickFocus)  # Sólo obtiene foco con clics
```
## 4. Layouts Avanzados
### 4.1 Espaciado y Márgenes
Puedes ajustar el espaciado interno entre widgets y márgenes del layout.

```python
layout = QVBoxLayout()
layout.setSpacing(20)  # Espaciado entre widgets
layout.setContentsMargins(10, 15, 10, 15)  # Márgenes (izq, arriba, der, abajo)
```
### 4.2 Expansión de Widgets
Controla cómo los widgets ocupan espacio dentro del layout.

```python
layout.addWidget(widget, stretch=1)  # Mayor "stretch" significa más espacio ocupado
```
5. Eventos Especiales
5.1 Reacciones al Movimiento del Ratón
Puedes capturar eventos personalizados, como el movimiento del ratón sobre widgets.

```python
def enterEvent(self, event):
    print("El ratón ha entrado en el área del widget")
```
## 6. Ejemplo Completo
Este ejemplo combina varias personalizaciones avanzadas.

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class AdvancedWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Avanzada")
        self.setGeometry(200, 200, 600, 400)
        self.setFixedSize(600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Etiqueta personalizada
        label = QLabel("Texto con fuente y color personalizados")
        label.setFont(QFont("Times New Roman", 18, QFont.Weight.Bold))
        label.setStyleSheet("color: #333399;")  # Azul oscuro
        layout.addWidget(label)

        # Botón personalizado
        button = QPushButton("Clic aquí")
        button.setStyleSheet("""
            QPushButton {
                background-color: #ffcccb;
                color: black;
                border: 2px solid #ff9999;
            }
            QPushButton:hover {
                background-color: #ff9999;
            }
        """)
        button.clicked.connect(lambda: print("Botón presionado"))
        layout.addWidget(button)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AdvancedWindow()
    window.show()
    sys.exit(app.exec())
```
# Conclusión
PyQt6 permite una personalización avanzada para crear interfaces visualmente atractivas y funcionales. Usando estilosheets, configuraciones de tamaño, y propiedades de foco e interacción, puedes adaptar los widgets y ventanas a cualquier necesidad.