import { useState } from 'react'
import './App.css'
import Divar from './app/DivarQuery'
import DivarPage from './components/templates/DivarPage'
import Jabama from './app/JabamaQuery'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
        <Divar/>
    <Jabama/>
    </>

  )
}

export default App
