import logo from './logo.svg';
import './App.css';

function AgendaCreate() {
  return (
    <header className="App-header" >
      <div className="App-top">
        Aqui vai o topo
      </div>
      <div className="App-content">
        <form>
          <label>
            Especialidade
            <select>
              <option value="" selected>Selecione...</option>
              <option value="1">Nome da Especialidade</option>
            </select>
          </label>

          <label>
            Profissional
            <select>
              <option value="" selected>Selecione...</option>
              <option value="1">Nome do Profissional</option>
            </select>
          </label>

          <label>
            Selecione o dia
            <input type="date" name="data" />
          </label>

          <label>
            Selecione o horário
            <input type="time" name="hora" />
          </label>

          <input type="submit" value="Continuar" className="Btn-Submit" />
        </form>
      </div>
      <div className="App-bottom">
        Rodape
      </div>
    </header>
  );
}

function AgendaList() {
  return (
    <header className="App-header">
      <div className="App-top">
        Aqui vai o topo
      </div>
      <div className="App-content">
        <div className="Card-List">
          <div className="Card-List-Date">
            <div>20</div>
            <div>Abr</div>
          </div>
          <div className="Card-List-Body">
            <p className="Card-Titulo">Chamada de vídeo com <br/>Dr. Fulano</p>
            <p className="Card-Especialidade">Psicologia - CRM 1234</p>
            <p className="Card-Data-Hora">Início as 12:12</p>
          </div>
        </div>
        <div className="Card-List">
          <div className="Card-List-Date">
            <div>22</div>
            <div>Mai</div>
          </div>
          <div className="Card-List-Body-Alternative">
          <p className="Card-Titulo">Chamada de vídeo com <br/>Dr. Fulano</p>
            <p className="Card-Especialidade">Psicologia - CRM 1234</p>
            <p className="Card-Data-Hora">Início as 12:12</p>
          </div>
        </div>
      </div>
      <div className="App-bottom">
        Rodape
      </div>
    </header>
  );
}

function App() {
  return (
    <div className="App">
      { 1==0 && (
        <AgendaCreate />
      )}

      <AgendaList />
    </div>
  );
}

export default App;
