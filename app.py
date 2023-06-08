from PyQt5 import QtCore ,QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGroupBox
from PyQt5.QtGui import QImage, QPixmap
from data import *

class Window(QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self, application):
        super(Window, self).__init__()
        screen = application.primaryScreen()
        screenWidth = screen.geometry().width()
        screenHeight = screen.geometry().height()
        self.setMinimumWidth(640)
        self.setMinimumHeight(500)
        self.width = int(screenWidth/3)
        self.height = int(screenHeight/3)
        self.setGeometry(int(screenWidth/2-self.width/2),int(screenHeight/2-self.height/2),int(self.width),int(self.height))
        self.setWindowTitle("Porównywarka Cen - Paulina Formas")
        self.resized.connect(self.updateSize)
        self.initUI()
    
    def initUI(self):
        #przycisk wyszukiwania
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setText("Wyszukaj")
        self.searchButton.clicked.connect(self.search)
        #okienko dialogowe i opis
        self.searchItemLabel = QtWidgets.QLabel(self)
        self.searchItemLabel.setText("Podaj nazwe produktu: ")
        self.searchItem = QtWidgets.QLineEdit(self)
        
        self.canvas = QGroupBox(self)
        
        #coco
        self.cocoLabel = QtWidgets.QLabel(self.canvas)
        self.cocoLabel.setText("Cocolita")

        self.cocoPrice = QtWidgets.QLabel(self.canvas)
        self.cocoPrice.setText("cena coco")

        self.cocoItem = QtWidgets.QLabel(self.canvas)

        self.cocoImage = QImage()
        self.cocoImage_Label = QtWidgets.QLabel(self.canvas)


        #minti
        self.mintiLabel = QtWidgets.QLabel(self.canvas)
        self.mintiLabel.setText("Minti Shop")

        self.mintiPrice = QtWidgets.QLabel(self.canvas)
        self.mintiPrice.setText("cena minti")

        self.mintiItem = QtWidgets.QLabel(self.canvas)

        self.mintiImage = QImage()
        self.mintiImage_Label = QtWidgets.QLabel(self.canvas)


        #makeup
        self.makeupLabel = QtWidgets.QLabel(self.canvas)
        self.makeupLabel.setText("Makeup")

        self.makeupPrice = QtWidgets.QLabel(self.canvas)
        self.makeupPrice.setText("cena makeup")

        self.makeupItem = QtWidgets.QLabel(self.canvas)

        self.makeupImage = QImage()
        self.makeupImage_Label = QtWidgets.QLabel(self.canvas)


        
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)
    def updateSize(self):
        self.width = self.geometry().width()
        self.height = self.geometry().height()
        self.canvas.setGeometry(50,100,int(self.width * 0.8), int(self.height* 0.7))
        canvasW = self.canvas.geometry().width()
        canvasH = self.canvas.geometry().width()

        self.searchButton.setGeometry(self.width- 130,40,90,40)
        self.searchItemLabel.setGeometry(50,20,200,20)
        self.searchItem.setGeometry(50,40,200,20)
        
        

        self.cocoLabel.setGeometry(50,10,50,20)
        self.mintiLabel.setGeometry(200,10,50,20)
        self.makeupLabel.setGeometry(350,10,50,20)
        
        self.cocoPrice.setGeometry(50,300,50,20)
        self.mintiPrice.setGeometry(200,300,50,20)
        self.makeupPrice.setGeometry(350,300,50,20)

        self.cocoItem.setGeometry(15,215,125,70)
        self.mintiItem.setGeometry(150,215,125,70)
        self.makeupItem.setGeometry(275,215,125,70)

        self.cocoImage_Label.setGeometry(15,30,125,175)
        self.cocoImage_Label.setScaledContents(True)
        
        self.mintiImage_Label.setGeometry(165,30,125,175)
        self.mintiImage_Label.setScaledContents(True)

        self.makeupImage_Label.setGeometry(305,30,125,175)
        #self.makeupImage_Label.setScaledContents(True)

    def search(self):
        query = self.searchItem.text()
        
        #coco
        coco_item, coco_price, coco_image = getCoco(query)
        self.cocoPrice.setText(coco_price)
        self.cocoPrice.adjustSize()

        self.cocoItem.setWordWrap(True)
        self.cocoItem.setText(coco_item)
    
        self.cocoImage.loadFromData(coco_image)
        self.cocoImage_Label.setPixmap(QPixmap(self.cocoImage))

        #minti
        minti_item, minti_price, minti_image = getMinti(query)
        self.mintiPrice.setText(minti_price)
        self.mintiPrice.adjustSize()

        self.mintiItem.setWordWrap(True)
        self.mintiItem.setText(minti_item)
    
        self.mintiImage.loadFromData(minti_image)
        self.mintiImage_Label.setPixmap(QPixmap(self.mintiImage))

        #makeup
        makeup_item, makeup_price, makeup_image = getMakeup(query)
        self.makeupPrice.setText(makeup_price)
        self.makeupPrice.adjustSize()

        self.makeupItem.setWordWrap(True)
        self.makeupItem.setText(makeup_item)
    
        self.makeupImage.loadFromData(makeup_image)
        self.makeupImage_Label.setPixmap(QPixmap(self.makeupImage))
        print("click")
    

    
