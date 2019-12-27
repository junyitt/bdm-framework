import platform
import socket
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

g = Graph()

# example of creating triples for a specific machine
machine1 = BNode()

# Data Extraction and Data Cleansing
cpu_info = cpuinfo.get_cpu_info()
system = platform.system()
os_version = platform.platform().split("-")[1]
update_version = platform.platform().split("-")[2].replace(".", "_")
proc_model = platform.processor()

# Add triples to graph
g.add( (machine1, RDF.type, FOAF.machine) )
g.add( (machine1, FOAF.name, Literal(socket.gethostname()) ))
g.add( (machine1, FOAF.ossystem, Literal(system) ))
g.add( (machine1, FOAF.osversion, Literal(os_version) ))
g.add( (machine1, FOAF.updateversion, Literal(update_version) ))
g.add( (machine1, FOAF.processor, Literal(proc_model) ))
g.add( (machine1, FOAF.architecture, Literal(cpu_info["arch"]) ))
g.add( (machine1, FOAF.bits, Literal(cpu_info["bits"]) ))
g.add( (machine1, FOAF.vendor, Literal(cpu_info["vendor_id"]) ))
g.add( (machine1, FOAF.brand, Literal(cpu_info["brand"]) ))


# print the triples in the entire graph
for s,p,o in g:
    print(s,p,o)
