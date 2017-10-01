import json

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--major', const="major", nargs='?',
                    help='Management,Business')

args = parser.parse_args()
Userinput = args.major
#Userinput = 'CIVL'

Fields = ['Campus','Faculty','Gender','International/Domestic','Measure Names','Primary Subject 1','Primary Subject 1 Code','Program','Session Year','Student Level','Measure Values']


class ubcInsight:

  def __init__(self,major):
    self.major = major
    self.json={}


  def addLine(self,array):
    if array[Fields.index('Session Year')] not in self.json:
      self.json[array[Fields.index('Session Year')]] = self.ToJson(array[Fields.index('Primary Subject 1')],array[Fields.index('Program')],array[Fields.index('Measure Values')],array[Fields.index('Session Year')],array[Fields.index('Faculty')])
    else:
      try:
        self.json[array[Fields.index('Session Year')]]['enrolled'] = int(self.json[array[Fields.index('Session Year')]]['enrolled']) + int(array[Fields.index('Measure Values')])
      except:
        # print '='
        # print array[Fields.index('Measure Values')]
        # print self.json[array[Fields.index('Session Year')]]['enrolled']
        # print '---'
        if array[Fields.index('Measure Values')] == '0.0' or array[Fields.index('Measure Values')] == '':
          self.json[array[Fields.index('Session Year')]]['enrolled'] = int(
            self.json[array[Fields.index('Session Year')]]['enrolled'])
          #print 'if'
        elif self.json[array[Fields.index('Session Year')]]['enrolled'] =='0.0' or self.json[array[Fields.index('Session Year')]]['enrolled'] =='':
          self.json[array[Fields.index('Session Year')]]['enrolled'] = array[Fields.index('Measure Values')]
          #print 'elof'
        else:
          self.json[array[Fields.index('Session Year')]]['enrolled'] =0


  def ToJson( self, major, degree, enrolled, year, Faculty):
    dict ={}
    dict['enrolled'] = enrolled
    dict['id'] = major
    dict['degree'] = degree
    dict['year'] = year
    dict['Faculty'] = Faculty
    return dict


ubc = ubcInsight(Userinput)

file =open('ProgramEnrolmentsOverTime_CSV.csv')

a = 0

for line in file:
  if 'Campus' in line: #handles first line
    continue
  index = Fields.index('Measure Values')
  # a+=1
  # if a>200:
  #
  #   break
  array = line.split(',')
  value = array[index][:-1]
  if '.' in value:
    value = value[:value.index('.')]
    value = float(value)
    #value += "k"
  array[index]=value
  #nso far enroll is handled
  #now we sort by fauculty
  index = Fields.index('Primary Subject 1 Code')
  if array[index] == Userinput:
    ubc.addLine(array)
  # if len(array[index]) > 1:
  #   if len(listofUbcInsights)<1 or listofUbcInsights[-1].major != array[index]:
  #       listofUbcInsights.append(ubcInsight(array[index]))
  #   listofUbcInsights[-1].addLine(array)


print ubc.json



