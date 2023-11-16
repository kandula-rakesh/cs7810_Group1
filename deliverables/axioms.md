# Name of Ontology

![all-schemas](relative/path/to/all/schemas)

## Accomodation
![Accomodation](../schema-diagrams/Accomodation.jpg)

### Axioms
* `Accomodation SubClassOf hasID some xsd:integer` <br />
"An accomodation has an ID represented by an integer value"
* `Accomodation SubClassOf hasName some xsd:string` <br />
"An accomodation has a name represented by a string value"
* `Accomodation SubClassOf hasDetails some Details` <br />
"An accomodation has some details"
* `Accomodation SubClassOf hasReviews some Reviews` <br />
"An accomodation has some reviews"
* `Accomodation SubClassOf isLocatedAt exactly 1 location` <br />
"An accomodation has exactly one location"
* `Accomodation SubClassOf isCategory exactly 1 Category` <br />
"An Accomodation has a exactly one category"
* `Accomodation SubClassOf hasCost exactly 1 FinancialResource` <br />
"An accomodation has exactly one cost of FinancialResource"
* `Accomodation SubClassOf hasGeometry exactly 1 Geometry` <br />
"An accomodation has exactly one geometry"
* `Geometry SubClassOf hasSerialization some rdsf:Literal` <br />
"A geometry has a serialization represented by some rdsf:Literal"

## Activities
![Activities](../schema-diagrams/Activity.png)

### Axioms
* `Activities SubClassOf hasCost exactly 1 FinancialResource` <br />
"Activities have a cost of exactly one FinancialResource"
* `Activities SubClassOf hasName some xsd:string` <br />
"Activities have a name that is represented by some xsd:string"
* `Activities SubClassOf atLocation exactly 1 location` <br />
"Activities have exactly one location"
* `Activities SubClassOf hasType Outdoor/Indoor` <br />
"Activities have a type that is either Indoor or Outdoor"
* `Type SubClassOf isOutdoor exactly 1 Outdoor` <br />
"If type is Outdoor then the type is represented by Outdoor"
* `Type SubClassOf isIndoor exactly 1 Indoor` <br />
"If type is Indoor then the type is represented by Indoor"

## Financial Resource
![Financial-Resource](../schema-diagrams/FinancialResource.png)

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Food
![Food](../schema-diagrams/Food.png)

### Axioms
* `Food/Restaurant SubClassOf hasRanking some xsd:int` <br />
"A Restaurant/Food has a ranking represented by an integer value"
* `Restaurant/Food SubClassOf hasName some rdfs:Literal` <br />
"A Restaurant/Food has a name represented by a string value"
* `Restaurant/Food SubClassOf hasRating some xsd:Decimal` <br />
"A Restaurant/Food has some rating represented by a decimal value"
* `Restaurant/Food SubClassOf hasFoodCategory some rdfs:Literal` <br />
"A Restaurant/Food has some Food Category represented by a string value"
* `Restaurant/Food SubClassOf isLocatedAt exactly 1 location` <br />
"A Restaurant/Food has exactly one location"
* `Restaurant/Food SubClassOf hasCost exactly 1 FinancialResource` <br />
"A Restaurant/Food has exactly one cost of FinancialResource"
* `Restaurant/Food SubClassOf hasGeometry exactly 1 Geometry` <br />
"A Restaurant/Food has exactly one geometry"
* `Geometry SubClassOf hasSerialization some rdsf:Literal` <br />
"A geometry has a serialization represented by some rdsf:Literal"

## Location
![Location](../schema-diagrams/LocationSchema1.png)

### Axioms
* `axiom in manchester syntax` <br />
natural language description
* `axiom in manchester syntax` <br />
natural language description

## Transport Schema Diagram
![Transport](../schema-diagrams/Transport.jpg)

### Axioms
* `Transport SubClassOf hasID some xsd:integer` <br />
"A transport has an ID represented by an integer value"
* `Transport SubClassOf hasName some xsd:string` <br />
"A transport has a name represented by a string value"
* `Transport SubClassOf hasDetails some Details` <br />
"A transport has some details"
* `Transport SubClassOf hasReviews some Reviews` <br />
"A transport has some reviews"
* `Transport SubClassOf isCategory exactly 1 Category` <br />
"A Transport has a exactly one category"
* `Transport SubClassOf hasCost exactly 1 FinancialResource` <br />
"A transport has exactly one cost of FinancialResource"
