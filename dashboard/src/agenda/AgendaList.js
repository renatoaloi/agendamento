
export default function AgendaList() {
    return (
      <>
        <div className="App-content">
          <div className="Card-List">
            <div className="Card-List-Date">
              <div>20</div>
              <div>Abr</div>
            </div>
            <div className="Card-List-Body">
              <p className="Card-Titulo">Chamada de vídeo com <br />Dr. Fulano</p>
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
              <p className="Card-Titulo">Chamada de vídeo com <br />Dr. Fulano</p>
              <p className="Card-Especialidade">Psicologia - CRM 1234</p>
              <p className="Card-Data-Hora">Início as 12:12</p>
            </div>
          </div>
        </div>
      </>
    );
  }