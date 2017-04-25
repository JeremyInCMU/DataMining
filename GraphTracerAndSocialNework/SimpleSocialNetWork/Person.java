import java.util.ArrayList;
/**
 * This class contains info of a single person.
 * @author Jeremy
 */
 public class Person {
     /** Name of a person */
     private String name;
     /** Contain friends of a person */
     private ArrayList<Person> friends = new ArrayList<Person>();
     /**
      * Constructor.
      * @param name
      */
     public Person(String name) {
          this.name = name;
      }
     /**
      * Add Friend.
      * @param name
      */
     public void addFriend(Person person) {
         this.friends.add(person);
     }
     /**
      * Get name.
      * @return name
      */
     public String getName() {
         return this.name;
     }
     /**
      * Get all friends.
      * @return friends included in an array list.
      */
     public ArrayList<Person> getFriends() {
         // Need defensive copies here
         ArrayList<Person> newFriends = new ArrayList<Person>();
         for (int i = 0; i < friends.size(); i++) {
             newFriends.add(friends.get(i));
         }
         return newFriends;
     }
}
