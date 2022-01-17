# NFDI4Culture Ontology

This is the work-in-progress for modelling the NFDI4Culture Ontology. The data can also be queried via SPARQL at https://nfdi.fiz-karlsruhe.de/

## Related Links

[Creating the NFDI4C Knowledge Graph](https://docs.google.com/document/d/1-Xe54rRiw37Z-Y2hJs7_bV5LhgA8DivC8ZFePelT0VU/edit)

[NFDI4C Requirements for CMS <-> Triple Store Connection](https://docs.google.com/document/d/1LjS6o-ZxH6VuXazGNwR3XVaZzKuhiye09gU39O8odMU/edit#heading=h.2e5xs352l20d)

[NFDI Mappings to external vocabs](https://docs.google.com/spreadsheets/d/1rd4-Aroxb1anWPrqQ-Vdt4G8gbPbgorV6u4ugP9xb3w/edit#gid=0)

[Schematically on Miro board](https://miro.com/app/board/uXjVOe0O_9M=/)

[Spreadsheet used to populate the graph](https://docs.google.com/spreadsheets/d/1KkNxgEqW-Y_Ail-Tbz1T-nI_BaDFhVr9nBuuuzi2xGc/edit#gid=1237549318)

### Notes on the endpoint

This is a preliminary version set up to start exploring the data.
We have now switched to using [Apache Jena/Fuseki](https://jena.apache.org/documentation/fuseki2/) as the triplestore and SPARQL query engine.

In a previous version we briefly explored using [Oxigraph](https://github.com/oxigraph/oxigraph) but it does not have sufficient inferencing capabilities at this point in time (eg. lacking [RDF Entailment](https://www.w3.org/TR/2013/REC-sparql11-entailment-20130321/)) It is something to keep an eye on for large-scale datasets and simplicity of implmentation.
