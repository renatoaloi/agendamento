import { useState } from "react";
import "./Agenda.css";
import moment from "moment";
import { useConstructor } from "../utils";
import ReactLoading from "react-loading";
import axios from "axios";

export default function AgendaCreate() {
  useConstructor(() => {});

  const [especialidade, setEspecialidade] = useState("");
  const [profissional, setProfissional] = useState("");
  const [data, setData] = useState("");
  const [hora, setHora] = useState("");
  const [sending, setSending] = useState(false);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState(false);
  const [ok, setOk] = useState(false);
  const [error_msg, setErrorMsg] = useState("Não foi possível enviar consulta!")

  const checkIfAllFieldsAreValid = () => {
    return (
      especialidade != "" && profissional != "" && data != "" && hora != ""
    );
  };

  const checkIfDateAndTimeAreValid = () => {
    try {
      let dt = moment(data + " " + hora + ":00", "YYYY-MM-DD HH:mm:ss");
      console.log(dt);
      return dt.isValid();
    } catch (error) {
      console.log(error);
    }
    return false;
  };

  const onContinuar = (e) => {
    e.preventDefault();

    if (checkIfAllFieldsAreValid() && checkIfDateAndTimeAreValid()) {
      setErr(false);
      setErrorMsg("Não foi possível enviar consulta!");
      setLoading(true);
      setSending(true);
      e.target.value = "Aguarde...";
      
      axios.post("/agenda/create", {
        'profissional_id': profissional,
        'data': data,
        'hora': hora
      })
      .then(function (response) {
        setData(response.data);
        //setLoading(!loading);
        setErr(false);
        setOk(true);
        //setSending(false);
      })
      .catch(function (error) {
        setLoading(!loading);
        setErr(true);
        setOk(false);
        //setSending(false);
        console.log(error);
      });

    }
    else {
      setLoading(false);
      setSending(false);
      setErrorMsg("Formulário incorreto!");
      setErr(true);
    }
  };

  return (
    <>
      <div className="App-content">
        {!sending && !loading && (
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
                value={profissional}
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
        )}
        {sending && loading && !err && !ok && (
          <div>
            <p>
              Enviando...
            </p>
            <ReactLoading type="bars" color="#FFFFFF" height="100%" width="100%" />
          </div>
        )}
        {err && (
          <div>
            <p>{error_msg}</p>
          </div>
        )}
        {loading && ok && (
          <div>
            <p>Consulta enviada com sucesso!</p>
          </div>
        )}
      </div>
    </>
  );
}
