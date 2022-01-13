# NFDI4Culture Ontology

This is the work-in-progress for modelling the NFDI4Culture Ontology. The data can also be queried via SPARQL at https://nfdi.fiz-karlsruhe.de/

## Related Links

[Creating the NFDI4C Knowledge Graph](https://docs.google.com/document/d/1-Xe54rRiw37Z-Y2hJs7_bV5LhgA8DivC8ZFePelT0VU/edit)

[NFDI4C Requirements for CMS <-> Triple Store Connection](https://docs.google.com/document/d/1LjS6o-ZxH6VuXazGNwR3XVaZzKuhiye09gU39O8odMU/edit#heading=h.2e5xs352l20d)

[NFDI Mappings to external vocabs](https://docs.google.com/spreadsheets/d/1rd4-Aroxb1anWPrqQ-Vdt4G8gbPbgorV6u4ugP9xb3w/edit#gid=0)

[Schematically on Miro board](https://miro.com/app/board/uXjVOe0O_9M=/)

[Spreadsheet used to populate the graph](https://docs.google.com/spreadsheets/d/1KkNxgEqW-Y_Ail-Tbz1T-nI_BaDFhVr9nBuuuzi2xGc/edit#gid=1237549318)

### Notes on the endpoint

This is a preliminary version set up to start exploring the data. It uses [Oxigraph](https://github.com/oxigraph/oxigraph) as the server. The endpoint is not protected in any way at the moment, so it means anyone (also from outside) can also execute UPDATE queries and mess with the data. Right now this is acceptable, but we will of course nail this down soon.

Why Oxigraph? To kick the tyres... ☺️ Blazegraph has to all intents and purposes become "abandonware" as the original authors have moved on to Amazon. The creator of Oxigraph has pitched it as a possible replacement (also for things like Wikidata), so maybe it is interesting fo rus to get a feel for it too already. At least the initial deployment is a no-brainer.
