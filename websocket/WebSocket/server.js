const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('Recebido:', message);
    
    // Exemplo: Enviando uma mensagem de volta para o cliente
    ws.send('Mensagem recebida pelo servidor: ' + message);
  });
  
  // Exemplo: Enviando uma mensagem para o cliente assim que a conexão é estabelecida
  ws.send('Conexão estabelecida com sucesso!');
});
