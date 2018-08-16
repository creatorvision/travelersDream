# -*- coding: utf-8 -*-
"""

@author: Nishant
"""
import facebook





class Node:
    def __init__(self,id,name,location,nextNode=None):
        self.id = id
        self.name = name
        self.location = location
        self.nextNode = nextNode
        
    def printNode(self):
       print(self.location)
       print(self.id)
       print(self.name)
         
def getPlaceList(locations_dict):
    for k,v in locations_dict.items():
        if k == "data" and isinstance(v,list)==True:
            return v
    
def locationsAdd(placeList,places):
    if not placeList:
        #print(places)
        placeList = []
    for objs in places:
        for k,v in objs.items():
            if k == "place" and isinstance(v,dict):
               #print(v)
               placeList.append(placeDetails(v))
    #print(placelist)           
    return placeList           

def placeDetails(places):
    #print(places)
    place = dict()
    for key,val in places.items():
        if key == "location" and isinstance(val,dict):
            place = val
        elif key == "name":
            place[key] = val        
    return place
        
token = 'EAADAZAPVj8EgBAJJ4X15UJfZAbd1PBV65EZCIstcgVLu2VQZCZAIVOHcNsWZBNZCtlvyPSA8SWkcVIM9dA2VqjTanBtiZCwI6lZBfzJhHoUmVZCef4c0gbdzSD83hxUKeWtCAEDn09PAnJ0lSTnZBttuiQZCgA3XWKvZBUQwnoZA2ZAADzL7NhCAqZAfIolH1SBhbnLIJMp10z5B3iVfNAZDZD'        
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")

locations_dict = graph.get_object(id='me', fields='tagged_places')
locations_dict = locations_dict['tagged_places']

placelist = []
me = Node(profile['id'],profile['name'],locationsAdd(placelist,getPlaceList(locations_dict)))        
me.printNode()


