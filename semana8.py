import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

# la clase principal
class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Simple")

        # Entradas
        self.num1 = QLineEdit()
        self.num2 = QLineEdit()

        # resultado
        self.lbl_resultado = QLabel("Resultado: ---")

        # Botones
        botones = QHBoxLayout()
        for simbolo, operacion in {"+": self.sumar, "-": self.restar, "×": self.multiplicar, "÷": self.dividir}.items():
            btn = QPushButton(simbolo)
            btn.clicked.connect(operacion)
            botones.addWidget(btn)

# interfaz
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Número 1:"))
        layout.addWidget(self.num1)
        layout.addWidget(QLabel("Número 2:"))
        layout.addWidget(self.num2)
        layout.addLayout(botones)
        layout.addWidget(self.lbl_resultado)

        self.setLayout(layout)

# aqui se obtienen los numeros
    def obtener_valores(self):
        try:
            return float(self.num1.text()), float(self.num2.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")
            return None, None
        
# sumar
    def sumar(self): 
        n1, n2 = self.obtener_valores()
        if n1 is not None: self.lbl_resultado.setText(f"Resultado: {n1 + n2}")

# restar
    def restar(self): 
        n1, n2 = self.obtener_valores()
        if n1 is not None: self.lbl_resultado.setText(f"Resultado: {n1 - n2}")

# multiplicar
    def multiplicar(self): 
        n1, n2 = self.obtener_valores()
        if n1 is not None: self.lbl_resultado.setText(f"Resultado: {n1 * n2}")

# dividir
    def dividir(self): 
        n1, n2 = self.obtener_valores()
        if n1 is not None:
            if n2 == 0:
                QMessageBox.critical(self, "Error", "No se puede dividir entre 0")
            else:
                self.lbl_resultado.setText(f"Resultado: {n1 / n2}")


# aqui se ejecuta la calculadora
app = QApplication(sys.argv)
ventana = Calculadora()
ventana.show()
sys.exit(app.exec_())
