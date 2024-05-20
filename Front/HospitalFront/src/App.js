// ********* EyeCare - Eye clinic Website is created by Zpunet ******************
// ********* If you get an error please contact us ******
// ******** Email:info@codemarketi.com *********
// ******** Email:minahmmassy@gmail.com *********
// ******** Email:laummassy@gmail.com *********
// ********* Website:www.codemarketi.com *********
// ********* WHATSAPP 👇👇👇👇👇 *********
// ********* Phone:+255 762 352 746 *********
// ********* Phone:+255 683 851 979 *********
// ********* Youtub Channel: https://www.youtube.com/channel/UCOYwYO-LEsrjqBs6xXSfq1w *********

// ******** Support my work with *********
// ********* https://www.patreon.com/zpunet *********
// ********* https://www.buymeacoffee.com/zpunet *********

// ********* This is the main component of the website *********

import './App.css';
import React, { Suspense } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Aos from 'aos';
import Toast from './components/Notifications/Toast';
import BigLoader from './components/Notifications/BigLoader';
import Chats from './screens/Chats/Chats';
const Dashboard = React.lazy(() => import('./screens/Dashboard'));
const Payments = React.lazy(() => import('./screens/Payments/Payments'));
const Appointments = React.lazy(() => import('./screens/Appointments'));
const Patients = React.lazy(() => import('./screens/Patients/Patients'));
const Campaings = React.lazy(() => import('./screens/Campaings'));
const Services = React.lazy(() => import('./screens/Services'));
const Invoices = React.lazy(() => import('./screens/Invoices/Invoices'));
const Settings = React.lazy(() => import('./screens/Settings'));



const CreateInvoice = React.lazy(() =>
  import('./screens/Invoices/CreateInvoice')
);
const EditInvoice = React.lazy(() => import('./screens/Invoices/EditInvoice'));
const PreviewInvoice = React.lazy(() =>
  import('./screens/Invoices/PreviewInvoice')
);
const EditPayment = React.lazy(() => import('./screens/Payments/EditPayment'));
const PreviewPayment = React.lazy(() =>
  import('./screens/Payments/PreviewPayment')
);

const PatientProfile = React.lazy(() =>
  import('./screens/Patients/PatientProfile')
);
const CreatePatient = React.lazy(() =>
  import('./screens/Patients/CreatePatient')
);
//empleado
const Employer = React.lazy(() => import('./screens/Employer/Employer'));
const DoctorProfile = React.lazy(() =>
  import('./screens/Employer/DoctorProfile')
);
//especialista
const Specialist = React.lazy(() => import('./screens/Specialist'));

//medicina
const Medicine = React.lazy(() => import('./screens/Medicine'));
//procedimiento
const Procedure = React.lazy(() => import('./screens/Inventory/Procedure'));
//Ayuda diagnostica
const DiagnosticHelp = React.lazy(() => import('./screens/Inventory/DiagnosticHelp'));
const NewMedicalRecode = React.lazy(() =>
  import('./screens/Patients/NewMedicalRecode')
);
const NotFound = React.lazy(() => import('./screens/NotFound'));
const Login = React.lazy(() => import('./screens/Login'));
const Reviews = React.lazy(() => import('./screens/Reviews'));

function App() {
  Aos.init();

  return (
    <>
      {/* Toaster */}
      <Toast />
      {/* Routes */}
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <Suspense fallback={<BigLoader />}>
                <Dashboard />
              </Suspense>
            }
          />
          {/* invoce */}
          <Route
            path="/invoices"
            element={
              <Suspense fallback={<BigLoader />}>
                <Invoices />
              </Suspense>
            }
          />
          <Route
            path="/invoices/create"
            element={
              <Suspense fallback={<BigLoader />}>
                <CreateInvoice />
              </Suspense>
            }
          />
          <Route
            path="/invoices/edit/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <EditInvoice />
              </Suspense>
            }
          />
          <Route
            path="/invoices/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <PreviewInvoice />
              </Suspense>
            }
          />
          {/* payments */}
          <Route
            path="/payments"
            element={
              <Suspense fallback={<BigLoader />}>
                <Payments />
              </Suspense>
            }
          />
          <Route
            path="/payments/edit/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <EditPayment />
              </Suspense>
            }
          />
          <Route
            path="/payments/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <PreviewPayment />
              </Suspense>
            }
          />
          {/* patient */}
          <Route
            path="/patients"
            element={
              <Suspense fallback={<BigLoader />}>
                <Patients />
              </Suspense>
            }
          />
          <Route
            path="/patients/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <PatientProfile />
              </Suspense>
            }
          />
          <Route
            path="/patients/create"
            element={
              <Suspense fallback={<BigLoader />}>
                <CreatePatient />
              </Suspense>
            }
          />
          <Route
            path="/patients/visiting/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <NewMedicalRecode />
              </Suspense>
            }
          />
          {/* Empleado */}
          <Route
            path="/employer"
            element={
              <Suspense fallback={<BigLoader />}>
                <Employer />
              </Suspense>
            }
          />
          <Route
            path="/doctors/preview/:id"
            element={
              <Suspense fallback={<BigLoader />}>
                <DoctorProfile />
              </Suspense>
            }
          />
          {/* especialistas */}
          <Route
            path="/specialist"
            element={
              <Suspense fallback={<BigLoader />}>
                <Specialist />
              </Suspense>
            }
          />
          {/* procedimientos */}
          <Route
            path="/inventory/procedure"
            element={
              <Suspense fallback={<BigLoader />}>
                <Procedure />
              </Suspense>
            }
          />
          {/* ayuda diagnostica */}
          <Route
            path="/inventory/diagnostichelp"
            element={
              <Suspense fallback={<BigLoader />}>
                <DiagnosticHelp />
              </Suspense>
            }
          />
          {/* others */}
          <Route
            path="/login"
            element={
              <Suspense fallback={<BigLoader />}>
                <Login />
              </Suspense>
            }
          />
          <Route
            path="/appointments"
            element={
              <Suspense fallback={<BigLoader />}>
                <Appointments />
              </Suspense>
            }
          />
          <Route
            path="/campaigns"
            element={
              <Suspense fallback={<BigLoader />}>
                <Campaings />
              </Suspense>
            }
          />
          <Route
            path="/medicine"
            element={
              <Suspense fallback={<BigLoader />}>
                <Medicine />
              </Suspense>
            }
          />
          <Route
            path="/services"
            element={
              <Suspense fallback={<BigLoader />}>
                <Services />
              </Suspense>
            }
          />
          <Route
            path="/settings"
            element={
              <Suspense fallback={<BigLoader />}>
                <Settings />
              </Suspense>
            }
          />
          {/* reviews */}
          <Route
            path="/reviews"
            element={
              <Suspense fallback={<BigLoader />}>
                <Reviews />
              </Suspense>
            }
          />
          {/* chats */}
          <Route
            path="/chats"
            element={
              <Suspense fallback={<BigLoader />}>
                <Chats />
              </Suspense>
            }
          />
          <Route
            path="*"
            element={
              <Suspense fallback={<BigLoader />}>
                <NotFound />
              </Suspense>
            }
          />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
