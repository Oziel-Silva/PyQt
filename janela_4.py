''' Esse progama faz parte dos estudos de PyQt'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__ (self):
        super().__init__()

        dimensao = (98, 98) #dimensao altura e largura dos botoes.
        self.topo = 100
        self.esquerda = 250
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(20, 25)
        self.caixa_texto.resize(250,40)

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

        #botao de acionar caixa de texto
        botao3 = QPushButton('enviar texto', self)
        botao3.move(550, 250)
        botao3.resize(dimensao[0], dimensao[1])
        botao3.setStyleSheet('QPushButton {background-color:#1b369;font:bold;font-size:}')
        botao3.clicked.connect(self.mostra_texto)


        self.label_1 = QLabel(self)
        self.label_1.setText('Ola Mundo!!')
        self.label_1.setStyleSheet('QLabel {font-size:30px;color:"blue"}')
        #label_1.setGeometry(150, 150, 150 ,150)
        self.label_1.resize(350,40)
        self.label_1.move(100, 70)

        self.wpp = QLabel(self)
        self.wpp.move(50, 400)
        #self.wpp.setPixmap(QtGui.QPixmap('wpp.png'))


        self.caixa = QLabel(self)
        self.caixa.setText('Digitou: ')
        self.caixa.setStyleSheet('QLabel {font-size:30px;color:"blue"}')
        #label_1.setGeometry(150, 150, 150 ,150)
        self.caixa.resize(350,40)
        self.caixa.move(300, 70)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('o botao 1 foi clicado!!')
        self.label_1.setText('Botao 1')
        self.wpp.setPixmap(QtGui.QPixmap('wpp.png'))
    
    def botao2_click(self):
        print('o botao 2 foi clicado!!')
        self.label_1.setText('Botao 2')
        self.wpp.setPixmap(QtGui.QPixmap('insta.png'))

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.caixa.setText(conteudo)


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())