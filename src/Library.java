import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class Library {

  private static final String DATA_FILE = "library_data.txt";

  private List<Member> members = new ArrayList<>();
  private List<Librarian> librarians = new ArrayList<>();
  private List<LibraryItem> items = new ArrayList<>();
  private List<Loan> loans = new ArrayList<>();

  public void registerMember(Member member) {
    members.add(member);
  }

  public void registerLibrarian(Librarian librarian) {
    librarians.add(librarian);
  }

  public void addItem(LibraryItem item) {
    items.add(item);
  }

  public List<Member> getMembers() {
    return members;
  }

  public List<Librarian> getLibrarians() {
    return librarians;
  }

  public List<LibraryItem> getItems() {
    return items;
  }

  public List<Loan> getLoans() {
    return loans;
  }

  public Member findMemberById(String id) {
    for (Member m : members) {
      if (m.getId().equalsIgnoreCase(id)) {
        return m;
      }
    }
    return null;
  }

  public LibraryItem findItemById(String id) {
    for (LibraryItem item : items) {
      if (item.getItemId().equalsIgnoreCase(id)) {
        return item;
      }
    }
    return null;
  }

  public List<LibraryItem> searchItemsByTitle(String keyword) {
    List<LibraryItem> results = new ArrayList<>();
    String lowerKeyword = keyword.toLowerCase();

    for (LibraryItem item : items) {
      if (item.getTitle().toLowerCase().contains(lowerKeyword)) {
        results.add(item);
      }
    }
    return results;
  }

  public boolean borrowItem(String memberId, String itemId, String borrowDate) {
    Member member = findMemberById(memberId);
    LibraryItem item = findItemById(itemId);

    if (member == null || item == null || !item.isAvailable()) {
      return false;
    }

    item.setAvailable(false);
    member.incrementBorrowedCount();
    loans.add(new Loan(member, item, borrowDate));
    return true;
  }

  public Loan findActiveLoanByItemId(String itemId) {
    for (Loan loan : loans) {
      if (
        !loan.isReturned() &&
        loan.getItem().getItemId().equalsIgnoreCase(itemId)
      ) {
        return loan;
      }
    }
    return null;
  }

  public double returnItem(String itemId, int daysLate) {
    Loan loan = findActiveLoanByItemId(itemId);

    if (loan == null) {
      return -1;
    }

    double fine = loan.calculateFine(daysLate);
    loan.markReturned();
    loan.getItem().setAvailable(true);
    loan.getMember().decrementBorrowedCount();

    if (fine > 0) {
      loan.getMember().addFine(fine);
    }
    return fine;
  }

  public void displayAllMembers() {
    if (members.isEmpty()) {
      System.out.println("No members registered yet.");
      return;
    }
    for (Member m : members) {
      System.out.println(m.displayDetails());
    }
  }

  public void displayAllLibrarians() {
    if (librarians.isEmpty()) {
      System.out.println("No librarians registered yet.");
      return;
    }
    for (Librarian l : librarians) {
      System.out.println(l.displayDetails());
    }
  }

  public void displayAllItems() {
    if (items.isEmpty()) {
      System.out.println("No items in the catalog yet.");
      return;
    }
    for (LibraryItem item : items) {
      System.out.println(item.displaySummary());
    }
  }

  public void displayAllLoans() {
    if (loans.isEmpty()) {
      System.out.println("No loan records yet.");
      return;
    }
    for (Loan loan : loans) {
      System.out.println(loan.displaySummary());
    }
  }

  public void saveToFile() {
    try (PrintWriter writer = new PrintWriter(new FileWriter(DATA_FILE))) {
      for (Member m : members) {
        writer.println(
          String.join(
            "|",
            "MEMBER",
            m.getName(),
            m.getId(),
            m.getContactNumber(),
            m.getMembershipId(),
            String.valueOf(m.getBorrowedCount()),
            String.valueOf(m.getFineBalance())
          )
        );
      }

      for (Librarian l : librarians) {
        writer.println(
          String.join(
            "|",
            "LIBRARIAN",
            l.getName(),
            l.getId(),
            l.getContactNumber(),
            l.getStaffId(),
            l.getDepartment()
          )
        );
      }

      for (LibraryItem item : items) {
        if (item instanceof Book) {
          Book b = (Book) item;
          writer.println(
            String.join(
              "|",
              "BOOK",
              b.getItemId(),
              b.getTitle(),
              b.getAuthor(),
              b.getIsbn(),
              String.valueOf(b.isAvailable())
            )
          );
        } else if (item instanceof DVD) {
          DVD d = (DVD) item;
          writer.println(
            String.join(
              "|",
              "DVD",
              d.getItemId(),
              d.getTitle(),
              d.getDirector(),
              String.valueOf(d.getDurationMinutes()),
              String.valueOf(d.isAvailable())
            )
          );
        }
      }

      for (Loan loan : loans) {
        writer.println(
          String.join(
            "|",
            "LOAN",
            loan.getMember().getId(),
            loan.getItem().getItemId(),
            loan.getBorrowDate(),
            String.valueOf(loan.isReturned())
          )
        );
      }

      System.out.println("Data saved to " + DATA_FILE);
    } catch (IOException e) {
      System.out.println("Failed to save data: " + e.getMessage());
    }
  }

  public void loadFromFile() {
    try (
      BufferedReader reader = new BufferedReader(new FileReader(DATA_FILE))
    ) {
      members.clear();
      librarians.clear();
      items.clear();
      loans.clear();

      String line;
      while ((line = reader.readLine()) != null) {
        if (line.isBlank()) {
          continue;
        }

        String[] parts = line.split("\\|");

        switch (parts[0]) {
          case "MEMBER":
            Member member = new Member(parts[1], parts[2], parts[3], parts[4]);
            member.setBorrowedCount(Integer.parseInt(parts[5]));
            member.addFine(Double.parseDouble(parts[6]));
            members.add(member);
            break;
          case "LIBRARIAN":
            librarians.add(
              new Librarian(parts[1], parts[2], parts[3], parts[4], parts[5])
            );
            break;
          case "BOOK":
            Book book = new Book(parts[1], parts[2], parts[3], parts[4]);
            book.setAvailable(Boolean.parseBoolean(parts[5]));
            items.add(book);
            break;
          case "DVD":
            DVD dvd = new DVD(
              parts[1],
              parts[2],
              parts[3],
              Integer.parseInt(parts[4])
            );
            dvd.setAvailable(Boolean.parseBoolean(parts[5]));
            items.add(dvd);
            break;
          case "LOAN":
            Member loanMember = findMemberById(parts[1]);
            LibraryItem loanItem = findItemById(parts[2]);
            if (loanMember != null && loanItem != null) {
              Loan loan = new Loan(loanMember, loanItem, parts[3]);
              if (Boolean.parseBoolean(parts[4])) {
                loan.markReturned();
              }
              loans.add(loan);
            }
            break;
          default:
            break;
        }
      }

      System.out.println("Data loaded from " + DATA_FILE);
    } catch (IOException e) {
      System.out.println(
        "Failed to load data (does " + DATA_FILE + " exist?): " + e.getMessage()
      );
    }
  }
}
