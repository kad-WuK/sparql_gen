#%%
import numpy as np
from bidict import bidict
from itertools import combinations
import copy

from rake_nltk import Rake
import spacy
import requests
import json
from spacy import displacy
class subgraphgen:
    def __init__(self):
        self.entityDict = {'Administrative Area':0,'Place':1,'date Created':2,'floor Size':3,'geometry':4,'Postal Address':5,'Postal Code':6,'Street Address':7,'House':8,'Building':9,'Neighbourhood':10,'Woonfunctie':11,'Hotel':12,'Mosque':13,'Church':14,'Castle':15,'Museum':16,'Police station':17,'City Hall':18,'Post office':19,'Woonplaats':20,'Name':21}
        self.linkDict =bidict({'containsPlace':0,'additionalType':1,'Address':2,'geo':3,'dateCreated':4,'floorSize':5,'PostalCode':6,'StreetAddress':7,'name':8})

        self.adjacencyMatrix = np.zeros((len(self.linkDict),len(self.entityDict),len(self.entityDict))).astype(int)

        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Administrative Area'],self.entityDict['Woonplaats']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Administrative Area'],self.entityDict['Neighbourhood']]=1

        self.adjacencyMatrix[self.linkDict['containsPlace'],self.entityDict['Administrative Area'],self.entityDict['Place']]=1
        self.adjacencyMatrix[self.linkDict['geo'],self.entityDict['Administrative Area'],self.entityDict['geometry']]=1
        self.adjacencyMatrix[self.linkDict['name'],self.entityDict['Administrative Area'],self.entityDict['Name']]=1


        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['House']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Building']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Woonfunctie']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Mosque']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Hotel']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Church']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Castle']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Museum']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Police station']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['City Hall']]=1
        self.adjacencyMatrix[self.linkDict['additionalType'],self.entityDict['Place'],self.entityDict['Post office']]=1

        self.adjacencyMatrix[self.linkDict['geo'],self.entityDict['Place'],self.entityDict['geometry']]=1
        self.adjacencyMatrix[self.linkDict['dateCreated'],self.entityDict['Place'],self.entityDict['date Created']]=1
        self.adjacencyMatrix[self.linkDict['floorSize'],self.entityDict['Place'],self.entityDict['floor Size']]=1
        self.adjacencyMatrix[self.linkDict['name'],self.entityDict['Place'],self.entityDict['Name']]=1
        self.adjacencyMatrix[self.linkDict['Address'],self.entityDict['Place'],self.entityDict['Postal Address']]=1


        self.adjacencyMatrix[self.linkDict['PostalCode'],self.entityDict['Postal Address'],self.entityDict['Postal Code']]=1
        self.adjacencyMatrix[self.linkDict['name'],self.entityDict['Postal Address'],self.entityDict['Name']]=1
        self.adjacencyMatrix[self.linkDict['StreetAddress'],self.entityDict['Postal Address'],self.entityDict['Street Address']]=1


    def remove_repeat(self,list):
        temp = []
        for item in list:
            if item not in temp:
                temp.append(item)
        return temp
    def word_similarity(self,word1,word2, NER):
        doc = NER(word1)
        doc2 = NER(word2)
        #print(word1,word2,doc.similarity(doc2))
        return doc.similarity(doc2)
    def getSurface(self,text,nlp,entities):
        doc = nlp(text)
        surfaceDict = []
        #print(text)
        rake_nltk_var = Rake()
        print(doc.ents)
        rake_nltk_var.extract_keywords_from_text(text)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()
        #print(keyword_extracted)
        for keyword in doc.ents:
            request = "https://data.labs.kadaster.nl/_api/datasets/kadaster/kg/services/search/search?query=" + str(keyword)[0].upper()+str(keyword)[1:]
            r = requests.get(request, headers={"content-type": "application/json"})
            respond = json.loads(r.text)
            resList = []
            #print(respond['hits']['hits'])
            if len(respond['hits']['hits']) != 0:
                
                max = 0
                for item in respond['hits']['hits']:
                    if item['_score']>=25 and item['_score'] >= max:
                        max = item['_score']
                        resList.append(item)
                    else:
                        break
                #if respond['hits']['hits'][0]['_score'] >= 25:
                if len(resList)!=0:
                    respond = json.loads(r.text)
                    for res in resList:
                        if 'http://www w3 org/1999/02/22-rdf-syntax-ns#type' in res['_source']:
                           
                            #type = respond['hits']['hits'][0]['_source']['http://www w3 org/1999/02/22-rdf-syntax-ns#type'][0].split('/')[-1]
                            type = res['_source']['http://www w3 org/1999/02/22-rdf-syntax-ns#type'][0].split('/')[-1]
                            if type == 'AdministrativeArea':
                                type = 'Administrative Area'
                            surfaceDict.append([(type,)])
                            break
                        else:
                            continue
        for keyword in keyword_extracted:
            max = 0.47
            target = 'None'
            for entity in entities:
                #print(keyword,entity,word_similarity(keyword,entity, nlp))
                if self.word_similarity(keyword,entity, nlp) > max:
                    #max = self.word_similarity(keyword,entity, nlp)
                    target = entity
                    max = self.word_similarity(keyword,entity, nlp)
            if target != 'None':
                surfaceDict.append([(target,)])
        return self.remove_repeat(surfaceDict)



    def expand_surface(self,surfaceDict):
        surfaceDict_temp = copy.deepcopy(surfaceDict)
        lenSurfaceDict = []
        allowed = ['Place','Postal Address','AdministrativeArea']
        for suface in surfaceDict:
            lenSurfaceDict.append(len(suface))
        for tri in surfaceDict[lenSurfaceDict.index(min(lenSurfaceDict))]:
            for entity in tri:
                if entity == 'PostalAddress':
                    entity = 'Postal Address'
                # elif entity == 'Administrative Area':
                #     print('entity == Administrative Area')
                #     entity = 'AdministrativeArea'
                incoming = []
                for i in np.where(self.adjacencyMatrix[:,:,self.entityDict[entity]]==1)[1]:
                    incoming.append(list(self.entityDict.keys())[i])
                if len(incoming) != 0:
                    items = []
                    for item in incoming:
                        if item not in allowed:
                            items.append(item)
                    for item in items:
                        incoming.remove(item)
                    for in_ in incoming:
                        if (in_,entity) not in surfaceDict_temp[lenSurfaceDict.index(min(lenSurfaceDict))]:
                            surfaceDict_temp[lenSurfaceDict.index(min(lenSurfaceDict))].append((in_,entity))                
                outgoing = []
                for i in np.where(self.adjacencyMatrix[:,self.entityDict[entity],:]==1)[1]:
                    outgoing.append(list(self.entityDict.keys())[i])
                if len(outgoing) !=0:
                    items = []
                    for item in outgoing:
                        if item not in allowed:
                            items.append(item)
                    for item in items:
                        outgoing.remove(item)
                    for out in outgoing:
                        if (entity,out) not in surfaceDict_temp[lenSurfaceDict.index(min(lenSurfaceDict))]:
                            surfaceDict_temp[lenSurfaceDict.index(min(lenSurfaceDict))].append((entity,out))
            if len(tri)==1:
                surfaceDict_temp[lenSurfaceDict.index(min(lenSurfaceDict))].remove(tri)
        surfaceDict = surfaceDict_temp
        return surfaceDict


    def merge_surfaces(self,surfaceDict):
        
        prevLen = len(surfaceDict)
        for comb_surface in combinations(surfaceDict,r=2):
            merged = False
            for tri in comb_surface[0]:
                for entity in tri:
                    outgoing = []
                    # if len(np.where(self.adjacencyMatrix[:,self.entityDict[entity],:]==1)) == 0:
                    if entity == 'PostalAddress':
                        entity = 'Postal Address'
                    # elif entity == 'Administrative Area':
                    #     entity = 'AdministrativeArea'
                    for i in np.where(self.adjacencyMatrix[:,self.entityDict[entity],:]==1)[1]:
                        outgoing.append(list(self.entityDict.keys())[i])
                    for matching in comb_surface[1]:
                        for out in outgoing:
                            if out in matching:
                                linkingTri = [(entity,out)]
                                if (len(comb_surface[0][0])==1) and (len(comb_surface[1][0])==1):
                                    merged_surface = linkingTri
                                elif len(comb_surface[0][0]) == 1:

                                    merged_surface = linkingTri + comb_surface[1]

                                elif len(comb_surface[1][0]) == 1:

                                    merged_surface = comb_surface[0] + linkingTri

                                else:
                                    merged_surface = comb_surface[0] + linkingTri + comb_surface[1]

                                surfaceDict.remove(comb_surface[0])
                                surfaceDict.remove(comb_surface[1])
                                surfaceDict.append(merged_surface)
                                merged = True
                                break
                        if merged == True:
                            break                
                    if merged == True:
                        break                
                if merged == True:
                    break
                else:
                    for entity in tri:
                        if entity == 'PostalAddress':
                            entity = 'Postal Address'
                        # elif entity == 'Administrative Area':
                        #     entity = 'AdministrativeArea'
                        incoming = []
                        for i in np.where(self.adjacencyMatrix[:,:,self.entityDict[entity]]==1)[1]:
                            incoming.append(list(self.entityDict.keys())[i])
                        for matching in comb_surface[1]:
                            for in_ in incoming:
                                if in_ in matching:
                                    linkingTri = [(in_,entity)]
                                    if (len(comb_surface[0][0])==1) and (len(comb_surface[1][0])==1):
                                        merged_surface = linkingTri
                                    elif len(comb_surface[0][0]) == 1:
                                        merged_surface = linkingTri + comb_surface[1]
                                    elif len(comb_surface[1][0]) == 1:
                                        merged_surface = comb_surface[0] + linkingTri
                                    else:
                                        merged_surface = comb_surface[0] + linkingTri + comb_surface[1]
                                    surfaceDict.remove(comb_surface[0])
                                    surfaceDict.remove(comb_surface[1])
                                    surfaceDict.append(merged_surface)
                                    merged = True
                                    break
                            if merged == True:
                                break
                        
                        if merged == True:
                            break                        
            if (merged == True):
                break
        if len(surfaceDict) == 1:
            return surfaceDict 
        elif len(surfaceDict) == prevLen:
            #print('surfaceDict:',surfaceDict)
            surfaceDict = self.expand_surface(surfaceDict)
            surfaceDict = self.merge_surfaces(surfaceDict)
            return self.merge_surfaces(surfaceDict)
        else:
            return self.merge_surfaces(surfaceDict)
    def to_description(self,surfaceDict):
        des = ''
        for tri in surfaceDict[0]:
            if len(tri) == 1:
                return des
            link_index = np.where(self.adjacencyMatrix[:,self.entityDict[tri[0]],self.entityDict[tri[1]]]==1)[0][0]
            link = list(self.linkDict.keys())[link_index]
            des = des + tri[0] + ', '+ link+ ', '+ tri[1] +'\n'
        return des
        # for i in np.where(self.adjacencyMatrix[:,:,self.entityDict[entity]]==1)[1]:
        #         incoming.append(list(self.entityDict.keys())[i])

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_md")
    text='Show the administrative area that street address Victoriapark 612 located in.'

    entities = ['Administrative Area','Place','date Created','floor Size','geometry','Postal Address','Postal Code','Street Address','House','Building','Neighbourhood','Woonfunctie','Hotel','Mosque','Church','Castle','Museum','Police station','City Hall','Post office','Woonplaats','Name']
    s = subgraphgen()
    surfaceDict = s.getSurface(text,nlp,entities)
    print(surfaceDict)
    surfaceDict = s.merge_surfaces(surfaceDict)
    #print(surfaceDict)
    des = s.to_description(surfaceDict)
    print(des)






#%%

import numpy as np
from bidict import bidict
from itertools import combinations
import copy

from rake_nltk import Rake
import spacy
import requests
import json
from spacy import displacy

nlp = spacy.load("en_core_web_md")
def word_similarity(word1,word2, NER):
    doc = NER(word1)
    doc2 = NER(word2)
    #print(word1,word2,doc.similarity(doc2))
    return doc.similarity(doc2)
#%%
word_similarity('located in','address locality',nlp)