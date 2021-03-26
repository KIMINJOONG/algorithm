import java.util.ArrayList;

class Queue<T> {
    ArrayList<T> queueList = new ArrayList<T>();

    public void push(T data) {
        this.queueList.add(data);
        return;
    }

    public T pop() {
        T data = this.queueList.get(0);
        this.queueList.remove(data);
        return data;
    }

    public void desc() {
        int size = this.getSize();
        for(int i = 0; i < size; i++) {
            System.out.println(this.queueList.get(i));
        }
    }

    public int getSize() {
        int size = this.queueList.size();
        return size;
    }


}

class Main {
    public static void main(String[] args) {
        Queue queue_list = new Queue();
        for(int i = 0; i < 10; i++) {
            if(i == 3) {
                queue_list.push("난 3이야");
            } else {
                queue_list.push(i);
            }

        }
        System.out.println(queue_list.pop());
        System.out.println(queue_list.pop());
        System.out.println(queue_list.pop());
        System.out.println("------------");
        queue_list.desc();
        System.out.println("------------");
        System.out.println(queue_list.getSize());
    }
}