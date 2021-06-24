''' Esse progama faz parte dos estudos de PyQt'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

class Janela(QMainWindow):
    def __init__ (self):
        super().__init__()

        dimensao = (98, 98) #dimensao altura e largura dos botoes.
        self.topo = 100
        self.esquerda = 250
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        botao1 = QPushButton('Botao 1', self)
        botao1.move(250, 250)
        botao1.resize(dimensao[0], dimensao[1])
        botao1.setStyleSheet('QPushButton {background-color:#0fb328}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botao 2', self)
        botao2.move(450, 250)
        botao2.resize(dimensao[0], dimensao[1])
        botao2.setStyleSheet('QPushButton {background-color:#0fa322;font:bold;font-size:}')
        botao2.clicked.connect(self.botao2_click)

        self.label_1 = QLabel(self)
        self.label_1.setText('Ola Mundo!!')
        self.label_1.setStyleSheet('QLabel {font-size:30px;color:"blue"}')
        #label_1.setGeometry(150, 150, 150 ,150)
        self.label_1.resize(350,30)
        self.label_1.move(100, 70)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('o botao 1 foi clicado!!')
        self.label_1.setText('O botao 1 mudou a label')
    
    def botao2_click(self):
        print('o botao 2 foi clicado!!')
        self.label_1.setText('O botao 2 mudou a label')



aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())