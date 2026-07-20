public class Member extends Person {

  private String membershipId;
  private int borrowedCount;
  private double fineBalance;

  public Member(
    String name,
    String id,
    String contactNumber,
    String membershipId
  ) {
    super(name, id, contactNumber);
    this.membershipId = membershipId;
    this.borrowedCount = 0;
    this.fineBalance = 0.0;
  }

  public String getMembershipId() {
    return membershipId;
  }

  public void setMembershipId(String membershipId) {
    this.membershipId = membershipId;
  }

  public int getBorrowedCount() {
    return borrowedCount;
  }

  public void setBorrowedCount(int borrowedCount) {
    this.borrowedCount = borrowedCount;
  }

  public void incrementBorrowedCount() {
    this.borrowedCount++;
  }

  public void decrementBorrowedCount() {
    if (this.borrowedCount > 0) {
      this.borrowedCount--;
    }
  }

  public double getFineBalance() {
    return fineBalance;
  }

  public void addFine(double amount) {
    if (amount > 0) {
      this.fineBalance += amount;
    }
  }

  @Override
  public String displayDetails() {
    return String.format(
      "[MEMBER] %-15s | ID: %-6s | Membership: %-8s | Contact: %-12s | Borrowed: %d | Fine: RM%.2f",
      getName(),
      getId(),
      membershipId,
      getContactNumber(),
      borrowedCount,
      fineBalance
    );
  }
}
