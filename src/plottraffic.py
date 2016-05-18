# coding: utf-8

import pyqtgraph as pg
from singleton import Singleton
from PyQt4.QtGui import QImage

@Singleton
class Plotter:
    def __init__(self):
        self._backgroundImage = "../roadlanes.png"
        self._roadLength = 5e4
        self._roadWidth = self._roadLength  * 663./1657
	self._laneWidth = self._roadWidth / 4.
        self._trafficManager = None
        self._pw = pg.plot(pen='y', symbol='t', symbolSize=200)
        rawImage = QImage("../roadlanes.png")
        rawImage = rawImage.convertToFormat(QImage.Format_ARGB32_Premultiplied)
        imgArray = pg.imageToArray(rawImage, copy=True)
        self._backgroundImage = pg.ImageItem(imgArray)

        
    def initPlot(self, trafficManager ):
        self._trafficManager = trafficManager
        self._roadLength = self._trafficManager.roadLength
        self._roadWidth = self._roadLength  * 663./1657
	self._laneWidth = self._roadWidth / 4.
        self._pw.setXRange(0, self._roadLength)
        self._pw.setYRange(0, self._roadWidth)
        self._pw.addItem(self._backgroundImage)
        self._backgroundImage.setZValue(-100)  # make sure image is behind other data
        self._backgroundImage.setRect(pg.QtCore.QRectF(0, 0, self._roadLength, self._roadWidth))
        
    def updatePlot(self):

        # Lists for positions of cars
        x=[]
        y=[]
        for car in Plotter.instance()._trafficManager.cars:
            print car.getPosition()
            x.append(car.getPosition())
            y.append(self._laneWidth - (self._laneWidth/2.))
            
        self._pw.plot(x, y, clear=True, pen=None, symbol='t', symbolSize=20)
        self._pw.addItem(self._backgroundImage)
        self._backgroundImage.setZValue(-100)  # make sure image is behind other data
        self._backgroundImage.setRect(pg.QtCore.QRectF(0, 0, self._roadLength, self._roadWidth))
        pg.QtGui.QApplication.processEvents()










