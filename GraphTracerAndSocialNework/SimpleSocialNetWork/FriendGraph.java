import java.util.ArrayList;
/**
 * This class will show friend graphs among people.
 * @author Jeremy
 */
public class FriendGraph {
    /** Contain all person in friend graphs */
    private ArrayList<Person> persons = new ArrayList<Person>();
    /** Contain checked persons */
    private ArrayList<Person> checkedPersons;;
    /**
     * Constructor
     */
    public FriendGraph() { }
    /**
     * Add Person.
     * @param whom
     */
    public void addPerson(Person whom) {
        persons.add(whom);
    }
    /**
     * Add FriendShip.
     * @param whomFirst whomSecond the first and second person
     */
    public void addFriendShip(String nameFirst, String nameSecond) {
        Person firstPerson = null;
        Person secondPerson = null;
        for(int i = 0; i < persons.size(); i++) {
            if(persons.get(i).getName() == nameFirst) {
                firstPerson = persons.get(i);
            }
            if(persons.get(i).getName() == nameSecond) {
                secondPerson = persons.get(i);
            }
        }
        /* Check if those two persons are in the person list */
        if (firstPerson == null) {
            firstPerson = new Person(nameFirst);
        }
        if (secondPerson == null) {
            secondPerson = new Person(nameSecond);
        }
        firstPerson.addFriend(secondPerson);
        secondPerson.addFriend(firstPerson);
    }
    /**
     * Get Distance.
     * @param nameFirst, nameSecond
     */
    public int getDistance(String nameFirst, String nameSecond) {
        Person personFirst = null;
        Person personSecond = null;
        int distance = 0;
        for(int i = 0; i < persons.size(); i++) {
            if (persons.get(i).getName() == nameFirst) {
                personFirst = persons.get(i);
            }
            if (persons.get(i).getName() == nameSecond) {
                personSecond = persons.get(i);
            }
        }
        checkedPersons = new ArrayList<Person>();
        if (personFirst == null || personSecond == null) {
            return -1;
        }
        return getDistanceHelper(personFirst, personSecond, distance);
    }
    /**
     * Get Distance helper.
     * @ param nameFirst, nameSecond
     */
    private int getDistanceHelper(Person personFirst, Person personSecond, int distance) {
         if (personFirst.equals(personSecond)) {
             return distance;
         }
         for (Person person: personFirst.getFriends()) {
             if (!isCheckedPerson(person)) {
                 if(personFirst.getFriends().contains(personSecond)) {
                     return (distance + 1);
                 } else {
                     distance += 1;
                     return getDistanceHelper(person, personSecond, distance);
                 }
             }
         }
         return -1;
    }
    /**
     * Check if the current instance has been checked.
     * @param person
     * @return result
     */
    private boolean isCheckedPerson(Person checkedPerson) {
        if (!checkedPersons.contains(checkedPerson)) {
            checkedPersons.add(checkedPerson);
            return false;
        }
        return true;
    }
}
