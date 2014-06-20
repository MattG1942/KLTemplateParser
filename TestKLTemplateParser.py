# Tests KLTemplateParser.py

import KLTemplateParser
TemplateFile = 'SampleKLTemplate2.klt'
KLFileName = 'SampleKL2.kl'
Substitutes = ['Float23', 'UInt32'] # must be a list of strings
KLTemplateParser.do(TemplateFile, KLFileName, Substitutes)