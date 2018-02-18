from csc148_queue import Queue


def list_queue(l: list, q: "Queue") -> None:
    for item in l:
        q.add(item)

    # Remove sequence.
    while not q.is_empty():
        obj = q.remove()
        if type(obj) == list:
            for sub_item in obj:
                q.add(sub_item)
        else:
            print(obj)


if __name__ == "__main__":
    queue = Queue()
    input_received = None
    while not input_received == 148:
        input_received = int(input("value to be added: "))
        if not input_received == 148:
            queue.add(input_received)

    accumulator = 0
    while not queue.is_empty():
        accumulator += queue.remove()
    print(accumulator)
