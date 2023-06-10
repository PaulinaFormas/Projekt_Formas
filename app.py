from PyQt5 import QtCore ,QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QGroupBox
from PyQt5.QtGui import QImage, QPixmap

from data import *
import webbrowser

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
    
        self.searchCanvas = QGroupBox(self)
        self.searchCanvasLayout = QtWidgets.QHBoxLayout()
        self.searchCanvas.setLayout(self.searchCanvasLayout)
        self.searchCanvasLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        #przycisk wyszukiwania
        self.searchButton = QtWidgets.QPushButton(self)
        self.searchButton.setText("Wyszukaj")
        self.searchButton.clicked.connect(self.search)
        self.searchCanvasLayout.addWidget(self.searchButton)

        
        
        #search
        
        self.inputCanvas = QGroupBox(self.searchCanvas)
        self.inputCanvasLayout = QtWidgets.QVBoxLayout()
        self.inputCanvas.setLayout(self.inputCanvasLayout)

        self.searchItemLabel = QtWidgets.QLabel(self.inputCanvas)
        self.searchItemLabel.setText("Podaj nazwe produktu: ")
        self.searchItem = QtWidgets.QLineEdit(self.inputCanvas)
        self.inputCanvasLayout.addWidget(self.searchItemLabel)
        self.inputCanvasLayout.addWidget(self.searchItem)
        self.searchCanvasLayout.addWidget(self.inputCanvas)

        self.searchProgress = QtWidgets.QProgressBar(self.searchCanvas)
        self.searchProgress.setValue(0)
        self.inputCanvasLayout.addWidget(self.searchProgress)

        #okna sklepow

        self.itemCanvas = QGroupBox(self)
        self.itemCanvasLayout =QtWidgets.QHBoxLayout()
        self.itemCanvas.setLayout(self.itemCanvasLayout)

        self.cocoLayout = QtWidgets.QVBoxLayout()
        self.mintiLayout = QtWidgets.QVBoxLayout()
        self.makeupLayout = QtWidgets.QVBoxLayout()

        self.cocoLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter )
        self.mintiLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter )
        self.makeupLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter )

        self.cocoCanvas = QGroupBox(self.itemCanvas)
        self.cocoCanvas.setLayout(self.cocoLayout)
        
        self.mintiCanvas = QGroupBox(self.itemCanvas)
        self.mintiCanvas.setLayout(self.mintiLayout)
        
        self.makeupCanvas = QGroupBox(self.itemCanvas)
        self.makeupCanvas.setLayout(self.makeupLayout)

        self.itemCanvasLayout.addWidget(self.makeupCanvas)
        self.itemCanvasLayout.addWidget(self.mintiCanvas)
        self.itemCanvasLayout.addWidget(self.cocoCanvas)
        
        #coco
        self.cocoLabel = QtWidgets.QLabel(self.cocoCanvas)
        self.cocoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.cocoLayout.addWidget(self.cocoLabel)
        self.cocoLabel.setText("Cocolita")

        self.cocoPrice = QtWidgets.QLabel(self.cocoCanvas)
        self.cocoPrice.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.cocoLayout.addWidget(self.cocoPrice)
        self.cocoPrice.setEnabled(False)

        self.cocoItem = QtWidgets.QLabel(self.cocoCanvas)
        self.cocoItem.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.cocoLayout.addWidget(self.cocoItem)

        self.cocoImage = QImage()
        self.cocoImage_Label = QtWidgets.QLabel(self.cocoCanvas)
        self.cocoImage_Label.setScaledContents(True)
        self.cocoLayout.addWidget(self.cocoImage_Label)

        self.cocoPageButton = QtWidgets.QPushButton(self.cocoCanvas)
        self.cocoLayout.addWidget(self.cocoPageButton)
        self.cocoPageButton.setText("Przejdź do strony")
        self.cocoPageButton.clicked.connect(self.cocoClicked)
        self.cocoPageButton.setEnabled(False)


        #minti
        self.mintiLabel = QtWidgets.QLabel(self.mintiCanvas)
        self.mintiLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mintiLayout.addWidget(self.mintiLabel)
        self.mintiLabel.setText("Minti Shop")

        self.mintiPrice = QtWidgets.QLabel(self.mintiCanvas)
        self.mintiPrice.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mintiLayout.addWidget(self.mintiPrice)
        self.mintiPrice.setEnabled(False)

        self.mintiItem = QtWidgets.QLabel(self.mintiCanvas)
        self.mintiItem.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mintiLayout.addWidget(self.mintiItem)

        self.mintiImage = QImage()
        self.mintiImage_Label = QtWidgets.QLabel(self.mintiCanvas)
        self.mintiImage_Label.setScaledContents(True)
        self.mintiLayout.addWidget(self.mintiImage_Label)

        self.mintiPageButton = QtWidgets.QPushButton(self.mintiCanvas)
        self.mintiLayout.addWidget(self.mintiPageButton)
        self.mintiPageButton.setText("Przejdź do strony")
        self.mintiPageButton.clicked.connect(self.mintiClicked)
        self.mintiPageButton.setEnabled(False)


        #makeup
        self.makeupLabel = QtWidgets.QLabel(self.makeupCanvas)
        self.makeupLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.makeupLabel.setText("Makeup")
        self.makeupLayout.addWidget(self.makeupLabel)

        self.makeupPrice = QtWidgets.QLabel(self.makeupCanvas)
        self.makeupPrice.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.makeupLayout.addWidget(self.makeupPrice)
        self.makeupPrice.setEnabled(False)

        self.makeupItem = QtWidgets.QLabel(self.makeupCanvas)
        self.makeupItem.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.makeupLayout.addWidget(self.makeupItem)

        self.makeupImage = QImage()
        self.makeupImage_Label = QtWidgets.QLabel(self.makeupCanvas)
        self.makeupImage_Label.setScaledContents(True)
        self.makeupLayout.addWidget(self.makeupImage_Label)

        self.makeupPageButton = QtWidgets.QPushButton(self.makeupCanvas)
        self.makeupLayout.addWidget(self.makeupPageButton)
        self.makeupPageButton.setText("Przejdź do strony")
        self.makeupPageButton.clicked.connect(self.makeupClicked)
        self.makeupPageButton.setEnabled(False)



        
    def resizeEvent(self, event):
        self.resized.emit()
        return super(Window, self).resizeEvent(event)
    def updateSize(self):
        self.width = self.geometry().width()
        self.height = self.geometry().height()
        self.searchCanvas.setGeometry(10,10,self.width-10,int(self.height*0.2))
        self.itemCanvas.setGeometry(10,int(self.height*0.2+10),self.width - 10, int(self.height-(self.height* 0.2) -10))

    def search(self):
        query = self.searchItem.text()
        if query.__len__() == 0:
            return
        self.searchButton.setText("Szukanie...")
        self.searchButton.setEnabled(False)
        self.searchProgress.setValue(10)
        
        shrugPic = QtGui.QPixmap("shrug.jpg")
        #coco
        self.coco = getCoco(query)
        if self.coco == None:
            self.cocoPrice.setText("--.--zł")
            self.cocoItem.setText("Nie znaleziono")
            self.cocoImage_Label.setPixmap(shrugPic)
            self.cocoPageButton.setEnabled(False)
        else:
            self.cocoPrice.setText(self.coco["price"])
        
            self.cocoItem.setText(self.coco["item"])

            self.cocoImage.loadFromData(self.coco["image"])
            self.cocoImage_Label.setPixmap(QPixmap(self.cocoImage))
        self.cocoPrice.setEnabled(True)
        self.cocoItem.setWordWrap(True)
        self.cocoPageButton.setEnabled(True)
        self.searchProgress.setValue(40)
        #minti
        self.minti = getMinti(query)
        if self.minti == None:
            self.mintiPrice.setText("--.--zł")
            self.mintiItem.setText("Nie znaleziono")
            self.mintiImage_Label.setPixmap(shrugPic)
            self.mintiPageButton.setEnabled(False)
        else :
            self.mintiPrice.setText(self.minti["price"])
    
            self.mintiItem.setText(self.minti["item"])        

            self.mintiImage.loadFromData(self.minti["image"])
            self.mintiImage_Label.setPixmap(QPixmap(self.mintiImage))

        self.mintiPageButton.setEnabled(True)
        self.mintiPrice.setEnabled(True)
        self.mintiItem.setWordWrap(True)
        self.searchProgress.setValue(70)
        #makeup
        self.makeup = getMakeup(query)
        if self.makeup == None:
            self.makeupPrice.setText("--.--zł")
            self.makeupItem.setText("Nie znaleziono")
            self.makeupImage_Label.setPixmap(shrugPic)
            self.makeupPageButton.setEnabled(False)
        else :
            self.makeupPrice.setText(self.makeup["price"])
            
            self.makeupItem.setText(self.makeup["item"])

            self.makeupImage.loadFromData(self.makeup["image"])
            self.makeupImage_Label.setPixmap(QPixmap(self.makeupImage))

        self.makeupPageButton.setEnabled(True)
        self.makeupItem.setWordWrap(True)
        self.makeupPrice.setEnabled(True)
        self.searchButton.setText("Wyszukaj")
        self.searchButton.setEnabled(True)
        self.searchProgress.setValue(100)
    
    def cocoClicked(self):
        try:
            url = self.coco["url"]
            webbrowser.open(f"https://www.cocolita.pl{url}")
        except:
            return
    def mintiClicked(self):
        try:
            url = self.minti["url"]
            webbrowser.open(f"https://mintishop.pl{url}")
        except:
            return
    def makeupClicked(self):
        try:
            url = self.makeup["url"]
            webbrowser.open(f"https://makeup.pl{url}")
        except:
            return

    
