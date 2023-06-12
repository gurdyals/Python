#!/usr/bin/env python3 -u

#This is started on April 08, '2019

########################################################################
##### id(obj), eval(obj), dir(obj), type(obj), str(obj)
########################################################################
######################     Function Definitions   ######################
def print_this(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    print(str([k for k, v in callers_local_vars if v is var][0])+': '+str(var))

# Defining Functions
def fib(n):
    """Print a Fibonacci Series up to n."""
    print( "Printing a Fibonacci Series up to n" )
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, b+a
    print()

# Return a list of Fibonacci List of Numbers instead of Printing it
def fib2(n):    # Return Fibonacci Series up to n
    """Return a list containing the Fibonacci Series up to n."""
    print( "Returning a LIST of Fibonacci Series up to n" )
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)     # See Below
        a, b = b, b+a
    print( "result : ", result )
    return result

def test_f(fl):
    try:
        result = float( fl )
    except ValueError:
        result = 0.0
    return( result )

def test_f1(fl):
  if not fl:
      result=0
  else:
      result=fl
  return( float( result ) )

def CnvDate( Dt ):
    result = parse( Dt, ignoretz=True ) 
    # print ( " CnvDate :", Dt, ":", result, ":", type(result), ":", type(Dt), ":" )
    return( result )

def prnt_header( row ):
    print( fmt_str0.format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ) )
    result = ( fmt_str0.format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ) )
    return( result )

def prnt_row( row ):
    result = ( fmt_str1.format( row[0], str( CnvDate(row[1]).strftime( '%a %b %d %H:%M:%S IST %Y' ) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    print( fmt_str1.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    return( result )

fmt_str15= '{0:>5},{1:^28},{3:<13},{5:<31},{6:9.2f},{7:7.2f},{8:7.2f}'

def prnt_row15( row ):
    result = ( fmt_str15.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    # print( fmt_str1.format( row[0], str( CnvDate(row[1]) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )
    return( result )

######################     Function Definitions   ######################
########################################################################

########################################################################
######################     Built-IN Utilities     ######################
import argparse		# for parsing Command line Arguments
import csv		# 11, 12, 13
import calendar         # 0
import hashlib          # 19
import heapq            # 34
import inspect		# for inspecting variables and program code
import locale		# 11
import logging          # 39
import os		# for OS related utilities     # 5
import pdb              # 40
import random           # 29
import sys		# 13
import subprocess
import time

from datetime      import date              # for date related utilities
from datetime      import datetime          # for datetime related
from datetime      import timedelta
from dateutil      import parser            # parser for date
from dateutil      import relativedelta as rdelta
from dateutil.parser import parse           # 11, 12
from functools     import reduce            # 35
from subprocess    import check_output      # for Shell Commands
from subprocess    import run
from string        import Template          # 28
from sys           import argv              # command line arguments

######################     Built-IN Utilities     ######################
########################################################################

fmt_str0= '{0:>5},{1:^28},{2:^13},{3:^13},{4:^9},{5:^31},{6:^9},{7:^7},{8:^7}'
fmt_str1= '{0:>5},{1:^28},{2:<13},{3:<13},{4:<9},{5:<31},{6:9.2f},{7:7.2f},{8:7.2f}'

print ( '\n\t STANDARD DETAILS\n1. sys.argv \t\t: ', argv, len(argv) )
print ( '2. SYS.EXECUTABLE \t: ', sys.executable )
print ( '3. SYS.VERSION \t\t: ', sys.version )
print ( '4. SYS.VERSION_INFO \t: ', sys.version_info )
print ( '5. SYS.PATH \t\t: ', sys.path )
print ( '6. SYS OS.ENVIRON["PATH"] \t: ', os.environ['PATH'] )
print ( '7. SYS OS.ENVIRON \t\t: ', os.environ )

print ( "\n" )






def main(argv):
# def main():
    print("argv[1]: ", argv, argv[1])
    print(f'argv[1]: , {argv=} {argv[0]=} {argv[1]=}')
    print("type(argv[1]): ", type(argv), type(argv[1]))
    print(f'type(argv[1]): , {type(argv)=} {type(argv[0])=} {type(argv[1])=}')







    if argv[1] == '1':
      print ( argv )
    #1.)     .         .         .         .         .         .    20190419
      word="Python"

      print ('word="Python"  and result of word[1:]')
      print ( word[1:] )

      print ( 'repr( word ) := ' + repr( word ), ': repr( type( word )) := ' + repr( type( word ) ), ": eval( 'word' ) := " + eval( 'word' ) )
      print ( "rutherhk ")

    #1.)     0         0         0         0         0         0    20190419







    elif argv[1] == '2':
      print ( argv )
    #2.)     .         .         .         .         .         .    20190419
      if_this_is_true = True
      if if_this_is_true :
          print ("Hey This is True ")

    #2.)     0         0         0         0         0         0    20190419







    elif argv[1] == '3':
      print ( argv )
    #3.)     .         .         .         .         .         .    20190420
      print ("The result of Multiply 5 * 7 ")
      s = 5 * 7 # The result of Multiply
      print (s)

      print ("The result of raise to power 5 ** 7 ")
      s = 5 ** 7 # The result of raise to power
      print (s)

    #3.)     0         0         0         0         0         0    20190420







    elif argv[1] == '4':
      print ( argv )
    #4.)     .         .         .         .         .         .    20190420
    # Lists are mutable and string is immutable
      squares = [1, 4, 9, 16, 25]
      cubes = [1, 8, 27, 65, 125] 
      print ( "squares is", squares )
      print ( "cubes is", cubes )

      squares=[]
      cubes=[]
      for i in range(10):
          squares.append((i+1) ** 2)
    #       print ( "squares in for loop ", squares )

          cubes.append((i+1) ** 3)
    #       print ( "cubes   in for loop ", cubes   )
      print ( "squares outside  for loop ", squares )
      print ( "cubes   outside  for loop ", cubes   )

      fives=list(range(10))
      print ( fives , "fives" )
      for i in fives:
          fives[i] = (i+1) ** 5
    #       print ( "fives in for loop ", fives )
      print ( "fives outside for loop ", fives )

      i=0
      foures=[]
      while i<10:
          foures.append( (i+1) ** 4 )
          i=i+1
    #       print ( "foures  in for loop ", foures  )
      print ( "foures outside for loop ", foures  )

      s = [ i+1 for i in range(10) ]
      print ( "s is", s )
      s = [ (i+1)**2 for i in range(10) ]
      print ( "squares is", s )
      s = [ (i+1)**3 for i in range(10) ]
      print ( "cubes is", s )
      s = [ (i+1)**4 for i in range(10) ]
      print ( "foures is", s )

      a = ['a', 'b', 'c']
      n = [1, 2, 3]
      x = [a, n]
      print ( "x is", x )
      print ( "x[0] is", x[0] )
      print ( "x[0][1] is", x[0][1] )

    #4.)     0         0         0         0         0         0    20190420







    elif argv[1] == '5':
      print ( argv )
    #5.)     .         .         .         .         .         .    20190424
    ##### https://docs.python.org/3.6/library/functions.html?highlight=enumerate#enumerate
    ##### https://docs.python.org/3.6/library/functions.html

    ##### open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
      f=open('DEL_faltu-file', 'a')

    #####  print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
      for i in range ( 10 ):
          print ( i, sep=' -------  SEPARATOR  ---     ', end=', saldkljf -----', file=f, flush=True )
      print ( i, sep=' -------  SEPARATOR  ---     ', end=', saldkljf -----\n', file=f, flush=True )

    ##### close(f)  #  Function close() is part of Package "os" so import os
      print ( "Remove the file  <DEL_faltu-file> " )

    #5.)     0         0         0         0         0         0    20190424







    elif argv[1] == '6':
      print ( argv )
    #6.)     .         .         .         .         .         .    20190606
    ##### https://docs.python.org/3.6/tutorial/controlflow.html
    ##### 4.4. break and continue Statements, and else Clauses on Loops

      for n in range(2, 10):
          print ( 'n :', n )
          for x in range(2, n):
              print ( 'x :', x, 'n :', n )
              if n % x == 0:
                  print ( 'n % x :', n % x, 'x :', x, 'n :', n )
                  print(n, 'equals', x, '*', n//x)
                  break
          else:
              # loop fell through without finding a factor
              print(n, 'is a prime number')

    #6.)     0         0         0         0         0         0    20190606







    elif argv[1] == '7':
      print ( argv )
    #7.)     .         .         .         .         .         .    20190607
      for num in range(2, 10):
          if num % 2 == 0:
              print("Found an even number", num)
              continue
          print("X4 Found a number", num)

    #7.)     0         0         0         0         0         0    20190607







    elif argv[1] == '8':
      print ( argv )
    #8.)     .         .         .         .         .         .    20190607
      while True:
          print ( 'Press <CTRL-C> as this is "pass" Statement' )
          pass
          break
      else:
          print ( 'Dress Press <CTRL-C> as this is "pass" Statement' )

    #8.)     0         0         0         0         0         0    20190607







    elif argv[1] == '9':
      print ( argv )
      # print ( argv, flush=True )
      sys.stdout.flush()
      print("\n")
    #9.)     .         .         .         .         .         .    20190609
      # Defining Functions
      def fib(n):
          """Print a Fibonacci Series up to n."""
          print( "Printing a Fibonacci Series up to n" )
          a, b = 0, 1
          while a < n:
              print(a, end=' ')
              a, b = b, b+a
          print()

      print("\n")
      x = int( input("Please Enter a Number for Fibonacci Series : ") )
      print("\n")

      fib(x)
      print(" fib(x) : ", fib(x) )

    #9.)     0         0         0         0         0         0    20190609







    elif argv[1] == '10':
      print ( argv )
      sys.stdout.flush()
      print("\n")
    #10.)    .         .         .         .         .         .    20190609
      # Return a list of Fibonacci List of Numbers instead of Printing it
      def fib2(n):    # Return Fibonacci Series up to n
          """Return a list containing the Fibonacci Series up to n."""
          print( "Returning a LIST of Fibonacci Series up to n" )
          result = []
          a, b = 0, 1
          while a < n:
              result.append(a)     # See Below
              a, b = b, b+a
          print( "result : ", result )
          return result

      print("\n")
      x = int( input( "Please Enter a Number for Fibonacci Series : ") )
      print("\n")

      fib2(x)
      print(" fib2(x) : ", fib2(x) )

    #10.)    0         0         0         0         0         0    20190609







    elif argv[1] == '11':
      print ( argv )
    #11.)    .         .         .         .         .         .    20190615
      # https://docs.python.org/3.6/library/csv.html
      # https://docs.python.org/3.6/library/string.html#string-formatting
      # https://docs.python.org/3.6/library/string.html#formatstrings

      print( "locale.getlocale() :", locale.getlocale() )

      with open('Meter_Reading_ALL.csv', newline='') as csvfile:
    #       each_row = csv.reader(csvfile, delimiter=',', quotechar='|')
          each_row = csv.reader(csvfile, delimiter=',' ) #, quotechar='|')
          for row in each_row:
              if row[0] == 'No':
                  print( '{0:>5},{1:^28},{2:^13},{3:^13},{4:^9},{5:^31},{6:^11},{7:^9},{8:^9}'.format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ) )
                  continue
    #           print(len(row) )
    #           print(', '.join(row))
    #           print("{0:>05},{1},{2},{3},{4},{5},{6:>9.9},{7:>7.7},{8:>7.7}".format( *row ) )
    #           print( '{0:>5},{1:^28},{2:<13},{3:<13},{4:<9},{5:<31},{6:11.2f},{7:9.2f},{8:9.2f}'.format( row[0].strip('- '), row[1], row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), float( row[6] ), float( row[7] ), float( row[8] ) ) )
              # print( '{0:>5},{1:^28},{2:<13},{3:<13},{4:<9},{5:<31},{6:11.2f},{7:9.2f},{8:9.2f}'.format( row[0], str( parse( row[1], ignoretz=True ) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), float( row[6] ), float( row[7] ), float( row[8] ) ) )
              prnt_row( row )

              a = row[1].split()
              dt1 = parse( row[1], ignoretz=True )
    #           print ( dt1, row[1].split(' '), a[0], a[1], a[2], a[3].split(':'), a[4], a[5] )
    #           print()
      print ( "\n\n", fmt_str0, "\n", fmt_str1 )

    #11.)    0         0         0         0         0         0    20190615







    elif argv[1] == '12':
      print ( argv )
    #12.)    .         .         .         .         .         .    20190619
      with open('Meter_Reading_ALL.csv', newline='') as csvfile:
          each_row = csv.reader(csvfile, delimiter=',' ) #, quotechar='|')
          for row in each_row:
              if row[0] == 'No':
                  print( '{0:>5},{1:^28},{2:^13},{3:^13},{4:^9},{5:^31},{6:^11},{7:^9},{8:^9}'.format( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8] ) )
                  continue

              # print( '{0:>5},{1:^28},{2:<13},{3:<13},{4:<9},{5:<31},{6:11.2f},{7:9.2f},{8:9.2f}'.format( row[0], str( parse( row[1], ignoretz=True ) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), float( row[6] ), float( row[7] ), float( row[8] ) ) )
              prnt_row( row )
    #           print()
      print ( "\n\n", fmt_str0, "\n", fmt_str1 )

    #12.)    0         0         0         0         0         0    20190619







    elif argv[1] == '13':
      print ( argv )
    #13.)    .         .         .         .         .         .    20190619
      # https://docs.python.org/3.6/library/csv.html#csv-fmt-params
      # A slightly more advanced use of the reader — catching and reporting errors:

      filename = 'some.csv'
      with open(filename, newline='') as f:
          reader = csv.reader(f)
          try:
              for row in reader:
                  # print( row )
                  # print( *row )
                  # print( filename, reader.line_num ) #, reader.fieldnames )
                  # print ( " if row[9] ", ":", row[9], ":", bool(row[9]), ":", test_f( row[9] ), ":" ) #, test_f1(row[9]), ":" ) 
                  # print ( " if row[8] ", ":", row[8], ":", bool(row[8]), ":", test_f( row[8] ), ":" ) #, test_f1(row[8]), ":" ) 

                  if reader.line_num == 1:
                      print( fmt_str0.format( row[0], str( row[1] ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), row[6], row[7], row[8], row[9] ) )
                      continue

                  # test_f( value ) is a function defined in this program
                  # CnvDate(value ) is a function defined in this program
                  print( fmt_str1.format( row[0], str( CnvDate( row[1] ) ), row[2].strip('- '), row[3].strip(' -'), row[4].strip(' -'), row[5].strip('- '), test_f( row[6] ), test_f( row[7] ), test_f( row[8] ) ) )

          except csv.Error as e:
              sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

      print ( "\nFileName : ", filename, "\n", fmt_str0, "\n", fmt_str1 )

    #13.)    0         0         0         0         0         0    20190619







    elif argv[1] == '14':
      print ( argv )
    #14.)    .         .         .         .         .         .    20190627
      # take line numbers and subtract units from them or arrive at number of units consumed in those many days 

      i0 = int( input("Please Enter the line number to subtract FROM : ") )
      i1 = int( input("Please Enter the line number to subtract TO : ") )
      price = test_f( input("Please Enter price per Unit of Electricity : ") )
      print("i0 :", i0, ":", "i1 :", i1, ":", price, ":" )

      FileName = 'Meter_Reading_ALL.csv'
      with open(FileName, newline='') as csvfile:
          each_row = csv.reader(csvfile, delimiter=',' ) #, quotechar='|')

          for row in each_row:
              if each_row.line_num == i0+1:
                  row0 = row
    #               prnt_row( row0 )
              if each_row.line_num == i1+1:
                  row1 = row
    #               prnt_row( row1 )

              if each_row.line_num == 1:
                  prnt_header( row )
                  continue

      prnt_row( row0 )
      prnt_row( row1 )

      dt0=(CnvDate(row0[1])).date()
      dt1=(CnvDate(row1[1])).date()
      unit0=test_f(row0[6])
      unit1=test_f(row1[6])

      print ( '\n{0} days, {1:7.2f} units, Price {2:.2f}, Amt {3:.2f}'.format((dt0 - dt1).days, unit0 - unit1, price, (unit0 - unit1) * price ) )

      # print ( "\n\n", fmt_str0, "\n", fmt_str1 )

    #14.)    0         0         0         0         0         0    20190627







    elif argv[1] == '15':
      print ( argv )
    #15.)    .         .         .         .         .         .    20190629
      row_D={}
      print( "row_D : ", row_D )

      FileName = 'Meter_Reading_ALL.csv'
      with open(FileName, newline='') as csvfile:
          each_row = csv.reader(csvfile, delimiter=',' ) #, quotechar='|')

          for row in each_row:
              if each_row.line_num == 1:
                  pass; #  prnt_header( row )
                  continue

              row3 = row[3].strip(' -')

              if row3 in row_D:
                  diff0 = '{:>7.2f}'.format( test_f( row[6] ) - float( row_D[row3][-1].split(',')[4] ) )
                  row_D[row3].append( prnt_row15( row ) + ', ' + diff0 )
              else:
                  row_D[row3] = [ prnt_row15( row ) + ',    0.00' ]

      for key, values in row_D.items():
          print( key, '-----------', values[0].split(',')[3] )
          for val in values:
              print( val )

    #15.)    0         0         0         0         0         0    20190629







    elif argv[1] == '16':
      print ( argv )
    #16.)    .         .         .         .         .         .    20190703
      row_D={}
      print( "row_D : ", row_D )

      OfileName = 'some.csv'
      FileName = 'Meter_Reading_ALL.csv'

      with open(FileName, newline='') as csvfile, open(OfileName, 'w', newline='') as csvOfile:
          each_row = csv.reader(csvfile, delimiter=',' ) #, quotechar='|')

    #       out_row = csv.writer( csvOfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL )
    #       out_row = csv.writer( csvOfile, delimiter=',', quoting=csv.QUOTE_NONE )
          out_row = csv.writer( csvOfile, delimiter=',', quoting=csv.QUOTE_MINIMAL )

          for row in each_row:
              if each_row.line_num == 1:
                  out_row.writerow( prnt_header( row ).split(',') + [ '  AMT0' ] )
                  continue

              row3 = row[3].strip(' -')

              if row3 in row_D:
                  diff0 = '{:>7.2f}'.format( test_f( row[6] ) - float( row_D[row3][-1].split(',')[4] ) )
                  row_D[row3].append( prnt_row15( row ) + ', ' + diff0 )
                  out_row.writerow( prnt_row( row ).split(',') + [ diff0 ] )
              else:
                  row_D[row3] = [ prnt_row15( row ) + ',    0.00' ]
                  out_row.writerow( prnt_row( row ).split(',') + [ '   0.00' ] )


      for key, values in row_D.items():
          print( key, '-----------', values[0].split(',')[3] )
          for val in values:
              print( val )

      print( "Please check the FILE : ", OfileName )

    #16.)    0         0         0         0         0         0    20190703







    elif argv[1] == '17':
      print ( argv )
    #17.)    .         .         .         .         .         .    20190705
      ##### 4.7.1. Default Argument Values
      ##### https://docs.python.org/3.6/tutorial/controlflow.html#default-argument-values

      def ask_ok(prompt, retries=4, reminder='Please try again!'):
          while True:
              ok = input(prompt)
              if ok in ('y', 'ye', 'yes'):
                  return True
              if ok in ('n', 'no', 'nop', 'nope'):
                  return False
              retries = retries - 1
              if retries < 0:
                  raise ValueError('invalid user response')
              print(reminder)

      ask_ok('1. Do you really want to quit?')

      ask_ok('2. OK to overwrite the file?', 2)

      ask_ok('3. OK to overwrite the file?', 2, 'Come on, only yes or no!')

    #17.)    0         0         0         0         0         0    20190705







    elif argv[1] == '18':
      print ( argv )
    #18.)    .         .         .         .         .         .    20190705
      ##### 4.7.2. Keyword Arguments
      ##### https://docs.python.org/3.6/tutorial/controlflow.html#keyword-arguments

      def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
          print("-- This parrot wouldn't", action, end=' ')
          print("if you put", voltage, "volts through it.")
          print("-- Lovely plumage, the", type)
          print("-- It's", state, "!")

      print( "1. : ", parrot(1000) )                                        # 1 positional argument
      print( "2. : ", parrot(voltage=1000) )                                # 1 keyword argument
      print( "3. : ", parrot(voltage=1000000, action='VOOOOOM') )           # 2 keyword arguments
      print( "4. : ", parrot(action='VOOOOOM', voltage=1000000) )           # 2 keyword arguments
      print( "5. : ", parrot('a million', 'bereft of life', 'jump') )       # 3 positional arguments
      print( "6. : ", parrot('a thousand', state='pushing up the daisies') )# 1 positional, 1 keyword

    #18.)    0         0         0         0         0         0    20190705







    elif argv[1] == '19':
      print ( argv )
    #19.)    .         .         .         .         .         .    20191103
      ##### https://stackoverflow.com/questions/58363920/how-to-fix-code-not-hashing-every-line-in-file

      import hashlib
      with open('hash.txt','r+') as fi:
        with open('DEL_faltu-file', 'w+') as fo:
            ##### for line in fi:
            for i, line in enumerate(fi, start=1):
                line = line.strip()
                fo.write(f'{i}\t: {line}  ====> {hashlib.sha3_256(line.encode()).hexdigest()}\n')

    #19.)    0         0         0         0         0         0    20191103







    elif argv[1] == '20':
      print ( argv, " : Calculate Number ( ABSOLUTE ) of days between TWO given Dates :\n" )
    #20.)    .         .         .         .         .         .    20191113
      ##### Num of Days between two dates

      # Dt  = str( datetime.today() )
      dt0 = input( "Please Enter the DATE to subtract FROM - 'YYYYMMDD' : " )
      dt1 = input( "Please Enter the DATE to be subtracted : " )
      Dt0 = CnvDate( dt0 )
      Dt1 = CnvDate( dt1 )
      Dt = Dt0
      result = Dt1
      Diff = Dt1 - Dt0
      # print ( " CnvDate :", Dt, ":", result, ":", type(result), ":", type(Dt), ":" )
      print ( "\nDate ONE : ", Dt0, "\nDate TWO : ", Dt1, "\n Number (Diff) of Days : ", abs( Diff ) )

    #20.)    0         0         0         0         0         0    20191113







    elif argv[1] == '21':
      print ( argv )
      print ( argv, " : Run a SHELL command in SHELL : " )
    #21.)    .         .         .         .         .         .    20191120
      # NOT sure if find is running correctly
      # from subprocess import run

      def bash(command):
          print(f'{command=}')                 # Added on 20230528
          run(command.split(), shell=True)

      string = 'find / -name ddddddsdsd  2>/dev/null'
      print ( string )
      bash( string )

    #21.)    0         0         0         0         0         0    20191120







    elif argv[1] == '22':
      print ( argv )
      print ( argv, " : Func with Parameters & Dictionary : " )
    #22.)    .         .         .         .         .         .    20191120
      ##### 4.7.2. Keyword Arguments
      # When a final formal parameter of the form **name is present, it
      # receives a dictionary (see Mapping Types — dict) containing all
      # keyword arguments except for those corresponding to a formal
      # parameter. This may be combined with a formal parameter of the form
      # *name (described in the next subsection) which receives a tuple
      # containing the positional arguments beyond the formal parameter list.
      # (*name must occur before **name.) For example, if we define a
      # function like this:

      def cheeseshop(kind, *arguments, **keywords):
          print("-- Do you have any", kind, "?")
          print("-- I'm sorry, we're all out of", kind)
          for arg in arguments:
              print(arg)
          print("-" * 40)
          for kw in keywords:
              print(kw, ":", keywords[kw])

      ##### Call the Function
      cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")

    #22.)    0         0         0         0         0         0    20191120







    elif argv[1] == '23':
      print ( argv, " : 4.7.3. Arbitrary Argument Lists : " )
    #23.)    .         .         .         .         .         .    20191121
      # 4.7.3. Arbitrary Argument Lists
      # https://docs.python.org/3.6/tutorial/controlflow.html#arbitrary-argument-lists

      def write_multiple_items(file, separator, *args):
        file.write(separator.join(args))

      def concat(*args, sep="/"):
          return sep.join(args)

      concat("earth", "mars", "venus")
      print ( concat("earth", "mars", "venus") )
      concat("earth", "mars", "venus", sep=".")
      print ( concat("earth", "mars", "venus", sep=".") )

    #23.)    0         0         0         0         0         0    20191121







    elif argv[1] == '24':
      print ( argv, " : 4.7.4. Unpacking Argument Lists : " )
    #24.)    .         .         .         .         .         .    20191121
      # 4.7.4. Unpacking Argument Lists
      # https://docs.python.org/3.6/tutorial/controlflow.html#unpacking-argument-lists

      list(range(3, 6))            # normal call with separate arguments
      print( list(range(3, 6)) )

      args = [3, 6]
      print (args, *args )
      list(range(*args))            # call with arguments unpacked from a list
      print ( list(range(*args)) )

      def parrot(voltage, state='a stiff', action='voom'):
          print("-- This parrot wouldn't", action, end=' ')
          print("if you put", voltage, "volts through it.", end=' ')
          print("E's", state, "!")

      d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
      parrot(**d)

      print ( "d : ", d, " : parrot(**d) : ", parrot(**d) )

    #24.)    0         0         0         0         0         0    20191121







    elif argv[1] == '25':
      print ( argv, " : 4.7.5. Lambda Expressions : " )
      print ( argv, " : https://docs.python.org/3.6/tutorial/controlflow.html#lambda-expressions : " )
    #25.)    .         .         .         .         .         .    20191125
      # https://docs.python.org/3.6/tutorial/controlflow.html#lambda-expressions
      # 4.7.5. Lambda Expressions

      def make_incrementor(n):
          return lambda x: x + n

      f = make_incrementor(42)
      f(0)

      print ( f(1) )

      pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
      pairs.sort(key=lambda pair: pair[1])
      print ( "pair[1] : ", pairs )

      pairs = [(1, 'one', 7777777), (2, 'two', 999999999), (3, 'three', 11111111), (4, 'four', 33333333)]
      pairs.sort(key=lambda pair: pair[2])
      print ( "pair[2] : ", pairs )

      pairs = [(1, 'one', 7777777), (2, 'two', 999999999), (3, 'three', 11111111), (4, 'four', 33333333)]
      pairs.sort(key=lambda pair: pair[1][1], reverse=True)
      print ( "pair[1][1], reverse=True : ", pairs )

    #25.)    0         0         0         0         0         0    20191125







    elif argv[1] == '26':
      # from dateutil import relativedelta as rdelta
      print ( "\t Usage : python3 ", argv[0], argv[1], " FIRST_DATE/DOB SECOND_DATE/DIED NAME \n" )
      print ( argv[:2], " : from dateutil import relativedelta as rdelta " )
      print ( argv )
      # print ( "argv[4:] : " , *argv[4:] )
    #26.)    .         .         .         .         .         .    20191217
      # name = 'Karamjeet Singh Judge VC'
      # t_born = '25 May 1923'
      # t_died = '18 March 1945'

      # print ( "argv Before : ", argv )
      argv = argv + [ '25 May 1923', '18 March 1945', 'Karamjeet Singh Judge VC' ] [ len( argv ) - 2: ]
      # print ( "argv After  : ", argv )

      dt_born = parse( argv[2] )
      dt_died = parse( argv[3] )
      name = " ".join( argv[4:] )

      rd = rdelta.relativedelta( dt_died, dt_born )

      print( "\n{3} was born on {2} \n{3} died on {1} \n{0.years} years, {0.months} months and {0.days} days".format( rd, dt_died.strftime("%A %d %B, %Y"), dt_born.strftime("%A %d %B, %Y"), name ) )

    #26.)    0         0         0         0         0         0    20191217







    elif argv[1] == '27':
      print ( argv )
    #27.)    .         .         .         .         .         .    20200520
      row_D={}
      print( "row_D : ", row_D )

      if ( len(argv) > 2 and test_f( argv[2] ) ):
          RS_per_unit = argv[2]
      else:
          RS_per_unit = '9.0'

      FileName  = 'Meter_Reading_ALL.csv'
      OfileName = 'Meter.csv'
      SfileName = 'some.csv'

    # Added on 20230527
      print(f'\nFile Names: \n{FileName=} \n{OfileName=} \n{SfileName=}\n')                        # Added on 20230527
      subprocess.call(["ls -alrt {} {} {}".format(FileName , OfileName , SfileName)], shell=True)  # Added on 20230527
      print("\n")                                                                                  # Added on 20230527
      subprocess.call(["ls -alrt " + FileName + ' ' + OfileName + ' ' + SfileName], shell=True)    # Added on 20230527
      print("\n")                                                                                  # Added on 20230527
    # Added on 20230527

      with open(FileName, newline='') as csvfile, open(OfileName, 'w', newline='') as csvOfile:
          each_row = csv.reader(csvfile, delimiter=',' ) #, quotechar='|')
    #       out_row = csv.writer( csvOfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL )
    #       out_row = csv.writer( csvOfile, delimiter=',', quoting=csv.QUOTE_NONE )

          out_row = csv.writer( csvOfile, delimiter=',', quoting=csv.QUOTE_MINIMAL )

          for row in each_row:
              if each_row.line_num == 1:
              # Changed on 20230528
                #   out_row.writerow( prnt_header( row ).split(',') + [ '  AMT' + RS_per_unit ] + [ row[10] ] ) # Commented 20230528
                  out_row.writerow( prnt_header( row ).split(',') + [ '  AMT' + RS_per_unit ] )                 # Added 20230528
              # Changed on 20230528
                  continue

              row3 = row[3].strip(' -')
              if row3 in row_D:
                  ##### print ( 'Remove this Test\nrow[1]' , row[1], '\nrow3', row3, '\nrow_D_row3-1', row_D[row3][-1], '\n', row_D[row3][-1].split(',')[1], '\nNot Before this test\n' )

                  diff0 = '{:>7.2f}'.format( test_f( row[6] ) - float( row_D[row3][-1].split(',')[4] ) )
                  diff_min0 = ( CnvDate( row[1] ) - CnvDate( row_D[row3][-1].split(',')[1] ) )

                  ##### rd = rdelta.relativedelta( CnvDate( row[1] ), CnvDate( row_D[row3][-1].split(',')[1] ) )
                  ##### print( "\n {0.years:>7} years {0.months:>2} months {0.days:>5} days {0.hours:>2} {0.minutes:>2} {0.seconds:>2} asdfg".format( rd ) )
                  ##### diff_min0  = ". {0.months:>2}M {0.days:>5}d {0.hours:>02}h {0.minutes:>02}m".format( rd )

                  print ( type(diff_min0), "diff_min0 : ", diff_min0, " :" )
                  DAYS, DLDLD = ' days - ', str( diff_min0 )[-8:]
                  if len(DLDLD) < 8:
                      DAYS =  ' days - 0'
                  ##### print ( str( diff_min0 ), diff_min0.days, DLDLD )
                  days_min0 = '{:>23}'.format( str( diff_min0.days ) + DAYS + DLDLD )
                  days_min1 = list( days_min0 )

                  if days_min1[-8] == ' ': days_min1[-8] = '0'
                  days_min0 = ''.join( days_min1 )

                  ##### print ( type( days_min0 ), days_min0 )
                  ##### print ( type( days_min1 ), days_min1, days_min1[-8] )

                  row[7] = diff0

                  ##### row[8] = diff0
                  row[8] = test_f( diff0 ) * 9.00
                  amt0 = '{:>7.2f}'.format( test_f( diff0 ) * float ( RS_per_unit ) )

                  ##### row_D[row3].append( prnt_row15( row ) + ', ' + amt0 + ', ' + diff_min0 )
                  row_D[row3].append( prnt_row15( row ) + ', ' + amt0 + ', ' + str( days_min0 ) )

                  ##### out_row.writerow( prnt_row( row ).split(',') + [ amt0 ] + [ diff_min0 ] )
                  out_row.writerow( prnt_row( row ).split(',') + [ amt0 ] + [ days_min0 ] )
              else:
                  row_D[row3] = [ prnt_row15( row ) + ',    0.00' + ',       0 days - 00:00:00' ]
                  out_row.writerow( prnt_row( row ).split(',') + [ '   0.00' ] + [ '       0 days - 00:00:00' ] )

      with open(SfileName, 'w', newline='') as csvSfile:
          for key, values in row_D.items():
              P_KeyValues = key + ' ----------- ' + values[0].split(',')[3]
              print ( P_KeyValues )
              csvSfile.write( P_KeyValues + '\n' )

              for val in values:
                  print( val )
                  csvSfile.write( ',' + str( val ) + '\n' )

          print( "Please check the FILE : ", OfileName )
          print( "Please check the FILE : ", SfileName )

    # Added on 20230528 from subprocess import run
          print(f'\nFile Names: \n{FileName=} \n{OfileName=} \n{SfileName=}\n')            # Added on 20230528
          run(["ls -alrt {} {} {}".format(FileName , OfileName , SfileName)], shell=True)  # Added on 20230528
          print("\n")                                                                      # Added on 20230528
          run(["ls -alrt " + FileName + ' ' + OfileName + ' ' + SfileName], shell=True)    # Added on 20230528
          print("\n")                                                                      # Added on 20230528
    # Added on 20230528

          print( " cd  /home/files/PY/Work ;" )
          print( " ( egrep -n -C 5 '\----------' some.csv ; tail -n -5 some.csv ) | less -i ;" )

    #27.)    0         0         0         0         0         0    20200520







    elif argv[1] == '28':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1653474436509741056 " )
    #28.)    .         .         .         .         .         .    20230503
      print( "Python Question;" )
      print( "Let's do another function." )
      print( "What is the output of this code, and why?🤔🤔" )

      from string import Template

      def strange_func(n):
          template = Template('$x is Not the $y letter')
          result = []
          for i in range(n):
              result.append(lambda x: template.substitute(x=x, y=i))
          return result

      funcs = strange_func(4)

      for f in funcs:
          print(f('A'))

    #####  Output:

    ##### a. A is Not the 3 letter
    ##### b. A is Not the 2 letter
    ##### c. A is Not the 1 letter
    ##### d. A is Not the 0 letter

      def strange_func_changed(n):
          template = Template('$x is Not the $y letter')
          result = []
          for i in range(n):
              result.append(lambda x: template.substitute(x=x, y=i))
              print("i: ", i, ": ", result)
              print(i, " : ", result[i]('S'))
          return result

      funcs = strange_func_changed(5)

      for i, f in enumerate(funcs):
          print(i, ":", f('T'))
          print(f"{i} : {f('N')}") #f-string

    #28.)    0         0         0         0         0         0    20230503







    elif argv[1] == '29':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/mathsppblog/status/1653745287330930689 " )
    #29.)    .         .         .         .         .         .    20230503
      print( "Do you know how OOP and inheritance works in Python 🐍?" )
      print( "Give this quiz a go! 🚀" )

      class Person:
          name = "Unknown"
          def greet(self):
              print(f"Hey, {self.name}!")

      class Programmer(Person):
          occupation = "programmer"

      class Pythonista(Programmer):
          language = "Python"
          def greet(self):
              print(f"{self.name} writes {self.language}")

      rodrigo = Pythonista()
      rodrigo.name = "Rodrigo"
    #  del Pythonista.greet
      rodrigo.greet()


    #29.)    0         0         0         0         0         0    20230503







    elif argv[1] == '30':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/phases3272/status/1654184858757783553 " )
    #30.)    .         .         .         .         .         .    20230505
      print("Test your #Python  skills with this pop-quiz! Whether you're a beginner or a seasoned pro, this quiz is a fun way to challenge yourself and learn something new.")
      print("Test your Python knowledge for the day! 🐍🧠")
      print("Coding tip: This is a good way to abuse a python lambda function 🤪")

      print("x = lambda x: (x, print('i'))")
      x = lambda x: (x, print('i'))
      print("y = lambda x: x")
      y = lambda x: x


      print("z = lambda f: (f(0), f(1))")
      z = lambda f: (f(0), f(1))

      print('result = f"{(y(1) in x(1))}, {(z(x) in z(y))}"')
      result = f"{(y(1) in x(1))}, {(z(x) in z(y))}"

      print("What will be the output of the folowing statement?")
      print(">>> print(result)")
      print("A) True, False")
      print("B) False, True")
      print("C) True, True")
      print("D) False, False")

    #30.)    0         0         0         0         0         0    20230505







    elif argv[1] == '31':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1654227593732804609 " )
    #31.)    .         .         .         .         .         .    20230505
      import random

      print("def get_day_of_week():")
      def get_day_of_week():
          return random.choice(["Mon", "Tue", "Wed"])

      print("def days_in_week():")
      def days_in_week():
          return ["Mon", "Tue", "Wed",
                  "Thu", "Fri", "Sat", "Sun"]

      print("def day_output(day_list):")
      def day_output(day_list):
          for day in day_list:
              if day == "Wed":
                  return get_day_of_week()
          return day

      print("days = days_in_week()")
      days = days_in_week()
      print("print(day_output(days))")
      print(day_output(days))

      print("Output:")
      print("a. Mon")
      print("b. Tue")
      print("c. Wed")
      print("d. Any of the above")
      print("e. All of the above")

    #31.)    0         0         0         0         0         0    20230505







    elif argv[1] == '32':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/clcoding/status/1654167256073486338 " )
    #32.)    .         .         .         .         .         .    20230505
      print("Scope of the variable and how to change it")

      print("Python Quiz | Day 79 | What is the output of following Python code ? Complete Playlist https://bit.ly/3GLnZPy")

      print("x = 10")
      x = 10

      print("def foo():")
      print("      global x")
      print("      x = 20")
      def foo():
          global x
          x = 20

      print("foo()")
      foo()
      print("print(x)")
      print(x)

      print("a) 10")
      print("b) 20")
      print("c) syntaxError: invalid syntax")
      print("d) None of the above")

    ##32)    0         0         0         0         0         0    20230505







    elif argv[1] == '33':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/phases3272/status/1654403152920059906 " )
      print ( argv, " : @Twitter https://twitter.com/DanielK_phd/status/1654510152001699846 " )
    #33.)    .         .         .         .         .         .    20230505
      print(" https://twitter.com/phases3272/status/1654403152920059906 ")
      print("Good morning, #Python  enthusiasts! ☀️  ")
      print("Let's start the day with a fun and educative activity to test our knowledge and help us grow.🧠🐍🚀 ")
      print("#DataScientists")

      print("list(map (lambda x: x.capitalize(), ['cat', 'dog', 'cow']))")
      list(map (lambda x: x.capitalize(), ['cat', 'dog', 'cow'] ))
      [i.capitalize() for i in ['cat', 'dog', 'cow']]

      print("dic1, dic2 = {1: 'a', 2: 'c'}, {'a': 9, 'b': 7}")
      print("{**dic1, **dic2}")
      dic1, dic2 = {1: 'a', 2: 'c'}, {'a': 9, 'b': 7}
      {**dic1, **dic2}

      print("l1 = [1, 2, 3, 4, 0]")
      print("[i for i in map(lambda x: {x: 0}, l1)]")
      l1 = [1, 2, 3, 4, 0]
      [i for i in map(lambda x: {x: 0}, l1)]

      print ( argv, " : @Twitter https://twitter.com/DanielK_phd/status/1654510152001699846 " )
      print("def quizz() -> int:")
      print('    a = "1"')
      print('    b = "2"')
      print("    return (a +b,)")
      def quizz() -> int:
          a = "1"
          b = "2"
          return (a +b,)

      print("print(quizz())")
      print(quizz())

      print("'What is the Outputof that code and WHY ??   `")
      print("Output:")
      print("a.  3")
      print("b.  (3,)")
      print("c.  TypeError")
      print("d.  SyntaxError")
      print("e.  None of the above")

    #33.)    0         0         0         0         0         0    20230505







    elif argv[1] == '34':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/driscollis/status/1654606919091490816 " )
    #34.)    .         .         .         .         .         .    20230506
      print("Want to find the N largest or N smallest values in a #Python list? Use the `heapq` module! 🐍🔥")
      print ( argv, " : @Twitter https://twitter.com/driscollis/status/1654606919091490816 " )

      print("import heapq")
      import heapq

      print("test_scores = [51, 88, 22, 67, 99, 100, 87, 75]")
      test_scores = [51, 88, 22, 67, 99, 100, 87, 75]

      print("heapq.nlargest(3, test_scores)")
      print(heapq.nlargest(3, test_scores))
      heapq.nlargest(3, test_scores)

      print("heapq.nsmallest(4, test_scores)")
      print(heapq.nsmallest(4, test_scores))
      heapq.nsmallest(4, test_scores)

    #34.)    0         0         0         0         0         0    20230506







    elif argv[1] == '35':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/driscollis/status/1655385736005439489 " )
    #35.)    .         .         .         .         .         .    20230508
    # Find all the prime numbers between 0 and 1000

      print("I came across this interesting tidbit last year about finding prime numbers with #Python")

      print("from functools import reduce")
      from functools import reduce

      list(filter(None,
                  map(lambda y: y * reduce(lambda x, y: x * y != 0,
                                           map(lambda x, y=y: y % x,
                                               range(2, int(pow(y, 0.5) + 1))), 1),
                      range(2, 1000))))

      print("Answer argv[1] == '35': @Twitter https://twitter.com/playfulpython/status/1655439072796749830 " )

    #35.)    0         0         0         0         0         0    20230508







    elif argv[1] == '36':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/s_gruppetta_ct/status/1655607247249227776 " )
    #36.)    .         .         .         .         .         .    20230509
      print ( argv, " : @Twitter https://twitter.com/s_gruppetta_ct/status/1655607247249227776 " )
      print("Don't you love it when you need to fill in a form and some fields are already filled in?")
      print('You can "pre-fill" a function in the same way using `partial()`, which is one of the tools in the functools module')
      print("Here's a brief summary…")

    #36.)    0         0         0         0         0         0    20230509







    elif argv[1] == '37':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1656003789080473601 " )
    #37.)    .         .         .         .         .         .    20230510
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1656003789080473601 " )
      print("Python Question;")
      print("What is the output of this code, and why?🤔🤔")

      print("def my_func(x, y, **kwargs):")
      print("    result = sum((x + y, x * y, x - y, x / y))")
      print('    if "round" in kwargs:')
      print('        return round(result, kwargs["round"])')
      def my_func(x, y, **kwargs):
          result = sum((x + y, x * y, x - y, x / y))
          if "round" in kwargs:
              return round(result, kwargs["round"])

      print("result = my_func(2, 3, round=2)")
      result = my_func(2, 3, round=2)
      print(result)

      print("Output:")
      print("a. 10.666666667")
      print("b. 10.67")
      print("c. (5, 6, -1, 0.67)")
      print("d. error")

      print("def my_func1(x, y, **kwargs):")
      print("    result = sum((x + y, x * y, x - y, x / y))")
      print('    if "round" in kwargs:')
      print('        return round(result, kwargs["round"])')
      def my_func1(x, y, **kwargs):
          print(f"{x:} {y:} {kwargs:}")
          result1 = sum((x + y, x * y, x - y, x / y))
          if "round" in kwargs:
              return round(result1, kwargs["round"])

    #37.)    0         0         0         0         0         0    20230510







    elif argv[1] == '38':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/phases3272/status/16621742252122439689 " )
    #38.)    .         .         .         .         .         .    20230527
      print("Python Pop-Quiz 💡")
      print("Good morning/afternoon/evening, Twitterverse! ")
      print("Let's kick off the weekend with a pop-quiz !🧠🐍")
      print("What will be the output of this code ? #DataScientists")

      numbers = [0, 3, 5, 7, 9, 3, 5, 1, 2]

      for number in numbers:
          if ( even := number % 2 == 0):
              print(f'Found even number: {number=}')
              break
          else:
              print('No even number found')

      print("What will be the output of this program and why ?")
      print("A) Found even number: 0")
      print("B) No even number found")
      print("C) Found even number: True")
      print("D) Found even number: 2")
      print("E) Error")

      for i, number in enumerate(numbers):
          print(f'{i=} Found even number: {number=} {(number % 2)=} {even=}')
          if ( even := number % 2 == 0):
              print(f'Found even number: {number=} {(number % 2)=} {even=}')
    #          break
              continue
          else:
              print('No even number found')
          print(f'{i=} Found even number: {number=} {(number % 2)=} {even=}')

      print(f'Found even number: {number=} {(number % 2)=} {even=}')
      print(f'{i=} Found even number: {number=} {(number % 2)=} {even=}')

    #38.)    0         0         0         0         0         0    20230527







    elif argv[1] == '39':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1666893595616452609 " )
    #39.)    .         .         .         .         .         .    20230609
      import logging
      logger = logging.getLogger(__name__)
      FORMAT = "[%(asctime)s %(levelname)s#  %(name)s %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
      F_NAME = argv[0].split('.')[0] + '.log'
      print(f"{F_NAME=}")
#      if len(argv) >= 5:
      if F_NAME[:4].upper() == 'TEST':
        logging.basicConfig(format=FORMAT)
      else:
#        logging.basicConfig(format=FORMAT, filename='testing.log')
        logging.basicConfig(format=FORMAT, filename=F_NAME)
      logger.setLevel(logging.DEBUG)

      def outer_func(x):
          def inner_func():
              return x
          x -= 2
          return inner_func()

      print(outer_func(5))

      print(f"Output:")
      print(f"a.")
      print(f"b.")
      print(f"c.")
      print(f"d.")

      def outer_func(x):
          logger.info(f'your message {F_NAME=}') 
          logger.info('your message') 
          print(f"{x=}")
          logger.debug(f"{x=}")
          def inner_func():
              print(f"{x=}")
              logger.debug(f"{x=}")
              return x
          print(f"{x=}")
          logger.debug(f"{x=}")
          x -= 2
          print(f"{x=}")
          logger.debug(f"{x=}")
          return inner_func()

      print(outer_func(5))

    #39.)    0         0         0         0         0         0    20230609







    elif argv[1] == '40':
      print ( argv )
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1667926051345817609 " )
    #40.)    .         .         .         .         .         .    20230611
      pdb.set_trace()
      def outer_func(x):
          y = 1 + x
          def inner_func():
              x = 2
              def inner_inner():
                  x = 3
                  return x + y
              return inner_inner
          return inner_func

      results = outer_func(4)
      my_results = results()
      print(my_results() + 2)

      print(f"Output:")
      print(f"a. 8")
      print(f"b. 5")
      print(f"c. 10")
      print(f"d. 4")

    #40.)    0         0         0         0         0         0    20230611














#####    elif argv[1] == '0':
#####      print ( argv )
#####      print ( argv, " : This is NOT Yet Ready " )  # DELETE
#####      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1654227593732804609 " )
#####      pass  # DELETE
#####    #00.)    .         .         .         .         .         .    10101010

#####    #00.)    0         0         0         0         0         0    10101010







    elif argv[1] == '0':
      print ( argv )
      print ( argv, " : This is NOT Yet Ready " )  # DELETE
      print ( argv, " : @Twitter https://twitter.com/RealBenjizo/status/1654227593732804609 " )
      pass  # DELETE
    #00.)    .         .         .         .         .         .    20230604
      # Added on 20230604
      # Python program to display calendar of
      import calendar

      # Dt = str( datetime.today() )
      # Dt = datetime.now()
      # Dt = datetime.today()
      Dt = date.today()

      print(f"{Dt=} {type(Dt)=}\n{Dt.year=} {type(Dt.year)=} {Dt.month=} {type(Dt.month)=} {Dt.day=} {type(Dt.day)=}")
      print("\n\n\n\n\n\n\n\n\n\n\n\n")

      # Dt.year := argv[2]
      # Dt.month := argv[3]

      if len(argv) >= 4:
          print(f"if len(argv) >= 4:\n{Dt.year=} {Dt.month=} {argv[2]=} {argv[3]=}")
          print("\n\n\n\n\n\n\n\n\n\n\n\n")
          print(calendar.month(int(argv[2]), int(argv[3])))
      elif len(argv) >= 3:
          print(f"elif len(argv) >= 3\n{Dt.year=} {type(Dt.year)=} {argv[2]=} {type(argv[2])=}")
          print("\n\n\n\n\n\n\n\n\n\n\n\n")
          print(calendar.calendar(int(argv[2])))
      else:
          print(f"else:\n{len(argv)=} {type(len(argv))=} {Dt.year=} {type(Dt.year)=} {Dt.month=} {type(Dt.month)=}")
          print("\n\n\n\n\n\n\n\n\n\n\n\n")
          print(calendar.month(Dt.year, Dt.month))

      # Added on 20230604

    #00.)    0         0         0         0         0         0    20230604







    else:
      print ( "argv : NOT FIT    > ", argv, "\n" )
      w2clist = [ ('@avarakai',     '31 jan 2020'),
          ('@jgopikrishnan70',      '19-FEB-2020'),
          ('@governorswaraj',       '19 FEB 2020'),
          ('@bababanaras',          '19-FEB-2020'),
          ('@AstroAmigo',           '19-FEB-2020'),
          ('@RulerOfGods1',         '14-jan-2020'),
          ('@nailainayat',          '06  jan 2020'),
          ('@RRRRRRRRRR',           '7  Jan 2020 '),
          ('@CrimeJuris',           'Apr 24, 2020'),
          ('@bluespec',             'Apr 24, 2020'),
          ('@RudraVS',              'Apr 24, 2020'),
          ('@EducateFwd',           'Apr 24, 2020'),
          ('@dabi_tina',            'Apr 24, 2020'),
          ('@ubuntu',               'Apr 30, 2020'),
          ('@gnome',                'Apr 24, 2020'),
          ('@60Minutes',            'Apr 24, 2020'),
          ('@KangriCarrier',        'Apr 24, 2020'),
          ('@RRRRRRRRRR',           '7  Jan 2020 '),
          ('@Indiametdept',         '17-jan-2020'),
          ('@swati_gs',             '09-DEC-2019'),
          ('@RMCpost',              '09-DEC-2019'),
          ('@VashiMant',            '09-DEC-2019'),
          ('@BasantPonwar',         'Jun 25, 2019'),
          ('@Swamy39',              '21-DEC-2019'),
          ('@OfficialDGISPR',       '19-DEC-2019'),
          ('@hujodaddy1',           '18 may 2018'),
          ('@Vidyut',               '24-DEC-2019'),
          ('@sidhant',              '17 JUL 2019'),
          ('@AudreyTruschke',       '17-DEC-2019'),
          ('@peaceforchange',       '17-DEC-2019'),
          ('@Shehla_Rashid',        '17-APR-2019'),
          ('@IJaising',             '09-FEB-2018'),
          ('@Leopard212',           '19-DEC-2019'),
          ('@Snowden',              '19-DEC-2019'),
          ('@nitingokhale',         '18-DEC-2019'),
          ('@BhaavnaArora',         '18-DEC-2019'),
          ('@ANI',                  '31-DEC-2019'),
          ('@tavleen_singh',        '25-DEC-2019') ]
      w2clist.sort(key=lambda pair: pair[0] )
      print ( w2clist )
      print()
      ordered_list = [ i[0] for i in w2clist ]
      # print ( ordered_list )
      for i in ordered_list: print ( i, end = ' : ' )

      w2clist.sort(key=lambda pair: CnvDate ( pair[1] ) )
      print()
      print( len(w2clist) )
      for i in w2clist:
          print ( "{0:^28} : {1}".format( i[0], CnvDate( i[1] ).strftime(" %d %B, %Y - %A") ) )
      print()
      print(f'{i=} {argv=} \nProgram is quitting now')
      sys.exit()    # Added on 20230528


print ( '\n\t STANDARD DETAILS\n1. SYS.ARGV       : ', argv, ',  # of args :', len(argv) )
print ( '2. SYS OS.ENVIRON :  os.environ["PWD"] := ', os.environ['PWD'] )







if __name__ == "__main__":
  print("Hey I am in __name__ == __main__", end="\n\n\n*****\n\n")
  print("argv: ", argv, len(argv))
  print(f'{argv=} {argv[0]=} {argv[1]=} {len(argv)=}')
  print(" __import__(name, globals=None, locals=None, fromlist=(), level=0)¶")
  print("spam = __import__('spam', globals(), locals(), [], 0)")

  F_NAME = argv[0].split('.')[0] + '.log'
  print(f"{F_NAME=}")

  if argv[1] >= '0':
      main(argv)
  else:
    for i in range(99):
        print(f"{i=} argv[{i=}] {type(i)=}")
        print("__import__(testing, globals=None, locals=None, fromlist=(), level=0)")

        argv[1] = str(i)
        print(f'{i=} {argv=} {argv[0]=} {argv[1]=} {str(i)=} {type(i)=}')

        try:
          main(argv)
        except:
          print(f"{argv=} Error raised and I'm in except:")

        finally:
          print(f"{argv=} I'm in finally:", end="\n\n\n\n\n\n\n*******\n\n\n\n\n")
          # subprocess.call(['/bin/bash', 'read -t 30'], shell=True)
          # subprocess.call('read 30', shell=True, timeout=11)
          time.sleep(11)
          print("After time.sleep_11")
          run("read -t 12".split(), shell=True, timeout=100)
