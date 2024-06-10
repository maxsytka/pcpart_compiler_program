from PySide6.QtCore import QSize

from PySide6.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QHeaderView
from PySide6.QtGui import QFont, QIcon, Qt

import pandas as pd
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from designMainWindow import Ui_mainWindow
from itertools import product
import numpy as np
import math
class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.algorithmButton.clicked.connect(self.launch)

        self.second_window = SecondWindow()




    def Saati(self, route, parameters, sortedData):
        numElementsIn1Line = len(sortedData)
        geoMeanSummaryArray = []
        geoMeanMatrix = [[]for _ in range(len(parameters))]
        normalizedGeoMeanMatrix = [[]for _ in range(len(parameters))]
        geoMeanMatrixCycleCount = 0
        for p in parameters:
            calculatingColumn = sortedData[p]
            parametersCombinating = list(product(calculatingColumn, repeat=2))
            resultsMatrix =[]
            temporaryArray = []
            countDivide=1
            for y, x in parametersCombinating:
                divisionNumber = round((x/y),5)
                temporaryArray.append(round(divisionNumber, 5))
                if countDivide==numElementsIn1Line:
                    resultsMatrix.append(temporaryArray)
                    temporaryArray=[]
                    countDivide=0
                countDivide += 1


            geoMeanSummary=0
            for line in resultsMatrix:
                multiplying = np.prod(line)
                geoMean = round(multiplying ** (1 / numElementsIn1Line),5)
                geoMeanSummary+=round(geoMean,5)
                geoMeanMatrix[geoMeanMatrixCycleCount].append(round(geoMean, 5))


            geoMeanMatrixCycleCount += 1
            geoMeanSummaryArray.append(round(geoMeanSummary, 5))
            '''print(resultsMatrix)
            print('//////////////////////////////////////////')
            print('/////{}/////////////////////////////////////'.format(p))
            '''

        for parameterCount in range(len(parameters)):
            for elementCount in range(len(geoMeanMatrix[parameterCount])):
                temporaryNormValue = round(geoMeanMatrix[parameterCount][elementCount]/geoMeanSummaryArray[parameterCount],5)
                normalizedGeoMeanMatrix[parameterCount].append(temporaryNormValue)


        criteriaCombinating = list(product(geoMeanSummaryArray, repeat=2))
        criteriaMatrix = []
        temporaryArray = []
        countDivide = 1
        for y, x in criteriaCombinating:
            divisionNumber = round((x / y),5)
            temporaryArray.append(divisionNumber)
            if countDivide == len(parameters):
                criteriaMatrix.append(temporaryArray)
                temporaryArray = []
                countDivide = 0
            countDivide += 1


        geoMeanCriteriaSummary = 0
        ###############################
        numElementsIn1LineCriteria = len(criteriaMatrix[0])
        #################################
        geoMeanCriteriaArray=[]
        for line in criteriaMatrix:
            multiplying = np.prod(line)
            geoMean = round(multiplying ** (1 / numElementsIn1LineCriteria),5)
            geoMeanCriteriaSummary += geoMean
            geoMeanCriteriaArray.append(geoMean)


        normalizedGeoMeanCriteriaArray=[]
        for value in geoMeanCriteriaArray:
            normalizedGeoMeanCriteriaArray.append(round(value/geoMeanCriteriaSummary, 5))


        globalValuesArray=[]
        for alternativeCount in range(numElementsIn1Line):
            temporaryGlobalValue = 0
            for criteriaCount in range(len(parameters)):
                temporaryGlobalValue += round(normalizedGeoMeanMatrix[criteriaCount][alternativeCount] * normalizedGeoMeanCriteriaArray[criteriaCount], 5)
            globalValuesArray.append(round(temporaryGlobalValue, 5))


        alternativeChoiceIndex = globalValuesArray.index(max(globalValuesArray))
        '''print('##############{}##################'.format(route))
        for line in criteriaMatrix:
            print(line)
        print('********************************')
        for line in normalizedGeoMeanCriteriaArray:
            print(line)
        
        print('//////////////////////////////////////////')
        print('//geoMeanSummaryArray////////////////////////////////////////')
        print(geoMeanSummaryArray)
        print('//////////////////////////////////////////')
        print('//geoMeanMatrix////////////////////////////////////////')
        print(geoMeanMatrix)
        print('//////////////////////////////////////////')
        print('////normalizedGeoMeanMatrix//////////////////////////////////////')
        print(normalizedGeoMeanMatrix)
        print('//////////////////////////////////////////')
        print('//////criteriaMatrix////////////////////////////////////')
        print(criteriaMatrix)
        print('//////////////////////////////////////////')
        print('/////geoMeanCriteriaArray/////////////////////////////////////')
        print(geoMeanCriteriaArray)
        print('//////////////////////////////////////////')
        print('/////normalizedGeoMeanCriteriaArray/////////////////////////////////////')
        print(normalizedGeoMeanCriteriaArray)
        print('//////////////////////////////////////////')
        print('/////globalValuesArray/////////////////////////////////////')
        print(globalValuesArray)
        print('//////////////////////////////////////////')
        print('/////alternativeChoiceIndex/////////////////////////////////////')
        
        print(alternativeChoiceIndex)
        '''
        return (sortedData.iloc[alternativeChoiceIndex])



    def processing(self, endConfig, endPrice):
        file = 'partdb.xlsx'
        # radiobuttons перевірка
        multithreadRadioButtonCheck = self.ui.multithreadRadioButton.isChecked()
        coreRadioButtonCheck = self.ui.coreRadioButton.isChecked()

        # checkbuttons перевірка
        sizeCheckBoxCheck = self.ui.sizeCheckBox.isChecked()
        upsCheckBoxCheck = self.ui.upsCheckBox.isChecked()
        peripheralCheckBoxCheck = self.ui.peripheralCheckBox.isChecked()
        widescreenCheckBoxCheck = self.ui.widescreenCheckBox.isChecked()
        soundcardCheckBoxCheck = self.ui.soundcardCheckBox.isChecked()
        webcamCheckBoxCheck = self.ui.webcamCheckBox.isChecked()
        wirelessCheckBox = self.ui.wirelessCheckBox.isChecked()
        opticCheckBox = self.ui.opticCheckBox.isChecked()
        dataCheckBox = self.ui.dataCheckBox.isChecked()

        # comboboxes перевірка
        companyComboBoxOption = self.ui.companyComboBox.currentText()
        graphicsComboBoxOption = self.ui.graphicsComboBox.currentText()
        matrixComboBoxOption = self.ui.matrixComboBox.currentText()
        soundComboBoxOption = self.ui.soundComboBox.currentText()
        modeComboBoxOption = self.ui.modeComboBox.currentText()

        self.ui.progressBar.setValue(8)
        step=0
        cpuSpecList=[]

        #Багатопотік/ядро
        if multithreadRadioButtonCheck:
            cpuSpecList = ['price','core_count','core_clock','tdp']
        if coreRadioButtonCheck:
            cpuSpecList = ['price', 'boost_clock', 'core_clock', 'tdp']

        #AMD/Intel
        self.companyVariable = None
        selectedCompany = companyComboBoxOption
        if selectedCompany == "Intel":
            self.companyVariable = "Intel"
        elif selectedCompany == "AMD":
            self.companyVariable = "AMD"
        elif selectedCompany == "AMD/Intel":
            self.companyVariable = " "

        #Відеопам'ять
        self.cpuGraphicsVariable= None
        self.systemGraphicCardVariable=None
        selectedSystemGraphicsType = graphicsComboBoxOption
        if selectedSystemGraphicsType == "Графіка інтегрована" :
            self.cpuGraphicsVariable = True
            self.systemGraphicCardVariable = False
        elif selectedSystemGraphicsType == "Графіка дискретна":
            self.cpuGraphicsVariable = False
            self.systemGraphicCardVariable = True
        elif selectedSystemGraphicsType == "Інтегрована + дискретна":
            self.cpuGraphicsVariable = True
            self.systemGraphicCardVariable = True


        #WATTAGE OF SYSTEM
        systemWattage = 0



        #Фільтрування за компанією процесора
        route = "cpu"
        df = pd.read_excel(file, sheet_name=route)
        filteredData1 = df.loc[df['name'].str.contains(self.companyVariable)]
        if self.cpuGraphicsVariable:
            filteredData2 = filteredData1.loc[filteredData1['graphics'].notna()]
        else:
            filteredData2 = filteredData1.loc[filteredData1['graphics'].isna()]

        
        filteredData3 = filteredData2.sort_values(by='price', ascending = True)
        '''
        print(len(filteredData3))
        print(filteredData3)
        '''
        # Режим роботи алгоритму
        selectedMode = modeComboBoxOption
        thirdPartLenght = int(len(filteredData3) * 0.33)
        meanLenght=int(len(filteredData3)/2)

        if selectedMode == "Максимальна економія коштів ":
            filteredData4 = filteredData3.head(min(thirdPartLenght,300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData4 = filteredData3.iloc[max(meanLenght-int(thirdPartLenght/2),meanLenght-150):min(-meanLenght+int(thirdPartLenght/2),-meanLenght+150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData4 = filteredData3.tail(min(thirdPartLenght,300))


        outputCPU=self.Saati(route, cpuSpecList, filteredData4)
        self.ui.progressBar.setValue(17)

        '''
        route = "test"
        params=['Боєзапас', 'Калібр', 'Скорострільність', 'Вага', 'Ціна']
        df = pd.read_excel(file, sheet_name=route)
        filteredData3 = filteredData2.sort_values(by='Ціна', ascending = False)
        print(filteredData3)
        self.Saati(route, params, filteredData3 )
        self.ui.progressBar.setValue(17)
        '''

        pairNamePriceArray = []
        print(outputCPU)
        pairNamePriceArray.append('Процесор')
        pairNamePriceArray.append(outputCPU['name'])
        pairNamePriceArray.append( outputCPU['price'])
        endConfig.append(pairNamePriceArray)
        systemWattage+=outputCPU['tdp']
        '''print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''

        ###################################################
        ###################################################
        ###################################################


        route ='motherboard'
        df = pd.read_excel(file, sheet_name=route)
        filteredData1 = df.loc[df['socket'] == outputCPU['socket']]
        '''print(filteredData1)'''
        if sizeCheckBoxCheck:
            filteredData1 = filteredData1.loc[filteredData1['form_factor'] !='ATX']
            if len(filteredData1) <= 3:
                filteredData1 = df.loc[df['socket'] == outputCPU['socket']]
                msgBox = QMessageBox()
                msgBox.setText("Вибірка із материнських плат лише малих розмірів неможлива, пункт 'Малі розміри ПК' відхилено")
                msgBox.setWindowTitle("Попередження")
                font = QFont("Segoe UI", 10)
                font.setBold(True)
                msgBox.setFont(font)
                msgBox.setStyleSheet("QMessageBox { background-color: rgb(12, 14, 35); }"
                                     "QMessageBox QLabel { color: white; }"
                                     "QPushButton { color: white; background-color: rgb(50, 50, 50); }")
                icon = QIcon()
                icon.addFile(u":/img/C:/Users/mx/Downloads/icon.png", QSize(), QIcon.Normal, QIcon.Off)
                msgBox.setWindowIcon(icon)
                msgBox.exec()

        motherSpecList=['price','max_memory','memory_slots']
        filteredData2 = filteredData1.sort_values(by='price', ascending=True)
        thirdPartLenght = int(len(filteredData2) * 0.33)
        meanLenght = int(len(filteredData2) / 2)
        '''print(meanLenght, thirdPartLenght)
        print(filteredData2)'''

        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[
                            max(meanLenght-1 - int(thirdPartLenght/2), meanLenght - 150):min(meanLenght +1+ int(thirdPartLenght/2),
                             meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

        '''print(meanLenght - int(thirdPartLenght/2), meanLenght - 150)
        print(meanLenght + int(thirdPartLenght/2),
                             meanLenght + 150)'''
        outputMother=self.Saati(route, motherSpecList,filteredData3)
        pairNamePriceArray = []
        print(outputMother)
        pairNamePriceArray.append('Материнська плата')
        pairNamePriceArray.append(outputMother['name'])
        pairNamePriceArray.append(outputMother['price'])

        endConfig.append(pairNamePriceArray)
        systemWattage += 35
        '''print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        self.ui.progressBar.setValue(25)
        ###################################################
        ###################################################
        #максимальні значення
        #ddr2  до 800
        #ddr3 до 2133
        #ddr4 до 5200 не включно

        route = 'memory'
        df = pd.read_excel(file, sheet_name=route)


        if outputCPU['socket'] in ['AM3+','G34','FM2+','LGA1150','LGA1151','LGA1155','LGA1156','LGA1356', 'LGA2011', 'LGA775' ]:
            lowerBound=801
            higherBound=2133
        elif outputCPU['socket'] in ['AM4','LGA1200','LGA2011-3', 'LGA2066', 'TR4', 'TRX4']:
            lowerBound=2133
            higherBound=5199
        elif outputCPU['socket'] in ['LGA1700', 'AM5']:
            lowerBound=5200
            higherBound=6766766766766766

        filteredData1 = df[(df['speed'] >= lowerBound) & (df['speed'] <= higherBound)]


        memorySpecList = ['price', 'speed', 'capacity', 'price_per_gb', 'first_word_latency', 'cas_latency']
        filteredData2 = filteredData1.sort_values(by='price', ascending=True)
        thirdPartLenght = int(len(filteredData2) * 0.33)
        meanLenght = int(len(filteredData2) / 2)

        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[
                            max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                    -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

        outputMemory = self.Saati(route, memorySpecList, filteredData3)
        pairNamePriceArray = []
        print(outputMemory)
        pairNamePriceArray.append("Оперативна пам'ять")
        pairNamePriceArray.append(outputMemory['name'])
        pairNamePriceArray.append(outputMemory['price'])
        endConfig.append(pairNamePriceArray)
        '''print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        systemWattage += 5
        self.ui.progressBar.setValue(33)
        ################################################################
        ################################################################


        route = 'cpu-cooler'
        df = pd.read_excel(file, sheet_name=route)
        if outputCPU['tdp'] <= 90:
            filteredData1 = df.loc[df['size'] == 120]
        else:
            filteredData1 = df.loc[df['size'] > 120]

        cpuCoolSpecList = ['price', 'rpm', 'noise_level', 'size']
        filteredData2 = filteredData1.sort_values(by='price', ascending=True)
        thirdPartLenght = int(len(filteredData2) * 0.33)
        meanLenght = int(len(filteredData2) / 2)

        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[
                            max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght +int(thirdPartLenght/2),
                                                                                    -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

        outputCool = self.Saati(route, cpuCoolSpecList, filteredData3)
        pairNamePriceArray = []
        print(outputCool)
        pairNamePriceArray.append("Охолодження процесору")
        pairNamePriceArray.append(outputCool['name'])
        pairNamePriceArray.append(outputCool['price'])
        endConfig.append(pairNamePriceArray)
        '''print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        systemWattage += 3
        self.ui.progressBar.setValue(41)



        ################################################################
        ################################################################################################

        if self.systemGraphicCardVariable:
            route = 'video-card'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)

            filteredData2 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData3 = filteredData2.iloc[
                                max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

            '''print(len(filteredData3))'''
            gpuSpecList=['price','memory','core_clock','boost_clock','length','tdp']
            outputGPU = self.Saati(route, gpuSpecList, filteredData3)
            pairNamePriceArray = []
            print(outputGPU)
            pairNamePriceArray.append("Відеокарта")
            pairNamePriceArray.append(outputGPU['name'])
            pairNamePriceArray.append(outputGPU['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)
            print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
            systemWattage += outputGPU['tdp']
            self.ui.progressBar.setValue(47)
            ################################################################
            ################################################################


        route = 'case'
        df = pd.read_excel(file, sheet_name=route)
        filteredData1= df.loc[df['type'] == outputMother['form_factor']]
        thirdPartLenght = int(len(filteredData1) * 0.33)
        meanLenght = int(len(filteredData1) / 2)
        filteredData2 = filteredData1.sort_values(by='price', ascending=True)

        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

        caseSpecList = ['price', 'external_volume', 'internal_35_bays']

        outputCase = self.Saati(route, caseSpecList, filteredData3)
        pairNamePriceArray = []
        print(outputCase)
        pairNamePriceArray.append("Корпус")
        pairNamePriceArray.append(outputCase['name'])
        pairNamePriceArray.append(outputCase['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)'''
        self.ui.progressBar.setValue(53)

        ################################################################
        ################################################################


        route = 'case-fan'
        df = pd.read_excel(file, sheet_name=route)
        if (systemWattage>=180) | (outputCPU['tdp']>=105):
            filteredData1 = df.loc[df['size'] > 120]
        else:
            filteredData1 = df.loc[df['size'] <= 120]

        thirdPartLenght = int(len(df) * 0.33)
        meanLenght = int(len(df) / 2)
        filteredData2 = filteredData1.sort_values(by='price', ascending=True)

        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[
                            max(meanLenght -int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                    -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

        caseFanSpecList = ['price', 'size', 'rpm', 'airflow','noise_level']
        outputCaseFan = self.Saati(route, caseFanSpecList, filteredData3)
        pairNamePriceArray = []
        print(outputCaseFan)
        pairNamePriceArray.append("Корпусний кулер")
        pairNamePriceArray.append(outputCaseFan['name'])
        pairNamePriceArray.append(outputCaseFan['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)'''
        self.ui.progressBar.setValue(61)
        ################################################################
        ################################################################

        route = 'monitor'
        df = pd.read_excel(file, sheet_name=route)
        if widescreenCheckBoxCheck:
            filteredData1 = df.loc[df['width'] > 1920]
        else:
            filteredData1 = df.loc[df['width'] <= 1920]

        if matrixComboBoxOption == "Баланс швидкості і якості":
            filteredData2 = filteredData1.loc[(filteredData1['panel_type'] == 'IPS') | (filteredData1['panel_type'] == 'PLS')]
        elif matrixComboBoxOption == "Швидкість передачі зображення":
            filteredData2 = filteredData1.loc[(filteredData1['panel_type'] == 'TN') | (filteredData1['panel_type'] == 'LED')]
        elif matrixComboBoxOption == "Якість передачі зображення":
            filteredData2 = filteredData1.loc[(filteredData1['panel_type'] == 'VA')]


        thirdPartLenght = int(len(filteredData2) * 0.33)
        meanLenght = int(len(filteredData2) / 2)
        filteredData3 = filteredData2.sort_values(by='price', ascending=True)


        if selectedMode == "Максимальна економія коштів ":
            filteredData4 = filteredData3.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData4 = filteredData3.iloc[
                            max(meanLenght -int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                    -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData4 = filteredData3.tail(min(thirdPartLenght, 300))

        monitorSpecList = ['price', 'screen_size', 'width', 'refresh_rate', 'response_time']
        outputMonitor = self.Saati(route, monitorSpecList, filteredData4)
        pairNamePriceArray = []
        print(outputMonitor)
        pairNamePriceArray.append("Монітор")
        pairNamePriceArray.append(outputMonitor['name'])
        pairNamePriceArray.append(outputMonitor['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)'''
        self.ui.progressBar.setValue(66)

        ################################################################
        ################################


        if soundComboBoxOption == "Звичайні динаміки":
            route = 'speakers'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)
            filteredData1 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData2 = filteredData1.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData2 = filteredData1.iloc[
                                max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                    -meanLenght + int(thirdPartLenght / 2),
                                    -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData2 = filteredData1.tail(min(thirdPartLenght, 300))

            speakersSpecList = ['price', 'configuration', 'wattage', 'frequency_response']
            outputSpeakers = self.Saati(route, speakersSpecList, filteredData2)
            pairNamePriceArray = []
            '''print(outputSpeakers)'''
            pairNamePriceArray.append("Динаміки")
            pairNamePriceArray.append(outputSpeakers['name'])
            pairNamePriceArray.append(outputSpeakers['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)'''
            self.ui.progressBar.setValue(70)



        elif soundComboBoxOption == "Навушники":
            route='headphones'
            df = pd.read_excel(file, sheet_name=route)

            if peripheralCheckBoxCheck:
                filteredData1 = df.loc[df['wireless'] == True]
            else:
                filteredData1 = df.loc[df['wireless'] == False]
            filteredData2=filteredData1.loc[filteredData1['microphone']==False]
            '''print(filteredData2)'''

            thirdPartLenght = int(len(filteredData2) * 0.33)
            meanLenght = int(len(filteredData2) / 2)
            filteredData3 = filteredData2.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData4 = filteredData3.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData4 = filteredData3.iloc[
                                max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                    -meanLenght + int(thirdPartLenght / 2),
                                    -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData4 = filteredData3.tail(min(thirdPartLenght, 300))

            headphonesSpecList = ['price', 'frequency_response']
            outputHeadphones = self.Saati(route, headphonesSpecList, filteredData4)
            pairNamePriceArray = []
            print(outputHeadphones)
            pairNamePriceArray.append("Навушники")
            pairNamePriceArray.append(outputHeadphones['name'])
            pairNamePriceArray.append(outputHeadphones['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)'''
            self.ui.progressBar.setValue(70)




        elif soundComboBoxOption == "Гарнітура":
            route = 'headphones'
            df = pd.read_excel(file, sheet_name=route)

            if peripheralCheckBoxCheck:
                filteredData1 = df.loc[df['wireless'] == True]
            else:
                filteredData1 = df.loc[df['wireless'] == False]
            filteredData2 = filteredData1.loc[filteredData1['microphone'] == True]
            '''print(filteredData2)'''

            thirdPartLenght = int(len(filteredData2) * 0.33)
            meanLenght = int(len(filteredData2) / 2)
            filteredData3 = filteredData2.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData4 = filteredData3.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData4 = filteredData3.iloc[
                                max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                    -meanLenght + int(thirdPartLenght / 2),
                                    -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData4 = filteredData3.tail(min(thirdPartLenght, 300))

            headphonesSpecList = ['price', 'frequency_response']
            outputHeadphones = self.Saati(route, headphonesSpecList, filteredData4)
            pairNamePriceArray = []
            print(outputHeadphones)
            pairNamePriceArray.append("Навушники")
            pairNamePriceArray.append(outputHeadphones['name'])
            pairNamePriceArray.append(outputHeadphones['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)'''
            self.ui.progressBar.setValue(70)



        elif soundComboBoxOption == "Гарнітура + динаміки":
            route = 'headphones'
            df = pd.read_excel(file, sheet_name=route)

            if peripheralCheckBoxCheck:
                filteredData1 = df.loc[df['wireless'] == True]
            else:
                filteredData1 = df.loc[df['wireless'] == False]
            filteredData2 = filteredData1.loc[filteredData1['microphone'] == True]
            '''print(filteredData2)'''

            thirdPartLenght = int(len(filteredData2) * 0.33)
            meanLenght = int(len(filteredData2) / 2)
            filteredData3 = filteredData2.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData4 = filteredData3.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData4 = filteredData3.iloc[
                                max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                    -meanLenght + int(thirdPartLenght / 2),
                                    -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData4 = filteredData3.tail(min(thirdPartLenght, 300))

            headphonesSpecList = ['price', 'frequency_response']
            outputHeadphones = self.Saati(route, headphonesSpecList, filteredData4)
            pairNamePriceArray = []
            print(outputHeadphones)
            pairNamePriceArray.append("Навушники")
            pairNamePriceArray.append(outputHeadphones['name'])
            pairNamePriceArray.append(outputHeadphones['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)'''
            self.ui.progressBar.setValue(68)



            '''|||||||||||||||||||||||||||||||||||||||'''
            route = 'speakers'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)
            filteredData1 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData2 = filteredData1.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData2 = filteredData1.iloc[
                                max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                    -meanLenght + int(thirdPartLenght / 2),
                                    -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData2 = filteredData1.tail(min(thirdPartLenght, 300))

            speakersSpecList = ['price', 'configuration', 'wattage', 'frequency_response']
            outputSpeakers = self.Saati(route, speakersSpecList, filteredData2)
            pairNamePriceArray = []
            '''print(outputSpeakers)'''
            pairNamePriceArray.append("Динаміки")
            pairNamePriceArray.append(outputSpeakers['name'])
            pairNamePriceArray.append(outputSpeakers['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)'''
            self.ui.progressBar.setValue(70)

        ################################
        ##################################

        if soundcardCheckBoxCheck:
            route = 'sound-card'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)

            filteredData2 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData3 = filteredData2.iloc[
                                max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

            soundcardSpecList=['price','channels','digital_audio', 'snr', 'sample_rate']
            outputSoundCard = self.Saati(route, soundcardSpecList, filteredData3)
            pairNamePriceArray = []
            '''print(outputSoundCard)'''
            pairNamePriceArray.append("Звукова карта")
            pairNamePriceArray.append(outputSoundCard['name'])
            pairNamePriceArray.append(outputSoundCard['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)
            print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
            systemWattage += 6
            self.ui.progressBar.setValue(74)
            #############################################
            #######################################



        if webcamCheckBoxCheck:
            route = 'webcam'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)

            filteredData2 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData3 = filteredData2.iloc[
                                max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

            webcamSpecList=['price','resolutions','fov']
            outputWebcam = self.Saati(route, webcamSpecList, filteredData3)
            pairNamePriceArray = []
            '''print(outputWebcam)'''
            pairNamePriceArray.append("Веб-камера")
            pairNamePriceArray.append(outputWebcam['name'])
            pairNamePriceArray.append(outputWebcam['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)
            print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
            self.ui.progressBar.setValue(78)
            systemWattage += 2
            #############################################
            #######################################



        if wirelessCheckBox:
            route = 'wireless-network-card'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)

            filteredData2 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData3 = filteredData2.iloc[
                                max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

            wirelessSpecList=['price','protocol']
            outputWireless = self.Saati(route, wirelessSpecList, filteredData3)
            pairNamePriceArray = []
            '''print(outputWireless)'''
            pairNamePriceArray.append("Мережева карта")
            pairNamePriceArray.append(outputWireless['name'])
            pairNamePriceArray.append(outputWireless['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)'''
            systemWattage+= 4
            '''print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
            self.ui.progressBar.setValue(84)

            #############################################
            #######################################


        if opticCheckBox:
            route = 'optical-drive'
            df = pd.read_excel(file, sheet_name=route)

            thirdPartLenght = int(len(df) * 0.33)
            meanLenght = int(len(df) / 2)

            filteredData2 = df.sort_values(by='price', ascending=True)

            if selectedMode == "Максимальна економія коштів ":
                filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData3 = filteredData2.iloc[
                                max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

            opticSpecList=['price','dvd','cd', 'dvd_write','cd_write']
            outputOptic = self.Saati(route, opticSpecList, filteredData3)
            pairNamePriceArray = []
            '''print(outputOptic)'''
            pairNamePriceArray.append("Оптичний привід")
            pairNamePriceArray.append(outputOptic['name'])
            pairNamePriceArray.append(outputOptic['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)
            print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
            self.ui.progressBar.setValue(88)
            systemWattage += 30
            #############################################
            #######################################

        route = 'internal-hard-drive'
        df = pd.read_excel(file, sheet_name=route)
        '''print(df)'''
        filteredData1 = df.loc[df['interface'] == 'M.2']
        if dataCheckBox:
            filteredData1 = filteredData1.loc[(df['capacity'] <= 700) & (df['capacity'] >= 240)]
        else:
            filteredData1 = filteredData1.loc[df['capacity'] > 500]

        filteredData2 = filteredData1.sort_values(by='price', ascending=True)
        thirdPartLenght = int(len(filteredData2) * 0.33)
        meanLenght = int(len(filteredData2) / 2)


        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[
                            max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                -meanLenght + int(thirdPartLenght / 2),
                                -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

        ssdSpecList = ['price', 'capacity']
        outputSSD = self.Saati(route, ssdSpecList, filteredData3)
        pairNamePriceArray = []
        print(outputSSD)
        pairNamePriceArray.append("SSD M.2")
        pairNamePriceArray.append(outputSSD['name'])
        pairNamePriceArray.append(outputSSD['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)
        print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        self.ui.progressBar.setValue(90)
        systemWattage += 2
        #############################################
        #######################################

        if dataCheckBox:
            df = pd.read_excel(file, sheet_name=route)

            filteredData1=df.loc[df['capacity'] >= 1500 ]

            filteredData2 = filteredData1.sort_values(by='price', ascending=True)
            '''print(filteredData2)'''


            if sizeCheckBoxCheck:
                filteredData3=filteredData2.loc[filteredData2['form_factor'] == '2.5']
                '''print(filteredData3)'''
            else:
                filteredData3 = filteredData2

            filteredData4=filteredData3.loc[filteredData3['type'] != "SSD"]

            thirdPartLenght = int(len(filteredData4) * 0.33)
            meanLenght = int(len(filteredData4) / 2)
            '''print(filteredData4)'''


            if selectedMode == "Максимальна економія коштів ":
                filteredData5 = filteredData4.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData5 = filteredData4.iloc[
                                max(meanLenght - int(thirdPartLenght/2-1), meanLenght - 150):min(-meanLenght +1+ int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData5 = filteredData4.tail(min(thirdPartLenght, 300))

            hddSpecList=['price', 'capacity', 'cache']
            outputHDD = self.Saati(route, hddSpecList, filteredData5)
            pairNamePriceArray = []
            print(outputHDD)
            pairNamePriceArray.append("Жорсткий диск")
            pairNamePriceArray.append(outputHDD['name'])
            pairNamePriceArray.append(outputHDD['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)
            print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
            systemWattage += 12
            self.ui.progressBar.setValue(92)
            ################################################################
            ################################################################



        route='keyboard'
        df = pd.read_excel(file, sheet_name=route)


        if sizeCheckBoxCheck:
            filteredData1 = df.loc[df['style'] != 'Standart']
        else:
            filteredData1 = df

        if peripheralCheckBoxCheck:
            filteredData2 = filteredData1.loc[filteredData1['connection_type'] != 'Wired']
        else:
            filteredData2 = filteredData1


        filteredData3 = filteredData2.sort_values(by='price', ascending=True)
        thirdPartLenght = int(len(filteredData3) * 0.33)
        meanLenght = int(len(filteredData3) / 2)

        if selectedMode == "Максимальна економія коштів ":
            filteredData4 = filteredData3.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData4 = filteredData3.iloc[
                            max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                -meanLenght + int(thirdPartLenght / 2),
                                -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData4 = filteredData3.tail(min(thirdPartLenght, 300))

        keySpecList = ['price']
        outputKey = self.Saati(route, keySpecList, filteredData4)
        pairNamePriceArray = []
        print(outputKey)
        pairNamePriceArray.append("Клавіатура")
        pairNamePriceArray.append(outputKey['name'])
        pairNamePriceArray.append(outputKey['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)
        print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        self.ui.progressBar.setValue(94)
        systemWattage += 3
        #############################################
        #######################################

        route = 'mouse'
        df = pd.read_excel(file, sheet_name=route)

        if peripheralCheckBoxCheck:
            filteredData2 = df.loc[df['connection_type'] != 'Wired']
        else:
            filteredData2 = df

        filteredData3 = filteredData2.sort_values(by='price', ascending=True)
        thirdPartLenght = int(len(filteredData3) * 0.33)
        meanLenght = int(len(filteredData3) / 2)

        if selectedMode == "Максимальна економія коштів ":
            filteredData4 = filteredData3.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData4 = filteredData3.iloc[
                            max(meanLenght - int(thirdPartLenght / 2), meanLenght - 150):min(
                                -meanLenght + int(thirdPartLenght / 2),
                                -meanLenght + 150)]
        elif selectedMode == "Максимальна продуктивність":
            filteredData4 = filteredData3.tail(min(thirdPartLenght, 300))

        mouseSpecList = ['price']
        outputMou = self.Saati(route, mouseSpecList, filteredData4)
        pairNamePriceArray = []
        print(outputMou)
        pairNamePriceArray.append("Миша")
        pairNamePriceArray.append(outputMou['name'])
        pairNamePriceArray.append(outputMou['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)
        print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        self.ui.progressBar.setValue(96)
        systemWattage += 2
        #############################################
        #######################################


        route = 'power-supply'
        df = pd.read_excel(file, sheet_name=route)

        print('Потужність системи = ', systemWattage)

        proposedPSUWatts =1.4 * systemWattage
        print("Пропонована потужність (*1,4) = ", proposedPSUWatts)
        suggestionsWattage = [300, 350, 400, 450, 500, 550,
                            600, 650, 700, 750, 850, 1000, 1200, 1300, 1500, 1600]

        closePSU = min(filter(lambda x: x > proposedPSUWatts, suggestionsWattage))
        print("Найближче значення блоку живлення = ", closePSU)
        filteredData1 = df.loc[df['wattage'] >= closePSU]
        filteredData2 = filteredData1.loc[df['wattage']==closePSU]
        thirdPartLenght = int(len(filteredData2) * 0.33)
        meanLenght = int(len(filteredData2) / 2)
        filteredData2=filteredData2.loc[filteredData2['type']=='ATX']

        if selectedMode == "Максимальна економія коштів ":
            filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
        elif selectedMode == "Баланс продуктивності та ціни":
            filteredData3 = filteredData2.iloc[
                            max(meanLenght - 1 - int(thirdPartLenght / 2), meanLenght - 150):min(
                                meanLenght + 1+int(thirdPartLenght / 2),
                                meanLenght + 150)]
        elif selectedMode == 'Максимальна продуктивність':
            filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))


        '''print(filteredData3)'''
        psuSpecList = ['price']
        outputPSU = self.Saati(route, psuSpecList, filteredData3)
        pairNamePriceArray = []
        print(outputPSU)
        pairNamePriceArray.append("Блок живлення")
        pairNamePriceArray.append(outputPSU['name'])
        pairNamePriceArray.append(outputPSU['price'])
        '''print(pairNamePriceArray)'''
        endConfig.append(pairNamePriceArray)
        '''print(endConfig)
        print('////////////////////////////////////////////////////////////////')
        print('////////////////////////////////////////////////////////////////')'''
        self.ui.progressBar.setValue(98)
        #############################################
        #############################################

        if upsCheckBoxCheck:

            route = 'ups'
            df = pd.read_excel(file, sheet_name=route)


            suggestionsWattage = [225,260,300,330,360,400,450,500,560,600,670,700,
                                  750,850,900,950,1000,1200,1350,1470,1650,1800]

            closeUPS = min(filter(lambda x: x > outputPSU['wattage'], suggestionsWattage))
            print("Пропоноване значення ДБЖ =", closeUPS)



            filteredData1 = df.loc[df['capacity_w'] == closeUPS]
            '''print(filteredData1)'''

            thirdPartLenght = int(len(filteredData1) * 0.33)
            meanLenght = int(len(filteredData1) / 2)

            filteredData2 = filteredData1.loc[filteredData1['capacity_w'] == closeUPS]
            filteredData2 = filteredData2.sort_values(by='price', ascending=True)
            '''print(filteredData2)'''

            if selectedMode == "Максимальна економія коштів ":
                filteredData3 = filteredData2.head(min(thirdPartLenght, 300))
            elif selectedMode == "Баланс продуктивності та ціни":
                filteredData3 = filteredData2.iloc[
                                max(meanLenght - int(thirdPartLenght/2), meanLenght - 150):min(-meanLenght + int(thirdPartLenght/2),
                                                                                        -meanLenght + 150)]
            elif selectedMode == "Максимальна продуктивність":
                filteredData3 = filteredData2.tail(min(thirdPartLenght, 300))

            '''print(filteredData3)'''
            '''print(len(filteredData3))'''
            upsSpecList=['price','capacity_w','capacity_va']
            outputUps = self.Saati(route, upsSpecList, filteredData3)
            pairNamePriceArray = []
            print(outputUps)
            pairNamePriceArray.append("Джерело живлення")
            pairNamePriceArray.append(outputUps['name'])
            pairNamePriceArray.append(outputUps['price'])
            '''print(pairNamePriceArray)'''
            endConfig.append(pairNamePriceArray)
            '''print(endConfig)
            print('////////////////////////////////////////////////////////////////')
            print('////////////////////////////////////////////////////////////////')'''
        self.ui.progressBar.setValue(100)

        for _ in endConfig:
            '''print(_)'''
        for priceCount in range (len(endConfig)):
            endPrice += endConfig[priceCount][2]
        '''print(round(endPrice,2))'''
        
            ################################################################
            ################################################################
        return round(endPrice, 2)

    def open_second_window(self, endConfig, endPrice):
        # Send data to the second window
        '''print(endPrice)'''
        self.second_window.receive_data(endConfig, endPrice)
        self.second_window.show()


    def launch(self):
        self.ui.progressBar.setValue(0)
        endPrice=0
        endConfig = []
        endPrice=self.processing(endConfig, endPrice)
        self.open_second_window(endConfig, endPrice)


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Кінцева конфігурація")
        self.setGeometry(400, 200, 800, 600)
        self.setStyleSheet("""
                    QWidget {
                        background-color:rgb(12, 14, 35); 
                        color: rgb(255, 255, 255); 
                        font-size: 14px; 
                    }
                """)

        icon = QIcon()
        icon.addFile(u":/img/C:/Users/mx/Downloads/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ТИП КОМПЛЕКТУЮЧОЇ", "НАЙМЕНУВАННЯ", "ЦІНА"])
        self.table.setStyleSheet('')
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)
        self.line_edit.setReadOnly(True)
        self.line_edit.setStyleSheet(
            """
            QLineEdit {
                padding-left: 4px; padding-right: 4px; text-align: center;
                background-color:rgb(12, 14, 35); 
                color: rgb(255, 255, 255); 
                font-size: 16px; 
                font-family: "Segoe UI", sans-serif;
                font-weight: bold;
            }
            """
        )
        self.line_edit.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.table)

        for i in range(3):
            self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.Stretch)

            # Встановлення гнучкої політики розміру для таблиці
        tableSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.table.setSizePolicy(tableSizePolicy)

        # Встановлення гнучкої політики розміру для віджету SecondWindow
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)



        self.table.setStyleSheet("""
            QTableWidget {
                background-color:rgb(12, 14, 35); 
                color: rgb(255, 255, 255); 
                font-size: 14px; 
                font-family: "Segoe UI", sans-serif;
                font-weight: bold;
            }
             QTableWidget::item:selected {
                background-color: #0078d7; /* Колір виділеного елементу */
                color: white; /* Колір тексту виділеного елементу */
            }
            QHeaderView::section {
                background-color: rgb(12, 14, 35); /* Колір фону заголовків стовпців */
                color: rgb(255, 255, 255); /* Колір тексту заголовків стовпців */
                font-size: 16px;
                border: 1px solid white; /* Стиль ліній поділу */
                font-weight: bold; /* Жирний шрифт для заголовків стовпців */
                font-family: "Segoe UI", sans-serif; /* Тип шрифту для заголовків стовпців */
            }
             QTableWidget::item {
                border-bottom: 1px solid white; /* Стиль ліній поділу */
            }
             QTableWidget::item:hover{
                color: #8bdbff
             }
        """)


    def receive_data(self, array, number):
        # Display array in QTableWidget
        self.table.setRowCount(len(array))
        for i, item in enumerate(array):
            self.table.setItem(i, 0, QTableWidgetItem(str(item[0])))  # First column
            self.table.setItem(i, 1, QTableWidgetItem(str(item[1])))  # Second column
            self.table.setItem(i, 2, QTableWidgetItem(str(item[2])))  # Third column
        # Display number in QLineEdit
        self.line_edit.setText('ВАРТІСТЬ ВСІЄЇ ЗБІРКИ: {}'.format(str(number)))

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
