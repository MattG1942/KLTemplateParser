KLTemplateParser
================

Generates KL code from template files for Fabric Engine

example: for creating variations of a function for multiple types

Substitues defaults to all numeric types (Num)
Filename defaults to "ParsedKL.kl"

Usage
=====

From Comand Line:

Method 1:

Run script with no arguments; will prompt for template file.
eg.

```
KLTemplateParser.py
```

Method 2:

Run script with one argument; will use template file specified in argument.
eg.

```
KLTemplateParser.py SampleKLTemplate2.klt
```

Method 3:

Run script with 2 arguments; will use template file and output file specified in arguments.
eg.

```
KLTemplateParser.py SampleKLTemplate2.klt SampleKL2c.kl
```

Method 4:

Run script with 3+ argument; will use template file, output file and Substitutes specified in arguments.

eg1.

```
KLTemplateParser.py SampleKLTemplate2.klt SampleKL2c.kl Float32 Uint8
```

eg2.

```
KLTemplateParser.py SampleKLTemplate2.klt -T Float32
```

'-T' = look in template for file name.

From another Python Script:

Method 5:

call KLTemplateParser.do and specify all arguments (Template File, KL File Name & Substitutes).

eg.

```python
import KLTemplateParser
TemplateFile = 'SampleKLTemplate2.klt'
KLFileName = 'SampleKL2.kl'
Substitutes = ['Float23', 'UInt32'] # must be a list of strings
KLTemplateParser.do(TemplateFile, KLFileName, Substitutes)
```

Using '-T' as KLFileName - will look in template for file name.
Substitutes can be an empty string - will look in template for substitutes.