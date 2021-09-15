# Introduction
This is the sparql generator where you can input your question in English and it will return a corresponding sparql code.

**For example, if we input a question:**

'Show all places in Eindhoven, floor size smaller than 1000.'

**It returns the query:** 

SELECT DISTINCT?address?floorsize WHERE {?city rdf:type schema:AdministrativeArea.?city schema:name "Eindhoven"@nl.?city schema:containsPlace?address.?address schema:floorSize?floorsize. FILTER(?floorsize <= 1000) }

# How to use
1. Clone this repo into your local environment

2. Download the model in https://drive.google.com/file/d/1E6S_q44YIQ1LeyR42Qwlol9kZ-wgvfe5/view?usp=sharing

3. Unzip into **./pretrained** folder

4. Install dependencies by command `pip install -r requirements.txt`

5. For comsuming the api, run `python api.py --question 'Your question here' `

# Types of questions allowed
For now, the model is able to answer questions about:

* Administrative area, like Amsterdam, Eindhoven, Apeldoorn etc.
* Places with their date created, floor size
* Additional types of places, like
Moskee(Mosque)
Kerk(Church)
Kasteel(Castle)
Museum
politiebureau(police station)
gemeentehuis(town hall)
postkantoor(post office)

* Postal code, like 5611BM
* Street address, like Victoriapark 612

Some examples of questions:

*	What are the addresses of Eindhoven, with built year between 2000 and 2021.
*	What are the addresses of Amsterdam, with floor size larger than 100 m2.
*	What are the addresses of Rotterdam, floor size between 100 and 500 m2, built year earlier than 2010.
*	Show all police stations in Apeldoorn.
*	Show all hotels in the administrative area where street address Victoriapark 612 is located.

## Important
When you want to query about a term act as a property or entity type like a ***administraive area*** or ***street address***, it is highly recommonded to explicitly include these words in the question. This is for the model to better match the terms in the database.

**For example:**
* Show all ***hotels*** in the ***administrative area*** where ***street address*** Victoriapark 612 is located. 
* Show all ***places*** in Eindhoven, ***floor size*** larger than 100, ***date created*** earlier than 2015.
* What is the ***administrative area*** that ***postal code*** 5611BM is located?
