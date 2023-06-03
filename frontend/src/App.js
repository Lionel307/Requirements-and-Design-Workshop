import './App.css';
import { Routes, Route } from "react-router-dom";
import Home from './pages/Home'
import GetStarted from './pages/GetStarted';
import Login from './pages/Login'
import Register from './pages/Register'
import RegisterIndiv from './pages/RegisterIndiv'
import View from './pages/View'
import DashboardB from './pages/DashboardBusiness'
import DashboardC from './pages/DashboardCustomer'
import Upload from './pages/Upload'
import UploadError from './pages/UploadError'

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/getstarted" element={<GetStarted/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/register" element={<Register/>} />
      <Route path="/registerindiv" element={<RegisterIndiv/>} />
      <Route path="/view" element={<View/>} />
      <Route path="/dashboardb" element={<DashboardB/>} />
      <Route path="/dashboardc" element={<DashboardC/>} />
      <Route path="/upload" element={<Upload/>} />
      <Route path="/uploaderror" element={<UploadError/>} />
    </Routes>
  );
}

export default App;
