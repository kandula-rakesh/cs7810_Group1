# Use Case
## Narrative
The topic of travel and vacations comes up frequently for many individuals and families across the world. Especially with the 
rise in social media marketing of travel destinations, the interest in traveling around Europe has gained global attention. 
After the effect of COVID deminished, and tourism gained popularity again, Europe saw tourists spend an astonishing 2.72 billion
nights in Europe in 2022 [1]. These tourists largely used social media or travel blogs to determine their destinations and other
vacation plans. These listed means of determining travel destination and details have weaknesses and limitations in providing the
traveler with adequate information necessary for planning the entire trip. The portrayal of popular destinations on social media
often deceives viewers and lead them to believe a false narrative about the destination [2]. Images of destinations are usually
overly photoshopped, hiding all the flaws which then catch tourists off guard or ruin trips [2]. Travel blogs often highlight 
what worked for the writer and all the activities that they did. Therefore, they are not a good means for one to determine the 
best trip for them or their families, as the blogs are not able to be personalized. A creation of a knowledge graph could help 
give the tourist all the necessary details for structuring their entire trip. 
	
This project would support many people from all walks of life and help them experience new destinations and cultures. Travel 
influencers across various social media platforms could grow their following and footprint on social media by using this project
to determine new travel destinations or details of a trip. On TikTok, a popular social media platform, the hashtag “‘travel’ 
boasts 74.4 billion views [2].” Additionally, roughly 60% of Gen Zs and 40% of millennials use social media” to get inspiration
for their vacation trips [2]. These statistics show that this project could support individuals and families alike, regardless of
economic status, to plan budget friendly short trips or long extravagant vacations for themselves and their families. Users could
consider all the popular spots that match their interests, as well as all the details regarding transportation, stay, and food. 
	
The goal of this project is to identify tourist destinations based on personal preferences and recommend possible destinations
for users. This project would ideally consider budget, length of time, destination interests, destination reviews, transportation
options, and activities. Users would not have to scour the internet searching for the best reviewed, most picturesque, 
destinations. They would have all the information needed for planning their trip all in one place. 
	
A knowledge graph on travel recommendations would positively impact the tourism industry. Tourists from across the world would
be encouraged to visit destinations across Europe that would be a best fit for them, and consequently tourism across Europe would
increase. This would also help travel agencies or travel blogs come up with best fit destinations for users and their families.  


## Competency Questions
* How to query the Knowledge Graph (KG) to get the details of the location, tourist is visting? (expected_input: state, popular city, popular tourist destination, expected_output: details of the location includes, activities, popular tourist spots, accomodation etc).
* How user can decide the mode of the transport (X), given his/her  budget (B)? (expected_input: float value, output: transport modes)
* what are the activities(A) can be performed, in the location(Y), for eg: kayaking, rafting, sky-diving, trekking etc. (this can be further filtered by using Budget (B) as the constraint.)
* List all the locations(Y), if user is interested to participate in specific activity(A), sorted the prices from low to high.
* List all the tourist spots (TS), for the given location (Y). Eg: Beaches, Mountains, National Parks and Monuments, Buildings etc. (this can be further filtered by using Budget (B) as the constraint).
* What type of accomodations/Housing (H) availble in Budget (B) for the location (Y).
* How user can search nearby places/tourist attractions?(input: tourist_location, output: nearby locations) (depends on data supports this or not?)
* Querying the KG, based on preferred activities for the current season.
* Which are the destinations offer pristine beaches, clear waters or water activities.
* Which location offers multi cuisine restaraunts, suitable for food lovers.

## Datasets for Europe Scope 
* https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw/
* http://tour-pedia.org/about/datasets.html
* https://data.world/datasets/berlin


## Potential Datasets For America Scope For If We Want To Expand Scope 
* Tourism Satellite Accounts: https://www.bea.gov/data/special-topics/travel-and-tourism/tourism-satellite-accounts-data-sheets
* Tourism Statistics: https://www.unwto.org/tourism-statistics/key-tourism-statistics
* Trips by distance: https://catalog.data.gov/dataset/trips-by-distance
* American Travel Survey: https://rosap.ntl.bts.gov/gsearch?ref=docDetails&related_series=American%20Travel%20Survey%20%28ATS%29
* https://catalog.data.gov/dataset/air-traffic-passenger-statistics
* https://www.bea.gov/data/special-topics/travel-and-tourism/tourism-satellite-accounts-data-sheets
* https://catalog.data.gov/dataset/trips-by-distance
* https://rosap.ntl.bts.gov/gsearch?ref=docDetails&related_series=American%20Travel%20Survey%20%28ATS%29
* Various hotel/Airbnb rating datasets on Kaggle
* https://www.gooutsidebook.com/articles/national-park-visitation.html

## Existing Resources
* Travel Attractions Recommendation with Knowledge Graphs: https://link.springer.com/chapter/10.1007/978-3-319-49004-5_27
* Travel Attractions Recommendation with Travel Spatial-Temporal Knowledge Graphs: https://link.springer.com/chapter/10.1007/978-981-13-2206-8_19

## References
[1] "Tourism in 2022 approaches pre-pandemic levels." EuroStat, 18 January 2023. https://ec.europa.eu/eurostat/web/products-eurostat-news/w/DDN-20230118-1. [Accessed 6 November 2023].

[2] Chelsea Ong. “People are Getting Travel Ideas From Social Media – Often With Hilarious Results.” CNBC, 26 April 2022. https://www.cnbc.com/2022/04/26/what-happens-when-people-use-tiktok-and-instagram-to-make-travel-plans.html. [Accessed 27 September 2023]. 
