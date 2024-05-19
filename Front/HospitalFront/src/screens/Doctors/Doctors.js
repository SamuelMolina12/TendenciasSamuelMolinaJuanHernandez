import React, { useState, useEffect } from 'react';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { useNavigate } from 'react-router-dom';
import AddDoctorModal from '../../components/Modals/AddDoctorModal';
import Updatedemployer from '../../components/Modals/UpdEmployer';
import { EmployerTable } from '../../components/Tables';
import { EmployerData } from '../../components/Datas';

function Doctor() {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  const [selectedEmployer, setSelectedEmployer] = useState(null);
  const [employerData, setEmployerData] = useState([]);
  const navigate = useNavigate();

  const onCloseAddModal = async () => {
    setIsAddModalOpen(false);
    await getData();
  };

  const onCloseUpdateModal = async () => {
    setIsUpdateModalOpen(false);
    setSelectedEmployer(null);
    await getData();
  };

  const preview = (id) => {
    const employer = employerData.find(emp => emp.id === id);
    setSelectedEmployer(employer);
    setIsUpdateModalOpen(true);
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
      {isAddModalOpen && (
        <AddDoctorModal
          closeModal={onCloseAddModal}
          isOpen={isAddModalOpen}
          doctor={true}
          datas={null}
        />
      )}
      {isUpdateModalOpen && (
        <Updatedemployer
          closeModal={onCloseUpdateModal}
          isOpen={isUpdateModalOpen}
          employerData={selectedEmployer}
        />
      )}
      <button
        onClick={() => setIsAddModalOpen(true)}
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
            }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Doctor;
