public class Librarian extends Person {

  private String staffId;
  private String department;

  public Librarian(
    String name,
    String id,
    String contactNumber,
    String staffId,
    String department
  ) {
    super(name, id, contactNumber);
    this.staffId = staffId;
    this.department = department;
  }

  public String getStaffId() {
    return staffId;
  }

  public void setStaffId(String staffId) {
    this.staffId = staffId;
  }

  public String getDepartment() {
    return department;
  }

  public void setDepartment(String department) {
    this.department = department;
  }

  @Override
  public String displayDetails() {
    return String.format(
      "[LIBRARIAN] %-15s | ID: %-6s | Staff ID: %-8s | Contact: %-12s | Dept: %s",
      getName(),
      getId(),
      staffId,
      getContactNumber(),
      department
    );
  }
}
