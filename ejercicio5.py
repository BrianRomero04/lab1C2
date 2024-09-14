import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class VentanaDatosPersonales(QWidget):
    def __init__(self):
        super().__init__()

        # Etiquetas y campos para los datos personales
        self.label_nombre = QLabel('Nombre:')
        self.input_nombre = QLineEdit()

        self.label_edad = QLabel('Edad:')
        self.input_edad = QLineEdit()

        self.label_direccion = QLabel('Dirección:')
        self.input_direccion = QLineEdit()

        self.label_telefono = QLabel('Teléfono:')
        self.input_telefono = QLineEdit()

        self.label_email = QLabel('Email:')
        self.input_email = QLineEdit()

        self.label_ciudad = QLabel('Ciudad:')
        self.input_ciudad = QLineEdit()

        self.label_departamento = QLabel('Departamento:')
        self.input_departamento = QLineEdit()

        self.label_pais = QLabel('País:')
        self.input_pais = QLineEdit()

        self.label_Ecivil = QLabel('Estado civil:')
        self.input_Ecivil = QLineEdit()

        self.label_fecha_nacimiento = QLabel('Fecha de Nacimiento:')
        self.input_fecha_nacimiento = QLineEdit()

        # Botón para enviar los datos
        self.boton_enviar = QPushButton('Enviar')
        self.boton_enviar.clicked.connect(self.mostrarDatos)

        # Etiquetas para mostrar los resultados
        self.resultado = QLabel('')

        # Crear el layout y agregar los widgets
        layout = QVBoxLayout()

        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)

        layout.addWidget(self.label_edad)
        layout.addWidget(self.input_edad)

        layout.addWidget(self.label_direccion)
        layout.addWidget(self.input_direccion)

        layout.addWidget(self.label_telefono)
        layout.addWidget(self.input_telefono)

        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)

        layout.addWidget(self.label_ciudad)
        layout.addWidget(self.input_ciudad)

        layout.addWidget(self.label_departamento)
        layout.addWidget(self.input_departamento)

        layout.addWidget(self.label_pais)
        layout.addWidget(self.input_pais)

        layout.addWidget(self.label_Ecivil)
        layout.addWidget(self.input_Ecivil)

        layout.addWidget(self.label_fecha_nacimiento)
        layout.addWidget(self.input_fecha_nacimiento)

        # Agregar el botón y el resultado
        layout.addWidget(self.boton_enviar)
        layout.addWidget(self.resultado)

        # Aplicar el layout a la ventana
        self.setLayout(layout)

        # Configurar la ventana
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 400, 600)

    def mostrarDatos(self):
        # Obtener los datos ingresados
        nombre = self.input_nombre.text()
        edad = self.input_edad.text()
        direccion = self.input_direccion.text()
        telefono = self.input_telefono.text()
        email = self.input_email.text()
        ciudad = self.input_ciudad.text()
        departamento = self.input_departamento.text()
        pais = self.input_pais.text()
        Ecivil = self.input_Ecivil.text()
        fecha_nacimiento = self.input_fecha_nacimiento.text()

        # Mostrar los resultados
        datos = (f'Nombre: {nombre}\n'
                 f'Edad: {edad}\n'
                 f'Dirección: {direccion}\n'
                 f'Teléfono: {telefono}\n'
                 f'Email: {email}\n'
                 f'Ciudad: {ciudad}\n'
                 f'Departamento: {departamento}\n'
                 f'País: {pais}\n'
                 f'Estado Civil: {Ecivil}\n'
                 f'Fecha de Nacimiento: {fecha_nacimiento}')
        self.resultado.setText(datos)

# Función principal para ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDatosPersonales()
    ventana.show()
    sys.exit(app.exec_())
