import { useState } from "react";
import "./Agenda.css";

export default function AgendaCreate() {
  const [especialidade, setEspecialidade] = useState("");
  const [profissional, setProfissional] = useState("");
  const [data, setData] = useState("");
  const [hora, setHora] = useState("");
  const [sending, setSending] = useState(false);

  const onContinuar = (e) => {
    e.preventDefault();
    setSending(!sending);
    e.target.value = "Aguarde...";
    //alert(e.target.value);
  };

  return (
    <>
      <div className="App-content">
        <form>
          <label>
            Especialidade
            <select
              required
              value={especialidade}
              onChange={(e) => setEspecialidade(e.target.value)}
            >
              <option value="" selected>
                Selecione...
              </option>
              <option value="1">Nome da Especialidade</option>
            </select>
          </label>

          <label>
            Profissional
            <select
              required
              value={especialidade}
              onChange={(e) => setProfissional(e.target.value)}
            >
              <option value="" selected>
                Selecione...
              </option>
              <option value="1">Nome do Profissional</option>
            </select>
          </label>

          <label>
            Selecione o dia
            <input
              type="date"
              name="data"
              required
              value={data}
              onChange={(e) => setData(e.target.value)}
            />
          </label>

          <label>
            Selecione o horário
            <input
              type="time"
              name="hora"
              required
              value={hora}
              onChange={(e) => setHora(e.target.value)}
            />
          </label>

          <input
            type="submit"
            value={sending ? "Aguarde..." : "Continuar"}
            className="Btn-Submit"
            onClick={(e) => onContinuar(e)}
            disabled={sending}
          />
        </form>
      </div>
    </>
  );
}
