# Name of Ontology

![all-schemas](relative/path/to/all/schemas)

## Accomodation
![Accomodation](../schema-diagrams/Accomodation.jpg)

### Axioms
* `Accomodation SubClassOf hasID some xsd:integer` <br />
"An accomodation has max one ID represented by an integer value"
* `Accomodation SubClassOf hasName some xsd:string` <br />
"An accomodation has max one name represented by a string value"
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
* `Restaurant SubClassOf hasName some xsd:string` <br />
"A Restaurant has a name represented by a string value"
* `Restaurant SubClassOf hasReview some Review` <br />
"A Restaurant has some review"
* `Restaurant SubClassOf hasFoodCategory 0 or 1 xsd:string` <br />
"A Restaurant may or may not have a Food Category represented by a string value"
* `Restaurant SubClassOf isLocatedAt exactly 1 location` <br />
"A Restaurant has exactly one location"
* `Restaurant SubClassOf hasCost exactly 1 FinancialResource` <br />
"A Restaurant has exactly one cost of FinancialResource"
* `Restaurant SubClassOf isA is a SpatialObject` <br />
"A Restaurant is of type SpatialObject"

## Location
![Location](../schema-diagrams/LocationSchema.png)

### Axioms
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

## Transport
![Transport](../schema-diagrams/Transport.jpg)

### Axioms
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

## Review
![Review](../schema-diagrams/Review.jpg)

### Axioms
* `Review SubClassOf hasURL some xsd:string` <br />
"Review has min 0 URL represented by a string URI"
* `Review SubClassOf hasSource some Source` <br />
"Review has min 0 Source some Source"
* `Source SubClassOf hasName some xsd:string` <br />
"Source has a Name represented by a string value"
* `Source SubClassOf hasText some xsd:string` <br />
"Source has a Text represented by a string value"
* `Source SubClassOf hasRating some xsd:integer` <br />
"Source has a Rating represented by an integer value"

## SpatialObject
![SpatialObject](../schema-diagrams/GeometrySpatialObject.png)

### Axioms
* `SpatialObject type Geometry` <br />
"SpatialObject is of type Geometry"
* `Geometry SubClassOf asWKT some geo:wktLiteral` <br />
"Geometry is represented as WKT by some wktLiteral value" 
