import React, { useState, useEffect } from 'react';
import Layout from '../../Layout';
import { BiPlus } from 'react-icons/bi';
import { Link, useNavigate } from 'react-router-dom';
import { PatientData } from '../../components/Datas';
import { PatientTable } from '../../components/Tables'
import AddPatientModal from '../../components/Modals/AddPatientModal';
import DeletePatientModal from '../../components/Modals/DelPatientModal';



function Patient() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [patientData, setPatientData] = useState([]);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedPatient, setSelectedPatient] = useState(null);
  const navigate = useNavigate();

  const onCloseModal = async () => { 
    setIsModalOpen(false);
    setSelectedPatient(null);
    await getData();
  };

  const onCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setSelectedPatient(null);
  }
  const handleUpdate = (id) => {
    const patient = patientData.find(emp => emp.id === id);
    setSelectedPatient(patient);
    setIsModalOpen(true);
  };
  const handleDelete = async (id) => {
    setSelectedPatient(id);
    setIsDeleteModalOpen(true);
  };

  const getData = async () => {
    const data = await PatientData();
    setPatientData(data);
  };  

  useEffect(() => {
    getData();
  }, []);




  const preview = (id) => {
    navigate(`/patients/preview/${id}`);
  };

  return (
    <Layout>
     
      <Link
        to="/patients/create"
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </Link>
      {isModalOpen && (
        <AddPatientModal
          closeModal={onCloseModal}
          isOpen={isModalOpen}
          patientData={selectedPatient}
        />
      )}
      {isDeleteModalOpen && (
        <DeletePatientModal
          closeModal={onCloseDeleteModal}
          isOpen={isDeleteModalOpen}
          patientId={selectedPatient?.id}
          onDeleteSuccess={getData}
        />
      )}
      <button
        onClick={() => setIsModalOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      <h1 className="text-xl font-semibold">Pacientes</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        <div className="mt-8 w-full overflow-x-scroll">
          <PatientTable
            data={patientData}
            functions={{
              preview: preview,
              handleUpdate: handleUpdate,
              handleDelete: handleDelete,
            }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Patient;