# Travel Knowledge Graph

![all-schemas](../schema-diagrams/Combined_Schema.jpg)

## Accommodation
![Accommodation](../schema-diagrams/Accommodation.jpg)

### Axioms
* `Accommodation SubClassOf hasName some xsd:string` <br />
"An Accommodation has max one name represented by a string value"
* `Accommodation SubClassOf hasReview some Review` <br />
"An Accommodation has some Review"
* `Accommodation SubClassOf hasLocation exactly 1 Location` <br />
"An Accommodation has exactly one Location"
* `Accommodation SubClassOf hasCategory exactly 1 Category` <br />
"An Accommodation has a exactly one Category"
* `Accommodation SubClassOf hasCost exactly 1 FinancialResource` <br />
"An Accommodation has exactly one cost of FinancialResource"
* `Accommodation SubClassOf SpatialObject` <br />
"Every Accommodation is a SpatialObject"

## Activity
![Activities](../schema-diagrams/Activity.png)

### Axioms
* `Activity SubClassOf hasCost exactly 1 FinancialResource` <br />
"Activity has a cost of exactly one FinancialResource"
* `Activity SubClassOf hasName some xsd:string` <br />
"Activity has a name that is represented by some string value"
* `Activity SubClassOf hasLocation exactly 1 Location` <br />
"Activity has exactly one Location"
* `Activity SubClassOf hasEnvironment some Environment` <br />
"Activity has some Environment"
* `Environment SubClassOf hasType either Outdoor or Indoor` <br />
"Environment is either Outdoor or Indoor"

## Financial Resource
![Financial-Resource](../schema-diagrams/FinancialResource.png)

### Axioms
* `FinancialResource SubClassOf hasCurrency some xsd:string` <br />
"FinancialResurce has a currency represented by a string value"
* `FinancialResource SubClassOf hasCurrencyValue some xsd:integer` <br />
"FinancialResurce has a currency value represented by an integer value"
* `Restaurant SubClassOf hasCost some FinancialResource` <br />
"Restaurant has a cost represented by FinancialResource"
* `Activity SubClassOf hasCost some FinancialResource` <br />
"Activity has a cost represented by FinancialResource."
* `Accommodation SubClassOf hasCost some FinancialResource` <br />
"Accommodation has a cost represented by FinancialResource."
* `Transport SubClassOf hasCost some FinancialResource` <br />
"Transport has a cost represented by FinancialResource."

## Restaurant
![Restaurant](../schema-diagrams/Restaurant.png)

### Axioms
* `Restaurant SubClassOf hasName some xsd:string` <br />
"A Restaurant has a name represented by a string value"
* `Restaurant SubClassOf hasReview some Review` <br />
"A Restaurant has some Review"
* `Restaurant SubClassOf hasCategory exactly 1 Category` <br />
"A Restaurant has exactly one Category"
* `Restaurant SubClassOf hasLocation exactly 1 Location` <br />
"A Restaurant has exactly one Location"
* `Restaurant SubClassOf hasCost exactly 1 FinancialResource` <br />
"A Restaurant has exactly one cost of FinancialResource"
* `Restaurant SubClassOf SpatialObject` <br />
"Every Restaurant is a SpatialObject"

## Location
![Location](../schema-diagrams/LocationSchema.png)

### Axioms
* `Location SubClassOf hasAccommodation some Accommodation` <br />
"Location has some Accommodation"
* `Location SubClassOf hasRestaurant some Restaurant` <br />
"Location has some Restaurant"
* `Location SubClassOf hasTransport some Transport` <br />
"Location has some Transport"
* `Location SubClassOf hasAttraction some Attraction` <br />
"Location has some Attraction"
* `Location SubClassOf hasName some xsd:string` <br />
"Location has max one name represented by a string value"
* `Attraction SubClassOf hasName some xsd:string` <br />
"An Attraction has max one name represented by a string value"
* `Attraction SubClassOf hasReview some Review` <br />
"An Attraction has some Review"
* `Attraction SubClassOf hasCategory exactly 1 Category` <br />
"An Attraction has exactly one Category"
* `Attraction SubClassOf hasCost exactly 1 FinancialResource` <br />
"An Attraction has exactly one cost of FinancialResource"
* `Attraction SubClassOf SpatialObject` <br />
"Every Attraction is a SpatialObject"

## Transport
![Transport](../schema-diagrams/Transport.jpg)

### Axioms
* `Transport SubClassOf hasName some xsd:string` <br />
"A Transport has a name represented by a string value"
* `Transport SubClassOf hasReview some Review` <br />
"A Transport has some Review"
* `Transport SubClassOf hasCategory exactly 1 Category` <br />
"A Transport has exactly one Category"
* `Transport SubClassOf hasCost exactly 1 FinancialResource` <br />
"A Transport has exactly one cost of FinancialResource"
* `Transport SubClassOf SpatialObject` <br />
"Every Transport is a SpatialObject"

## Review
![Review](../schema-diagrams/Review.jpg)

### Axioms
* `Review SubClassOf hasURL some xsd:stringURI` <br />
"Review has min 0 URL represented by a string URI"
* `Review SubClassOf hasSource some Source` <br />
"Review has min 0 Source some Source"
* `Source SubClassOf hasName some xsd:string` <br />
"Source has a name represented by a string value"
* `Source SubClassOf hasText some xsd:string` <br />
"Source has a text represented by a string value"
* `Source SubClassOf hasRating some xsd:integer` <br />
"Source has a rating represented by an integer value"

## SpatialObject
![SpatialObject](../schema-diagrams/GeometrySpatialObject.jpg)

### Axioms
* `SpatialObject SubClassOf hasGeometry some Geometry` <br />
"SpatialObject has some Geometry"
* `Geometry SubClassOf asWKT some geo:wktLiteral` <br />
"Geometry is represented as WKT by some wktLiteral value"
* `Transport SubClassOf SpatialObject` <br />
"Every Transport is a SpatialObject"
* `Attraction SubClassOf SpatialObject` <br />
"Every Attraction is a SpatialObject"
* `Restaurant SubClassOf SpatialObject` <br />
"Every Restaurant is a SpatialObject"
* `Accommodation SubClassOf SpatialObject` <br />
"Every Accommodation is a SpatialObject"

## Category
![Category](../schema-diagrams/Category.png)

### Axioms
* `Transport SubClassOf hasCategory exactly 1 Category` <br />
"A Transport has exactly one Category"
* `Accommodation SubClassOf hasCategory exactly 1 Category` <br />
"An Accommodation has exactly one Category"
* `Restaurant SubClassOf hasCategory exactly 1 Category` <br />
"A Restaurant has exactly one Category"
* `Attraction SubClassOf hasCategory exactly 1 Category` <br />
"An Attraction has exactly one Category"