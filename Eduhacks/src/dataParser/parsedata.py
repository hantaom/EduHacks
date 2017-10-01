import argparse

class DataFetcher:
  FilteredArray = []
  Fields = ['NOC', 'Description', 'NOC_Description', 'Industry', 'Variable', 'Geographic Area', 2015, 2016, 2017, 2018,
            2019, 2020, 2021, 2022, 2023, 2024, 2025]
  input1 = None
  input2 = None
  spec = None
  job = None
  location = None
  keyword=None
  def __init__(self):
    parser = argparse.ArgumentParser()
    parser.add_argument('--field', const="field", nargs='?',
                        help='Management,Business')
    parser.add_argument('--education', const="education", nargs='?',
                        help='0-1:University Degree   2-3:Two to three years of post-secondary education at community college   4-5:Completion of secondary school and some short-duration courses     6-7:Short work demonstration or on-the-job training')
    parser.add_argument('--spec', const="spec", nargs='?',
                        help='Management,Business')
    parser.add_argument('--location', const="location", nargs='?',default="British Columbia")
    parser.add_argument('--job', const="job", nargs='?')
    parser.add_argument('--keyword', const="keyword", nargs='?')

    args = parser.parse_args()
    self.input1 = args.field
    self.input2 = args.education
    self.spec = args.spec
    self.job = args.job
    self.location = args.location
    self.keyword = args.keyword

    if self.keyword is not None:
      self.Find_by_keyword()
    else:
      self.Find_by_field_and_Education()

    self.Filter_by_location()

    for item in self.FilteredArray:
      print item
    #print self.FilteredArray




  def Filter_by_location(self):
    index = self.Fields.index("Geographic Area")
    newArray = []
    for array in self.FilteredArray:
      if array[index] == self.location:
        array[self.Fields.index(2025)] = array[self.Fields.index(2025)][:-1]
        newArray.append(array)
    self.FilteredArray = newArray



  def Find_by_keyword(self):
    file =open('2015_2015data.csv')
    for line in file:
      array = line.split(',')
      if array[0] == '#T' or array[0] == 'NOC':
        continue
      for text in array:
        if self.keyword in text or text in self.keyword:
          self.FilteredArray.append(array)
          break




  def Find_by_field_and_Education(self):
    file =open('2015_2015data.csv')
    for line in file:
      array = line.split(',')
      if array[0] == '#T' or array[0] == 'NOC':
        continue
      if (self.input1 is None or self.input1 == array[0][1]) and (self.input2 is None or self.input2 == array[0][2]) and (self.spec is None or self.spec == array[0][3]) and (self.job is None or self.job == array[0][4]):
        self.FilteredArray.append(array)





#actual run time
datafecther = DataFetcher()











# Fields = ['NOC','Description','NOC_Description','Industry','Variable','Geographic Area',2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
# input1 = '0'
# input2 = '0'
#
#
# FilteredArray = []
#
# with open('2015_2015data.csv') as file:
#   for line in file:
#     array = line.split(',')
#     if array[0] == '#T' or array[0] == 'NOC':
#       continue
#     if (input1 is None or input1 == array[0][1]) and (input2 is None or input2 == array[0][2]):
#       FilteredArray.append(array)
#
# print FilteredArray
