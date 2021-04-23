import { useState } from "react";
import "./Agenda.css";
import moment from "moment";
import { useConstructor } from "../utils";
import ReactLoading from "react-loading";
import axios from "axios";

export default function AgendaCreate() {
  useConstructor(() => {
    loadEspecialidades();
  });

  const [especialidades, setEspecialidades] = useState([]);
  const [profissionals, setProfissionals] = useState([]);
  const [especialidade, setEspecialidade] = useState("");
  const [profissional, setProfissional] = useState("");
  const [data, setData] = useState("");
  const [hora, setHora] = useState("");
  const [sending, setSending] = useState(false);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState(false);
  const [ok, setOk] = useState(false);
  const [error_msg, setErrorMsg] = useState("Não foi possível enviar consulta!")

  function loadEspecialidades() {
    axios.get("/agenda/especialidades/list")
    .then(function (response) {
      console.clear();
      console.log(response.data);
      setEspecialidades(response.data);
      setLoading(false);
    })
    .catch(function (error) {
      setErrorMsg("Erro ao carregar especialidades!");
      setErr(true);
      console.log(error);
    });
  }

  function loadProfissionaisByEspecialidadeId(especialidadeId) {
    axios.get("/agenda/profissionais/find-by-especialidade/" + especialidadeId)
    .then(function (response) {
      console.clear();
      console.log(response.data);
      setProfissionals(response.data);
    })
    .catch(function (error) {
      setErrorMsg("Erro ao carregar profissionais!");
      setErr(true);
      console.log(error);
    });
  }

  const changeEspecialidade = (e) => {
    loadProfissionaisByEspecialidadeId(e.target.value);
    setEspecialidade(e.target.value);
  }

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

      const post_data = {
        'profissional_id': profissional,
        'data': moment(data).format("DD/MM/YYYY"),
        'hora': hora
      };

      console.clear();
      console.log(post_data);
      
      axios.post("/agenda/create", post_data)
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

  const tentarNovamente = (limparCampos) => {
    loadEspecialidades();
    if (limparCampos) {
      setEspecialidade("");
      setProfissional("");
      setData("");
      setHora("");
    }
    setSending(false);
    setLoading(false);
    setOk(false);
    setErr(false);
  }

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
                onChange={(e) => changeEspecialidade(e)}
              >
                <option value="" selected>
                  Selecione...
                </option>
                {especialidades.map(m => {
                  return(
                    <option value={m.id}>{m.description}</option>
                  );
                })}
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
                {profissionals.map(m => {
                  return(
                    <option value={m.id}>Dr(a). {m.name}</option>
                  );
                })}
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
        {loading && !sending && !err && !ok && (
          <div>
            <p>
              Carregando...
            </p>
            <ReactLoading type="bars" color="#FFFFFF" height="100%" width="100%" />
          </div>
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
            <input
              type="button"
              value="Tentar novamente"
              className="Btn-Submit"
              onClick={() => tentarNovamente(false)}
            />
          </div>
        )}
        {loading && ok && (
          <div>
            <p>Consulta enviada com sucesso!</p>
            <input
              type="button"
              value="Criar nova consulta"
              className="Btn-Submit"
              onClick={() => tentarNovamente(true)}
            />
          </div>
        )}
      </div>
    </>
  );
}
