import threading

class Filter:
    def __init__(self, inbound_queue, outbound_queue):
        self.inbound_queue = inbound_queue
        self.outbound_queue = outbound_queue
        
    def run(self):
        def process_thread():
            try:
                while True:
                    data = self.inbound_queue.get()
                    if data is None:
                        break
                    processed_data = self.process(data)
                    self.outbound_queue.put(processed_data)
            except KeyboardInterrupt:
                print("KeyboardInterrupt detected. Stopping filter.")
            finally:
                self.inbound_queue.task_done()
        self.thread = threading.Thread(target=process_thread)
        self.thread.start()
    
    def process(self, data):
        raise NotImplementedError("Filter.process method must be overridden.")
