import simpy
import random
import numpy as np
import matplotlib.pyplot as plt


ARRIVAL_RATE = 12  
SERVICE_RATE = 3 
SIM_TIME = 100  
RANDOM_SEED = 100  


wait_time = []

class MM1Queue:
    def __init__(self, env, service_rate):
        self.server = simpy.Resource(env, capacity=1)
        self.service_rate = service_rate
        self.env = env

    def serve(self, customer):
        """Service process for a customer."""
        service_time = random.expovariate(self.service_rate)
        yield self.env.timeout(service_time)

def customer(env, name, queue):
    """Customer arrival process."""
    arrival_time = env.now
    with queue.server.request() as request:
        yield request  
        wait_time.append(env.now - arrival_time)  
        yield env.process(queue.serve(name))

def arrival_generator(env, queue, arrival_rate):
    """Generates arriving customers."""
    customer_id = 0
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        customer_id += 1
        env.process(customer(env, f'Customer {customer_id}', queue))


random.seed(RANDOM_SEED)
env = simpy.Environment()
queue = MM1Queue(env, SERVICE_RATE)
env.process(arrival_generator(env, queue, ARRIVAL_RATE))
env.run(until=SIM_TIME)


avg_wait = np.mean(wait_time)
print(f"Average wait time in queue: {avg_wait:.2f} units")


plt.hist(wait_time, bins=20, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel("Wait Time")
plt.ylabel("Frequency")
plt.title("Distribution of Wait Time in M/M/1 Queue")
plt.grid(True)
plt.show()
