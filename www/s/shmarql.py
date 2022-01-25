from htmltree import *

status_box = document.getElementById("status_box")
results_element = document.getElementById("results")

document.curr_s = "?s"
document.curr_p = "?p"
document.curr_o = "?o"

PREFIX = {
    "https://www.nfdi4culture.de/ontology/": "nfdico:",
    "https://www.nfdi4culture.de/resource/": "nfdires:",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#": "rdf:",
    "http://www.w3.org/2000/01/rdf-schema#": "rdfs:",
}


def find_attr_parents(element, attr):
    val = element.getAttribute(attr)
    if val and len(val) > 0:
        return val
    parent = element.parentElement
    if parent:
        return find_attr_parents(parent, attr)


def snippet(param, elem):
    value = elem["value"]
    d = Div()
    if elem["type"] == "uri":
        if param == "s" and value == document.curr_s:
            d.C.append(Span("&middot;"))
        else:
            d.C.append(
                Span(
                    "S",
                    _class="selektor",
                    uri=value,
                    wanted="S",
                ),
            )

        if param == "p" and value == document.curr_p:
            d.C.append(Span("&middot;"))
        else:
            d.C.append(
                Span("P", _class="selektor", uri=value, wanted="P"),
            )

        if param == "o" and value == document.curr_o:
            d.C.append(Span("&middot;"))
        else:
            d.C.append(
                Span("O", _class="selektor", uri=value, wanted="O"),
            )
        display_value = value
        for prefix, replacement in PREFIX.items():
            if value.startswith(prefix):
                display_value = value.replace(prefix, replacement)

        d.C.append(
            A(
                display_value,
                href=value,
                target="other",
                style={"text-decoration": "none", "color": "black"},
            ),
        )
    else:
        d.C.append(Span(value))
    return d.render()


def display(results):
    if "results" in results and "bindings" in results["results"]:
        results = results["results"]["bindings"]
    t = Table(
        Thead(
            Tr(
                Td(Span(document.curr_s, _class="btn btn-sm", uri="?s", wanted="S")),
                Td(Span(document.curr_p, _class="btn btn-sm", uri="?p", wanted="P")),
                Td(Span(document.curr_o, _class="btn btn-sm", uri="?o", wanted="O")),
            )
        ),
        _class="table table-striped",
    )
    tbody = Tbody()
    t.C.append(tbody)
    for row in results:
        if "s" not in row:
            row["s"] = {"type": "uri", "value": document.curr_s}
        if "p" not in row:
            row["p"] = {"type": "uri", "value": document.curr_p}
        if "o" not in row:
            row["o"] = {"type": "uri", "value": document.curr_o}

        tbody.C.append(
            Tr(
                Td(snippet("s", row["s"])),
                Td(snippet("p", row["p"])),
                Td(snippet("o", row["o"])),
            )
        )
    buf = t.render()
    results_element.innerHTML = buf


async def sparql(endpoint, q):
    __pragma__("jsiter")
    res = await fetch(
        endpoint,
        {
            "method": "POST",
            "headers": {
                "Accept": "application/sparql-results+json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            "body": "query=" + encodeURIComponent(q),
        },
    )
    return await res.json()
    __pragma__("nojsiter")


def flash(msg):
    status_box.innerHTML = msg
    status_box.style.display = "block"


async def change_endpoint():
    ep = "https://nfdi.fiz-karlsruhe.de/nfdico/sparql"
    results_element.innerHTML = '<div style="margin-top: 20px" class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>'

    q = "SELECT * WHERE { "
    if document.curr_s != "?s":
        q += "<" + document.curr_s + "> "
    else:
        q += document.curr_s + " "
    if document.curr_p != "?p":
        q += "<" + document.curr_p + "> "
    else:
        q += document.curr_p + " "
    if document.curr_o != "?o":
        q += "<" + document.curr_o + ">"
    else:
        q += document.curr_o
    q += " } ORDER BY DESC(?s) LIMIT 1000"

    results = await sparql(ep, q)
    display(results)


async def results_clicker(event):
    document.getElementById("status_box").style.display = "none"
    wanted = find_attr_parents(event.target, "wanted")  # One of: S, P, O
    uri = find_attr_parents(event.target, "uri")
    if wanted == "S":
        document.curr_s = uri
    if wanted == "P":
        document.curr_p = uri
    if wanted == "O":
        document.curr_o = uri
    change_endpoint()


async def navtabs_clicker(event):
    event.preventDefault()
    document.getElementById("sprql").style.display = "none"
    document.getElementById("shmrql").style.display = "none"
    for nav_link in document.getElementsByClassName("nav-link"):
        nav_link.classList.remove("active")
    event.target.classList.add("active")
    tabid = find_attr_parents(event.target, "tabid")
    if len(tabid) > 2:
        elemt = document.getElementById(tabid)
        elemt.style.display = "block"


async def init():
    navtabs = document.getElementById("navtabs")
    navtabs.addEventListener("click", navtabs_clicker)
    results_element.addEventListener("click", results_clicker)
    change_endpoint()


window.addEventListener("load", init)
