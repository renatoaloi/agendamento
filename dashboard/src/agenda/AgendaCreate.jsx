import "./Agenda.css";

export default function AgendaCreate() {
  return (
    <>
      <div className="App-content">
        <form>
          <label>
            Especialidade
            <select>
              <option value="" selected>
                Selecione...
              </option>
              <option value="1">Nome da Especialidade</option>
            </select>
          </label>

          <label>
            Profissional
            <select>
              <option value="" selected>
                Selecione...
              </option>
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
    </>
  );
}
