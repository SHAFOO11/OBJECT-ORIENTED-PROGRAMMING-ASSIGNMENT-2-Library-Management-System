public class DVD extends LibraryItem {

  private static final double LATE_FEE_PER_DAY = 1.00;

  private String director;
  private int durationMinutes;

  public DVD(
    String itemId,
    String title,
    String director,
    int durationMinutes
  ) {
    super(itemId, title);
    this.director = director;
    this.durationMinutes = durationMinutes;
  }

  public String getDirector() {
    return director;
  }

  public void setDirector(String director) {
    this.director = director;
  }

  public int getDurationMinutes() {
    return durationMinutes;
  }

  public void setDurationMinutes(int durationMinutes) {
    this.durationMinutes = durationMinutes;
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
    return "DVD";
  }
}
