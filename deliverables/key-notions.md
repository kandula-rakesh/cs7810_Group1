* Specifications of Location
  * Knowing the specifications of a travel location can help the traveller go to a place that they would enjoy. The traveller has in mind general information on a location that they want to go to. It would be important that someone who wants to go to the beach got there instead of ending up on the ski slopes of a mountain.These specifications can include details about the geographical features, climate, topography, and primary attractions of the location, ensuring that travelers can choose destinations that align with their preferences and expectations. 
  * Connected Pattern: [SpatialObject](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-object/spatial-object.owl)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)
    
* Transport
  * The mode of transportation can also affect the enjoyment the traveller experiences during their trip. They may not want to ride in public transportation and would rather drive themselves to anywhere they want to go at their destination. The traveller could also want their primary transportation to come in the form of walking so it would be better to know that so they can take a trip in a walkable city instead of a place where everything is far away from each other. Recognizing these transportation preferences helps travelers select modes that align with their comfort and travel style, ultimately enhancing their overall travel experience.
  * Connected Pattern:  [Part-whole](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/part-whole), [Hierarchial-cell-features](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/hierarchical-cell-features)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Budget
  * Depending on how high or low the user's budget is they will be provided with more or fewer options to travel to. Providing options that are available for a particular range of budget makes it possible to plan for a trip despite the constraints. Recognizing the budgetary limitations of travelers helps in tailoring recommendations that not only fit their financial capabilities but also ensure that their travel plans are realistic and enjoyable.
  * Connected Pattern: [QuantityPattern](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/quantity/quantity.owl)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Activities
  * Some users would like to plan their trip around certain activies that they can do while travelling. This could also help other users know what sorts of activities are available so that if needed they can make reservations ahead of time so they do not have to miss out on something they might want to do. Recognizing the significance of activities in travel planning allows users to align their travel experiences with their interests and also ensures that they can make necessary arrangements to fully enjoy the activities they desire during their trip.
  * Connected Pattern: [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/provenance), [Temporal extent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/temporal-extent)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Locations based on activity
  * Given the users activity interest they could choose from different locations that offer some or all of the activities. This approach empowers travelers to select destinations that are tailored to their preferred activities, enhancing their overall travel experience by ensuring that their chosen location aligns with their activity interests and enabling them to make the most of their trip.
  * Connected Pattern: [SpatialObject](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-object) or [SpatioTemporalExtent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatiotemporal-extent)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Tourist Spots
  * Tourist spots would be things such as historical monuments, artistic statues, or a particular sight from a mountain that people like to see that the traveller might also want to see while on vacation. This could be important to someone who wants to plan a trip to see both the Colosseum and the statue of David on the same trip to Italy. Understanding the availability and significance of tourist spots aids travelers in creating well-rounded itineraries that encompass cultural, historical, and scenic attractions, ensuring that they can maximize their exploration of the chosen destination.
  * Connected Pattern: [SpatialObject](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-object/spatial-object.owl) or [SpatialExtent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-extent/spatial-extent.owl)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Housing
  * Housing is important while on a vacation. This is where your stuff will be and where you will be sleeping. If your housing is in a bad part of town you may be worrying your entire trip whether or not something will get stolen. Also, if you can not sleep well in whatever housing you choose it will impact your experience as you most likely will not feel as good as you could if you got a full rest each night. Recognizing the significance of suitable accommodations in travel planning ensures that travelers have a secure and comfortable base during their journey, reducing concerns about safety and the quality of their rest, ultimately enhancing the overall travel experience.
  * Connected Pattern: [Part-whole](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/part-whole/part-whole.owl), [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/quantity/quantity.owl), [SpatioTemporalExtent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatiotemporal-extent/spatiotemporal-extent.owl)
  * Source Datasets: [Berlin Airbnb Dataset](https://data.world/datasets/berlin)

* Food
  * Different destinations offer diverse culinary experiences. Understanding the food options available in a location allows travelers to explore and savor the local cuisine, which for food lovers is often a highlight of the trip. For travelers who appreciate culinary adventures, discovering the local cuisine is a significant aspect of their journey. Different destinations provide unique and diverse culinary traditions. Understanding the food options available in a location ensures that food enthusiasts can indulge in the flavors and culinary delights of the region, enhancing their overall travel experience by savoring the local gastronomy.
  * Connected Pattern: [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/provenance), [Temporal extent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/temporal-extent)
  * Source Datasets: [Restaurant info](https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw/) and [Tour Dataset](http://tour-pedia.org/about/datasets.html)

## Contributors
* Rakesh Kandula
