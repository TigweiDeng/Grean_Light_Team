
rowName = [ 'Select\nGeometry', 'Select\nUnit', 'Set\nParameter' ,'Get\nArea']
buttonName = [['Triangle', 'Rectangular', 'Square', 'Circular'], ['In cm', 'In inch'], \
   [], ['In cm²', 'In inch²']]

geometryName = buttonName[0]
parameterUnit = buttonName[1]
resultUnit = buttonName[3]

resultIndex = 3

buttonTypeNumber = len(buttonName)
geometryNumber = len(geometryName)
parameterUnitNumber = len(parameterUnit)
resultUnitNumber = len(resultUnit)

defaultColumnNumber = [geometryNumber, parameterUnitNumber, 1, resultUnitNumber+2]
defaultGridRowNumber = len(rowName)

# defaultMaxGridColumnNumber = max(defaultGridColumnNumber)

defaultColor = '#EEE9E9'
initialColor = [['blue']+[defaultColor]*(geometryNumber-1), ['red']+[defaultColor]*(parameterUnitNumber-1), \
    [], ['yellow']+[defaultColor]*(resultUnitNumber-1)]
changedColor = ['blue', 'red', '', 'yellow']

interfaceWidth = 800
interfaceHeight = 400

firstColumnWidth = 160
restWidth = interfaceWidth-firstColumnWidth

defaultGridHeight = interfaceHeight / defaultGridRowNumber

# defaultGridWidth = interfaceWidth / defaultMaxGridColumnNumber