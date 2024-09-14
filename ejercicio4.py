import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class VentanaMascotas(QWidget):
    def __init__(self):
        super().__init__()

        # Etiquetas y campos para la primera mascota
        self.label_mascota1 = QLabel('Mascota 1 - Ingrese el nombre, edad y tipo de animal:')
        self.input_nombre1 = QLineEdit()  
        self.input_edad1 = QLineEdit()   
        self.input_tipo1 = QLineEdit()    

        # Etiquetas y campos para la segunda mascota
        self.label_mascota2 = QLabel('Mascota 2 - Ingrese el nombre, edad y tipo de animal:')
        self.input_nombre2 = QLineEdit()  
        self.input_edad2 = QLineEdit()    
        self.input_tipo2 = QLineEdit()    

        # Etiquetas y campos para la tercera mascota
        self.label_mascota3 = QLabel('Mascota 3 - Ingrese el nombre, edad y tipo de animal:')
        self.input_nombre3 = QLineEdit()  
        self.input_edad3 = QLineEdit()    
        self.input_tipo3 = QLineEdit()    

        # Botón para enviar los datos
        self.boton_enviar = QPushButton('Enviar')
        self.boton_enviar.clicked.connect(self.mostrarDatos)

        # Etiquetas para mostrar los resultados
        self.resultado_mascota1 = QLabel('')
        self.resultado_mascota2 = QLabel('')
        self.resultado_mascota3 = QLabel('')

        # Crear el layout y agregar los widgets
        layout = QVBoxLayout()

        # Agregar los campos de la primera mascota
        layout.addWidget(self.label_mascota1)
        layout.addWidget(self.input_nombre1)
        layout.addWidget(self.input_edad1)
        layout.addWidget(self.input_tipo1)

        # Agregar los campos de la segunda mascota
        layout.addWidget(self.label_mascota2)
        layout.addWidget(self.input_nombre2)
        layout.addWidget(self.input_edad2)
        layout.addWidget(self.input_tipo2)

        # Agregar los campos de la tercera mascota
        layout.addWidget(self.label_mascota3)
        layout.addWidget(self.input_nombre3)
        layout.addWidget(self.input_edad3)
        layout.addWidget(self.input_tipo3)

        # Agregar el botón y los resultados
        layout.addWidget(self.boton_enviar)
        layout.addWidget(self.resultado_mascota1)
        layout.addWidget(self.resultado_mascota2)
        layout.addWidget(self.resultado_mascota3)

        # Aplicar el layout a la ventana
        self.setLayout(layout)

        # Configurar la ventana
        self.setWindowTitle('Datos de 3 Mascotas')
        self.setGeometry(100, 100, 400, 400)

    def mostrarDatos(self):
        # Obtener los datos de la primera mascota
        nombre1 = self.input_nombre1.text()
        edad1 = self.input_edad1.text()
        tipo1 = self.input_tipo1.text()

        # Obtener los datos de la segunda mascota
        nombre2 = self.input_nombre2.text()
        edad2 = self.input_edad2.text()
        tipo2 = self.input_tipo2.text()

        # Obtener los datos de la tercera mascota
        nombre3 = self.input_nombre3.text()
        edad3 = self.input_edad3.text()
        tipo3 = self.input_tipo3.text()

        # Mostrar los resultados
        self.resultado_mascota1.setText(f'Mascota 1 - Nombre: {nombre1}, Edad: {edad1}, Tipo: {tipo1}')
        self.resultado_mascota2.setText(f'Mascota 2 - Nombre: {nombre2}, Edad: {edad2}, Tipo: {tipo2}')
        self.resultado_mascota3.setText(f'Mascota 3 - Nombre: {nombre3}, Edad: {edad3}, Tipo: {tipo3}')

# Función principal para ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaMascotas()
    ventana.show()
    sys.exit(app.exec_())


