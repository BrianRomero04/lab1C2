import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class VentanaClave(QWidget):
    def __init__(self):
        super().__init__()

        # Creamos una etiqueta que pide al usuario que ingrese su clave
        self.label_clave = QLabel('Ingrese su clave secreta:')

        # Creamos un campo de texto para que el usuario escriba su clave
        # Usamos setEchoMode para que no se vean los caracteres al escribir
        self.input_clave = QLineEdit()
        self.input_clave.setEchoMode(QLineEdit.Password)  # Así los caracteres aparecen ocultos

        # Creamos un botón que, al hacer clic, va a ejecutar la función para procesar la clave
        self.boton_enviar = QPushButton('mostrar clave')
        self.boton_enviar.clicked.connect(self.mostrarcla)

        # Creamos una etiqueta vacía donde después mostraremos un mensaje
        self.resultado_clave = QLabel('')

        # Ahora organizamos los widgets (la etiqueta, el campo de texto, el botón y el mensaje) en un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_clave)
        layout.addWidget(self.input_clave)
        layout.addWidget(self.boton_enviar)
        layout.addWidget(self.resultado_clave)

        # Aplicamos este layout a la ventana
        self.setLayout(layout)

        # Configuramos la ventana, su título y su tamaño
        self.setWindowTitle('Ingreso de Clave Secreta')
        self.setGeometry(100, 100, 300, 200)

    # Esta función se ejecuta cuando el botón de "Enviar" es presionado
    def mostrarcla(self):
        # Obtenemos la clave que el usuario escribió
        clave = self.input_clave.text()

        # Mostramos un mensaje que confirma que la clave se ingresó, sin mostrarla directamente por seguridad
        self.resultado_clave.setText(f'Clave ingresada correctamente.')

# Esta es la parte principal del programa, donde se ejecuta la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaClave()
    ventana.show()
    sys.exit(app.exec_())
