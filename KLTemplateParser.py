# KL Template Parser

import sys

# Default type groups
Floats = ['Float32', 'Float64']
Ints = ['UInt8', 'SInt8', 'UInt16', 'SInt16', 'UInt32', 'SInt32', 'UInt64', 'SInt64']
UInts = ['UInt8', 'UInt16', 'UInt32', 'UInt64']
SInts = ['SInt8', 'SInt16', 'SInt32', 'SInt64']
Num = ['UInt8', 'SInt8', 'UInt16', 'SInt16', 'UInt32', 'SInt32', 'UInt64', 'SInt64', 'Float32', 'Float64']
AllBase = ['UInt8', 'SInt8', 'UInt16', 'SInt16', 'UInt32', 'SInt32', 'UInt64', 'SInt64', 'Float32', 'Float64' , 'Boolean', 'String']

def defaults(sList):
  """replace default group name for list"""
  if 'Floats' in sList[:]:
    sList[sList[:].index('Floats') : sList[:].index('Floats') + 1] = Floats
  if 'Ints' in sList[:]:
    sList[sList[:].index('Ints') : sList[:].index('Ints') + 1] = Ints
  if 'UInts' in sList[:]:
    sList[sList[:].index('UInts') : sList[:].index('UInts') + 1] = UInts
  if 'SInts' in sList[:]:
    sList[sList[:].index('SInts') : sList[:].index('SInts') + 1] = SInts
  if 'Num' in sList[:]:
    sList[sList[:].index('Num') : sList[:].index('Num') + 1] = Num
  if 'AllBase' in sList[:]:
    sList[sList[:].index('AllBase') : sList[:].index('AllBase') + 1] = AllBase

def do(TemplateFileName, KLFileNameIN, SubstitutesIN):
  TemplateFile = open(TemplateFileName, 'r')

  if KLFileNameIN == '-T':
    KLFileName = 'ParsedKL.kl'
  else:
    KLFileName = KLFileNameIN
  if SubstitutesIN != []:
    Substitutes = [['<T>'] + SubstitutesIN]
  else:
    Substitutes = []

  #TemplatethisLine = TemplateFile.readline() # Read line
  for line in TemplateFile:
    if SubstitutesIN == [] and line[0:3] == '# <':
      SubList = line[2:].split()
      defaults(SubList)
      Substitutes = Substitutes + [SubList]
    elif KLFileNameIN == '-T' and line[0:10] == '# Filename':
      KLFileName = line[12:-2]
    elif line[0:11] == '# Functions':
      break
  if len(Substitutes) == 0:
    Substitutes = [['<T>'] + Num] # Default if no Substitutes specified

  functionID = -1
  functionText = []
  thisSub = []

  for line in TemplateFile:
    if line[0] == '#':
      functionID = functionID + 1
      functionText = functionText + ['']
      thisSub = thisSub + [line[2:-1]]
    else:
      functionText[functionID] = functionText[functionID] + line

  functionReturn = []

  for i, func in enumerate(functionText):
    if thisSub[i] != '':
      sl = 0
      for s, SubList in enumerate(Substitutes):
        if SubList[0] == thisSub[i]:
          sl = s
      for Sub in Substitutes[sl][1:]:
        functionReturn = functionReturn + [func.replace(thisSub[i], Sub)]
    else:
      functionReturn = functionReturn + [func]

  KLFile = open(KLFileName, 'w') #maybe 'a'

  for i, func in enumerate(functionReturn):
    KLFile.writelines(functionReturn[i])

  TemplateFile.close()
  KLFile.close()

if __name__ == "__main__":
  if len(sys.argv) == 1:
    # TemplateFileName = 'SampleKLTemplate.klt'
    import tkFileDialog
    TemplateFileName = tkFileDialog.askopenfilename()
    KLFileName = '-T'
    Substitutes = []
  elif len(sys.argv) == 2:
    TemplateFileName = sys.argv[1]
    KLFileName = '-T'
    Substitutes = []
  elif len(sys.argv) == 3:  
    TemplateFileName = sys.argv[1]
    KLFileName = sys.argv[2]
    Substitutes = []
  else:
    TemplateFileName = sys.argv[1]
    KLFileName = sys.argv[2]
    Substitutes = sys.argv[3:]

  do(TemplateFileName, KLFileName, Substitutes)

# -T = look in template for file name.
