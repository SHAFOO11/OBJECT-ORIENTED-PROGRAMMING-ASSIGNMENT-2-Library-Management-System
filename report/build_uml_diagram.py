"""Builds uml_class_diagram.dot -> uml_class_diagram.png via Graphviz.

Manual layout (instead of Mermaid's auto-router) so relationship lines can be
routed cleanly without crossing through unrelated boxes.
"""

FILL = "#ECECFF"
BORDER = "#9370DB"
HEADER_BORDER = "#9370DB"

CLASSES = {
    "Person": {
        "abstract": True,
        "attrs": ["- name : String", "- id : String", "- contactNumber : String"],
        "methods": [
            "+ getName() : String",
            "+ setName(name) : void",
            "+ getContactNumber() : String",
            "+ setContactNumber(contactNumber) : void",
            ("+ displayDetails() : String", True),
        ],
    },
    "Member": {
        "abstract": False,
        "attrs": ["- membershipId : String", "- borrowedCount : int", "- fineBalance : double"],
        "methods": [
            "+ getMembershipId() : String",
            "+ incrementBorrowedCount() : void",
            "+ decrementBorrowedCount() : void",
            "+ getFineBalance() : double",
            "+ addFine(amount) : void",
            "+ displayDetails() : String",
        ],
    },
    "Librarian": {
        "abstract": False,
        "attrs": ["- staffId : String", "- department : String"],
        "methods": [
            "+ getStaffId() : String",
            "+ getDepartment() : String",
            "+ displayDetails() : String",
        ],
    },
    "LibraryItem": {
        "abstract": True,
        "attrs": ["- itemId : String", "- title : String", "- available : boolean"],
        "methods": [
            "+ getItemId() : String",
            "+ getTitle() : String",
            "+ isAvailable() : boolean",
            "+ setAvailable(available) : void",
            ("+ calculateLateFee(daysLate) : double", True),
            ("+ getItemType() : String", True),
            "+ displaySummary() : String",
        ],
    },
    "Book": {
        "abstract": False,
        "attrs": ["- author : String", "- isbn : String"],
        "methods": ["+ calculateLateFee(daysLate) : double", "+ getItemType() : String"],
    },
    "DVD": {
        "abstract": False,
        "attrs": ["- director : String", "- durationMinutes : int"],
        "methods": ["+ calculateLateFee(daysLate) : double", "+ getItemType() : String"],
    },
    "Loan": {
        "abstract": False,
        "attrs": ["- member : Member", "- item : LibraryItem", "- borrowDate : String", "- returned : boolean"],
        "methods": [
            "+ calculateFine(daysLate) : double",
            "+ markReturned() : void",
            "+ displaySummary() : String",
        ],
    },
    "Library": {
        "abstract": False,
        "attrs": [
            "- members : List&lt;Member&gt;",
            "- librarians : List&lt;Librarian&gt;",
            "- items : List&lt;LibraryItem&gt;",
            "- loans : List&lt;Loan&gt;",
        ],
        "methods": [
            "+ registerMember(member) : void",
            "+ registerLibrarian(librarian) : void",
            "+ addItem(item) : void",
            "+ borrowItem(memberId, itemId, borrowDate) : boolean",
            "+ returnItem(itemId, daysLate) : double",
            "+ searchItemsByTitle(keyword) : List",
            "+ saveToFile() : void",
            "+ loadFromFile() : void",
        ],
    },
    "Main": {
        "abstract": False,
        "attrs": [],
        "methods": ["+ main(args) : void"],
    },
}


def method_line(m):
    text, italic = m if isinstance(m, tuple) else (m, False)
    return f"<I>{text}</I>" if italic else text


def node_label(name, spec):
    rows = []
    header = f"<B>{name}</B>"
    if spec["abstract"]:
        header = f'<FONT POINT-SIZE="10"><I>&laquo;abstract&raquo;</I></FONT><BR/>' + header
    rows.append(f'<TR><TD BGCOLOR="{FILL}">{header}</TD></TR>')

    if spec["attrs"]:
        body = '<BR ALIGN="LEFT"/>'.join(spec["attrs"]) + '<BR ALIGN="LEFT"/>'
        rows.append(f'<TR><TD BGCOLOR="{FILL}" ALIGN="LEFT">{body}</TD></TR>')

    if spec["methods"]:
        body = '<BR ALIGN="LEFT"/>'.join(method_line(m) for m in spec["methods"]) + '<BR ALIGN="LEFT"/>'
        rows.append(f'<TR><TD BGCOLOR="{FILL}" ALIGN="LEFT">{body}</TD></TR>')

    table = (
        f'<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="6" '
        f'COLOR="{BORDER}">' + "".join(rows) + "</TABLE>"
    )
    return f'{name} [shape=plaintext, fontname="Helvetica", fontsize=11, label=<{table}>];'


lines = []
lines.append("digraph LibrarySystem {")
lines.append('  rankdir=TB;')
lines.append('  splines=ortho;')
lines.append('  nodesep=0.65;')
lines.append('  ranksep=0.9;')
lines.append('  bgcolor="white";')
lines.append('  node [fontname="Helvetica"];')
lines.append('  edge [fontname="Helvetica", fontsize=9, color="#333333", penwidth=1.1];')
lines.append("")

for name, spec in CLASSES.items():
    lines.append("  " + node_label(name, spec))
lines.append("")

# Explicit rank rows to keep the two hierarchies visually separated,
# with Loan and Library bridging them down the middle.
lines.append("  { rank=same; Main; }")
lines.append("  { rank=same; Library; }")
lines.append("  { rank=same; Person; LibraryItem; }")
lines.append("  { rank=same; Librarian; Member; Loan; Book; DVD; }")
lines.append("")

# Invisible ordering edges to fix left-to-right node order per rank
# without adding a visible relationship line.
lines.append('  Person -> LibraryItem [style=invis];')
lines.append('  Librarian -> Member [style=invis];')
lines.append('  Member -> Loan [style=invis];')
lines.append('  Loan -> Book [style=invis];')
lines.append('  Book -> DVD [style=invis];')
lines.append("")

# Inheritance (hollow triangle sits at the superclass end; tail=superclass
# keeps it ranked above the subclass so the layout reads top-down).
lines.append('  Person -> Member [dir=back, arrowtail=onormal, arrowsize=1.3, weight=10];')
lines.append('  Person -> Librarian [dir=back, arrowtail=onormal, arrowsize=1.3, weight=10];')
lines.append('  LibraryItem -> Book [dir=back, arrowtail=onormal, arrowsize=1.3, weight=10];')
lines.append('  LibraryItem -> DVD [dir=back, arrowtail=onormal, arrowsize=1.3, weight=10];')
lines.append("")

# Association (Loan refers to a Member and a LibraryItem). constraint=false
# stops these from fighting the explicit rank layout below.
lines.append('  Loan -> Member [arrowhead=vee, arrowsize=0.9, xlabel="borrowed by", '
              'taillabel="many", headlabel="1", labeldistance=1.8, weight=5, constraint=false];')
lines.append('  Loan -> LibraryItem [arrowhead=vee, arrowsize=0.9, xlabel="refers to", '
              'taillabel="many", headlabel="1", labeldistance=1.8, weight=5, constraint=false];')
lines.append("")

# Aggregation (Library owns the collections; open diamond sits at Library).
lines.append('  Library -> Member [dir=both, arrowtail=odiamond, arrowhead=none, '
              'xlabel="registers", taillabel="1", headlabel="many", labeldistance=1.8, weight=3];')
lines.append('  Library -> Librarian [dir=both, arrowtail=odiamond, arrowhead=none, '
              'xlabel="registers", taillabel="1", headlabel="many", labeldistance=1.8, weight=3];')
lines.append('  Library -> LibraryItem [dir=both, arrowtail=odiamond, arrowhead=none, '
              'xlabel="catalogs", taillabel="1", headlabel="many", labeldistance=1.8, weight=8];')
lines.append('  Library -> Loan [dir=both, arrowtail=odiamond, arrowhead=none, '
              'xlabel="tracks", taillabel="1", headlabel="many", labeldistance=1.8, weight=8];')
lines.append("")

# Dependency (Main uses Library).
lines.append('  Main -> Library [style=dashed, arrowhead=vee, xlabel="uses", weight=10];')
lines.append("")
lines.append("}")

with open("/Users/shariiif77icloud.com/Desktop/BIT1123-Library-Management-System/report/uml_class_diagram.dot", "w") as f:
    f.write("\n".join(lines) + "\n")

print("DOT file written.")
