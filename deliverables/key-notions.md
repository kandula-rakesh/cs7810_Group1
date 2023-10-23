* Specifications of Location
  * Having an understanding of the location where the tourist is going helps in having a better experience of the trip.
  * Connected Pattern: [SpatialObject](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-object/spatial-object.owl)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)
    
* Transport
  * Figuring out what mode of transportation works well with the budget keeps the traveler planned
  * Connected Pattern:  [Part-whole](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/part-whole), [Hierarchial-cell-features](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/hierarchical-cell-features)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Budget
  * Depending on how high or low the user's budget is they will be provided with more or fewer options to travel to. Providing options that are available for a particular range of budget makes it possible to plan for a trip despite the constraints
  * Connected Pattern: [QuantityPattern](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/quantity/quantity.owl)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Activities
  * Giving the user a variety of activities they can partake in helps ensure that the trip is personalized for them. 
  * Connected Pattern: [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/provenance), [Temporal extent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/temporal-extent)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Locations based on activity
  * Given the users activity interest they could choose from different locations that offer some or all of the activities.
  * Connected Pattern: [SpatialObject](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-object) or [SpatioTemporalExtent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatiotemporal-extent)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Tourist Spots
  * Knowledge of tourist locations help users identify must-see locations around their destination. 
  * Connected Pattern: [SpatialObject](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-object/spatial-object.owl) or [SpatialExtent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatial-extent/spatial-extent.owl)
  * Source Datasets: [Tour Dataset](http://tour-pedia.org/about/datasets.html)

* Housing
  * Having differnt housing options available for users is vital for ensuring a comfortable and budget friendly stay during the trip.
  * Connected Pattern: [Part-whole](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/part-whole/part-whole.owl), [Quantity](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/quantity/quantity.owl), [SpatioTemporalExtent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/spatiotemporal-extent/spatiotemporal-extent.owl)
  * Source Datasets: [Berlin Airbnb Dataset](https://data.world/datasets/berlin)

* Food
  * Different destinations offer diverse culinary experiences. Understanding the food options available in a location allows travelers to explore and savor the local cuisine, which for food lovers is often a highlight of the trip.
  * Connected Pattern: [Provenance](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/provenance), [Temporal extent](https://github.com/kastle-lab/modular-ontology-design-library/blob/master/modl/temporal-extent)
  * Source Datasets: [Restaurant info](https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw/) and [Tour Dataset](http://tour-pedia.org/about/datasets.html)

