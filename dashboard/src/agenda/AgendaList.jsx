import { useState } from 'react';
import axios from "axios";
import moment from 'moment';

function useConstructor(callBack = () => {}) {
  const [hasBeenCalled, setHasBeenCalled] = useState(false);
  if (hasBeenCalled) return;
  callBack();
  setHasBeenCalled(true);
}

export default function AgendaList() {
  useConstructor(() => {
    loadData();
    console.log(
      "This only happens ONCE and it happens BEFORE the initial render."
    );
  });

  const [ data, setData ] = useState([]);

  function loadData() {
    axios
      .get("/agenda/list")
      .then(function (response) {
        setData(response.data);
      })
      .catch(function (error) {
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
      {data.map((m) => { 
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
      </div>
    </>
  );
}
