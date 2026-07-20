public class Book extends LibraryItem {

  private static final double LATE_FEE_PER_DAY = 0.50;

  private String author;
  private String isbn;

  public Book(String itemId, String title, String author, String isbn) {
    super(itemId, title);
    this.author = author;
    this.isbn = isbn;
  }

  public String getAuthor() {
    return author;
  }

  public void setAuthor(String author) {
    this.author = author;
  }

  public String getIsbn() {
    return isbn;
  }

  public void setIsbn(String isbn) {
    this.isbn = isbn;
  }

  @Override
  public double calculateLateFee(int daysLate) {
    if (daysLate <= 0) {
      return 0.0;
    }
    return daysLate * LATE_FEE_PER_DAY;
  }

  @Override
  public String getItemType() {
    return "BOOK";
  }
}
