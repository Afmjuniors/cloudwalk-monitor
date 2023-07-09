import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from database.queries_database import get_all_transactions


# Função para atualizar o gráfico em tempo real
def update_graph(frame):
    # Obter os dados do banco de dados
    results = get_all_transactions()

    # Criar um DataFrame com os resultados
    df = pd.DataFrame(results, columns=['id', 'time', 'status', 'count'])
    df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')

    # Agrupar os dados por intervalos de 10 minutos e status, e calcular a soma das contagens
    df_grouped = df.groupby([pd.Grouper(key='time', freq='10Min'), 'status']).sum().reset_index()
    print(df_grouped)
    # Limpar o gráfico anterior
    plt.cla()

    # Iterar sobre os status únicos e criar as linhas correspondentes
    for status in df_grouped['status'].unique():
        status_data = df_grouped[df_grouped['status'] == status]
        plt.plot(status_data['time'], status_data['count'], color=colors[status], marker='o', label=status)

    # Definir os rótulos dos eixos e o título do gráfico
    plt.xlabel('Hora')
    plt.ylabel('Contagem')
    plt.title('Gráfico de Linhas em Tempo Real')

    # Formatar o eixo x para exibir apenas HH:MM
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    # Ajustar os intervalos dos ticks do eixo x
    ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))

    # Girar os rótulos dos ticks do eixo x
    plt.xticks(rotation=45)

    # Obter os rótulos e locais dos ticks do eixo x
    x_ticks = ax.get_xticks()
    x_tick_labels = ax.get_xticklabels()

    # Definir o espaçamento entre os ticks do eixo x
    new_x_ticks = [x_ticks[i] for i in range(len(x_ticks)) if i % 2 == 0]
    new_x_tick_labels = [x_tick_labels[i] for i in range(len(x_tick_labels)) if i % 2 == 0]

    # Definir os novos ticks e rótulos do eixo x
    plt.xticks(new_x_ticks, new_x_tick_labels)

    # Adicionar uma legenda
    plt.legend()


# Criar uma figura e um eixo para o gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Definir as cores para cada status
colors = {'approved': 'green',
          'refunded': 'green',
          'denied': 'red',
          'failed': 'darkred',
          'processing': 'yellow',
          'reversed': 'blue',
          'backend_reversed': 'blue'}

# Configurar a atualização periódica do gráfico
ani = animation.FuncAnimation(fig, update_graph, interval=60000)  # Atualiza a cada 1 minuto (60000 ms)

# Exibir o gráfico
plt.show()

