import csv
import os
import pandas as pd
from rdflib import URIRef, Graph, Namespace, Literal
from rdflib import OWL, RDF, RDFS, XSD, TIME

name_space = "https://kastle-lab.org/"
pfs = {
"kl-res": Namespace(f"{name_space}lod/resource/"),
"kl-ont": Namespace(f"{name_space}lod/ontology/"),
"geo": Namespace("http://www.opengis.net/ont/geosparql#"),
"rdf": RDF,
"rdfs": RDFS,
"xsd": XSD,
"owl": OWL,
"time": TIME
}

# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]
#defining entities
Restaurant = pfs["kl-ont"]["Restaurant"]
Category = pfs["kl-ont"]["Category"]
Location = pfs["kl-ont"]["Location"]
Accomodation = pfs['kl-ont']['Accomodation']
Attraction =  pfs['kl-ont']['Attraction']
Review = pfs["kl-ont"]["Review"]
Source = pfs["kl-ont"]["Source"]
SpatialObject = pfs["kl-ont"]["SpatialObject"]
Geometry = pfs['geo']['Geometry']
                       
#defining object properties
hasName = pfs["kl-ont"]["hasName"]
hasCategory = pfs["kl-ont"]["hasCategory"]
hasSource = pfs["kl-ont"]["hasSource"]
hasRating = pfs["kl-ont"]["hasRating"]
hasText = pfs["kl-ont"]["hasText"]
hasID = pfs["kl-ont"]["hasID"]
hasLocation = pfs["kl-ont"]["hasLocation"]
hasRestaurant = pfs["kl-ont"]["hasRestaurant"]
hasAccomodation = pfs["kl-ont"]["hasAccomodation"]
hasAttraction = pfs["kl-ont"]["hasAttraction"]
hasCost = pfs["kl-ont"]["hasCost"]
hasURL = pfs["kl-ont"]["hasURL"]
hasReview = pfs["kl-ont"]["hasReview"]
isA = pfs["kl-ont"]["isA"]

# Initialize an empty graph
g = init_kg()

#creating a dataframe for reviews data
restaurant_review_file = '..\\dataset\\restaurant_reviews.csv'
accomodation_review_file = '..\\dataset\\accomodation_reviews.csv'
attraction_review_file = '..\\dataset\\attractions_reviews.csv'
transport_review_file = '..\\dataset\\transport_reviews.csv'
# Read the reviews CSV file and store it in a DataFrame
restaurant_reviews_df = pd.read_csv(restaurant_review_file)
accomodation_reviews_df = pd.read_csv(accomodation_review_file)
attraction_reviews_df = pd.read_csv(attraction_review_file)
transport_reviews_df = pd.read_csv(transport_review_file)

def add_reviews_to_kg(id,dataframe,entity_uri,review_uri):
    if id in dataframe['id'].values:
        #print("entering into reviews",id)
        filtered_rows = dataframe[dataframe['id'] == id]
        # Display the filtered rows
        #print(filtered_rows)
        for index, row in filtered_rows.iterrows():
            # extract each review of the current restaurant
            #print(f"index is: {index}")
            id_value = row['id']
            source = row['source']
            rating = row['rating']
            text = row['text']
            source_uri = pfs["kl-res"][source]
            g.add((source_uri, a, Source))
            g.add((review_uri, hasSource, source_uri))
            g.add((source_uri, hasRating, Literal(rating,datatype=XSD.integer)))
            g.add((source_uri, hasName, Literal(source,datatype=XSD.string)))
            g.add((source_uri, hasText, Literal(text,datatype=XSD.string)))
            g.add((source_uri, hasID, entity_uri))


# Reading the restaurant data from csv file
# for a better experience, we can pass the file name through CLI arguments
with open('..\\dataset\\restaurant_combined.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    row_num = 1
    for row in reader:
        id = row['id'].strip()
        name = row['name']
        food_category = row['subCategory'].replace(' ', '_')
        location_name = row['location']
        geometry_lat = row['lat']
        geometry_lon = row['lng']
        price = int(row['Cost'])
        review_url = row['reviews']
        
        # Creating URI for the restaurant
        # strip the spaces it creates a problem while creating URI
        #g.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) )
        restaurant_uri = pfs["kl-res"][id]

        # Adding triples related to the restaurant
        g.add((restaurant_uri, a,Restaurant))
        g.add((restaurant_uri, hasName, Literal(name,datatype=XSD.string)))
        
        if food_category != "":
            food_category_uri = pfs["kl-res"][food_category]
            g.add((food_category_uri, a,Category))
            g.add((restaurant_uri, hasCategory, food_category_uri))
            
        location_uri = pfs["kl-res"][location_name]
        g.add((location_uri, a, Location))
        g.add((location_uri,  hasName, Literal(location_name,datatype=XSD.string)))
        g.add((location_uri,  hasRestaurant, restaurant_uri))
        g.add((restaurant_uri, hasLocation, location_uri))
        g.add((restaurant_uri, hasCost, Literal(price,datatype=XSD.integer)))
        
        review_uri = pfs["kl-res"][review_url]
        g.add((restaurant_uri, hasReview, review_uri))
        g.add((review_uri, a, Review))
        g.add((review_uri, hasURL, Literal(review_url, datatype=XSD.string)))
        #filtering the reviews of the restaurant using its ID and adding it into graph
        id = int(id)
        if id in restaurant_reviews_df['id'].values:
            #print("entering into reviews",id)
            filtered_rows = restaurant_reviews_df[restaurant_reviews_df['id'] == id]
            # Display the filtered rows
            #print(filtered_rows)
            for index, row in filtered_rows.iterrows():
                # extract each review of the current restaurant
                #print(f"index is: {index}")
                id_value = row['id']
                source = row['source']
                rating = row['rating']
                text = row['text']
                source_uri = pfs["kl-res"][source]
                g.add((source_uri, a, Source))
                g.add((review_uri, hasSource, source_uri))
                g.add((source_uri, hasRating, Literal(rating,datatype=XSD.integer)))
                g.add((source_uri, hasName, Literal(source,datatype=XSD.string)))
                g.add((source_uri, hasText, Literal(text,datatype=XSD.string)))
                g.add((source_uri, hasID, restaurant_uri))
                # Process or perform operations on the current row
                #print(f"id: {id_value}, source: {source}, rating: {rating}, text: {text}")
        #Adding Geometry point as WKT
        wkt_literal = f"POINT({geometry_lon} {geometry_lat})"
        point_uri = pfs["kl-res"][f"{'geometry.point'}.{id}"]
        g.add((restaurant_uri,  pfs["geo"]["hasGeometry"],point_uri))
        #g.add((point_uri,  pfs["rdfs"]["subClassOf"],SpatialObject))
        g.add((point_uri, a, pfs["geo"]["hasGeometry"]))
        #g.add((point_uri, a, Geometry))
        g.add((point_uri, pfs["geo"]["asWKT"], Literal(wkt_literal, datatype=pfs["geo"]["wktLiteral"]) ))


with open('..\\dataset\\accomodation_filtered.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    row_num = 1
    for row in reader:
        id = row['id'].strip()
        name = row['name']
        category = row['subCategory'].replace(' ', '_')
        location_name = row['location']
        geometry_lat = row['lat']
        geometry_lon = row['lng']
        price = int(row['Cost'])
        review_url = row['reviews']
        # Creating URI for the restaurant
        # strip the spaces it creates a problem while creating URI
        # g.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) )
        accomodation_uri = pfs["kl-res"][id]

        # Adding triples related to the restaurant
        g.add((accomodation_uri, a,Accomodation))
        g.add((accomodation_uri, hasName, Literal(name,datatype=XSD.string)))
        
        if category != "":
            category_uri = pfs["kl-res"][category]
            g.add((category_uri, a,Category))
            g.add((accomodation_uri, hasCategory, category_uri))
            
        location_uri = pfs["kl-res"][location_name]
        g.add((location_uri, a, Location))
        g.add((location_uri,  hasName, Literal(location_name,datatype=XSD.string)))
        g.add((location_uri,  hasAccomodation, accomodation_uri))
        g.add((accomodation_uri, hasLocation, location_uri))
        g.add((accomodation_uri, hasCost, Literal(price,datatype=XSD.integer)))
        
        review_uri = pfs["kl-res"][review_url]
        g.add((accomodation_uri, hasReview, review_uri))
        g.add((review_uri, a, Review))
        g.add((review_uri, hasURL, Literal(review_url, datatype=XSD.string)))
        #filtering the reviews of the restaurant using its ID and adding it into graph
        id = int(id)
        if id in restaurant_reviews_df['id'].values:
            #print("entering into reviews",id)
            filtered_rows = restaurant_reviews_df[restaurant_reviews_df['id'] == id]
            # Display the filtered rows
            #print(filtered_rows)
            for index, row in filtered_rows.iterrows():
                # extract each review of the current restaurant
                #print(f"index is: {index}")
                id_value = row['id']
                source = row['source']
                rating = row['rating']
                text = row['text']
                source_uri = pfs["kl-res"][source]
                g.add((source_uri, a, Source))
                g.add((review_uri, hasSource, source_uri))
                g.add((source_uri, hasRating, Literal(rating,datatype=XSD.integer)))
                g.add((source_uri, hasName, Literal(source,datatype=XSD.string)))
                g.add((source_uri, hasText, Literal(text,datatype=XSD.string)))
                g.add((source_uri, hasID, accomodation_uri))
                # Process or perform operations on the current row
                #print(f"id: {id_value}, source: {source}, rating: {rating}, text: {text}")
        #Adding Geometry point as WKT
        wkt_literal = f"POINT({geometry_lon} {geometry_lat})"
        point_uri = pfs["kl-res"][f"{'geometry.point'}.{id}"]
        g.add((accomodation_uri,  pfs["geo"]["hasGeometry"],point_uri))
        #g.add((point_uri,  pfs["rdfs"]["subClassOf"],SpatialObject))
        g.add((point_uri, a, pfs["geo"]["hasGeometry"]))
        #g.add((point_uri, a, Geometry))
        g.add((point_uri, pfs["geo"]["asWKT"], Literal(wkt_literal, datatype=pfs["geo"]["wktLiteral"]) ))


with open('..\\dataset\\attractions_combined.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    row_num = 1
    for row in reader:
        id = row['id'].strip()
        name = row['name']
        category = row['subCategory'].replace(' ', '_')
        location_name = row['location']
        geometry_lat = row['lat']
        geometry_lon = row['lng']
        price = int(row['Cost'])
        review_url = row['reviews']
        # Creating URI for the restaurant
        # strip the spaces it creates a problem while creating URI
        # g.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) )
        attraction_uri = pfs["kl-res"][id]

        # Adding triples related to the restaurant
        g.add((attraction_uri, a,Attraction))
        g.add((attraction_uri, hasName, Literal(name,datatype=XSD.string)))
        
        if category != "":
            category_uri = pfs["kl-res"][category]
            g.add((category_uri, a,Category))
            g.add((attraction_uri, hasCategory, category_uri))
            
        location_uri = pfs["kl-res"][location_name]
        g.add((location_uri, a, Location))
        g.add((location_uri,  hasName, Literal(location_name,datatype=XSD.string)))
        g.add((location_uri,  hasAttraction, attraction_uri))
        g.add((attraction_uri, hasLocation, location_uri))
        g.add((attraction_uri, hasCost, Literal(price,datatype=XSD.integer)))
        
        review_uri = pfs["kl-res"][review_url]
        g.add((attraction_uri, hasReview, review_uri))
        g.add((review_uri, a, Review))
        g.add((review_uri, hasURL, Literal(review_url, datatype=XSD.string)))
        #filtering the reviews of the restaurant using its ID and adding it into graph
        id = int(id)
        if id in attraction_reviews_df['id'].values:
            #print("entering into reviews",id)
            filtered_rows = attraction_reviews_df[attraction_reviews_df['id'] == id]
            # Display the filtered rows
            #print(filtered_rows)
            for index, row in filtered_rows.iterrows():
                # extract each review of the current restaurant
                #print(f"index is: {index}")
                id_value = row['id']
                source = row['source']
                rating = row['rating']
                text = row['text']
                source_uri = pfs["kl-res"][source]
                g.add((source_uri, a, Source))
                g.add((review_uri, hasSource, source_uri))
                g.add((source_uri, hasRating, Literal(rating,datatype=XSD.integer)))
                g.add((source_uri, hasName, Literal(source,datatype=XSD.string)))
                g.add((source_uri, hasText, Literal(text,datatype=XSD.string)))
                g.add((source_uri, hasID, attraction_uri))
                # Process or perform operations on the current row
                #print(f"id: {id_value}, source: {source}, rating: {rating}, text: {text}")
        #Adding Geometry point as WKT
        wkt_literal = f"POINT({geometry_lon} {geometry_lat})"
        point_uri = pfs["kl-res"][f"{'geometry.point'}.{id}"]
        g.add((attraction_uri,  pfs["geo"]["hasGeometry"],point_uri))
        #g.add((point_uri,  pfs["rdfs"]["subClassOf"],SpatialObject))
        g.add((point_uri, a, pfs["geo"]["hasGeometry"]))
        #g.add((point_uri, a, Geometry))
        g.add((point_uri, pfs["geo"]["asWKT"], Literal(wkt_literal, datatype=pfs["geo"]["wktLiteral"]) ))

with open('..\\dataset\\transport_filtered.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    row_num = 1
    for row in reader:
        id = row['id'].strip()
        name = row['name']
        category = row['subCategory'].replace(' ', '_')
        location_name = row['location']
        geometry_lat = row['lat']
        geometry_lon = row['lng']
        price = int(row['Cost'])
        review_url = row['reviews']
        # Creating URI for the restaurant
        # strip the spaces it creates a problem while creating URI
        # g.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) )
        transport_uri = pfs["kl-res"][id]

        # Adding triples related to the restaurant
        g.add((transport_uri, a,Attraction))
        g.add((transport_uri, hasName, Literal(name,datatype=XSD.string)))
        
        if category != "":
            category_uri = pfs["kl-res"][category]
            g.add((category_uri, a,Category))
            g.add((transport_uri, hasCategory, category_uri))
            
        location_uri = pfs["kl-res"][location_name]
        g.add((location_uri, a, Location))
        g.add((location_uri,  hasName, Literal(location_name,datatype=XSD.string)))
        g.add((location_uri,  hasAttraction, transport_uri))
        g.add((transport_uri, hasLocation, location_uri))
        g.add((transport_uri, hasCost, Literal(price,datatype=XSD.integer)))
        
        review_uri = pfs["kl-res"][review_url]
        g.add((transport_uri, hasReview, review_uri))
        g.add((review_uri, a, Review))
        g.add((review_uri, hasURL, Literal(review_url, datatype=XSD.string)))
        #filtering the reviews of the restaurant using its ID and adding it into graph
        id = int(id)
        if id in attraction_reviews_df['id'].values:
            #print("entering into reviews",id)
            filtered_rows = attraction_reviews_df[attraction_reviews_df['id'] == id]
            # Display the filtered rows
            #print(filtered_rows)
            for index, row in filtered_rows.iterrows():
                # extract each review of the current restaurant
                #print(f"index is: {index}")
                id_value = row['id']
                source = row['source']
                rating = row['rating']
                text = row['text']
                source_uri = pfs["kl-res"][source]
                g.add((source_uri, a, Source))
                g.add((review_uri, hasSource, source_uri))
                g.add((source_uri, hasRating, Literal(rating,datatype=XSD.integer)))
                g.add((source_uri, hasName, Literal(source,datatype=XSD.string)))
                g.add((source_uri, hasText, Literal(text,datatype=XSD.string)))
                g.add((source_uri, hasID, transport_uri))
                # Process or perform operations on the current row
                #print(f"id: {id_value}, source: {source}, rating: {rating}, text: {text}")
        #Adding Geometry point as WKT
        wkt_literal = f"POINT({geometry_lon} {geometry_lat})"
        point_uri = pfs["kl-res"][f"{'geometry.point'}.{id}"]
        g.add((transport_uri,  pfs["geo"]["hasGeometry"],point_uri))
        #g.add((point_uri,  pfs["rdfs"]["subClassOf"],SpatialObject))
        g.add((point_uri, a, pfs["geo"]["hasGeometry"]))
        #g.add((point_uri, a, Geometry))
        g.add((point_uri, pfs["geo"]["asWKT"], Literal(wkt_literal, datatype=pfs["geo"]["wktLiteral"]) ))

# Define the output folder and file name
output_folder = "..\\output"
output_file = os.path.join(output_folder, 'travel_knowledge_graph.ttl')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Folder '{output_folder}' created successfully.")

# Serialize the RDF graph and store in the output file
temp = g.serialize(format="turtle", encoding="utf-8", destination=output_file)
print(f"File '{output_file}' created in the output folder.")