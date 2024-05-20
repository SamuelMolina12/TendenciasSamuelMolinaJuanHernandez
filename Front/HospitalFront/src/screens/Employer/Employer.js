import React, { useState, useEffect } from 'react';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { useNavigate } from 'react-router-dom';
import AddDoctorModal from '../../components/Modals/AddDoctorModal';
import DeleteEmployerModal from '../../components/Modals/DelEmployerModal'; 
import { EmployerTable } from '../../components/Tables';
import { EmployerData, deleteEmployer } from '../../components/Datas'; 

function Doctor() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false); 
  const [selectedEmployer, setSelectedEmployer] = useState(null);
  const [employerData, setEmployerData] = useState([]);
  const navigate = useNavigate();

  const onCloseModal = async () => {
    setIsModalOpen(false);
    setSelectedEmployer(null);
    await getData();
  };

  const onCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setSelectedEmployer(null);
  };

  const preview = (id) => {
    const employer = employerData.find(emp => emp.id === id);
    setSelectedEmployer(employer);
    setIsModalOpen(true);
  };

  const handleDelete = async (id) => {
    setSelectedEmployer(id);
    setIsDeleteModalOpen(true);
  };

  const getData = async () => {
    const data = await EmployerData();
    setEmployerData(data);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <Layout>
      {isModalOpen && (
        <AddDoctorModal
          closeModal={onCloseModal}
          isOpen={isModalOpen}
          employerData={selectedEmployer}
        />
      )}
      {isDeleteModalOpen && (
        <DeleteEmployerModal
          closeModal={onCloseDeleteModal}
          isOpen={isDeleteModalOpen}
          employeeId={selectedEmployer?.id}
          onDeleteSuccess={getData}
        />
      )}
      <button
        onClick={() => setIsModalOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      <h1 className="text-xl font-semibold">Empleados</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        <div className="mt-8 w-full overflow-x-scroll">
          <EmployerTable
            data={employerData}
            functions={{
              preview: preview,
              handleDelete: handleDelete, 
            }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Doctor;
