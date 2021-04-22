import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
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
              Data para marcação
              <input type="date" name="data" />
            </label>

            <label>
              Hora desejada para a consulta
              <input type="time" name="hora" />
            </label>

            <input type="submit" value="ENVIAR" className="Btn-Submit" />
          </form>
        </div>
        <div className="App-bottom">
          Rodape
        </div>
      </header>
    </div>
  );
}

export default App;
