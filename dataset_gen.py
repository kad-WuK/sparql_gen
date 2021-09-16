#%%
import pandas as pd
import random
import string
cityList = pd.read_csv('cities.csv')['u_1']
streetaddresses = pd.read_csv('streetaddress.csv')['streetAddress']
exampleList = []
smaple_count = 50
from gen import subgraphgen
import spacy
nlp = spacy.load("en_core_web_md")
#text='Show all hotels and police stations in Eindhoven'
entities = ['Administrative Area','Place','date Created','floor Size','geometry','Postal Address','Postal Code','Street Address','House','Building','Neighbourhood','Woonfunctie','Hotel','Mosque','Church','Castle','Museum','Police station','City Hall','Post office','Woonplaats','Name']
s = subgraphgen()

def postcode_gen():
    number = random.randint(1000,9999)
    alphabet = string.ascii_uppercase
    s1 = random.choice(alphabet)
    s2 = random.choice(alphabet)
    postcode = str(number)+s1+s2
    return postcode


# qPattern = "Show me the geometry of {}."
# sampledList = cityList
# selectedCities = []
def generate_description(question):
    #print(question)
    #question = qPattern.format(city)
    #print(question)
    surfaceDict = s.getSurface(question,nlp,entities)
    #print(surfaceDict)
    surfaceDict = s.merge_surfaces(surfaceDict)
    #print(surfaceDict)
    des = s.to_description(surfaceDict)
    return des
        #print(des)
        # if des == 'AdministrativeArea, geo, geometry\n':
        #     selectedCities.append(city)
#print(selectedCities)
# dict = {'u_1': selectedCities} 
# df = pd.DataFrame(dict)
# df.to_csv('selectedCities.csv',index=False)



#Show the number of hotels in each administrative area.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of hotels in each administrative area."
qList.append(qPattern)
qPattern = "The number of hotels group by administrative area."
qList.append(qPattern)
qPattern = "How many hotels in each administrative area."
qList.append(qPattern)
qPattern = "Show the number of hotels in the Netherlands group by administrative area."
qList.append(qPattern)

#streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    #for streetaddress in streetaddressList:
    question = q
    type = generate_description(question)
    print(type)
    query = 'SELECT DISTINCT ?name (COUNT(?address) as ?number) WHERE {?city rdf:type schema:AdministrativeArea. ?city schema:name ?name. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:hotel.} GROUP BY ?name'
    example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
    exampleList.append(example)
    #streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)




#Show the number of museums in each administrative area.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of museums in each administrative area."
qList.append(qPattern)
qPattern = "The number of museums in each administrative area."
qList.append(qPattern)
qPattern = "How many museums in each administrative area."
qList.append(qPattern)
qPattern = "Show the number of museums in the Netherlands group by administrative area."
qList.append(qPattern)

#streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    #for streetaddress in streetaddressList:
    question = q
    type = generate_description(question)
    query = 'SELECT DISTINCT ?name (COUNT(?address) as ?number) WHERE {?city rdf:type schema:AdministrativeArea. ?city schema:name ?name. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:museum.} GROUP BY ?name'
    example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
    exampleList.append(example)
    #streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)






#Given a street address, return Mosques in the administrative area it is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the mosques of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What are the mosques in the administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Mosques in administrative area where street address {} located in."
qList.append(qPattern)
qPattern = "Show mosques of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show mosques of the administrative area where street address {} is located."
qList.append(qPattern)

#streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(streetaddress,'moskee')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)







#Given a street address, return Churches in the administrative area it is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the churches of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What are the churches in the administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Churches in administrative area where street address {} located in."
qList.append(qPattern)
qPattern = "Show churches of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show churches of the administrative area where street address {} is located."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(streetaddress,'kerk')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)





#Given a street address, return the post offices in the administrative area it is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the post offices of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What are the post offices in the administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Post office in administrative area where street address {} located in."
qList.append(qPattern)
qPattern = "Show post office of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show post offices of the administrative area where street address {} is located."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(streetaddress,'postkantoor')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)



#Given a street address, return the hotels in the administrative area it is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the hotels of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What are the hotels in the administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Hotels in administrative area where street address {} located in."
qList.append(qPattern)
qPattern = "Show hotels of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show hotels of the administrative area where street address {} is located."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(streetaddress,'hotel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)





#Given a street address, return the museums in the administrative area it is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the museums of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What is the museums in the administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Museum in administrative area where street address {} located in."
qList.append(qPattern)
qPattern = "Show museums of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show museums of the administrative area where street address {} is located."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(streetaddress,'museum')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)




#Given a street address, return the geometry of the administrative area it located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the geometry of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What is the geometry of administrative area that street address {} in?"
qList.append(qPattern)
qPattern = "Geometry of administrative area where street address {} located in."
qList.append(qPattern)
qPattern = "Show geometry of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show geometry of the administrative area where street address {} is located."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?geo WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:geo ?geo }}'.format(streetaddress)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#Given a street address, return number of places of administrative area it located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show number of places of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "How many places of administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Number of places of administrative area where {} located in."
qList.append(qPattern)
qPattern = "Show number of palces of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show number of places of administrative area that street address {} located in."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?places) as ?number) WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places.}}'.format(streetaddress)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

##############################
#Given a street address, return places of administrative area it located, floor size smaller than a upper bound.
type = 'AdministrativeArea'
qList = []

qPattern = "Show places of administrative area where street address {} is in, floor size smaller than {}"
qList.append(qPattern)
qPattern = "What are places of administrative area that street address {} is in, the floor size should smaller than {} m2"
qList.append(qPattern)
qPattern = "Places of administrative area where {} located in, floor size smaller than {} squared meters"
qList.append(qPattern)
qPattern = "Show palces of administrative area that street adress {} in, the floor size should smaller than {} m2"
qList.append(qPattern)
qPattern = "Show places of administrative area that street address {} located in, floor size no larger than {}."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    lower_size = random.randint(50,200)
    upper_size = random.randint(200,500)
    lower_year = random.randint(1800,1950)
    upper_year = random.randint(1950,2021)
    for streetaddress in streetaddressList:
        question = q.format(streetaddress,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:floorSize ?floorsize. FILTER(?floorsize <= {})}}'.format(streetaddress,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#Given a street address, return places of administrative area it located, floor size larger than a lower bound.
type = 'AdministrativeArea'
qList = []

qPattern = "Show places of administrative area where street address {} is in, floor size larger than {}"
qList.append(qPattern)
qPattern = "What are places of administrative area that street address {} is in, the floor size should bigger than {} m2"
qList.append(qPattern)
qPattern = "Places of administrative area where {} located in, floor size bigger than {} squared meters"
qList.append(qPattern)
qPattern = "Show palces of administrative area that street adress {} in, the floor size should larger than {} m2"
qList.append(qPattern)
qPattern = "Show places of administrative area that street address {} located in, floor size no smaller than {}."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    lower_size = random.randint(50,200)
    upper_size = random.randint(200,500)
    lower_year = random.randint(1800,1950)
    upper_year = random.randint(1950,2021)
    for streetaddress in streetaddressList:
        question = q.format(streetaddress,lower_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:floorSize ?floorsize. FILTER(?floorsize >= {})}}'.format(streetaddress,lower_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#Given a street address, return places of administrative area it located, floor size between a interval.
type = 'AdministrativeArea'
qList = []

qPattern = "Show places of administrative area where street address {} is in, floor size between {} and {}."
qList.append(qPattern)
qPattern = "What are places of administrative area that street address {} is in, the floor size should bigger than {} but smaller than {}"
qList.append(qPattern)
qPattern = "Places of administrative area where {} located in, floor size between {} and {} squared meters"
qList.append(qPattern)
qPattern = "Show palces of administrative area that street adress {} in, the floor size should between {} and {} m2"
qList.append(qPattern)
qPattern = "Show places of administrative area that street address {} located in, floor size between {} and {}."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    lower_size = random.randint(50,200)
    upper_size = random.randint(200,500)
    lower_year = random.randint(1800,1950)
    upper_year = random.randint(1950,2021)
    for streetaddress in streetaddressList:
        question = q.format(streetaddress,lower_size,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {})}}'.format(streetaddress,lower_size,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#Given a street address, return places of administrative area it located, date created later than a lower bound.
type = 'AdministrativeArea'
qList = []

qPattern = "Show places of administrative area where street address {} is in, date created earlier than {}."
qList.append(qPattern)
qPattern = "What are places of administrative area that street address {} is in, date created should earlier than {}."
qList.append(qPattern)
qPattern = "Places of administrative area where {} located in, date created should earlier than {}."
qList.append(qPattern)
qPattern = "Show palces of administrative area that street adress {} in, date created no later than than {}"
qList.append(qPattern)
qPattern = "Show places of administrative area that street address {} located in, date created should earlier than {}."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    lower_size = random.randint(50,200)
    upper_size = random.randint(200,500)
    lower_year = random.randint(1800,1950)
    upper_year = random.randint(1950,2021)
    for streetaddress in streetaddressList:
        question = q.format(streetaddress,lower_year)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:dateCreated ?datecreated. FILTER(?datecreated >= {})}}'.format(streetaddress,lower_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#Given a street address, return places of administrative area it located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show places of administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What are places of administrative area that street address {} is in?"
qList.append(qPattern)
qPattern = "Places of administrative area where {} located in."
qList.append(qPattern)
qPattern = "Show palces of administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show places of administrative area that street address {} located in."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places.}}'.format(streetaddress)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)







#Given a street address, return the administrative area it located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show administrative area where street address {} is in."
qList.append(qPattern)
qPattern = "What administrative area is street address {} in?"
qList.append(qPattern)
qPattern = "Administrative area where {} located in."
qList.append(qPattern)
qPattern = "Show administrative area that street adress {} in."
qList.append(qPattern)
qPattern = "Show the administrative area that street address {} located in."
qList.append(qPattern)

streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for q in qList:
    for streetaddress in streetaddressList:
        question = q.format(streetaddress)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?name WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:streetAddress "{}"@nl. ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. }}'.format(streetaddress)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    streetaddressList = streetaddresses.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)





#Given a post code, return hotel of the administrative area where this post code is located
type = 'AdministrativeArea'
qList = []

qPattern = "Show hotel of the administrative area where postal code {} is in."
qList.append(qPattern)
qPattern = "What are the hotel in the administrative area that {} in?"
qList.append(qPattern)
qPattern = "Hotels in the administrative area where {} located in."
qList.append(qPattern)
qPattern = "Show hotels of the administrative area that postal address {} in."
qList.append(qPattern)
qPattern = "Show hotels in the administrative area that postal address {} located in."
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode)
        type = generate_description(question)
        print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(postcode,'hotel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)

#Given a post code, return museums of the administrative area where this post code is located
type = 'AdministrativeArea'
qList = []

qPattern = "Show museums of the administrative area where postal code {} is in."
qList.append(qPattern)
qPattern = "What are the museums in the administrative area that {} in?"
qList.append(qPattern)
qPattern = "Museums in the administrative area where {} located in."
qList.append(qPattern)
qPattern = "Show museum of the administrative area that postal address {} in."
qList.append(qPattern)
qPattern = "Show museums in the administrative area that postal address {} located in."
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode)
        type = generate_description(question)
        print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:additionalType typeBuilding:{}. }}'.format(postcode,'museum')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)





#Given a post code, return places of the administrative area where this postal address is located, with floor size and date created have a upper bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in, floor size should smaller than {}, date created earlier than {}"
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in that floor size smaller than {}, , date created earlier than {}?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in with floor size no larger than {} and date created smaller than {}"
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in, floor size should smaller than {} and date created no later than {}"
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in, floor size smaller than {}, date created earlier than {}"
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,upper_size,upper_year)
        type = generate_description(question)
        print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:floorSize ?floorsize. FILTER(?floorsize <= {}). ?places schema:dateCreated ?datecreated. FILTER(?datecreated <= {})}}'.format(postcode,lower_size,lower_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)





#Given a post code, return places of the administrative area where this postal address is located, with floor size and date created have a lower bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in, floor size should larger than {}, date created later than {}"
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in that floor size bigger than {}, date created later than {}?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in with floor size no smaller than {} and date created larger than {}"
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in, floor size should bigger than {} and date created no earlier than {}"
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in, floor size lager than {}, date created later than {}"
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,lower_size,lower_year)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:floorSize ?floorsize. FILTER(?floorsize >= {}). ?places schema:dateCreated ?datecreated. FILTER(?datecreated >= {})}}'.format(postcode,lower_size,lower_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)



#Given a post code, return places of the administrative area where this postal address is located, with floor size have a lower bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in, floor size should larger than {}"
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in that floor size bigger than {}?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in with floor size no smaller than {}"
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in, floor size should bigger than {}"
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in, floor size lager than {}"
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,lower_size)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:floorSize ?floorsize. FILTER(?floorsize >= {})}}'.format(postcode,lower_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)

#Given a post code, return places of the administrative area where this postal address is located, with floor size have a upper bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in, floor size should earlier than {}"
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in that floor size smaller than {}?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in with floor size no later than {}"
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in, floor size should earlier than {}"
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in, floor size smaller than {}"
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,upper_size)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:dateCreated ?datecreated. FILTER(?datecreated <= {})}}'.format(postcode,upper_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)








#Given a post code, return places of the administrative area where this postal address is located, with date created have a lower bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in, date created should larger than {}"
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in that date created later than {}?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in with date created no earlier than {}"
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in, date created should later than {}"
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in, date created later than {}"
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,lower_year)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:dateCreated ?datecreated. FILTER(?datecreated >= {})}}'.format(postcode,lower_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)

#Given a post code, return places of the administrative area where this postal address is located, with date created have a upper bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in, date created should earlier than {}"
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in that date created smaller than {}?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in with date created no later than {}"
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in, date created should earlier than {}"
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in, date created smaller than {}"
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,upper_year)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. ?places schema:dateCreated ?datecreated. FILTER(?datecreated <= {})}}'.format(postcode,upper_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)


#Given a post code, return the number of places of the administrative area where this postal address is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in."
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in."
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in."
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in."
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        question = q.format(postcode)
        type = generate_description(question)
        #print(type)
        #print(postcode)
        query = 'SELECT DISTINCT ?name (COUNT(?places) as ?number) WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. }}'.format(postcode)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)



#Given a post code, return places of the administrative area where this postal address is located.
type = 'AdministrativeArea'
qList = []

qPattern = "Show palces of administrative area where post code {} is in."
qList.append(qPattern)
qPattern = "What are the palces in the administrative area that postal address {} in?"
qList.append(qPattern)
qPattern = "The palces in the administrative area where postal address {} located in."
qList.append(qPattern)
qPattern = "Show places of the administrative area that postal address {} in."
qList.append(qPattern)
qPattern = "Show the places of the administrative area that postal address {} located in."
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        question = q.format(postcode)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name ?places WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name. ?administrativearea schema:containsPlace ?places. }}'.format(postcode)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)





#Given a post code, return the administrative area where this postal address located in.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the administrative area where post code {} is located."
qList.append(qPattern)
qPattern = "Which administrative area does postal address {} in?"
qList.append(qPattern)
qPattern = "The city that postal address {} located in."
qList.append(qPattern)
qPattern = "Show the administrative area that postal address {} located in."
qList.append(qPattern)
qPattern = "Show the name of the administrative area that postal address {} located in."
qList.append(qPattern)

postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        question = q.format(postcode)
        type = generate_description(question)
        #print(type)
        print(postcode)
        query = 'SELECT DISTINCT ?name WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name}}'.format(postcode)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)



# #Given a post code, return the administrative area where this postal address located in.
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show the administrative area where post code {} is located."
# qList.append(qPattern)
# qPattern = "Which administrative area does postal address {} in?"
# qList.append(qPattern)
# qPattern = "The city that postal address {} located in."
# qList.append(qPattern)
# qPattern = "Show the administrative area that postal address {} located in."
# qList.append(qPattern)
# qPattern = "Show the name of the administrative area that postal address {} located in."
# qList.append(qPattern)

# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         question = q.format(postcode)
#         type = generate_description(question)
#         #print(type)
#         print(postcode)
#         query = 'SELECT DISTINCT ?name WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name}}'.format(postcode)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)



#Show all postal addresses with a given postal code.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all postal addresses with postal code {}."
qList.append(qPattern)
qPattern = "Show addresses of post code {}"
qList.append(qPattern)
qPattern = "The postal addresses that have postal code {}."
qList.append(qPattern)
qPattern = "Return all postal addresses with post code {}."
qList.append(qPattern)


postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        question = q.format(postcode)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?postaladdress  WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}".}}'.format(postcode)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)


#Show all postal addresses with a given postal code, floor size smaller than a upper bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show all postal addresses with postal code {}, floor size smaller than {}."
qList.append(qPattern)
qPattern = "Show addresses of post code {} with floor size smaller than {}"
qList.append(qPattern)
qPattern = "The postal addresses that have postal code {} with floor size no larger than {}."
qList.append(qPattern)
qPattern = "Return all postal addresses with post code {}, with floor size smaller than {}."
qList.append(qPattern)


postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(10,500)
        upper_size = random.randint(500,1000)
        question = q.format(postcode,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?postaladdress ?floorsize WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:floorSzie ?floorsize. FILTER(?floorsize <= {}) }}'.format(postcode,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)



#Show all postal addresses with a given postal code, floor size larger than a lower bound
type = 'AdministrativeArea'
qList = []

qPattern = "Show all postal addresses with postal code {}, floor size larger than {}."
qList.append(qPattern)
qPattern = "Show addresses of post code {} with floor size bigger than {}"
qList.append(qPattern)
qPattern = "The postal addresses that have postal code {} with floor size larger than {}."
qList.append(qPattern)
qPattern = "Return all postal addresses with post code {}, with floor size no smaller than {}."
qList.append(qPattern)


postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(10,500)
        upper_size = random.randint(500,1000)
        question = q.format(postcode,lower_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?postaladdress ?floorsize WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:floorSzie ?floorsize. FILTER(?floorsize >= {}) }}'.format(postcode,lower_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)


#Show all postal addresses with a given postal code, date created larger than a lower bound.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all postal addresses with postal code {}, date created later than {}."
qList.append(qPattern)
qPattern = "Show addresses of post code {} with date created later than {}"
qList.append(qPattern)
qPattern = "The postal addresses that have postal code {} with date created after {}."
qList.append(qPattern)
qPattern = "Return all postal addresses with post code {}, with date created no earlier than {}."
qList.append(qPattern)


postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,lower_year)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?postaladdress ?datecreated WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:dateCreated ?datecreated. FILTER(?datecreated >= {}) }}'.format(postcode,lower_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)

#Show all postal addresses with a given postal code, date created earlier than a upper bound.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all postal addresses with postal code {}, date created earlier than {}."
qList.append(qPattern)
qPattern = "Show addresses of post code {} with date created earlier than {}"
qList.append(qPattern)
qPattern = "The postal addresses that have postal code {} with date created earlier than {}."
qList.append(qPattern)
qPattern = "Return all postal addresses with post code {}, with date created no later than {}."
qList.append(qPattern)


postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,upper_year)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?postaladdress ?datecreated WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:dateCreated ?datecreated. FILTER(?datecreated <= {}) }}'.format(postcode,upper_year)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)


#Show all postal addresses with a given postal code, date created earlier than a upper bound, floor size smaller than a upper bound.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all postal addresses with postal code {}, date created earlier than {}, floor size smaller than {}."
qList.append(qPattern)
qPattern = "Show addresses of post code {} with date created earlier than {}, floor size smaller than {}"
qList.append(qPattern)
qPattern = "The postal addresses that have postal code {} with date created earlier than {}, floor size smaller than {}."
qList.append(qPattern)
qPattern = "Return all postal addresses with post code {}, with date created no later than {}, floor size no larger than {}."
qList.append(qPattern)


postcodeList = []
for i in range(20):
    postcode = postcode_gen()
    postcodeList.append(postcode)
for q in qList:
    for postcode in postcodeList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(postcode,upper_year,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?postaladdress ?datecreated WHERE {{?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:dateCreated ?datecreated. FILTER(?datecreated <= {}). ?place schema:floorSzie ?floorsize. FILTER(?floorsize <= {}). }}'.format(postcode,upper_year,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    postcodeList = []
    for i in range(20):
        postcode = postcode_gen()
        postcodeList.append(postcode)


# Show all police stations, post offices and Mosques of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all police stations, post offices and mosques of {}."
qList.append(qPattern)
qPattern = "Give me all post offices, police stations and mosques of {}."
qList.append(qPattern)
qPattern = "Where are all mosques, police stations and post offices in {}?"
qList.append(qPattern)
qPattern = "Police stations, post offices and mosques in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?policestation ?postoffice ?mosque WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?policestation. ?city schema:containsPlace ?postoffice. ?city schema:containsPlace ?mosque. ?policestation schema:additionalType typeBuilding:politiebureau. ?mosque schema:additionalType typeBuilding:moskee. ?postoffice schema:additionalType typeBuilding:postkantoor. }}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)




# Show all police stations and Mosques of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all police stations and mosques of {}."
qList.append(qPattern)
qPattern = "Give me all police stations and mosques of {}."
qList.append(qPattern)
qPattern = "Where are all mosques and police stations in {}?"
qList.append(qPattern)
qPattern = "Police stations, mosques in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?policestation ?mosque WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?policestation. ?city schema:containsPlace ?mosque. ?policestation schema:additionalType typeBuilding:politiebureau. ?mosque schema:additionalType typeBuilding:moskee. }}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)




# Show all Castles and police stations of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all police stations and castles of {}."
qList.append(qPattern)
qPattern = "Give me all police stations and castles of {}."
qList.append(qPattern)
qPattern = "Where are all castles and police stations in {}?"
qList.append(qPattern)
qPattern = "Police stations, castles in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?castle ?policestation WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?castle. ?city schema:containsPlace ?policestation. ?castle schema:additionalType typeBuilding:kasteel. ?policestation schema:additionalType typeBuilding:politiebureau. }}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)




# Show all Churches and Castles of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches and castles of {}."
qList.append(qPattern)
qPattern = "Give me all churches and castles of {}."
qList.append(qPattern)
qPattern = "Where are all castles and churches in {}?"
qList.append(qPattern)
qPattern = "Churches, castles in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?castle ?church WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?castle. ?city schema:containsPlace ?church. ?castle schema:additionalType typeBuilding:kasteel. ?church schema:additionalType typeBuilding:kerk. }}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)





# Show all museums, hotels and churches of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches, museums and hotels of {}."
qList.append(qPattern)
qPattern = "Give me all hotels, churches and museums of {}."
qList.append(qPattern)
qPattern = "Where are all museums, hotels and churches in {}?"
qList.append(qPattern)
qPattern = "Churches, hotels and museums in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?museum ?church ?hotel WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?museum. ?city schema:containsPlace ?church. ?city schema:containsPlace ?hotel. ?church schema:additionalType typeBuilding:kerk. ?museum schema:additionalType typeBuilding:museum. ?hotel schema:additionalType typeBuilding:hotel.}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)






# Show all museums and churches of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches and museums of {}."
qList.append(qPattern)
qPattern = "Give me all churches and museums of {}."
qList.append(qPattern)
qPattern = "Where are all museums and churches in {}?"
qList.append(qPattern)
qPattern = "Churches and museums in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?museum ?church WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?museum. ?city schema:containsPlace ?church. ?church schema:additionalType typeBuilding:kerk. ?museum schema:additionalType typeBuilding:museum.}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)



# Show all hotels and churches of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches and hotels of {}."
qList.append(qPattern)
qPattern = "Give me all hotels, churches of {}."
qList.append(qPattern)
qPattern = "Where are all hotels and churches in {}?"
qList.append(qPattern)
qPattern = "Churches and hotels in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?church ?hotel WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?museum. ?city schema:containsPlace ?hotel. ?church schema:additionalType typeBuilding:kerk. ?hotel schema:additionalType typeBuilding:hotel.}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)





# Show all museums and hotels of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all museums and hotels of {}."
qList.append(qPattern)
qPattern = "Give me all hotels, museums of {}."
qList.append(qPattern)
qPattern = "Where are all hotels and museums in {}?"
qList.append(qPattern)
qPattern = "Museums and hotels in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?museum ?hotel WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?museum. ?city schema:containsPlace ?hotel. ?museum schema:additionalType typeBuilding:museum. ?hotel schema:additionalType typeBuilding:hotel.}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)







# Show all hotels of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all hotels of {}."
qList.append(qPattern)
qPattern = "Give me all hotels of {}."
qList.append(qPattern)
qPattern = "Where are all hotels in {}?"
qList.append(qPattern)
qPattern = "Hotels in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'hotel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show all police stations of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all police stations of {}."
qList.append(qPattern)
qPattern = "Give me all police stations of {}."
qList.append(qPattern)
qPattern = "Where are all police stations in {}?"
qList.append(qPattern)
qPattern = "Police stations in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'politiebureau')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show all post offices of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all post offices of {}."
qList.append(qPattern)
qPattern = "Give me all post stations of {}."
qList.append(qPattern)
qPattern = "Where are all post offices in {}?"
qList.append(qPattern)
qPattern = "Post stations in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'politiebureau')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show all Churches of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches of {}."
qList.append(qPattern)
qPattern = "Give me all churches of {}."
qList.append(qPattern)
qPattern = "Where are all churches in {}?"
qList.append(qPattern)
qPattern = "Churches in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'kerk')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all Castles of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all castles of {}."
qList.append(qPattern)
qPattern = "Give me all castles of {}."
qList.append(qPattern)
qPattern = "Where are all castles in {}?"
qList.append(qPattern)
qPattern = "Castles in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'kasteel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all Mosques of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all mosques of {}."
qList.append(qPattern)
qPattern = "Give me all mosques of {}."
qList.append(qPattern)
qPattern = "Where are all mosques in {}?"
qList.append(qPattern)
qPattern = "Mosques in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'moskee')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all museums of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all museums of {}."
qList.append(qPattern)
qPattern = "Give me all museums of {}."
qList.append(qPattern)
qPattern = "Where are all museums in {}?"
qList.append(qPattern)
qPattern = "Museums in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'museum')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show town hall of a city.
type = 'AdministrativeArea'
qList = []

qPattern = "Show town hall of {}."
qList.append(qPattern)
qPattern = "Give me town hall of {}."
qList.append(qPattern)
qPattern = "Where are the town hall of {}?"
qList.append(qPattern)
qPattern = "Town hall in {}"
qList.append(qPattern)
qPattern = "Show municipality in {}"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}.}}'.format(city,'gemeentehuis')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all museums of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all museums of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give me all museums of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are all museums in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Museums in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'museum')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#%%
# Show all Castles of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all castles of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give me all castles of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are all castles in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Castles in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'kasteel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#%%
# Show all hotels of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all hotels of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give me hotels of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are hotels in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Hotels in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'hotel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all churches of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give me churches of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are churches in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Churches in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'kerk')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all mosques of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all mosques of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give me mosques of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are mosques in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Mosques in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'moskee')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all police stations of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show police station of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give police station of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are police station in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Police station in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'politiebureau')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show town hall of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show town hall of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give town hall of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are town hall in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Town hall in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'gemeentehuis')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show post offices of a city, together with their date created and floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all post office of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give post office of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are post office in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Post offices in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. ?address schema:floorSize ?floorsize. }}'.format(city,'postkantoor')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)










# Show all museums of a city with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all museums of {} with floor size."
qList.append(qPattern)
qPattern = "Give me all museums of {}, together with floor size"
qList.append(qPattern)
qPattern = "Where are all museums in {} with floor size?"
qList.append(qPattern)
qPattern = "Museums in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'museum')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show all Castles of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all castles of {} with floor size."
qList.append(qPattern)
qPattern = "Give me all castles of {} with floor size"
qList.append(qPattern)
qPattern = "Where are all castles in {} with floor size?"
qList.append(qPattern)
qPattern = "Castles in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'kasteel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all hotels of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all hotels of {} with floor size."
qList.append(qPattern)
qPattern = "Give me hotels of {}, together with floor size."
qList.append(qPattern)
qPattern = "Where are hotels in {} with floor size?"
qList.append(qPattern)
qPattern = "Hotels in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'hotel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all churches of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches of {} with floor size."
qList.append(qPattern)
qPattern = "Give me churches of {}, together with floor size"
qList.append(qPattern)
qPattern = "Where are churches in {} with floor size?"
qList.append(qPattern)
qPattern = "Churches in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'kerk')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all mosques of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all mosques of {} with floor size."
qList.append(qPattern)
qPattern = "Give me mosques of {}, together with floor size"
qList.append(qPattern)
qPattern = "Where are mosques in {} with floor size?"
qList.append(qPattern)
qPattern = "Mosques in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'moskee')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all police stations of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show police station of {} with floor size."
qList.append(qPattern)
qPattern = "Give police station of {}, together with floor size"
qList.append(qPattern)
qPattern = "Where are police station in {} with floor size?"
qList.append(qPattern)
qPattern = "Police station in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'politiebureau')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show town hall of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show town hall of {} with floor size."
qList.append(qPattern)
qPattern = "Give town hall of {}, together with floor size"
qList.append(qPattern)
qPattern = "Where are town hall in {} with floor size?"
qList.append(qPattern)
qPattern = "Town hall in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'gemeentehuis')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show post offices of a city, together with their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all post office of {} with floor size."
qList.append(qPattern)
qPattern = "Give post office of {}, together with floor size"
qList.append(qPattern)
qPattern = "Where are post office in {} with floor size?"
qList.append(qPattern)
qPattern = "Post offices in {} with floor size."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:floorSize ?floorsize. }}'.format(city,'postkantoor')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)











# Show all museums of a city with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all museums of {} with date created."
qList.append(qPattern)
qPattern = "Give me all museums of {}, together with date created."
qList.append(qPattern)
qPattern = "Where are all museums in {} with date created?"
qList.append(qPattern)
qPattern = "Museums in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'museum')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show all Castles of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all castles of {} with date created."
qList.append(qPattern)
qPattern = "Give me all castles of {} with date created"
qList.append(qPattern)
qPattern = "Where are all castles in {} with date created?"
qList.append(qPattern)
qPattern = "Castles in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'kasteel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all hotels of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all hotels of {} with date created."
qList.append(qPattern)
qPattern = "Give me hotels of {}, together with date created."
qList.append(qPattern)
qPattern = "Where are hotels in {} with date created?"
qList.append(qPattern)
qPattern = "Hotels in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'hotel')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all churches of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all churches of {} with date created."
qList.append(qPattern)
qPattern = "Give me churches of {}, together with date created."
qList.append(qPattern)
qPattern = "Where are churches in {} with date created?"
qList.append(qPattern)
qPattern = "Churches in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'kerk')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all mosques of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all mosques of {} with floor size and date created"
qList.append(qPattern)
qPattern = "Give me mosques of {}, together with date created and floor size"
qList.append(qPattern)
qPattern = "Where are mosques in {} with date created and floor size?"
qList.append(qPattern)
qPattern = "Mosques in {} with floor size, date of creation"
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'moskee')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show all police stations of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show police station of {} with date created."
qList.append(qPattern)
qPattern = "Give police station of {}, together with date created"
qList.append(qPattern)
qPattern = "Where are police station in {} with date created?"
qList.append(qPattern)
qPattern = "Police station in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'politiebureau')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show town hall of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show town hall of {} with date created."
qList.append(qPattern)
qPattern = "Give town hall of {}, together with date created"
qList.append(qPattern)
qPattern = "Where are town hall in {} with date created?"
qList.append(qPattern)
qPattern = "Town hall in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'gemeentehuis')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show post offices of a city, together with their date created.
type = 'AdministrativeArea'
qList = []

qPattern = "Show all post office of {} with date created."
qList.append(qPattern)
qPattern = "Give post office of {}, together with date created"
qList.append(qPattern)
qPattern = "Where are post office in {} with date created?"
qList.append(qPattern)
qPattern = "Post offices in {} with date created."
qList.append(qPattern)


sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:additionalType typeBuilding:{}. ?address schema:dateCreated ?datecreated. }}'.format(city,'postkantoor')
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)


#%%
# Show the geometry of a city.
type = 'AdministrativeArea'
qList = []
qPattern = "Show me the geometry of {}."
qList.append(qPattern)
qPattern = "What is the the geometry of {}?"
qList.append(qPattern)
qPattern = "What is the the shape of {}?"
qList.append(qPattern)
qPattern = "Show the the geometry of {}?"
qList.append(qPattern)
qPattern = "Geometry of {}"
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        surfaceDict = s.getSurface(question,nlp,entities)
        surfaceDict = s.merge_surfaces(surfaceDict)
        print(surfaceDict)
        des = s.to_description(surfaceDict)
        query = 'SELECT DISTINCT ?city ?geo WHERE {{?city rdf:type schema:AdministrativeArea.?city schema:geo ?geo. ?city schema:name "{}"@nl}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#Examples = pd.DataFrame({'text':exampleList})
#Examples.to_csv('text.csv',index=False)
#%%
# Show addresses of a city.
type = 'AdministrativeArea'
qList = []
qPattern = "Show the addresses of {}."
qList.append(qPattern)
qPattern = "List all registered places of {}."
qList.append(qPattern)
qPattern = "What are the addresses in {}?"
qList.append(qPattern)
qPattern = "Addresses in {}"
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address WHERE {{?city rdf:type schema:AdministrativeArea.?city schema:containsPlace ?address. ?city schema:name "{}"@nl}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#Examples = pd.DataFrame({'text':exampleList})
#Examples.to_csv('text.csv',index=False)


#%%
# Show the number of addresses of a city.
type = 'AdministrativeArea'
qList = []
qPattern = "How many addresses in {}?"
qList.append(qPattern)
qPattern = "Give me the number of addresses in {}."
qList.append(qPattern)
qPattern = "Give me the number of registered places in {}."
qList.append(qPattern)
qPattern = "How many registered addresses in {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT (COUNT(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea.?city schema:containsPlace ?address. ?city schema:name "{}"@nl}}'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show addresses of a city, then ascendingly sort by their floor size.
type = 'AdministrativeArea'
qList = []
qPattern = "Show the addresses of {} and sort by their floor size. "
qList.append(qPattern)
qPattern = "Show the addresses of {} and ascendingly sort by their floor size."
qList.append(qPattern)
qPattern = "Give me places in {} then sort them by floor size ascendingly."
qList.append(qPattern)
qPattern = "Give me places in {} then sort by floor size from small to large."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize }} ORDER BY ?floorsize'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)


#%%
# Show addresses of a city, then descendingly sort by their floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} and descendingly sort by their floor size."
qList.append(qPattern)
qPattern = "Give me places in {} then sort them by floor size descendingly."
qList.append(qPattern)
qPattern = "Give me places in {} then sort by floor size from large to small."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        question = q.format(city)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize }} ORDER BY DESC(?floorsize)'.format(city)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#%%
# Show addresses of a city, then filter with floor size (with upper and lower boundaries).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} with their floor size between {} and {} squared meters."
qList.append(qPattern)
qPattern = "Give me places in {} and the floor size should between {} and {}."
qList.append(qPattern)
qPattern = "Give me places in {}, the floor size should larger than {} but smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }}'.format(city,lower,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#%%
# Show addresses of a city, then filter with floor size (larger than a lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} with their floor size larger than {} squared meters."
qList.append(qPattern)
qPattern = "Give me places in {}, their floor size should larger than {} m2."
qList.append(qPattern)
qPattern = "Show places in {}, floor size larger than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, lower)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }}'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
#%%
# Show addresses of a city, then filter with floor size (larger than a lower boundary), then sort ascendingly.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} with their floor size larger than {} squared meters, then sort them ascendingly"
qList.append(qPattern)
qPattern = "Give me places in {}, their floor size should larger than {} m2, and order them."
qList.append(qPattern)
qPattern = "Show places in {}, floor size larger than {} squared meters then order by the floor size from small to large."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, lower)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }} ORDER BY ?floorsize'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show addresses of a city, then filter with floor size (larger than a lower boundary), then sort descendingly.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} with their floor size larger than {} squared meters, then sort them from big to small"
qList.append(qPattern)
qPattern = "Give me places in {}, their floor size should larger than {} m2, and order them descendingly."
qList.append(qPattern)
qPattern = "Show places in {}, floor size larger than {} squared meters then descendingly order by the floor size."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, lower)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }} ORDER BY DESC(?floorsize)'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show the addresses of a city, then filter with floor size (lower than a upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} with their floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give me places in {}, their floor size should smaller than {} m2."
qList.append(qPattern)
qPattern = "Show places in {}, floor size smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }}'.format(city,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show the addresses of a city, then filter with floor size (lower than a upper boundary), then order them ascendingly.
type = 'AdministrativeArea'
qList = []

qPattern = "Show the addresses of {} with their floor size smaller than {} squared meters then order them ascendingly."
qList.append(qPattern)
qPattern = "Give me places in {}, their floor size should smaller than {} m2 and order them."
qList.append(qPattern)
qPattern = "Show places in {}, floor size smaller than {} squared meters, then order ascendingly"
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }} ORDER BY ?floorsize'.format(city,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show the number of addresses of a city with floorsize meet the requirement (with a lower and a upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of addresses of {} with their floor size between {} and {} squared meters."
qList.append(qPattern)
qPattern = "Give me the quantity of places in {} where floor size between {} and {}."
qList.append(qPattern)
qPattern = "How many addresses in {} with floor size larger than {} but smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,200)
        upper = random.randint(200,600)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }}'.format(city,lower,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show the number of addresses of a city with floorsize meet the requirement (with a lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of addresses of {} with their floor size bigger than {} squared meters."
qList.append(qPattern)
qPattern = "Give me the quantity of places in {} where floor larger than {} squared meters."
qList.append(qPattern)
qPattern = "How many addresses in {} with floor size larger than {} m2."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,500)
        upper = random.randint(500,800)
        question = q.format(city, lower)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }}'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show the number of addresses of a city with floorsize meet the requirement (with a upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of addresses of {} with their floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give me the quantity of places in {} where floor smaller than {} squared meters."
qList.append(qPattern)
qPattern = "How many addresses in {} with floor size smaller than {} m2."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,100)
        upper = random.randint(100,500)
        question = q.format(city, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }}'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show addresses of a city with date of creation meet the requirement (with a upper and a lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built between year {} and {}."
qList.append(qPattern)
qPattern = "Give all places in {} with building year between {} and {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, the date of creation should between {} and {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,500)
        upper = random.randint(500,1000)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}) }}'.format(city,lower,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)


#%%
# Show addresses of a city with date of creation meet the requirement (with a lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that after year {}."
qList.append(qPattern)
qPattern = "Give all places in {} with building year later than {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, the date of creation should after {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(1800,1950)
        upper = random.randint(1950,2021)
        question = q.format(city, lower)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}) }}'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show addresses of a city with date of creation meet the requirement (with a lower boundary), then sort ascendingly.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that after year {}, and sort them from old to new."
qList.append(qPattern)
qPattern = "Give all places in {} with building year later than {} then order them by the year of creation."
qList.append(qPattern)
qPattern = "Show registered places in {}, the date of creation should after {}, then order ascendingly by built year."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(1800,1950)
        upper = random.randint(1950,2021)
        question = q.format(city, lower)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}) }} ORDER BY ?datecreated'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show addresses of a city with date of creation meet the requirement (with a upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that before year {}."
qList.append(qPattern)
qPattern = "Give all places in {} with building year earlier than {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, the date of creation should earlier than year {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(1800,1950)
        upper = random.randint(1950,2021)
        question = q.format(city, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}) }}'.format(city,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation meet the requirement (with a upper boundary), then sort ascendingly.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that before year {}, these addresses should be sorted by the year of creation."
qList.append(qPattern)
qPattern = "Give all places in {} with building year earlier than {}, order by building year ascendingly."
qList.append(qPattern)
qPattern = "Show registered places in {}, the date of creation should earlier than year {} then order them by date."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(1800,1950)
        upper = random.randint(1950,2021)
        question = q.format(city, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}) }} ORDER BY ?datecreated'.format(city,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

#%%
# Show the number of addresses of a city with date of creation meet the requirement (with a upper and a lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of addresses in {} that built between year {} and {}."
qList.append(qPattern)
qPattern = "Give the number of places in {} with building year between {} and {}."
qList.append(qPattern)
qPattern = "Show the quantity of registered places in {}, the date of creation should between {} and {}."
qList.append(qPattern)
qPattern = "How many places in {} that built between year {} and {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,500)
        upper = random.randint(500,1000)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}) }}'.format(city,lower,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation meet the requirement (with a upper and a lower boundary), then descendingly order by date.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses in {} that built between year {} and {}, then descendingly order them."
qList.append(qPattern)
qPattern = "Give places in {} with building year between {} and {}, order them from new to old."
qList.append(qPattern)
qPattern = "Show the registered places in {}, the date of creation should between {} and {}, then descendingly sort them."
qList.append(qPattern)
qPattern = "What are places in {} that built between year {} and {}, the result should be descendingly orderd."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,500)
        upper = random.randint(500,1000)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}) }} ORDER BY DESC(?datacreated)'.format(city,lower,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation meet the requirement (with a upper and a lower boundary), then ascendingly order by date.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses in {} that built between year {} and {}, then order them."
qList.append(qPattern)
qPattern = "Give places in {} with building year between {} and {}, order them."
qList.append(qPattern)
qPattern = "Show the registered places in {}, the date of creation should between {} and {}, then sort them."
qList.append(qPattern)
qPattern = "What are places in {} that built between year {} and {}, the result should be ascendingly orderd."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(0,500)
        upper = random.randint(500,1000)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}) }} ORDER BY ?datacreated'.format(city,lower,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)


#%%
# Show the number ofaddresses of a city with date of creation meet the requirement (with a lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number addresses of {} that after year {}."
qList.append(qPattern)
qPattern = "Give the number of places in {} with building year later than {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, the date of creation should after {}."
qList.append(qPattern)
qPattern = "How many addresses in {} with the built year after {}."
qList.append(qPattern)
qPattern = "How many places in {} that built after year {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(1800,1950)
        upper = random.randint(1950,2021)
        question = q.format(city, lower, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}) }}'.format(city,lower)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show the number of addresses of a city with date of creation meet the requirement (with a upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show the number of addresses of {} that before year {}."
qList.append(qPattern)
qPattern = "Give the quantity of places in {} with building year earlier than {}."
qList.append(qPattern)
qPattern = "Show number of registered places in {}, the date of creation should earlier than year {}."
qList.append(qPattern)
qPattern = "How many palces in {} that built earlier than year {}."
qList.append(qPattern)
qPattern = "How many addresses in {} that created before {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower = random.randint(1800,1950)
        upper = random.randint(1950,2021)
        question = q.format(city, upper)
        type = generate_description(question)
        query = 'SELECT DISTINCT (count(?address) as ?quantity) WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}) }}'.format(city,upper)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show addresses of a city with date of creation and floor size meet the requirements (both with lower and upper boundaries).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built between year {} and {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Give all places in {}, building year between {} and {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, built between {} and {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Give all places in {} with built between {} and {}, floor size larger than {} but smaller than {}."
qList.append(qPattern)
qPattern = "Give all places in {} built later than {} but earlier than {}, floor size larger than {} but smaller than {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_year, upper_year,lower_size,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }}'.format(city,lower_year,upper_year,lower_size,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (both with lower and upper boundaries) then order by floor size.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built between year {} and {}, floor size between {} and {}, then order them by floor size."
qList.append(qPattern)
qPattern = "Give all places in {}, building year between {} and {}, floor size between {} and {}, sort by floor size."
qList.append(qPattern)
qPattern = "Show registered places in {}, built between {} and {}, floor size between {} and {}, order by floor space."
qList.append(qPattern)
qPattern = "Give all places in {} with built between {} and {}, floor size larger than {} but smaller than {}, the result should be ordered by floor size."
qList.append(qPattern)
qPattern = "Give all places in {} built later than {} but earlier than {}, floor size larger than {} but smaller than {}, order by floor size ascendingly."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_year, upper_year,lower_size,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }} ORDER BY ?floorsize'.format(city,lower_year,upper_year,lower_size,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (date created with lower boundary, floor size have lower and upper boundaries).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built after {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Give all places in {}, building year after {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, built after {}, floor size between {} and {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} that built after {}, floor size larger than {} but smaller than {}."
qList.append(qPattern)
qPattern = "Give all places in {} with creation date later than {} and floor size bigger than {} but smaller than {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_year, lower_size,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize  WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }}'.format(city,lower_year,lower_size,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (date created with lower boundary, floor size have lower and upper boundaries).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} with floor size between {} and {} built after {}."
qList.append(qPattern)
qPattern = "Give all places in {}, floor size between {} and {}, building year after {}."
qList.append(qPattern)
qPattern = "Show registered places in {}, floor size between {} and {} squared meters, built after {}, ."
qList.append(qPattern)
qPattern = "Give all places in {} floor size larger than {} but smaller than {} and built year should after {}, ."
qList.append(qPattern)
qPattern = "Give all places in {} with floor size bigger than {} but smaller than {} creation date later than year {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_size, upper_size, lower_year)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize  WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }}'.format(city,lower_year,lower_size,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (date created with upper boundary, floor size have lower and upper boundaries).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built before {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Give all places in {}, building year earlier than {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Show registered places in {} built earlier than year {}, floor size between {} and {}."
qList.append(qPattern)
qPattern = "Give all places in {} that registered before year {} and with floor size larger than {} but smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} built before {} with floor size bigger than {} but smaller than {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, upper_year,lower_size,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {} && ?floorsize <= {}) }}'.format(city,upper_year,lower_size,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show addresses of a city with date of creation and floor size meet the requirements (date created with upper and lower boundaries, floor size have lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built between year {} and {}, floor size bigger than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {}, building year between {} and {}, floor size larger than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built between year {} and {}, floor size larger than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} built between {} and {} and floor size larger than {}."
qList.append(qPattern)
qPattern = "Give all places in {} built later than {} earlier than {}, floor size no smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_year, upper_year,lower_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }}'.format(city,lower_year,upper_year,lower_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (date created with upper and lower boundaries, floor size have upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built between year {} and {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {}, building year between {} and {}, floor size smaller than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built between year {} and {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} with date created between {} and {}, floor size no bigger than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} with built later than {} earlier than {} and floor size smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_year, upper_year,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {} && ?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }}'.format(city,lower_year,upper_year,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show addresses of a city with date of creation and floor size meet the requirements (date created with upper boundary, floor size have lower boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built before {}, floor size bigger than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {}, building year before {}, floor size bigger than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built before year {}, floor size bigger than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} created before {} and floor size larger than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} built earlier than {}, floor size no smaller than {} squared meters."
qList.append(qPattern)
qPattern = "List addresses in {} built earlier than {}, floor size no smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, upper_year,lower_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }}'.format(city,upper_year,lower_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)

# Show addresses of a city with date of creation and floor size meet the requirements (date created with lower boundaries, floor size have upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built later than {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {}, building year after {}, floor size no larger than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built after year {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} that created after {} and floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} built later than {} with floor size no bigger than {}."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city, lower_year, upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }}'.format(city,lower_year,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (both with upper boundary).
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built earlier than {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {}, building year before {}, floor size smaller than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built earlier than year {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} created before {} and floor size smaller than {} m2."
qList.append(qPattern)
qPattern = "Give all places in {} built earlier than {}, floor size no bigger than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city,upper_year,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }}'.format(city,upper_year,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (both with upper boundary), then order by building year.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built earlier than {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {}, building year before {}, floor size smaller than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built earlier than year {}, floor size smaller than {} squared meters."
qList.append(qPattern)
qPattern = "Give all places in {} created before {} and floor size smaller than {} m2."
qList.append(qPattern)
qPattern = "Give all places in {} built earlier than {}, floor size no bigger than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city,upper_year,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated <= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize <= {}) }} ORDER BY ?datecreated'.format(city,upper_year,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
# Show addresses of a city with date of creation and floor size meet the requirements (both with lower boundary), then descendingly order by building year.
type = 'AdministrativeArea'
qList = []

qPattern = "Show addresses of {} that built later than {}, floor size larger than {} squared meters."
qList.append(qPattern)
qPattern = "Give me all places in {}, building year after {}, floor size bigger than {} m2."
qList.append(qPattern)
qPattern = "Show registered places in {}, built later than year {}, floor size larger than {} squared meters."
qList.append(qPattern)
qPattern = "List places in {} created before {} and floor size larger than {} m2."
qList.append(qPattern)
qPattern = "Give all places in {} built after {}, floor size no smaller than {} squared meters."
qList.append(qPattern)

sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)
for city in sampledList:
    for q in qList:
        lower_size = random.randint(50,200)
        upper_size = random.randint(200,500)
        lower_year = random.randint(1800,1950)
        upper_year = random.randint(1950,2021)
        question = q.format(city,upper_year,upper_size)
        type = generate_description(question)
        query = 'SELECT DISTINCT ?address ?datecreated ?floorsize WHERE {{?city rdf:type schema:AdministrativeArea. ?city schema:name "{}"@nl. ?city schema:containsPlace ?address. ?address schema:dateCreated ?datecreated. FILTER(?datecreated >= {}). ?address schema:floorSize ?floorsize. FILTER(?floorsize >= {}) }} ORDER BY DESC(?datecreated)'.format(city,upper_year,upper_size)
        example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
        exampleList.append(example)
    sampledList = cityList.sample(n=smaple_count, frac=None, replace=False, weights=None, random_state=None, axis=None)















# #Given a post code, return where this postal address located in.
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show the administrative area where post code {} is located."
# qList.append(qPattern)
# qPattern = "Which administrative area does postal address {} in?"
# qList.append(qPattern)
# qPattern = "The city that postal address {} located in."
# qList.append(qPattern)
# qPattern = "Show the administrative area that postal address {} located in."
# qList.append(qPattern)
# qPattern = "Show the name of the administrative area that postal address {} located in."
# qList.append(qPattern)

# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         question = q.format(postcode)
#         type = generate_description(question)
#         query = 'SELECT DISTINCT ?name WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?administrativearea schema:containsPlace ?place. ?administrativearea schema:name ?name}'.format(postcode)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)



# #Show all postal addresses with a given postal code.
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show all postal addresses with postal code {}."
# qList.append(qPattern)
# qPattern = "Show addresses of post code {}"
# qList.append(qPattern)
# qPattern = "The postal addresses that have postal code {}."
# qList.append(qPattern)
# qPattern = "Return all postal addresses with post code {}."
# qList.append(qPattern)


# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         question = q.format(postcode)
#         type = generate_description(question)
#         query = 'SELECT DISTINCT ?postaladdress  WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}".}'.format(postcode)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)


# #Show all postal addresses with a given postal code, floor size smaller than a upper bound
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show all postal addresses with postal code {}, floor size smaller than {}."
# qList.append(qPattern)
# qPattern = "Show addresses of post code {} with floor size smaller than {}"
# qList.append(qPattern)
# qPattern = "The postal addresses that have postal code {} with floor size no larger than {}."
# qList.append(qPattern)
# qPattern = "Return all postal addresses with post code {}, with floor size smaller than {}."
# qList.append(qPattern)


# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         lower_size = random.randint(10,500)
#         upper_size = random.randint(500,1000)
#         question = q.format(postcode,upper_size)
#         type = generate_description(question)
#         query = 'SELECT DISTINCT ?postaladdress ?floorsize WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:floorSzie ?floorsize. FILTER(?floorsize <= {}) }'.format(postcode,upper_size)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)



# #Show all postal addresses with a given postal code, floor size larger than a lower bound
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show all postal addresses with postal code {}, floor size larger than {}."
# qList.append(qPattern)
# qPattern = "Show addresses of post code {} with floor size bigger than {}"
# qList.append(qPattern)
# qPattern = "The postal addresses that have postal code {} with floor size larger than {}."
# qList.append(qPattern)
# qPattern = "Return all postal addresses with post code {}, with floor size no smaller than {}."
# qList.append(qPattern)


# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         lower_size = random.randint(10,500)
#         upper_size = random.randint(500,1000)
#         question = q.format(postcode)
#         type = generate_description(question,lower_size)
#         query = 'SELECT DISTINCT ?postaladdress ?floorsize WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:floorSzie ?floorsize. FILTER(?floorsize >= {}) }'.format(postcode,lower_size)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)


# #Show all postal addresses with a given postal code, date created larger than a lower bound.
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show all postal addresses with postal code {}, date created later than {}."
# qList.append(qPattern)
# qPattern = "Show addresses of post code {} with date created later than {}"
# qList.append(qPattern)
# qPattern = "The postal addresses that have postal code {} with date created after {}."
# qList.append(qPattern)
# qPattern = "Return all postal addresses with post code {}, with date created no earlier than {}."
# qList.append(qPattern)


# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         lower_size = random.randint(50,200)
#         upper_size = random.randint(200,500)
#         lower_year = random.randint(1800,1950)
#         upper_year = random.randint(1950,2021)
#         question = q.format(postcode,lower_year)
#         type = generate_description(question)
#         query = 'SELECT DISTINCT ?postaladdress ?datecreated WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:dateCreated ?datecreated. FILTER(?datecreated >= {}) }'.format(postcode,lower_year)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)

# #Show all postal addresses with a given postal code, date created earlier than a upper bound.
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show all postal addresses with postal code {}, date created earlier than {}."
# qList.append(qPattern)
# qPattern = "Show addresses of post code {} with date created earlier than {}"
# qList.append(qPattern)
# qPattern = "The postal addresses that have postal code {} with date created earlier than {}."
# qList.append(qPattern)
# qPattern = "Return all postal addresses with post code {}, with date created no later than {}."
# qList.append(qPattern)


# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         lower_size = random.randint(50,200)
#         upper_size = random.randint(200,500)
#         lower_year = random.randint(1800,1950)
#         upper_year = random.randint(1950,2021)
#         question = q.format(postcode,upper_year)
#         type = generate_description(question)
#         query = 'SELECT DISTINCT ?postaladdress ?datecreated WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:dateCreated ?datecreated. FILTER(?datecreated <= {}) }'.format(postcode,upper_year)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)


# #Show all postal addresses with a given postal code, date created earlier than a upper bound, floor size smaller than a upper bound.
# type = 'AdministrativeArea'
# qList = []

# qPattern = "Show all postal addresses with postal code {}, date created earlier than {}, floor size smaller than {}."
# qList.append(qPattern)
# qPattern = "Show addresses of post code {} with date created earlier than {}, floor size smaller than {}"
# qList.append(qPattern)
# qPattern = "The postal addresses that have postal code {} with date created earlier than {}, floor size smaller than {}."
# qList.append(qPattern)
# qPattern = "Return all postal addresses with post code {}, with date created no later than {}, floor size no larger than {}."
# qList.append(qPattern)


# postcodeList = []
# for i in range(20):
#     postcode = postcode_gen()
#     postcodeList.append(postcode)
# for q in qList:
#     for postcode in postcodeList:
#         lower_size = random.randint(50,200)
#         upper_size = random.randint(200,500)
#         lower_year = random.randint(1800,1950)
#         upper_year = random.randint(1950,2021)
#         question = q.format(postcode,upper_year,upper_size)
#         type = generate_description(question)
#         query = 'SELECT DISTINCT ?postaladdress ?datecreated WHERE {?postaladdress rdf:type schema:PostalAddress. ?postaladdress schema:postalCode "{}". ?place schema:address ?postaladdress. ?place schema:dateCreated ?datecreated. FILTER(?datecreated <= {}). ?place schema:floorSzie ?floorsize. FILTER(?floorsize <= {}). }'.format(postcode,upper_year,upper_size)
#         example = 'Suppose we have a graph pattern:\n' + type + '\n\nNow we have a natural language question: \n' + question + '\n\nThe corresponding sparql query is:\n' + query
#         exampleList.append(example)
#     postcodeList = []
#     for i in range(20):
#         postcode = postcode_gen()
#         postcodeList.append(postcode)
    

#%%
Examples = pd.DataFrame({'text':exampleList})
Examples.to_csv('auto_gen.csv',index=False)

#%%
# autogen = pd.read_csv('auto_gen.csv')['text']
# i=0
# for des in autogen:
#     with open('./dataset/autogen_{}.txt'.format(i+1),'a',encoding='utf-8') as f:
#         f.writelines(des)
#         i+=1
# %%
# for i in range(len(exampleList)):
#     exampleList[i] = '<startoftext>'+exampleList[i]+'<endoftext>\n'
# #%%
# with open('./autogen.txt','w', encoding="utf-8") as f:
#     f.writelines(exampleList)


#%%
for i in range(10):
    print(i)