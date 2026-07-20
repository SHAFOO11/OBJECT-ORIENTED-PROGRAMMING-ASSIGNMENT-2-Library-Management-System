public abstract class Person {

  private String name;
  private String id;
  private String contactNumber;

  public Person(String name, String id, String contactNumber) {
    this.name = name;
    this.id = id;
    this.contactNumber = contactNumber;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public String getId() {
    return id;
  }

  public void setId(String id) {
    this.id = id;
  }

  public String getContactNumber() {
    return contactNumber;
  }

  public void setContactNumber(String contactNumber) {
    this.contactNumber = contactNumber;
  }

  public abstract String displayDetails();
}
