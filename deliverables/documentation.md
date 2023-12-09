# Travel Knowledge Graph 
**Authors:** 
* Chaitanya Anumula
* Skyler Gentner
* Calvin Greenewald
* Rakesh Kandula

## Use Case Scenario
### Narrative 
The topic of travel and vacations comes up frequently for many individuals and families across the world. Especially with the rise in social media marketing of travel destinations, the interest in traveling around Europe has gained global attention. After the effect of COVID deminished, and tourism gained popularity again, Europe saw tourists spend an astonishing 2.72 billion nights in Europe in 2022 [1]. These tourists largely used social media or travel blogs to determine their destinations and other vacation plans. These listed means of determining travel destination and details have weaknesses and limitations in providing the traveler with adequate information necessary for planning the entire trip. The portrayal of popular destinations on social media often deceives viewers and lead them to believe a false narrative about the destination [2]. Images of destinations are usually overly photoshopped, hiding all the flaws which then catch tourists off guard or ruin trips [2]. Travel blogs often highlight what worked for the writer and all the activities that they did. Therefore, they are not a good means for one to determine the best trip for them or their families, as the blogs are not able to be personalized. A creation of a knowledge graph could help give the tourist all the necessary details for structuring their entire trip.

This project would support many people from all walks of life and help them experience new destinations and cultures. Travel influencers across various social media platforms could grow their following and footprint on social media by using this project to determine new travel destinations or details of a trip. On TikTok, a popular social media platform, the hashtag “‘travel’ boasts 74.4 billion views [2].” Additionally, roughly 60% of Gen Zs and 40% of millennials use social media” to get inspiration for their vacation trips [2]. These statistics show that this project could support individuals and families alike, regardless of economic status, to plan budget friendly short trips or long extravagant vacations for themselves and their families. Users could consider all the popular spots that match their interests, as well as all the details regarding transportation, stay, and food.

The goal of this project is to identify tourist destinations based on personal preferences and recommend possible destinations for users. This project would ideally consider budget, length of time, destination interests, destination reviews, transportation options, and activities. Users would not have to scour the internet searching for the best reviewed, most picturesque, destinations. They would have all the information needed for planning their trip all in one place.

A knowledge graph on travel recommendations would positively impact the tourism industry. Tourists from across the world would be encouraged to visit destinations across Europe that would be a best fit for them, and consequently tourism across Europe would increase. This would also help travel agencies or travel blogs come up with best fit destinations for users and their families.

### References
[1] "Tourism in 2022 approaches pre-pandemic levels." EuroStat, 18 January 2023. https://ec.europa.eu/eurostat/web/products-eurostat-news/w/DDN-20230118-1. [Accessed 6 November 2023].

[2] Chelsea Ong. “People are Getting Travel Ideas From Social Media – Often With Hilarious Results.” CNBC, 26 April 2022. https://www.cnbc.com/2022/04/26/what-happens-when-people-use-tiktok-and-instagram-to-make-travel-plans.html. [Accessed 27 September 2023].

### Competency Questions
1. How to query the Knowledge Graph (KG) to get the details of the location, tourist is visting? (expected_input: state, popular city, popular tourist destination, expected_output: details of the location includes, activities, popular tourist spots, accomodation etc).
2. How user can decide the mode of the transport (X), given his/her budget (B)? (expected_input: float value, output: transport modes)
3. What are the activities(A) can be performed, in the location(Y), for eg: kayaking, rafting, sky-diving, trekking etc. (this can be further filtered by using Budget (B) as the constraint.)
4. List all the locations(Y), if user is interested to participate in specific activity(A), sorted the prices from low to high.
5. List all the tourist spots (TS), for the given location (Y). Eg: Beaches, Mountains, National Parks and Monuments, Buildings etc. (this can be further filtered by using Budget (B) as the constraint).
6. What type of accomodations/Housing (H) availble in Budget (B) for the location (Y).
7. How user can search nearby places/tourist attractions?(input: tourist_location, output: nearby locations) (depends on data supports this or not?)
8. Querying the KG, based on preferred activities for the current season.
9. Which are the destinations offer pristine beaches, clear waters or water activities.
10. Which location offers multi cuisine restaraunts, suitable for food lovers.


### Integrated Datasets
Source: [Tourist Information](http://tour-pedia.org/about/datasets.html)
- A complete dataset containing a large amout of data describing the actions that we are covering, locations, reviews, and prices. 

Source: [AirBnB](https://data.world/datasets/berlin)
- Overview of AirBnB data from Berlin.

Source: [Restaurant Data] (https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw/)
- Dataset showing descriptive information regarding important restaurant information. 


## Modules
### Transport
**Source Pattern:** Part-whole, Hierarchial-cell-features <br />
**Source Data:** Tour Dataset

#### Description
The mode of transportation can affect the enjoyment the traveller experiences during their trip. They may not want to ride in public transportation and would rather drive themselves to anywhere they want to go at their destination. The traveller could also want their primary transportation to come in the form of walking so it would be better to know that so they can take a trip in a walkable city instead of a place where everything is far away from each other. Recognizing these transportation preferences helps travelers select modes that align with their comfort and travel style, ultimately enhancing their overall travel experience.

![Transport](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/Transport.png)

#### Axioms
* `Transport SubClassOf hasID some xsd:integer` <br />
"A transport has an ID represented by an integer value"
* `Transport SubClassOf hasName some xsd:string` <br />
"A transport has a name represented by a string value"
* `Transport SubClassOf hasReview some Review` <br />
"A transport has some review"
* `Transport SubClassOf isCategory exactly 1 Category` <br />
"A Transport has a exactly one category"
* `Transport SubClassOf hasCost exactly 1 FinancialResource` <br />
"A transport has exactly one cost of FinancialResource"

### Financial Resource
**Source Pattern:** QuantityPattern <br />
**Source Data:** Tour Dataset

#### Description
Depending on how high or low the user's budget is they will be provided with more or fewer options to travel to. Providing options that are available for a particular range of budget makes it possible to plan for a trip despite the constraints. Recognizing the budgetary limitations of travelers helps in tailoring recommendations that not only fit their financial capabilities but also ensure that their travel plans are realistic and enjoyable.

![FinancialResource](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/FinancialResource.png)

#### Axioms
* `FinancialResource SubClassOf Currency some qudt:USD` <br />
"FinancialResurce has a currency represented by USD"
* `Food SubClassOf hasCost some FinancialResource` <br />
"Food has a cost represented by FinancialResource"
* `Activity SubClassOf hasCost some FinancialResource` <br />
"Activity has a cost represented by FinancialResource."
* `Housing SubClassOf hasCost some FinancialResource` <br />
"Housing has a cost represented by FinancialResource."
* `Transportation SubClassOf hasCost some FinancialResource` <br />
"Transportation has a cost represented by FinancialResource."

### Activity
**Source Pattern:** SpatioTemporalExtent, Temporal extent <br />
**Source Data:** Tour Dataset

#### Description
Some users would like to plan their trip around certain activies that they can do while travelling. This could also help other users know what sorts of activities are available so that if needed they can make reservations ahead of time so they do not have to miss out on something they might want to do. Recognizing the significance of activities in travel planning allows users to align their travel experiences with their interests and also ensures that they can make necessary arrangements to fully enjoy the activities they desire during their trip. Given the users activity interest they could choose from different locations that offer some or all of the activities. This approach empowers travelers to select destinations that are tailored to their preferred activities, enhancing their overall travel experience by ensuring that their chosen location aligns with their activity interests and enabling them to make the most of their trip.

![Activity](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/Activity.png)

#### Axioms
* `Activity SubClassOf hasCost exactly 1 FinancialResource` <br />
"Activity have a cost of exactly one FinancialResource"
* `Activity SubClassOf hasName some xsd:string` <br />
"Activity have a name that is represented by some string"
* `Activity SubClassOf atLocation exactly 1 location` <br />
"Activity have exactly one location"
* `Activity SubClassOf hasType Outdoor/Indoor` <br />
"Activity have a type that is either Indoor or Outdoor"
* `Type SubClassOf isOutdoor exactly 1 Outdoor` <br />
"If type is Outdoor then the type is represented by Outdoor"
* `Type SubClassOf isIndoor exactly 1 Indoor` <br />
"If type is Indoor then the type is represented by Indoor"

### Location
**Source Pattern:** SpatialObject or SpatialExtent <br />
**Source Data:** Tour Dataset

#### Description
Tourist spots would be things such as historical monuments, artistic statues, or a particular sight from a mountain that people like to see that the traveller might also want to see while on vacation. This could be important to someone who wants to plan a trip to see both the Colosseum and the statue of David on the same trip to Italy. Understanding the availability and significance of tourist spots aids travelers in creating well-rounded itineraries that encompass cultural, historical, and scenic attractions, ensuring that they can maximize their exploration of the chosen destination. And knowing the specifications of a travel location can help the traveller go to a place that they would enjoy. The traveller has in mind general information on a location that they want to go to. It would be important that someone who wants to go to the beach got there instead of ending up on the ski slopes of a mountain.These specifications can include details about the geographical features, climate, topography, and primary attractions of the location, ensuring that travelers can choose destinations that align with their preferences and expectations.

![Location](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/LocationSchema.png)

#### Axioms
* `Attraction SubClassOf hasID some xsd:integer` <br />
"An attraction has max one ID represented by an integer value"
* `Attraction SubClassOf hasName some xsd:string` <br />
"An attraction has max one name represented by a string value"
* `Attraction SubClassOf hasReview some Review` <br />
"An attraction has some review"
* `Attraction SubClassOf isLocatedAt exactly 1 location` <br />
"An attraction has exactly one location"
* `Attraction SubClassOf isCategory exactly 1 Category` <br />
"An attraction has a exactly one category"
* `Attraction SubClassOf hasCost exactly 1 FinancialResource` <br />
"An attraction has exactly one cost of FinancialResource"
* `Attraction SubClassOf hasActivity some Activity` <br />
"An attraction has some activity"
* `Attraction SubClassOf isA is a SpatialObject` <br />
"An Attraction is of type SpatialObject"

### Accommodation
**Source Pattern:** Part-whole, Quantity, SpatioTemporalExtent <br />
**Source Data:** Berlin Airbnb Dataset, Tour Dataset

#### Description
Housing is important while on a vacation. This is where your belongings will be kept and where you will be sleeping. If your housing is in a bad part of town you may be worrying your entire trip whether or not something will get stolen. Also, if you can not sleep well in whatever housing you choose it will impact your experience as you most likely will not feel as good as you could if you got a full rest each night. Recognizing the significance of suitable accommodations in travel planning ensures that travelers have a secure and comfortable base during their journey, reducing concerns about safety and the quality of their rest, ultimately enhancing the overall travel experience.

![Accommodation](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/Accomodation.png)

#### Axioms
* `Accomodation SubClassOf hasID some xsd:integer`<br />
"An accomodation has max one ID represented by an integer value"
* `Accomodation SubClassOf hasName some xsd:string`<br />
"An accomodation has max one name represented by a string value"
* `Accomodation SubClassOf hasReview some Review`<br />
"An accomodation has some review"
* `Accomodation SubClassOf isLocatedAt exactly 1 location`<br />
"An accomodation has exactly one location"
* `Accomodation SubClassOf isCategory exactly 1 Category`<br />
"An Accomodation has a exactly one category"
* `Accomodation SubClassOf hasCost exactly 1 FinancialResource`<br />
"An accomodation has exactly one cost of FinancialResource"
* `Accomodation SubClassOf isA is a SpatialObject`<br />
"An Accomodation is of type SpatialObject"

### Restaurant
**Source Pattern:** Provenance, Temporal extent <br />
**Source Data:** Restaurant info, Tour Dataset

#### Description
Different destinations offer diverse culinary experiences. Understanding the food options available in a location allows travelers to explore and savor the local cuisine, which for food lovers is often a highlight of the trip. For travelers who appreciate culinary adventures, discovering the local cuisine is a significant aspect of their journey. Different destinations provide unique and diverse culinary traditions. Understanding the food options available in a location ensures that food enthusiasts can indulge in the flavors and culinary delights of the region, enhancing their overall travel experience by savoring the local gastronomy.

![Restaurant](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/Restaurant.png)

#### Axioms
* `Restaurant SubClassOf hasName some xsd:string` <br />
"A Restaurant has a name represented by a string value"
* `Restaurant SubClassOf hasReview some Review` <br />
"A Restaurant has some review"
* `Restaurant SubClassOf hasCategory 0 or 1 xsd:string` <br />
"A Restaurant may or may not have a Category represented by a string value"
* `Restaurant SubClassOf hasLocation exactly 1 location` <br />
"A Restaurant has exactly one location"
* `Restaurant SubClassOf hasCost exactly 1 FinancialResource` <br />
"A Restaurant has exactly one cost of FinancialResource"
* `Restaurant SubClassOf isA is a SpatialObject` <br />
"A Restaurant is of type SpatialObject"






#### Remarks
* Any remarks re: usage

## The Overall Knowledge Graph
### Namespaces
* prefix: namespace
* prefix: namespace

### Schema Diagram
![CombinedSchema](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/schema-diagrams/Combined_Schema.png)


### Usage
Adapted from `validation.md`, i.e., the competency questions + SPARQL queries.
