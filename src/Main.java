import java.util.List;
import java.util.Scanner;

public class Main {

  private static final Scanner scanner = new Scanner(System.in);
  private static final Library library = new Library();

  public static void main(String[] args) {
    System.out.println("=========================================");
    System.out.println(" LIBRARY MANAGEMENT SYSTEM ");
    System.out.println("=========================================");

    boolean running = true;
    while (running) {
      printMenu();
      int choice = readInt("Enter your choice: ");
      switch (choice) {
        case 1:
          registerMember();
          break;
        case 2:
          registerLibrarian();
          break;
        case 3:
          addBook();
          break;
        case 4:
          addDVD();
          break;
        case 5:
          library.displayAllMembers();
          break;
        case 6:
          library.displayAllLibrarians();
          break;
        case 7:
          library.displayAllItems();
          break;
        case 8:
          library.displayAllLoans();
          break;
        case 9:
          borrowItem();
          break;
        case 10:
          returnItem();
          break;
        case 11:
          searchItem();
          break;
        case 12:
          library.saveToFile();
          break;
        case 13:
          library.loadFromFile();
          break;
        case 0:
          running = false;
          System.out.println("Goodbye!");
          break;
        default:
          System.out.println("Invalid choice, please try again.");
      }
    }
    scanner.close();
  }

  private static void printMenu() {
    System.out.println("\n----------------- MENU -----------------");
    System.out.println(" 1. Register new member");
    System.out.println(" 2. Register new librarian");
    System.out.println(" 3. Add new book");
    System.out.println(" 4. Add new DVD");
    System.out.println(" 5. Display all members");
    System.out.println(" 6. Display all librarians");
    System.out.println(" 7. Display all catalog items");
    System.out.println(" 8. Display all loan records");
    System.out.println(" 9. Borrow an item");
    System.out.println("10. Return an item");
    System.out.println("11. Search item by title");
    System.out.println("12. Save data to file");
    System.out.println("13. Load data from file");
    System.out.println(" 0. Exit");
    System.out.println("-----------------------------------------");
  }

  private static void registerMember() {
    System.out.println("\n-- Register New Member --");
    String name = readLine("Name: ");
    String id = readLine("ID: ");
    String contact = readLine("Contact number: ");
    String membershipId = readLine("Membership ID: ");
    library.registerMember(new Member(name, id, contact, membershipId));
    System.out.println("Member registered successfully.");
  }

  private static void registerLibrarian() {
    System.out.println("\n-- Register New Librarian --");
    String name = readLine("Name: ");
    String id = readLine("ID: ");
    String contact = readLine("Contact number: ");
    String staffId = readLine("Staff ID: ");
    String department = readLine("Department: ");
    library.registerLibrarian(
      new Librarian(name, id, contact, staffId, department)
    );
    System.out.println("Librarian registered successfully.");
  }

  private static void addBook() {
    System.out.println("\n-- Add New Book --");
    String itemId = readLine("Item ID: ");
    String title = readLine("Title: ");
    String author = readLine("Author: ");
    String isbn = readLine("ISBN: ");
    library.addItem(new Book(itemId, title, author, isbn));
    System.out.println("Book added to catalog.");
  }

  private static void addDVD() {
    System.out.println("\n-- Add New DVD --");
    String itemId = readLine("Item ID: ");
    String title = readLine("Title: ");
    String director = readLine("Director: ");
    int duration = readInt("Duration (minutes): ");
    library.addItem(new DVD(itemId, title, director, duration));
    System.out.println("DVD added to catalog.");
  }

  private static void borrowItem() {
    System.out.println("\n-- Borrow an Item --");
    String memberId = readLine("Member ID: ");
    String itemId = readLine("Item ID: ");
    String borrowDate = readLine("Borrow date (e.g. 2026-07-20): ");

    if (library.findMemberById(memberId) == null) {
      System.out.println("No member found with that ID.");
      return;
    }
    LibraryItem item = library.findItemById(itemId);
    if (item == null) {
      System.out.println("No item found with that ID.");
      return;
    }
    if (!item.isAvailable()) {
      System.out.println("Sorry, that item is currently on loan.");
      return;
    }
    boolean success = library.borrowItem(memberId, itemId, borrowDate);
    System.out.println(
      success ? "Item borrowed successfully." : "Borrow failed."
    );
  }

  private static void returnItem() {
    System.out.println("\n-- Return an Item --");
    String itemId = readLine("Item ID: ");
    int daysLate = readInt("Days late (0 if on time): ");

    double fine = library.returnItem(itemId, daysLate);
    if (fine < 0) {
      System.out.println("No active loan found for that item.");
    } else if (fine == 0) {
      System.out.println("Item returned on time. No fine.");
    } else {
      System.out.printf("Item returned late. Fine charged: RM%.2f%n", fine);
    }
  }

  private static void searchItem() {
    System.out.println("\n-- Search Item by Title --");
    String keyword = readLine("Enter title keyword: ");
    List<LibraryItem> results = library.searchItemsByTitle(keyword);
    if (results.isEmpty()) {
      System.out.println("No items matched your search.");
    } else {
      for (LibraryItem item : results) {
        System.out.println(item.displaySummary());
      }
    }
  }

  private static String readLine(String prompt) {
    System.out.print(prompt);
    return scanner.nextLine().trim();
  }

  private static int readInt(String prompt) {
    while (true) {
      System.out.print(prompt);
      String input = scanner.nextLine().trim();
      try {
        return Integer.parseInt(input);
      } catch (NumberFormatException e) {
        System.out.println("Please enter a valid whole number.");
      }
    }
  }
}
