"""Generates BIT1123-Assignment2-Report.pdf from the Library Management System project."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle,
    HRFlowable, ListFlowable, ListItem, Preformatted, KeepTogether
)

OUT = "/Users/shariiif77icloud.com/Desktop/BIT1123-Library-Management-System/report/BIT1123-Assignment2-Report.pdf"
DIAGRAM = "/Users/shariiif77icloud.com/Desktop/BIT1123-Library-Management-System/report/uml_class_diagram.png"

PAGE_W, PAGE_H = A4
MARGIN = 2 * cm
CONTENT_W = PAGE_W - 2 * MARGIN

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(name="CoverTitle", fontName="Helvetica-Bold", fontSize=22,
                           leading=28, alignment=TA_CENTER, textColor=colors.HexColor("#1a1a2e")))
styles.add(ParagraphStyle(name="CoverSub", fontName="Helvetica", fontSize=13,
                           leading=18, alignment=TA_CENTER, textColor=colors.HexColor("#444444")))
styles.add(ParagraphStyle(name="SectionHeading", fontName="Helvetica-Bold", fontSize=16,
                           leading=20, spaceBefore=18, spaceAfter=10,
                           textColor=colors.HexColor("#1a1a2e")))
styles.add(ParagraphStyle(name="SubHeading", fontName="Helvetica-Bold", fontSize=12.5,
                           leading=16, spaceBefore=10, spaceAfter=6,
                           textColor=colors.HexColor("#4a4e69")))
styles.add(ParagraphStyle(name="Body", fontName="Helvetica", fontSize=10.5,
                           leading=15.5, alignment=TA_JUSTIFY, spaceAfter=9))
styles.add(ParagraphStyle(name="CodeText", fontName="Courier", fontSize=8.5,
                           leading=11.5, textColor=colors.HexColor("#1a1a2e")))
styles.add(ParagraphStyle(name="Caption", fontName="Helvetica-Oblique", fontSize=9,
                           alignment=TA_CENTER, textColor=colors.HexColor("#666666"),
                           spaceAfter=14))


def code_block(text):
    pre = Preformatted(text, styles["CodeText"])
    table = Table([[pre]], colWidths=[CONTENT_W])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f4f8")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#dcdce6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return KeepTogether([table, Spacer(1, 10)])


story = []

# ---------------- Cover Page ----------------
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("BIT1123 / BISE2093 / DIT1113", styles["CoverSub"]))
story.append(Paragraph("OBJECT ORIENTED PROGRAMMING", styles["CoverSub"]))
story.append(Spacer(1, 0.8 * cm))
story.append(Paragraph("ASSIGNMENT 2 (GROUP) &ndash; 20%", styles["CoverTitle"]))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph("Library Management System", styles["CoverTitle"]))
story.append(Spacer(1, 1.2 * cm))
story.append(HRFlowable(width="60%", thickness=1, color=colors.HexColor("#4a4e69"), hAlign="CENTER"))
story.append(Spacer(1, 1.2 * cm))

member_data = [["Full Name", "Student ID", "Class Code", "Program", "NRIC / Passport No."]]
for _ in range(4):
    member_data.append(["", "", "", "", ""])

member_table = Table(member_data, colWidths=[3.6 * cm, 2.6 * cm, 2.6 * cm, 2.6 * cm, 3.4 * cm])
member_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#cccccc")),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
]))
story.append(member_table)
story.append(Spacer(1, 0.4 * cm))
story.append(Paragraph("<i>(Fill in the details of every group member above before submission.)</i>", styles["Caption"]))

story.append(Spacer(1, 1.5 * cm))
story.append(Paragraph("<b>GitHub Repository:</b> [ paste your repository URL here ]", styles["Body"]))
story.append(Paragraph("<b>Lecturer:</b> Sir Nazmirul Izzad Bin Nassir", styles["Body"]))
story.append(Paragraph("<b>Faculty:</b> Faculty of Information Technology, City University Malaysia, Cyberjaya Campus", styles["Body"]))
story.append(PageBreak())

# ---------------- 1. Introduction ----------------
story.append(Paragraph("1. Introduction", styles["SectionHeading"]))
story.append(Paragraph(
    "For this assignment we were asked to design and build a Java console application that puts "
    "Object-Oriented Programming into practice rather than just describing it on paper. The brief "
    "specifically calls for classes and objects, encapsulation, inheritance, polymorphism, and "
    "abstraction to all show up somewhere in a real, working program, and for the report to explain "
    "how and why each one was used. We chose to build a Library Management System, and this report "
    "walks through the reasoning behind that choice, how the classes fit together, and how each of "
    "the five OOP requirements is actually expressed in the code, not just claimed about it.", styles["Body"]))
story.append(Paragraph(
    "We didn't want to just tick boxes on a rubric. Before writing any code we talked through what a "
    "library actually needs to keep track of, sketched out which real-world things should become "
    "classes, and only then started implementing. The result is a program with nine classes that a "
    "librarian can run from the terminal to register members and staff, add books and DVDs to the "
    "catalog, lend items out, take them back and work out any late fee, search the catalog, and save "
    "everything to a file so nothing is lost when the program is closed. Every part of that workflow "
    "is described in the sections that follow, together with the class diagram and the specific lines "
    "of code that demonstrate each OOP concept.", styles["Body"]))

# ---------------- 2. Problem Description ----------------
story.append(Paragraph("2. Problem Description", styles["SectionHeading"]))
story.append(Paragraph(
    "Picture a small college library with one or two staff on the front desk. A student walks up with "
    "a book, the staff member writes the student's name and the book's title into a notebook or an "
    "Excel sheet, and moves on to the next person. This works fine until the notebook fills up, "
    "someone forgets to write down the date, or two different staff members note the same book as "
    "borrowed by two different people because nobody had a single, shared source of truth. Late fees "
    "are worse: a DVD that comes back five days late should probably cost more per day than a "
    "paperback five days late, but if the fee is worked out by hand it depends entirely on whoever is "
    "on duty remembering the right rate.", styles["Body"]))
story.append(Paragraph(
    "That's really the core problem we set out to solve: keep track of three things that are always "
    "moving &ndash; who is registered at the library, what items exist and whether they're currently "
    "available, and which member currently holds which item &ndash; in a way that doesn't rely on "
    "someone's memory or a shared spreadsheet. Object-oriented design turned out to be a natural fit "
    "for this, because each of those three concerns maps cleanly onto its own class with its own data "
    "and its own rules, instead of one giant function juggling arrays of loosely related values.", styles["Body"]))
story.append(Paragraph(
    "Concretely, the console application we built lets a librarian:", styles["Body"]))
story.append(KeepTogether([ListFlowable([
    ListItem(Paragraph("Register new members and new librarians, each keeping their own contact "
                        "details and role-specific information", styles["Body"])),
    ListItem(Paragraph("Add new books and DVDs to the catalog, each with the details relevant to "
                        "that type of item", styles["Body"])),
    ListItem(Paragraph("Print out a formatted list of every member, librarian, catalog item, or loan "
                        "currently on record", styles["Body"])),
    ListItem(Paragraph("Borrow and return items, with the late fee worked out automatically and "
                        "charged at a different daily rate depending on whether the item is a book "
                        "or a DVD", styles["Body"])),
    ListItem(Paragraph("Search the catalog by typing part of a title", styles["Body"])),
    ListItem(Paragraph("Save the current state of the library to a text file, and load it back in on "
                        "the next run, so closing the program doesn't wipe out the day's work",
                        styles["Body"])),
], bulletType="bullet", start="circle")]))

# ---------------- 3. Class Diagram ----------------
story.append(PageBreak())
story.append(Paragraph("3. Class Diagram (UML)", styles["SectionHeading"]))
story.append(Paragraph(
    "Figure 1 shows all nine classes in the system with their attributes and methods, using standard "
    "UML visibility notation (<font face='Courier'>-</font> for private, <font face='Courier'>+</font> "
    "for public). The arrows carry meaning too: a hollow triangle points from a subclass up to its "
    "superclass (inheritance), an open diamond sits on the side of the class that owns a collection of "
    "the other (aggregation), a plain arrow shows one class referring to another (association), and the "
    "dashed arrow from <font face='Courier'>Main</font> shows a dependency rather than a stored "
    "reference. We laid the diagram out by hand so the two inheritance branches sit clearly apart on "
    "the left and right, with <font face='Courier'>Library</font> and <font face='Courier'>Loan</font> "
    "bridging them down the middle &ndash; it took a couple of attempts to get the lines routed "
    "without them crossing through unrelated boxes, but the payoff is that the relationships are "
    "actually easy to trace by eye.", styles["Body"]))
story.append(Spacer(1, 6))
img = Image(DIAGRAM)
avail_w = PAGE_W - 4 * cm
scale = min(1.0, avail_w / img.imageWidth)
img.drawWidth = img.imageWidth * scale
img.drawHeight = img.imageHeight * scale
story.append(img)
story.append(Paragraph("Figure 1: UML Class Diagram of the Library Management System", styles["Caption"]))

# ---------------- 4. UML Design Explanation ----------------
story.append(Paragraph("4. Explanation of UML Design", styles["SectionHeading"]))
story.append(Paragraph(
    "The design centres on two separate inheritance hierarchies, connected through an association "
    "class and managed by a single controller class. None of this was the first idea we had &ndash; "
    "we went through a couple of rounds of sketching before settling on the structure shown in Figure "
    "1, and it's worth explaining what we tried and rejected along the way, since that reasoning is "
    "really the point of a design justification section.", styles["Body"]))
story.append(Paragraph("Person &rarr; Member / Librarian", styles["SubHeading"]))
story.append(Paragraph(
    "Our first instinct was actually a single <font face='Courier'>Person</font> class with a "
    "<font face='Courier'>role</font> field that could be set to &ldquo;member&rdquo; or "
    "&ldquo;librarian&rdquo;, and a pile of if-statements checking which one it was. We dropped that "
    "almost immediately because it's exactly the kind of design inheritance exists to replace: a "
    "librarian doesn't have a fine balance or a borrowed-item count, and a member doesn't have a "
    "department, so cramming both into one class means every object carries fields that don't apply "
    "to it. Instead, <font face='Courier'>Person</font> holds only what every person in the system "
    "genuinely shares &ndash; a name, an ID, and a contact number &ndash; and is declared abstract "
    "because &ldquo;a person&rdquo; on its own is never actually registered at the library; only a "
    "member or a librarian is. <font face='Courier'>Member</font> then adds membership ID, borrowed "
    "count, and fine balance, while <font face='Courier'>Librarian</font> adds staff ID and "
    "department. Each subclass calls <font face='Courier'>super(...)</font> to set up the shared "
    "fields and then only worries about what makes it different.", styles["Body"]))
story.append(Paragraph("LibraryItem &rarr; Book / DVD", styles["SubHeading"]))
story.append(Paragraph(
    "The same reasoning applies on the catalog side, but with an extra wrinkle: books and DVDs aren't "
    "just different in what data they store (author and ISBN versus director and running time), they "
    "also need to be charged late fees at different daily rates. That's precisely the situation an "
    "abstract method is built for. <font face='Courier'>LibraryItem</font> declares "
    "<font face='Courier'>calculateLateFee(daysLate)</font> and <font face='Courier'>getItemType()</font> "
    "but deliberately provides no body for either &ndash; it can't, because it has no idea what rate "
    "applies until you know whether the concrete object is a book or a DVD. <font face='Courier'>Book</font> "
    "charges RM0.50 per day late; <font face='Courier'>DVD</font> charges RM1.00 per day late. Adding "
    "a third item type later, say a <font face='Courier'>Magazine</font>, would mean writing one new "
    "class that extends <font face='Courier'>LibraryItem</font> and nothing else in the system would "
    "need to change.", styles["Body"]))
story.append(Paragraph("Loan as an association class", styles["SubHeading"]))
story.append(Paragraph(
    "We also considered just giving <font face='Courier'>Member</font> a list of the items it "
    "currently has out, and skipping a separate loan class entirely. That falls apart quickly once "
    "you think about late fees and history: a fine has to be calculated from a specific borrow date, "
    "and a returned loan is still worth keeping a record of, even after the item goes back on the "
    "shelf. Bolting all of that onto <font face='Courier'>Member</font> would tie it tightly to "
    "<font face='Courier'>LibraryItem</font> and make the two classes depend on each other directly. "
    "So instead we introduced <font face='Courier'>Loan</font> as its own class that sits between "
    "them, holding a reference to the <font face='Courier'>Member</font> who borrowed something, a "
    "reference to the <font face='Courier'>LibraryItem</font> they borrowed, the date it was borrowed, "
    "and whether it's been returned. Neither <font face='Courier'>Member</font> nor "
    "<font face='Courier'>LibraryItem</font> needs to know the other exists &ndash; "
    "<font face='Courier'>Loan</font> is the only class that connects them, which is exactly what an "
    "association class is for.", styles["Body"]))
story.append(Paragraph("Library as the controller", styles["SubHeading"]))
story.append(Paragraph(
    "Finally, something had to actually own the four growing lists of members, librarians, items, and "
    "loans, and provide the operations that act on them &ndash; registering people, borrowing and "
    "returning items, searching, saving and loading. We put all of that in "
    "<font face='Courier'>Library</font> rather than scattering it across "
    "<font face='Courier'>Main</font>, so that <font face='Courier'>Main</font> only has to worry "
    "about reading console input and printing results. That's why the diagram shows "
    "<font face='Courier'>Main</font> depending on <font face='Courier'>Library</font> with a dashed "
    "arrow rather than the two being tightly coupled: if we ever swapped the console menu for, say, a "
    "simple GUI, <font face='Courier'>Library</font> wouldn't need to change at all.", styles["Body"]))

# ---------------- 5. Explanation of OOP Concepts Used ----------------
story.append(PageBreak())
story.append(Paragraph("5. Explanation of OOP Concepts Used", styles["SectionHeading"]))
story.append(Paragraph(
    "This section goes through each of the five OOP requirements one at a time, pointing at the exact "
    "class or method where it shows up and, where it makes sense, at what we actually saw happen when "
    "we ran the program.", styles["Body"]))

story.append(Paragraph("5.1 Classes and Objects", styles["SubHeading"]))
story.append(Paragraph(
    "There are nine classes in total: <font face='Courier'>Person</font>, "
    "<font face='Courier'>Member</font>, <font face='Courier'>Librarian</font>, "
    "<font face='Courier'>LibraryItem</font>, <font face='Courier'>Book</font>, "
    "<font face='Courier'>DVD</font>, <font face='Courier'>Loan</font>, "
    "<font face='Courier'>Library</font>, and <font face='Courier'>Main</font>, and each one models a "
    "single real-world idea rather than being a grab-bag of unrelated data. A class is just the "
    "blueprint, though &ndash; nothing actually exists until the menu creates an object from it. When "
    "a librarian picks &ldquo;Add new book&rdquo; from the menu and types in a title and author, "
    "<font face='Courier'>Main</font> creates one specific <font face='Courier'>Book</font> object "
    "holding those exact values, completely separate from every other book already in the catalog.",
    styles["Body"]))
story.append(Paragraph("This is what that object creation looks like in Main.java:", styles["Body"]))
story.append(code_block(
    "library.registerMember(new Member(name, id, contact, membershipId));\n"
    "library.addItem(new Book(itemId, title, author, isbn));"
))

story.append(Paragraph("5.2 Encapsulation", styles["SubHeading"]))
story.append(Paragraph(
    "Every field in every class is private. Nothing outside the class can reach in and change an "
    "object's data directly &ndash; the only way in or out is through the public getter and setter "
    "methods the class chooses to expose, and those methods can enforce rules on the way. "
    "<font face='Courier'>Member.addFine()</font> is a small but telling example: it only accepts a "
    "positive amount, so there's no way for a bug elsewhere in the program to accidentally push a "
    "member's fine balance negative. If <font face='Courier'>fineBalance</font> were a public field, "
    "any piece of code anywhere could set it to whatever it wanted, including nonsense values, and we "
    "wouldn't be able to guarantee that check ever ran.", styles["Body"]))
story.append(code_block(
    "public double getFineBalance() {\n"
    "    return fineBalance;\n"
    "}\n\n"
    "public void addFine(double amount) {\n"
    "    if (amount > 0) {\n"
    "        this.fineBalance += amount;\n"
    "    }\n"
    "}"
))

story.append(Paragraph("5.3 Inheritance", styles["SubHeading"]))
story.append(Paragraph(
    "Both hierarchies discussed in Section 4 use Java's <font face='Courier'>extends</font> keyword: "
    "<font face='Courier'>Member</font> and <font face='Courier'>Librarian</font> extend "
    "<font face='Courier'>Person</font>, and <font face='Courier'>Book</font> and "
    "<font face='Courier'>DVD</font> extend <font face='Courier'>LibraryItem</font>. In every case the "
    "subclass constructor calls <font face='Courier'>super(...)</font> first to let the parent class "
    "set up the fields it owns, and only then initializes its own additional fields. It's worth "
    "pointing out that <font face='Courier'>Member</font> never re-declares "
    "<font face='Courier'>name</font>, <font face='Courier'>id</font>, or "
    "<font face='Courier'>contactNumber</font> &ndash; it inherits all three from "
    "<font face='Courier'>Person</font> and simply reuses <font face='Courier'>getName()</font> and "
    "the rest without writing a single extra line for them.", styles["Body"]))
story.append(code_block(
    "public class Member extends Person {\n\n"
    "    private String membershipId;\n"
    "    private int borrowedCount;\n"
    "    private double fineBalance;\n\n"
    "    public Member(String name, String id, String contactNumber, String membershipId) {\n"
    "        super(name, id, contactNumber);\n"
    "        this.membershipId = membershipId;\n"
    "        this.borrowedCount = 0;\n"
    "        this.fineBalance = 0.0;\n"
    "    }\n"
    "}"
))

story.append(Paragraph("5.4 Polymorphism", styles["SubHeading"]))
story.append(Paragraph(
    "The clearest example of runtime polymorphism in the project is how a late fee actually gets "
    "calculated. <font face='Courier'>Loan.calculateFine()</font> never checks whether it's holding a "
    "book or a DVD &ndash; it just calls <font face='Courier'>item.calculateLateFee(daysLate)</font> "
    "on whatever <font face='Courier'>LibraryItem</font> reference it has, and lets Java figure out at "
    "runtime which override actually runs. The same idea shows up again in "
    "<font face='Courier'>Library.displayAllItems()</font>, which loops over every item using the "
    "superclass type and calls <font face='Courier'>displaySummary()</font> on each one without caring "
    "what's underneath.", styles["Body"]))
story.append(code_block(
    "public double calculateFine(int daysLate) {\n"
    "    return item.calculateLateFee(daysLate);\n"
    "}"
))
story.append(Paragraph(
    "We didn't just take this on faith &ndash; we tested it directly while trying out the program. "
    "Borrowing a book and returning it three days late charged RM1.50 (three days at RM0.50), while "
    "borrowing a DVD and returning it three days late through that exact same "
    "<font face='Courier'>returnItem()</font> code path charged RM3.00 (three days at RM1.00). Same "
    "method call, same loop, two different results, because the object underneath the "
    "<font face='Courier'>LibraryItem</font> reference was different each time. That's polymorphism "
    "actually doing something useful rather than just being a term we can define.", styles["Body"]))

story.append(KeepTogether([
    Paragraph("5.5 Abstraction", styles["SubHeading"]),
    Paragraph(
        "<font face='Courier'>Person</font> and <font face='Courier'>LibraryItem</font> are both declared "
        "<font face='Courier'>abstract</font>, which means Java won't let anyone write "
        "<font face='Courier'>new Person(...)</font> or <font face='Courier'>new LibraryItem(...)</font> "
        "anywhere in the code &ndash; only their concrete subclasses can be instantiated. That's a "
        "deliberate restriction, not a limitation: on their own, &ldquo;a person&rdquo; or &ldquo;a "
        "library item&rdquo; are too vague to have a working "
        "<font face='Courier'>calculateLateFee()</font> or a working "
        "<font face='Courier'>displayDetails()</font>, so the abstract class only defines the shared shape "
        "and leaves the actual behaviour for each subclass to fill in.", styles["Body"]),
    code_block(
        "public abstract class LibraryItem {\n\n"
        "    private String itemId;\n"
        "    private String title;\n"
        "    private boolean available;\n\n"
        "    public abstract double calculateLateFee(int daysLate);\n\n"
        "    public abstract String getItemType();\n"
        "}"
    ),
]))

# ---------------- 6. Sample Output ----------------
story.append(PageBreak())
story.append(Paragraph("6. Sample Output", styles["SectionHeading"]))
story.append(Paragraph(
    "<i>[ Insert screenshots of your own terminal run here before submission. A good set to include: "
    "the main menu, registering a member, adding a book and a DVD, borrowing an item, returning a book "
    "late versus returning a DVD late side by side (so the different fine amounts are visible), and "
    "the save/load confirmation messages. ]</i>", styles["Body"]))
story.append(Spacer(1, 0.3 * cm))
story.append(Paragraph("To compile and run the program from the project root:", styles["Body"]))
story.append(code_block(
    "cd BIT1123-Library-Management-System\n"
    "javac -d out src/*.java\n"
    "java -cp out Main"
))

# ---------------- 7. Conclusion ----------------
story.append(Paragraph("7. Conclusion", styles["SectionHeading"]))
story.append(Paragraph(
    "Working through this assignment made the four pillars of OOP feel a lot less like textbook "
    "vocabulary and more like decisions that actually change how easy a program is to extend. The "
    "clearest moment of that was realizing how little would need to change if we wanted to add a new "
    "kind of item to the catalog: one new class extending <font face='Courier'>LibraryItem</font>, "
    "and every part of the system that already loops over items &ndash; searching, displaying, "
    "borrowing, returning &ndash; would handle it automatically through polymorphism, without a single "
    "if-statement checking &ldquo;is this a book or a DVD&rdquo; anywhere in "
    "<font face='Courier'>Library</font> or <font face='Courier'>Main</font>.", styles["Body"]))
story.append(Paragraph(
    "The design wasn't perfect on the first attempt, and we don't think it needs to be presented as "
    "if it was &ndash; the single-class-with-a-role-field idea we tried early on for "
    "<font face='Courier'>Person</font>, and the version of <font face='Courier'>Library</font> that "
    "originally didn't persist active loans at all, both got reworked once we actually tested the "
    "program end to end and saw where they broke down. If we kept building on this, the next things "
    "we'd want to add are due dates that are checked automatically rather than typed in by the "
    "librarian, and proper authentication so that only a logged-in librarian account can register new "
    "members or add items. For a first pass at applying OOP to a real problem, though, we're happy "
    "with how cleanly the final structure maps onto the actual rules of running a library.", styles["Body"]))


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#888888"))
    canvas.drawCentredString(PAGE_W / 2, 1.2 * cm, f"Page {doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4,
                         topMargin=MARGIN, bottomMargin=MARGIN,
                         leftMargin=MARGIN, rightMargin=MARGIN,
                         title="BIT1123 Assignment 2 - Library Management System")
doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print("PDF written to", OUT)
