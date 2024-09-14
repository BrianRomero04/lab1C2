import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout

# Este programa es una calculadora de descuentos para productos.
# Permite seleccionar una categoría de producto y la cantidad comprada.
# Calcula el descuento basado en la categoría y muestra el precio final.

class CalculadoraDescuento(QWidget):
    def __init__(self):
        super().__init__()

        # Aquí se crea una etiqueta para mostrar los resultados del cálculo
        self.resultado = QLabel('')

        # Aquí se crea un combobox para que el usuario seleccione la categoría del producto
        self.combobox_categoria = QComboBox()
        # Se añaden las opciones de categorías al combobox
        self.combobox_categoria.addItems(['Seleccionar categoría', 'Electrónica', 'Ropa', 'Alimentos'])

        # Aquí se crea un spinbox para que el usuario ingrese la cantidad de productos
        self.spinbox_cantidad = QSpinBox()
        # Se define el rango de la cantidad de productos, de 1 a 100
        self.spinbox_cantidad.setRange(1, 100)

        # Aquí se crea un botón que, al hacer clic, calculará el descuento
        self.boton_calcular = QPushButton('Calcular Descuento')
        # Se conecta el clic del botón a la función que realiza el cálculo
        self.boton_calcular.clicked.connect(self.calcularDescuento)

        # Aquí se crea un layout vertical y se añaden los widgets
        layout = QVBoxLayout()
        # Se añaden los widgets al layout
        layout.addWidget(QLabel('Seleccione la categoría del producto:'))
        layout.addWidget(self.combobox_categoria)
        layout.addWidget(QLabel('Ingrese la cantidad:'))
        layout.addWidget(self.spinbox_cantidad)
        layout.addWidget(self.boton_calcular)
        layout.addWidget(self.resultado)

        # Se aplica el layout a la ventana
        self.setLayout(layout)

        # Se configura la ventana
        self.setWindowTitle('Calculadora de Descuentos')
        self.setGeometry(100, 100, 350, 250)

    def calcularDescuento(self):
        # Aquí se obtiene la categoría seleccionada por el usuario
        categoria = self.combobox_categoria.currentText()
        # Si no se selecciona una categoría, se muestra un mensaje de error
        if categoria == 'Seleccionar categoría':
            self.resultado.setText('Por favor, seleccione una categoría.')
            return
        
        # Aquí se obtiene la cantidad de productos ingresada
        cantidad = self.spinbox_cantidad.value()

        # Se definen los descuentos para cada categoría
        descuentos = {
            'Electrónica': 0.10,  # 10% de descuento
            'Ropa': 0.20,         # 20% de descuento
            'Alimentos': 0.05     # 5% de descuento
        }

        # Aquí se calcula el descuento y el precio final
        descuento = descuentos[categoria]
        precio_original = 10  # Supongamos que el precio original de cada producto es 10
        total_descuento = cantidad * precio_original * descuento
        precio_final = cantidad * precio_original - total_descuento

        # Se muestra el resultado del cálculo en la etiqueta
        self.resultado.setText(f'Categoría: {categoria}\nCantidad: {cantidad}\n'
                               f'Descuento aplicado: {total_descuento:.2f}\n'
                               f'Precio final: {precio_final:.2f}')

# Función principal para ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculadoraDescuento()
    ventana.show()
    sys.exit(app.exec_())
