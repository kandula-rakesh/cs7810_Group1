# Name of Ontology

![all-schemas](relative/path/to/all/schemas)

## Accomodation
![Accomodation](../schema-diagrams/Accomodation.jpg)

### Axioms
* `Accomodation SubClassOf hasID some xsd:integer` <br />
"An accomodation has max one ID represented by an integer value"
* `Accomodation SubClassOf hasName some xsd:string` <br />
"An accomodation has max one name represented by a string value"
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
* `Geometry SubClassOf inverse hasGeometry exactly 1 Accomodation` <br />
"Every accomodation has exactly one geometry"
* `Geometry SubClassOf hasSerialization some rdsf:Literal` <br />
"A geometry has a serialization represented by some rdsf:Literal"

## Activity
![Activities](../schema-diagrams/Activity.png)

### Axioms
* `Activity SubClassOf hasCost exactly 1 FinancialResource` <br />
"Activity have a cost of exactly one FinancialResource"
* `Activity SubClassOf hasName some xsd:string` <br />
"Activity have a name that is represented by some xsd:string"
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
* `Activity SubClassOf hasCost some FinancialResource` <br />
* `Housing SubClassOf hasCost some FinancialResource` <br />
* `Transportation SubClassOf hasCost some FinancialResource` <br />
"Food, Activity, Housing, and Transportation all have a cost represented by FinancialResource."

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
* `Geometry SubClassOf inverse hasGeometry exactly 1 Restaurant` <br />
"Every Restaurant has exactly one geometry"
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
