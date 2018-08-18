
rowName = [ 'Select geometry', 'Select unit', 'Set parameter' ,'Get area']
buttonName = [['Triangle', 'Rectangular', 'Square', 'Circular'], ['In centimeter', 'In inch']]
geometryName = buttonName[0]
unitName = buttonName[1]

buttonTypeNumber = len(buttonName)
geometryNumber = len(geometryName)
unitNumber = len(unitName)

defaultColumnNumber = [geometryNumber+1, unitNumber+1]
defaultGridRowNumber = len(rowName)

# defaultMaxGridColumnNumber = max(defaultGridColumnNumber)

initialColor = ['#EEE9E9']*2
laterColor = ['blue', 'red']

interfaceWidth = 800
interfaceHeight = 400

defaultGridHeight = interfaceHeight / defaultGridRowNumber

# defaultGridWidth = interfaceWidth / defaultMaxGridColumnNumber