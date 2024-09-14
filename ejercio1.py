import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

# Definimos la clase Ventana que hereda de QWidget
class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        # Creamos una etiqueta (QLabel) para el nombre y un campo de texto (QLineEdit) para ingresar el nombre
        self.label_nombre = QLabel('Ingrese su nombre completo:')
        self.input_nombre = QLineEdit()

        self.label_edad = QLabel('Ingrese su edad:')
        self.input_edad = QLineEdit()

        # Creamos un botón que al hacer clic ejecutará la función mostrarInfo
        self.boton_mostrar = QPushButton('Mostrar Info')
        self.boton_mostrar.clicked.connect(self.mostrarInfo)

        # Creamos dos etiquetas vacías donde se mostrarán el nombre y la edad ingresados
        # Centramos el texto usando setAlignment
        self.resultado_nombre = QLabel('')
        self.resultado_edad = QLabel('')
        self.resultado_nombre.setAlignment(Qt.AlignCenter)
        self.resultado_edad.setAlignment(Qt.AlignCenter)

        # Configuramos el layout vertical (QVBoxLayout) y agregamos los widgets en orden
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_edad)
        layout.addWidget(self.input_edad)
        layout.addWidget(self.boton_mostrar)
        layout.addWidget(self.resultado_nombre)
        layout.addWidget(self.resultado_edad)

        # Asignamos el layout a la ventana
        self.setLayout(layout)

        # Definimos las propiedades básicas de la ventana, como título y tamaño inicial
        self.setWindowTitle('Información Personal')
        self.setGeometry(100, 100, 300, 250)
        # Función que se ejecuta al presionar el botón
    def mostrarInfo(self):
        # Obtenemos los textos ingresados en los campos de nombre y edad
        nombre = self.input_nombre.text()
        edad = self.input_edad.text()

        # Actualizamos las etiquetas para mostrar el nombre y la edad
        self.resultado_nombre.setText(f'Nombre: {nombre}')
        self.resultado_edad.setText(f'Edad: {edad}')

# Bloque principal para ejecutar la aplicación
if __name__ == '__main__':
    # Creamos una instancia de la aplicación
    app = QApplication(sys.argv)
    # Creamos la ventana y la mostramos
    ventana = Ventana()
    ventana.show()
    # Iniciamos el loop de eventos de la aplicación
    sys.exit(app.exec_())
