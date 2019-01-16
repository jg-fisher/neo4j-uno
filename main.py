"""
Imports for connecting to the NEO4J Database.
"""
from config import NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD
from neo4j import GraphDatabase
from flask import Flask

""""
Initial username is 'neo4j'
Password is set with $ROOT_NEO4J_PATH\neo4j-admin.bat set-initial-password <password_name>
"""
print(NEO4J_USERNAME, NEO4J_PASSWORD)

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

"""
Flask server object instance.
"""
app = Flask(__name__)

"""
Route for executing queries against the database.
"""
# TODO: Set the parameter value for the query or read it off of the body (safer this cant be sniffed)
@app.route('/query', methods=['POST'])
def index():
    return session.read_transaction()

if __name__ == '__main__':
    """
    Scoping NEO4J DB context.
    """
    with driver.session() as session:

        """
        Starting Flask server.
        """
        app.run(debug=True)

    
