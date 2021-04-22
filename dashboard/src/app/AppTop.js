
export default function AppTop(props) {
    return(
      <div className="App-top">
        <img src={props.logo} className="App-logo" alt="logo" />
        <span className="App-top-title">
          { props.modo == "novo" ? "AGENDAMENTO" : "CONSULTA" }
        </span>
      </div>
    );
  }