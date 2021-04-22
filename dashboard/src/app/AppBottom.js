
export default function AppBottom(props) {
    return(
      <div className="App-bottom">
        <div className={"Card-bottom" + (props.novo ? "-inv" : "")}>
          <img 
            src={'notas.png'} 
            className={"App-new-icon" + (props.novo ? "-inv" : "")}
            onMouseOver={() => props.setNovo(true) }
            onMouseOut={() =>  props.setNovo(false) }
            onClick={() => props.setModo("novo")}
          />
        </div>
        <div className={"Card-bottom" + (props.lista ? "-inv" : "")}>
          <img 
            src={'noticia.png'} 
            className={"App-new-icon" + (props.lista ? "-inv" : "")}
            onMouseOver={() => props.setLista(true) }
            onMouseOut={() => props.setLista(false) }
            onClick={() => props.setModo("lista")}
          />
        </div>
      </div>
    );
  }