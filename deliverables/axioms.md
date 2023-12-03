# Name of Ontology

![all-schemas](relative/path/to/all/schemas)

## Accomodation
![Accomodation](../schema-diagrams/Accomodation.jpg)

### Axioms
* `Accomodation SubClassOf hasID some xsd:integer` <br />
"An accomodation has max one ID represented by an integer value"
* `Accomodation SubClassOf hasName some xsd:string` <br />
"An accomodation has max one name represented by a string value"
* `Accomodation SubClassOf hasDetail some Detail` <br />
"An accomodation has some detail"
* `Accomodation SubClassOf hasReview some Review` <br />
"An accomodation has some review"
* `Accomodation SubClassOf isLocatedAt exactly 1 location` <br />
"An accomodation has exactly one location"
* `Accomodation SubClassOf isCategory exactly 1 Category` <br />
"An Accomodation has a exactly one category"
* `Accomodation SubClassOf hasCost exactly 1 FinancialResource` <br />
"An accomodation has exactly one cost of FinancialResource"
* `Accomodation SubClassOf isA is a SpatialObject` <br />
"An Accomodation is of type SpatialObject"
* `Detail SubClassOf hasURL some xsd:string` <br />
"Detail has min 0 URL represented by a string URI"
* `Detail SubClassOf hasSource some Source` <br />
"Detail has min 0 Source some Source"
* `Review SubClassOf hasURL some xsd:string` <br />
"Review has min 0 URL represented by a string URI"
* `Review SubClassOf hasSource some Source` <br />
"Review has min 0 Source some Source"

## Activity
![Activities](../schema-diagrams/Activity.png)

### Axioms
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

## Financial Resource
![Financial-Resource](../schema-diagrams/FinancialResource.png)

### Axioms
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

## Restaurant
![Restaurant](../schema-diagrams/Restaurant.png)

### Axioms
* `Restaurant SubClassOf hasDetailURL 0 or 1 xsd:stringURI` <br />
"A Restaurant has either has or doesn't have a URL pointing to its details"
* `Restaurant SubClassOf hasName some xsd:string` <br />
"A Restaurant has a name represented by a string value"
* `Restaurant SubClassOf hasReviewURL 0 or 1 xsd:stringURI` <br />
"A Restaurant has either has or doesn't have a URL pointing to its reviews"
* `Restaurant SubClassOf hasFoodCategory some xsd:string` <br />
"A Restaurant has some Food Category represented by a string value"
* `Restaurant SubClassOf isLocatedAt exactly 1 location` <br />
"A Restaurant has exactly one location"
* `Restaurant SubClassOf hasCost exactly 1 FinancialResource` <br />
"A Restaurant has exactly one cost of FinancialResource"

## Location
![Location](../schema-diagrams/LocationSchema.png)

### Axioms
* `Attraction SubClassOf hasID some xsd:integer` <br />
"An attraction has max one ID represented by an integer value"
* `Attraction SubClassOf hasName some xsd:string` <br />
"An attraction has max one name represented by a string value"
* `Attraction SubClassOf hasDetail some Detail` <br />
"An attraction has some detail"
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
* `Detail SubClassOf hasURL some xsd:string` <br />
"Detail has min 0 URL represented by a string URI"
* `Detail SubClassOf hasSource some Source` <br />
"Detail has min 0 Source some Source"
* `Review SubClassOf hasURL some xsd:string` <br />
"Review has min 0 URL represented by a string URI"
* `Review SubClassOf hasSource some Source` <br />
"Review has min 0 Source some Source"

## Transport Schema Diagram
![Transport](../schema-diagrams/Transport.jpg)

### Axioms
* `Transport SubClassOf hasID some xsd:integer` <br />
"A transport has an ID represented by an integer value"
* `Transport SubClassOf hasName some xsd:string` <br />
"A transport has a name represented by a string value"
* `Transport SubClassOf hasDetail some Detail` <br />
"A transport has some detail"
* `Transport SubClassOf hasReview some Review` <br />
"A transport has some review"
* `Transport SubClassOf isCategory exactly 1 Category` <br />
"A Transport has a exactly one category"
* `Transport SubClassOf hasCost exactly 1 FinancialResource` <br />
"A transport has exactly one cost of FinancialResource"
* `Detail SubClassOf hasURL some xsd:string` <br />
"Detail has min 0 URL represented by a string URI"
* `Detail SubClassOf hasSource some Source` <br />
"Detail has min 0 Source some Source"
* `Review SubClassOf hasURL some xsd:string` <br />
"Review has min 0 URL represented by a string URI"
* `Review SubClassOf hasSource some Source` <br />
"Review has min 0 Source some Source"
