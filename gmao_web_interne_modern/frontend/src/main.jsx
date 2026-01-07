import React from 'react'
import ReactDOM from 'react-dom/client'

const API_URL = "https://gmao-armax-1.onrender.com"

function App() {
  return (
    <div>
      <h1>GMAO Web Moderne</h1>
      <p>Backend connecté :</p>
      <p>{API_URL}</p>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)
