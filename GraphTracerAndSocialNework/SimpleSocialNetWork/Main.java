public class Main {
    public static void main(String[] args) {
        // Un-comment the following code (CTRL + /).

         FriendGraph graph = new FriendGraph();
         Person rachel = new Person("Rachel");
         Person ross = new Person("Ross");
         Person ben = new Person("Ben");
         Person kramer = new Person("Kramer");
         Person dan = new Person("Dan");
         Person alex = new Person("Alex");
         Person pablo = new Person("Pablo");
         Person charlie = new Person("Charlie");
         Person shannon = new Person("Shannon");
         graph.addPerson(rachel);
         graph.addPerson(ross);
         graph.addPerson(ben);
         graph.addPerson(kramer);
         graph.addPerson(dan);
         graph.addPerson(alex);
         graph.addPerson(pablo);
         graph.addPerson(charlie);
         graph.addPerson(shannon);
         graph.addFriendShip("Dan","Alex");
         graph.addFriendShip("Dan","Shannon");
         graph.addFriendShip("Alex", "Pablo");
         graph.addFriendShip("Charlie","Alex");
         graph.addFriendShip("Shannon", "Pablo");
         graph.addFriendShip("Shannon", "Charlie");
         System.out.println(graph.getDistance("Dan", "Charlie"));
         System.out.println(graph.getDistance("Alex", "Shannon"));
         System.out.println(graph.getDistance("Alex", "Pablo"));
         System.out.println(graph.getDistance("Shannon", "Pablo")); // 1
         System.out.println(graph.getDistance("Dan", "Charlie")); // 2
         System.out.println(graph.getDistance("Alex", "Jonathan")); // -1
         System.out.println(graph.getDistance("Alex", "Alex")); // 0
         graph.addFriendship("Rachel", "Ross");
         graph.addFriendship("Ross", "Ben");
         System.out.println(graph.getDistance("Rachel", "Ross"));
         System.out.println(graph.getDistance("Ross", "Ben"));
         System.out.println(graph.getDistance("Rachel", "Ben"));
         System.out.println(graph.getDistance("Rachel", "Rachel"));
         System.out.println(graph.getDistance("Rachel", "Kramer"));

        // You may write more tests if you'd like.
    }
}
