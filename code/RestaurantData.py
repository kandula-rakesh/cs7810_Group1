import csv
from rdflib import Graph, Namespace, RDF, RDFS, URIRef, Literal, XSD

# Creating the empty graph
g = Graph()

# Defining the RDF namespaces
# we can define all namespaces in one dictionary.
restaurant = Namespace("restaurant")
location = Namespace("location")
financialResource = Namespace("financialResource")
review = Namespace("review")
schema = Namespace("http://schema.org/")
rdf = RDF
rdfs = RDFS
wkt = Namespace("http://www.opengis.net/ont/geosparql#")
#qudt = Namespace("http://qudt.org/schema/qudt/"),
#time = Namespace("http://www.w3.org/2006/time#")

# Bind the prefixes into the graph
# Multiple usage of bind can be eliminated by using for loop and dict
g.bind("restaurant", restaurant)
g.bind("schema", schema)
g.bind("rdf", rdf)
g.bind("rdfs", rdfs)
g.bind("wkt", wkt)

# Reading the restaurant data from csv file
# for a better experience, we can pass the file name through CLI arguments
with open('../dataset/restaurant-data.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    row_num = 1
    for row in reader:
        rest_id = row['id'].strip()
        name = row['name']
        foodCategory = row['subCategory']
        location_name = row['location']
        geometry_lat = row['lat']
        geometry_lon = row['lng']
        price = row['price']
        review_url = row['reviews']
        review_source = row['source']
        review_rating = row['rating']
        review_text = row['text']
        
        # Creating URI for the restaurant
        # strip the spaces it creates a problem while creating URI
        
        restaurant_uri = restaurant[rest_id]

        # Adding triples related to the restaurant
        g.add((restaurant_uri, rdf.type, schema.Restaurant))
        g.add((restaurant_uri, schema.hasName, Literal(name,datatype=XSD.string)))
        
        if foodCategory != "":
            g.add((restaurant_uri, schema.hasFoodCategory, Literal(price,datatype=XSD.string)))
            
        location_uri = location[rest_id]
        g.add((location_uri, rdf.type, schema.Location))
        g.add((location_uri,  schema.hasName, Literal(location_name,datatype=XSD.string)))
        g.add((restaurant_uri, schema.hasLocation, location_uri))
        
        financial_resource_uri = financialResource[rest_id]
        g.add((financial_resource_uri, rdf.type, schema.FinancialResource))
        g.add((financial_resource_uri,  schema.hasCost, Literal(price,datatype=XSD.double)))
        g.add((restaurant_uri, schema.hasCost, financial_resource_uri))
        
        review_uri = review[rest_id]
        g.add((review_uri, rdf.type, schema.Review))
        g.add((review_uri, schema.hasURL, Literal(review_url, datatype=XSD.stringURI)))
        if review_source != "":
            g.add((review_uri, schema.hasName, Literal(review_source, datatype=XSD.string)))
            if review_rating != "":
                g.add((review_uri, schema.hasRating, Literal(review_rating, datatype=XSD.integer)))
            if review_text != "":
                g.add((review_uri, schema.hasText, Literal(review_text, datatype=XSD.string)))
        
        g.add((restaurant_uri, schema.hasReview, review_uri))
        
        wkt_literal = f"POINT({geometry_lon} {geometry_lat})"
        spacial_object_uri = wkt[rest_id]
        g.add((spacial_object_uri, rdf.type, schema.SpacialObject))
        g.add((spacial_object_uri, schema.asWKT, Literal(wkt_literal, datatype=wkt.wktLiteral)))
        g.add((restaurant_uri, schema.isA, spacial_object_uri))
        

# Serializing the graph into turtle format to query using SPARQL
output_file = "restaurant-data.ttl"
g.serialize(destination=output_file, format="turtle")