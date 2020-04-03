using System;
using System.Collections.Generic;

public class CircularBuffer<T>
{
    private readonly int capacity;
    private readonly Queue<T> queue;

    public CircularBuffer(int capacity)
    {
        this.capacity = capacity;
        queue = new Queue<T>();
    }

    public T Read()
    {
        if (queue.Count == 0)
            throw new InvalidOperationException("Buffer is empty.");

        return queue.Dequeue();
    }

    public void Write(T value)
    {
        if (queue.Count == capacity)
            throw new InvalidOperationException("Buffer is full.");

        queue.Enqueue(value);
    }

    public void Overwrite(T value)
    {
        if (queue.Count == capacity)
            Read();

        Write(value);
    }

    public void Clear()
    {
        queue.Clear();
    }
}