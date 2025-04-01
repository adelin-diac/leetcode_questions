package data_structures.linked_list;

/**
 * Linked List node that can be implemented using any type.
 */
public class LinkedNode<T> {
    public T data;
    public LinkedNode<T> next;

    public LinkedNode(T data){
        this.data = data;
        this.next = null;
    }
    
    /* Overload - if next variable node given */
    public LinkedNode(T data, LinkedNode<T> next){
        this.data = data;
        this.next = next;
    }

    @Override public String toString(){
        return this.data.toString();
    }
}
