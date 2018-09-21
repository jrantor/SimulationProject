import random, simpy

seed = 100
time_arrival = 12
print("Enter number of processes: ")
process_number = int(input())

def source(env,number,interval, counter):
    #generates customers randomly
    
    for i in range(number):
        p = task(env, 'Process%02d' %i, counter, service_time=12)
        env.process(p)
        t = random.expovariate(1.0/interval)
        yield env.timeout(t)

def task(env, pro_name,counter, service_time):
    #arrival, service and leaves
      arrive = env.now
      print('%f %s: Arrives'% (arrive,pro_name))

      with counter.request() as req:
          yield req
  
            
           
          wait = env.now - arrive
          print('%s: Waited %f minutes' % (pro_name, wait))
          print('__________________________________________')

          ts = random.expovariate(1.0 / service_time)
          yield env.timeout(ts)
          time_spend_in_system = env.now - arrive
          service_time = time_spend_in_system - wait
        
          print('%f %s is Finished' % (env.now, pro_name))
          print('__________________________________________')
          print('Service time for %s is %f'%(pro_name,service_time))
          print('__________________________________________')
          print('%s: spent %f minutes in system. '% (pro_name,time_spend_in_system))
          print('__________________________________________')
    



# Setting-up and start the simulation
print('---------------------------------------')
random.seed(seed)
env = simpy.Environment()

# Start processes and run
counter = simpy.Resource(env, capacity=1)
env.process(source(env, process_number, time_arrival, counter))
env.run()
    
                        
