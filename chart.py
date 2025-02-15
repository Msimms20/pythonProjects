from graphviz import Digraph

# Create a properly formatted UML class diagram with rectangular styling
uml_fixed = Digraph('HouseUML_Fixed', format='pdf')

# Set node shape to rectangle
uml_fixed.attr('node', shape='record')

# Define the House class in proper UML style
uml_fixed.node('houses for a real estate broker', '''\
{ houses for a real estate broker |
- address: String\l
- price: Double\l
- squareFootage: Integer\l
- numBedrooms: Integer\l
- numBathrooms: Integer\l
- yearBuilt: Integer\l
- propertyType: String\l
- listingStatus: String\l
- agentName: String\l
- MLSNumber: String\l |
+ getDetails(): String\l
+ updatePrice(newPrice: Double)\l
+ changeListingStatus(newStatus: String)\l
+ scheduleViewing(date: Date, time: String)\l
+ calculatePricePerSquareFoot(): Double\l
+ assignAgent(agentName: String)\l
}''')

# Save and display the fixed diagram
uml_fixed_path = "C:\\Users\\Owner\\PycharmProjects\\UserDefinedObjectDesign\\House_UML_Fixed"
uml_fixed.render(uml_fixed_path)

uml_fixed_path + ".pdf"