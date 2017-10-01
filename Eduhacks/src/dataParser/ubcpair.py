import json

fields = ['Campus','Faculty','Gender','International/Domestic','Measure Names','Primary Subject 1','Primary Subject 1 Code','Program','Session Year','Student Level','Measure Values']


class ubcInsight:

  def __init__(self,major):
    self.major = major
    self.json ={}


  def addLine(self,array):
    pass



  def ToJson( self, major, degree, enrolled, year):
    dict ={}
    dict['id'] = major
    dict['degree'] = degree
    dict['enrolled'] = enrolled
    dict['year'] = year
    return dict


listofUbcInsights = []




