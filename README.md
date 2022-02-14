# Gerenciador de leituras
O abjetivo da atividade era desenvolver serviços cliente-servidor UDP nos padrões RMI.

## Aplicação
A aplicação foi desenvolvida por Elias Frota, Dheymison Nunes e Marcos Paulo. <br>
O sistema consiste, principalmente, em quatro funções para gerenciar a
lista de leitura: adicionar livro, abandonar livro, finalizar livro e ver lista de
leitura. <br>
<ul>
  <li>
  <strong>Adicionar livro:</strong> o cliente solicita informações para adicionar um
  livro a lista de leitura (título, autor e quantidade de páginas do
  livro).
  </li>
  <li>
  <strong>Abandonar livro:</strong> o cliente informa ao servidor que o usuário não
  gostaria de ler mais um determinado livro. A única informação
  coletada para abandonar uma leitura é o título do livro.
  </li>
  <li>
  <strong>Ver lista de leitura:</strong> O cliente solicita ao servidor a lista de livros
  que já foram lidos e que ainda estão sendo lidos pelo usuário.
  </li>
  <li>
  <strong>Finalizar livro:</strong> O cliente informa que o usuário terminou um
  determinado livro. A informações coletadas são o título do livro,
  uma avaliação de 0 a 5 do livro.
  </li>
</ul>

## Implementação nos lados Cliente e Servidor

<ul>
  <li>
    <strong>Server:</strong>
    <ul>
      <li>
        <strong>despachante:</strong> o servidor chama a função <em>invoke()</em> do
        despachante passando a mensagem recebida pelo cliente
        como parâmetro de entrada. A <em>invoke()</em> verifica qual o
        serviço que está sendo solicitado e direciona para o
        esqueleto.
      </li>
      <li>
        <strong>Esqueleto:</strong> o esqueleto possui quatro funções: <em>addBook()</em>,
        <em>leaveReading()</em>, <em>seeList()</em>, <em>finishReading()</em>. Todas elas
        recebem como parâmetro de entrada o objeto que foi
        recebido na mensagem vinda do cliente. Esse objeto é
        passado para sua respectiva função do <em>bookDB()</em>.
      </li>
      <li>
        <strong>BookDB:</strong> é o responsável por implementar realmente o
        serviço. É ela que interage com o banco de dados para
        adicionar, remover ou atualizar informações.
      </li>
    </ul>
  </li>
  <li>
    <strong>Client:</strong>
    <ul>
      <li>
        <strong>user:</strong> interage com o usuário coletando as informações
        necessárias para execução de determinado serviço. É aqui
        onde o usuário consegue selecionar o serviço que será
        solicitado ao servidor. É aqui também onde a resposta do
        servidor é mostrada ao usuário de acordo com o serviço
        solicitado.
      </li>
      <li>
        <strong>proxy:</strong> as informações coletadas do usuários são colocadas
        em um dict, juntamente com o serviço que foi solicitado. Esse dicionário é serializado e mandado para o servidor
        como requisição.
      </li>
    </ul>
  </li>
</ul>
