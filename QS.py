from random import randint
from matplotlib import pyplot as plt
import numpy as np
import time


def list_generator(n):                      #Generating list of tasks
    clients = []
    tasks = ["A","B","C"]
    placeholder = []
    for i in range(n):
        task = randint(0,2)
        placeholder.append(tasks[task])
        difficulty = randint(1,10)
        placeholder.append(difficulty)
        clients.append(placeholder)
        placeholder = []
    return clients

def window_generator(a,b,c,e):              #Generating list with windows
    windows=[]
    for i in range(a):
        windows.append(["A",0])#[Type of window|for how long it will be occupied]
    for i in range(b):
        windows.append(["B",0])
    for i in range(c):
        windows.append(["C",0])
    for i in range(e):
        windows.append(["E",0])
    return windows

def job_simulator(clients,windows,window_price, max_time): #Tasks handling
    iterations=0                    #Number of iterations
    price = 0                       #Summed price of using windows
    earnings = 0                    #Earnings 
    satisfied_clients = 0           #Number of customers served
    len_start = len(clients)
    #print(Clients)
    current_Job=clients[0]
    for _ in range(max_time):
        for i in range(len(windows)):
            if (windows[i][0] == current_Job[0] or windows[i][0] == "E") and windows[i][1] == 0 and current_Job != [0,0]: #Przydzielanie nowego zadania
                windows[i][1] = current_Job[1]
                earnings += current_Job[1]                                                                              #Dodanie zarobku za wykonanie zadania
                #print(f'Window {Windows[i][0]} {i} got new job for {Windows[i][1]} iterations')
                if len(clients) > 1:                                                                                    #Nowe oczekujące zadanie
                    del clients[0]           
                    current_Job = clients[0]
                    #satisfied_clients += 1
                elif len(clients) == 1:                                                                                 #Placeholder jeżeli skońćzyły się zadania                                                                                 
                    del clients[0]
                    current_Job = [0,0]
            elif windows[i][1] > 0:                                                                                     #Jeżeli okienko ma zadanie- zmniejsz pozostałą liczbe iteracji okienka                                                     
                windows[i][1] -=1
                if windows[i][0] == 'A':                                                                                #Dodanie ceny za wykorzystanie okienka
                    price += window_price[0]
                if windows[i][0] == 'B':
                    price += window_price[1]
                if windows[i][0] == 'C':
                    price += window_price[2]
                if windows[i][0] == 'E':
                    price += window_price[3]
        iterations+=1
        satisfied_clients = len_start - len(clients)
        Iterations_left = []
        for i in range(len(windows)):                                                                                    #Pętla zbierająca ile każdemu z okienek pozostało iteracji
            Iterations_left.append(windows[i][1])
        #print(f'|End of iteration {iterations}|____________________________________________')
    return satisfied_clients, price, earnings
    
def simulation(window_price, windows1, windows2, max_time, clients):
    satsified_clients1 = 0
    satisfied_clietns2 = 0
    clients1 = list_generator(clients)
    clients2 = clients1.copy()
    satsified_clients1,price1, earnings1 = job_simulator(clients1,windows1,window_price,max_time)
    satisfied_clietns2,price2, earnings2 = job_simulator(clients2,windows2,window_price, max_time)
    satsified_clients1_list.append(satsified_clients1)
    satisfied_clietns2_list.append(satisfied_clietns2)
    price_list1.append(price1)
    price_list2.append(price2)
    earnings_list1.append(earnings1)
    earnings_list2.append(earnings2)

#######PREPARING PARAMETERS#######

satsified_clients1_list = []
satisfied_clietns2 = 0
satisfied_clietns2_list = []
price_list1 = []
price_list2 = []
earnings_list1 = []
earnings_list2 = []
window_price = [0.5,0.5,0.5,0.85]           #Setting cost of every window (earings = 1/iteration)
windows1 = window_generator(2,2,2,0)        #Generating windows [A, B, C, E]
windows2 = window_generator(1,1,1,3)
repetitions = 200                           #Repetitions of simulation
max_time = 100                              #Limit of iterations
clients = 100                               #Number of clients

#######SIMULATION#######

print('Starting.')
start = time.time()
for _ in range(repetitions):
    simulation(window_price, windows1, windows2, max_time, clients)

end = time.time()
print(f"Ending.\nWorking time : {end - start}") 

#######PREPARING DATA FOR PLOTTING#######

min_list = [min(satsified_clients1_list),min(satisfied_clietns2_list)]
avg_list = (sum(satsified_clients1_list)/repetitions,sum(satisfied_clietns2_list)/repetitions)
max_price_list = [max(price_list1),max(price_list2)]
avg_price_list = [sum(price_list1)/repetitions, sum(price_list2)/repetitions]
min_earnings_list = [min(earnings_list1),min(earnings_list2)]
avg_earnings_list = [sum(earnings_list1)/repetitions, sum(earnings_list2)/repetitions]
diff_list = [sum(earnings_list1)/repetitions - sum(price_list1)/repetitions, sum(earnings_list2)/repetitions - sum(price_list2)/repetitions]

#######PLOTS#######

labels=np.array(["2A|2B|2C|0E",'1A|1B|1C|3E'])
x = np.arange(len(labels))
width=0.2
fig, axs = plt.subplots(2, 2,figsize=(8,8))
plt.style.use('ggplot')
axs[0,0].set_title('Number of clients served')
axs[0,0].set(xlabel = 'Arrangement of the windows', ylabel = "Clients")
axs[0,0].bar(x+width/2,avg_list,width,label="Avg values", color = 'limegreen')
axs[0,0].bar(x-width/2,min_list,width,label="Min values", color = 'gold')
axs[0,0].legend()
axs[0,0].set_xticks(x)
axs[0,0].set_xticklabels(labels)
axs[0,0].grid()
axs[1,0].set_title('Cost of completing the tasks ')
axs[1,0].set(xlabel = 'Arrangement of the windows', ylabel = "Costs")
axs[1,0].bar(x+width/2,avg_price_list,width,label="Avg values", color = 'limegreen')
axs[1,0].bar(x-width/2,max_price_list,width,label="Max values", color = 'crimson')
axs[1,0].legend()
axs[1,0].set_xticks(x)
axs[1,0].set_xticklabels(labels)
axs[1,0].grid()
axs[1,1].set_title('Earnings from completing the tasks')
axs[1,1].set(xlabel = 'Arrangement of the windows', ylabel = "Earnings")
axs[1,1].bar(x+width/2,avg_earnings_list,width,label="Avg values", color = 'limegreen')
axs[1,1].bar(x-width/2,min_earnings_list,width,label="Min values", color = 'gold')
axs[1,1].legend()
axs[1,1].set_xticks(x)
axs[1,1].set_xticklabels(labels)
axs[1,1].grid()
axs[0,1].set_title('Profit from completing the tasks')
axs[0,1].set(xlabel = 'Arrangement of the windows', ylabel = "Profit")
axs[0,1].bar(x,diff_list,width,label="Avg  values", color = 'limegreen')
axs[0,1].legend()
axs[0,1].set_xticks(x)
axs[0,1].set_xticklabels(labels)
axs[0,1].grid()
fig.tight_layout()
plt.show()