import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class VentanaDatos(QWidget):
    def __init__(self):
        super().__init__()

        # Etiqueta que pide al usuario que ingrese su nombre completo
        self.label_nombre = QLabel('Ingrese su nombre completo:')
        # Campo de texto donde el usuario escribe su nombre
        self.input_nombre = QLineEdit()

        # Etiqueta que pide al usuario que ingrese su número de cédula
        self.label_cedula = QLabel('Ingrese su número de cédula:')
        # Campo de texto donde el usuario escribe su número de cédula
        self.input_cedula = QLineEdit()

        # Botón para enviar los datos. Al hacer clic, ejecuta la función mostrardatos
        self.boton_enviar = QPushButton('Enviar')
        self.boton_enviar.clicked.connect(self.mostrardatos)

        # Etiquetas vacías que mostrarán los datos ingresados después
        self.resultado_nombre = QLabel('')
        self.resultado_cedula = QLabel('')

        # Organizamos todo en un layout vertical para que se vea bien
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)
        layout.addWidget(self.label_cedula)
        layout.addWidget(self.input_cedula)
        layout.addWidget(self.boton_enviar)
        layout.addWidget(self.resultado_nombre)
        layout.addWidget(self.resultado_cedula)

        # Aplicamos el layout a la ventana
        self.setLayout(layout)

        # Configuramos el título y el tamaño de la ventana
        self.setWindowTitle('Ingreso de Datos Personales')
        self.setGeometry(100, 100, 300, 250)

    def mostrardatos(self):
        # Obtenemos lo que el usuario escribió en los campos de texto
        nombre = self.input_nombre.text()
        cedula = self.input_cedula.text()

        # Mostramos los datos ingresados en las etiquetas
        self.resultado_nombre.setText(f'Nombre: {nombre}')
        self.resultado_cedula.setText(f'Cédula: {cedula}')

# Esta es la parte principal del programa, aquí se ejecuta la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDatos()
    ventana.show()
    sys.exit(app.exec_())
