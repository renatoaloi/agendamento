import React, { useState } from 'react';

import logo from './logo.svg';

import './App.css';
import AgendaCreate from './agenda/AgendaCreate';
import AgendaList from './agenda/AgendaList';
import AppTop from './app/AppTop';
import AppBottom from './app/AppBottom';

function App() {

  const [novo, setNovo] = useState(false);
  const [lista, setLista] = useState(false);
  const [modo, setModo] = useState("novo");

  return (
    <div className="App">
      <header className="App-header" >
        <AppTop 
          logo={logo}
          modo={modo}
        />

        {modo == "novo" && (<AgendaCreate />)}
        {modo == "lista" && (<AgendaList />)}
        
        <AppBottom 
          novo={novo}
          lista={lista}
          setNovo={(val) => setNovo(val)}
          setLista={(val) => setLista(val)}
          setModo={(val) => setModo(val)}
        />
      </header>
    </div>
  );
}

export default App;
