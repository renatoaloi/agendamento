import { useState } from 'react';
import axios from "axios";
import ReactLoading from 'react-loading';
import { useConstructor } from '../utils';

export default function AgendaList() {
  useConstructor(() => {
    loadData();
  });

  const [ data, setData ] = useState([]);
  const [ loading, setLoading ] = useState(true);
  const [ err, setErr ] = useState(false);

  function loadData() {
    axios
      .get("/agenda/list")
      .then(function (response) {
        setData(response.data);
        setLoading(!loading);
        setErr(false);
      })
      .catch(function (error) {
        setLoading(!loading);
        setErr(true);
        console.log(error);
      });
  }

  function findMonthByNumber(number) {
    let a = [ "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov" ];
    return a[number-1];
  }

  return (
    <>
      <div className="App-content">
        {!loading && data.map((m) => { 
          return(
            <div className="Card-List">
              <div className="Card-List-Date">
                <div>{m.data.substr(0,2)}</div>
                <div>{findMonthByNumber(m.data.substr(3, 2))}</div>
              </div>
              <div className="Card-List-Body">
                <p className="Card-Titulo">
                  Chamada de vídeo com <br />
                  Dr. {m.profissional}
                </p>
                <p className="Card-Especialidade">{m.especialidade} - CRM {m.crm}</p>
                <p className="Card-Data-Hora">Início as {m.hora}</p>
              </div>
            </div>
          );
        })}
        {loading && (
          <div>
            <p>
              Carregando...
            </p>
            <ReactLoading type="bars" color="#FFFFFF" height="100%" width="100%" />
          </div>
        )}
        {!loading && err && (
          <div>
            <p>
              Não foi possível carregar a lista!
            </p>
          </div>
        )}
      </div>
    </>
  );
}
