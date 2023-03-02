from model.Maze import Maze
from model.environment import MyEnvironment
from model.goal import MyGoal

# Define o labirinto
maze = Maze(start_pos=(0, 0), end_pos=(3, 3), maze=[[0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0]])

# Cria uma instância da classe MyEnvironment
environment = MyEnvironment(maze)

# Cria uma instância da classe MyGoal
goal = MyGoal()

# Define a posição inicial do agente
agent_pos = (0, 0)

# Loop principal do agente
while agent_pos != environment.goal_pos:
    # Calcula a ação a ser tomada pelo agente
    action = goal.choose_action()

    # Executa a ação na environment
    new_agent_pos, reward = environment.perform_action(agent_pos, action)

    # Atualiza a posição do agente
    agent_pos = new_agent_pos

    # Imprime informações sobre a ação tomada e o novo estado do agente
    print("Action: ", action)
    print("New agent position: ", agent_pos)
    print("Reward: ", reward)

print("Objetivo alcançado!")
