
rowName = [ 'Select\nGeometry', 'Select\nUnit', 'Set\nParameter' ,'Get\nArea']
buttonName = [['Square', 'Circular', 'Triangle', 'Rectangular'], ['In cm', 'In inch'], \
   [], ['In cm²', 'In inch²']]
parameterName = [['Side length'], ['Radius'], ['Base', 'Height'], ['Length', 'Width']]

geometryName = buttonName[0]
parameterUnit = buttonName[1]
resultUnit = buttonName[3]
squareParameter = parameterName[0]
circularParameter = parameterName[1]
triangleParameter = parameterName[2]
rectangularParameter = parameterName[3]

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

Pi = 3.14159
Coefficient = 2.54**2

# defaultGridWidth = interfaceWidth / defaultMaxGridColumnNumber