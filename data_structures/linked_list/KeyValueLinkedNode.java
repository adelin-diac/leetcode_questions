package data_structures.linked_list;

public class KeyValueLinkedNode<K, V>{
    public K key;
    public V value;
    public KeyValueLinkedNode<K, V> next;

    public KeyValueLinkedNode(K k, V val){
        this.key = k;
        this.value = val;
        this.next = null;
    }
    
    /* Overload - if next variable node given */
    public KeyValueLinkedNode(K k, V val, KeyValueLinkedNode<K, V> next){
        this.key = k;
        this.value = val;
        this.next = next;
    }

    @Override
    public String toString(){
        return "{ " + this.key.toString() + ": " + this.value.toString() + " }";
    }
}
