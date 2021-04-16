from rand_tools import dist_erlang
import numpy as np


class Client_1():

    def __init__(self, id):
        self.type = 0
        self.id = id
        self.arrival_time = 0
        self.enter_queque_time = 0
        self.exit_queue_time = 0
        self.exit_server_time = 0

    def __repr__(self):
        return f"C1: {self.id}, {self.arrival_time:.2f}, {self.exit_queue_time:.2f}, {self.exit_server_time:.2f}"


class Client_2():

    def __init__(self, id):
        self.type = 1
        self.id = id
        self.arrival_time = 0
        self.enter_queque_time = 0
        self.exit_queue_time = 0
        self.exit_server_time = 0

    def __repr__(self):
        return f"C2: {self.id}, {self.arrival_time:.2f}, {self.exit_queue_time:.2f}, {self.exit_server_time:.2f}"


class Event():
    NEW_CLIENT_1_ARRIVAL = 1
    NEW_CLIENT_2_ARRIVAL = 2
    SERVER_EXIT = 3

    def __init__(self, time, event_type, client):
        self.time = time
        self.event_type = event_type
        self.client = client

    # def getTime(self):
    #     return self.event.time

def getTime(event):
    return event.time


class Simulation():
    EMPTY = 0
    BUSY = 1
    FULL = 2

    def __init__(self):
        self.clock = 0
        self.events = []
        self.server_queue = []
        self.exits = []
        self.server_state = self.EMPTY
        self.max_queue_len = 0
        self.prepare_entries()

    def prepare_entries(self):
        time = 0
        id = 1
        while len(self.events) < 500:
            time += 120
            c2 = Client_2(id)
            id += 1
            c2.arrival_time = time
            self.events.append(Event(time, Event.NEW_CLIENT_2_ARRIVAL, c2))

        max_time = time
        time = 0
        id = 1
        while True:
            time += np.random.uniform(100, 150)
            c1 = Client_1(id)
            id += 1
            c1.arrival_time = time
            self.events.append(Event(time, Event.NEW_CLIENT_1_ARRIVAL, c1))
            if time > max_time:
                self.events.pop()
                break
        self.events.sort(key=getTime)

    def next_event(self):
        event = self.events.pop(0)
        self.clock = event.time
        return event

    def run(self):
        client_server = ""
        iteration = 0
        while self.events:
            iteration += 1
            event = self.next_event()
            self.clock = event.time

            if event.event_type == event.NEW_CLIENT_1_ARRIVAL:
                event.client.enter_queque_time = self.clock
                self.server_queue.append(event.client)

            elif event.event_type == event.NEW_CLIENT_2_ARRIVAL:
                event.client.enter_queque_time = self.clock
                self.server_queue.append(event.client)

            elif event.event_type == event.SERVER_EXIT:
                self.server_state = self.EMPTY
                event.client.exit_server_time = self.clock
                self.exits.append(event.client)

            queue_len = len(self.server_queue)
            if self.server_state == self.EMPTY and queue_len != 0:
                self.server_state = self.BUSY              
                self.max_queue_len = queue_len if queue_len > self.max_queue_len else self.max_queue_len
                next_client = self.server_queue.pop(0)

                if type(next_client).__name__ == "Client_1":
                    busy_time = np.random.exponential(25)
                else:
                    busy_time = np.random.gamma(2, 35 / 2)
                
                next_client.exit_queue_time = self.clock
                self.events.append(
                    Event(self.clock + busy_time, Event.SERVER_EXIT, next_client))
                self.events.sort(key=getTime)


sim = Simulation()

sim.run()

office_time_c1 = []
office_time_c2 = []
count_for_type1 = 0
for exit in sim.exits:
    # if exit.type == 0:
    #     count_for_type1 += 1
    count_for_type1 = count_for_type1 + 1 if not exit.type else count_for_type1
    if exit.type == 0:
        office_time_c1.append(exit.exit_server_time - exit.arrival_time)
    else:
        office_time_c2.append(exit.exit_server_time - exit.arrival_time)


print(f"a) = Total sim time: {sim.clock}")
print(f"b) = Type 1 clients: {count_for_type1}")
print(f"c) = Average for client 1: {np.average(office_time_c1)}, Average for client 2: {np.average(office_time_c2)}")
print(f"d) = Max clients: {sim.max_queue_len}")

# timeinsystem_engrane_avg = 0
# timeinsystem_placa_avg = 0
# engranes = []
# placas = []
# for piece in sim.exits:
#     if type(piece).__name__ == "Client_2":
#         if timeinsystem_placa_avg:
#             timeinsystem_placa_avg = timeinsystem_placa_avg + \
#                 ((piece.exit_empacado_time - piece.arrival_time) -
#                  timeinsystem_placa_avg)/(len(placas)+1)
#         else:
#             timeinsystem_placa_avg = piece.exit_empacado_time - piece.arrival_time
#         placas.append((piece.exit_empacado_time, timeinsystem_placa_avg))
# for piece in sim.exits:
#     if type(piece).__name__ == "Client_1":
#         if timeinsystem_engrane_avg:
#             timeinsystem_engrane_avg = timeinsystem_engrane_avg + \
#                 ((piece.exit_empacado_time - piece.arrival_time) -
#                  timeinsystem_engrane_avg)/(len(engranes)+1)
#         else:
#             timeinsystem_engrane_avg = piece.exit_empacado_time - piece.arrival_time
#         engranes.append((piece.exit_empacado_time, timeinsystem_engrane_avg))


# print("Salieron {} engranes".format(len(engranes)))
# print("Salieron {} placas".format(len(placas)))
# print("Rechazaron {} engranes".format(len(sim.rejected_engrane)))
# print("Rechazaron {} placas".format(len(sim.rejected_placa)))

# #Graficas
# engranes = np.array(engranes)
# placas = np.array(placas)
# print(engranes[:10])

# fig, ax = plt.subplots()
# ax.plot(engranes[:, 0], engranes[:, 1], label="Client_1")
# ax.plot(placas[:, 0], placas[:, 1], label="Placas")

# ax.set(xlabel='Tiempo (m)', ylabel='Estancia Promedio (m)',
#        title='Estancia promedio de piezas')
# legend = ax.legend(shadow=True, fontsize='x-large')
# legend.get_frame().set_facecolor('C0')
# ax.grid()
# # fig.savefig("test.png")
# plt.show()
