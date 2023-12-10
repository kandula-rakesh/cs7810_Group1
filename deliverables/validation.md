## Deciding Mode of Transport

* **Competency Question:** "What can be the mode of transport for a given range of budget?"
* **Datasets:** "Tourpedia POI Dataset of 7 cities"

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#> 
        PREFIX kl-ont: <https://kastle-lab.org/lod/ontology/> 
        PREFIX kl-res: <https://kastle-lab.org/lod/resource/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
        
        
        SELECT ?transport ?category  ?price
        WHERE {
          ?transport a kl-ont:Transport ;
                  kl-ont:hasName ?name;
                  kl-ont:hasLocation ?location;
                  kl-ont:hasCategory ?category;
                  kl-ont:hasCost ?financialRes .
            ?financialRes kl-ont:hasCurrency ?currencyType ;
                  kl-ont:hasCurrencyValue ?price .
          FILTER(?price < 30)
        } LIMIT 10
* ___SPARQL Query Output:___

![Output](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/deliverables/images/CQ1_Output.jpg)

## Deciding on Activities in a selective location

* **Competency Question:** "What kind of Activities can be performed at the given location?"
* **Datasets:** "Tourpedia Attractions Dataset of 7 cities"

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#> 
        PREFIX kl-ont: <https://kastle-lab.org/lod/ontology/> 
        PREFIX kl-res: <https://kastle-lab.org/lod/resource/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
        
        
        SELECT ?locName ?attraction  ?category
        WHERE {
          ?location a kl-ont:Location;
          kl-ont:hasName ?locName;
          kl-ont:hasAttraction ?attraction .
          ?attraction kl-ont:hasCategory ?category
          
          FILTER (?location = kl-res:Amsterdam)
          
        } LIMIT 10
* ___SPARQL Query Output:___

![Output](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/deliverables/images/CQ2_Output.jpg)

## Deciding the place to stay

* **Competency Question:** "What type of Accommodation options available in a budget range for given location?"
* **Datasets:** "Tourpedia Accommodation Dataset of 7 Cities"

        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        PREFIX kl-ont: <https://kastle-lab.org/lod/ontology/>
        PREFIX kl-res: <https://kastle-lab.org/lod/resource/>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        SELECT ?locName ?accomodationName ?currencyType  ?price
        WHERE {
          ?location a kl-ont:Location;
          kl-ont:hasName ?locName;
          kl-ont:hasAccomodation ?accomodation .
          ?accomodation kl-ont:hasName ?accomodationName;
          kl-ont:hasCost ?financialRes .
          ?financialRes kl-ont:hasCurrency ?currencyType ;
                        kl-ont:hasCurrencyValue ?price .
          FILTER (?location = kl-res:London && ?price > 110 && ?price < 150)
        } LIMIT 10

* ___SPARQL Query Output:___

![Output](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/deliverables/images/CQ3_Output.jpg)

## Deciding Activities based on location with price from low to high

* **Competency Question:** "What are locations that facilitate a particular activity, sorted from low to high based on price range?"
* **Datasets:** "Tourpedia Attraction Dataset of 7 cities"
 
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#> 
        PREFIX kl-ont: <https://kastle-lab.org/lod/ontology/> 
        PREFIX kl-res: <https://kastle-lab.org/lod/resource/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
        
        
        SELECT ?locName ?attraction  ?category ?currencyType ?price
        WHERE {
          ?location a kl-ont:Location;
          kl-ont:hasName ?locName;
          kl-ont:hasAttraction ?attraction .
          ?attraction kl-ont:hasCategory ?category;
                      kl-ont:hasCost ?financialRes .
          ?financialRes kl-ont:hasCurrency ?currencyType ;
                        kl-ont:hasCurrencyValue ?price .
          
          FILTER (?category = kl-res:Skydiving)
          
        }
        ORDER BY ASC(?price)
        LIMIT 10

* ___SPARQL Query Output:___

![Output](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/deliverables/images/CQ4_Output.jpg)

## Deciding top rated Accommodation in a selective location

* **Competency Question:** "What are the top rated accomodation in a particular location, along with its price?"
* **Datasets:** "Tourpedia Accommodation Dataset of 7 cities"

  
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX geo: <http://www.opengis.net/ont/geosparql#> 
        PREFIX kl-ont: <https://kastle-lab.org/lod/ontology/> 
        PREFIX kl-res: <https://kastle-lab.org/lod/resource/> 
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
        
        
        SELECT ?locName ?accomodationName  ?rating ?currencyType ?price
        WHERE {
          ?location a 	kl-ont:Location;
                  kl-ont:hasName ?locName;
                  kl-ont:hasAccomodation ?accomodation .
          ?accomodation kl-ont:hasName ?accomodationName;
                        kl-ont:hasReview ?review;
                  kl-ont:hasCost ?financialRes .
          ?financialRes kl-ont:hasCurrency ?currencyType ;
                        kl-ont:hasCurrencyValue ?price .
          ?review kl-ont:hasRating ?rating.
          FILTER(?location = kl-res:London)
        } 
        ORDER BY DESC(?rating)
        LIMIT 10

* ___SPARQL Query Output:___

![Output](https://github.com/Rakesh-Sri/cs7810_Group1/blob/main/deliverables/images/CQ5_Output.jpg)

