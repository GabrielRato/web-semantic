from SPARQLWrapper import SPARQLWrapper, JSON

#sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql = SPARQLWrapper("http://localhost:3030/teste/sparql")
query0 = """
    SELECT ?s ?p ?o
    WHERE{
        ?s ?p ?o.
    }
"""
query1 = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
"""
sparql.setQuery(query0)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print (results)

for result in results["results"]["bindings"]:
    print('%s: %s' % (result["label"]["xml:lang"], result["label"]["value"]))
