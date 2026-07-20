public abstract class LibraryItem {

  private String itemId;
  private String title;
  private boolean available;

  public LibraryItem(String itemId, String title) {
    this.itemId = itemId;
    this.title = title;
    this.available = true;
  }

  public String getItemId() {
    return itemId;
  }

  public void setItemId(String itemId) {
    this.itemId = itemId;
  }

  public String getTitle() {
    return title;
  }

  public void setTitle(String title) {
    this.title = title;
  }

  public boolean isAvailable() {
    return available;
  }

  public void setAvailable(boolean available) {
    this.available = available;
  }

  public abstract double calculateLateFee(int daysLate);

  public abstract String getItemType();

  public String displaySummary() {
    return String.format(
      "[%-4s] %-6s | %-30s | %s",
      getItemType(),
      itemId,
      title,
      available ? "Available" : "On Loan"
    );
  }
}
