public class Loan {

  private Member member;
  private LibraryItem item;
  private String borrowDate;
  private boolean returned;

  public Loan(Member member, LibraryItem item, String borrowDate) {
    this.member = member;
    this.item = item;
    this.borrowDate = borrowDate;
    this.returned = false;
  }

  public Member getMember() {
    return member;
  }

  public LibraryItem getItem() {
    return item;
  }

  public String getBorrowDate() {
    return borrowDate;
  }

  public boolean isReturned() {
    return returned;
  }

  public void markReturned() {
    this.returned = true;
  }

  public double calculateFine(int daysLate) {
    return item.calculateLateFee(daysLate);
  }

  public String displaySummary() {
    return String.format(
      "Loan | Member: %-15s | Item: %-30s | Borrowed: %-10s | Status: %s",
      member.getName(),
      item.getTitle(),
      borrowDate,
      returned ? "Returned" : "Active"
    );
  }
}
