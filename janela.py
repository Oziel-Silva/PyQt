''' Esse progama faz parte dos estudos de PyQt'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.topo = 100
        self.esquerda = 250
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv)

j = Janela()
sys.exit(aplicacao.exec_())