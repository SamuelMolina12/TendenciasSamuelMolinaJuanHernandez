// src/pages/Doctor/Doctor.js

import React, { useState, useEffect } from 'react';
import { MdOutlineCloudDownload } from 'react-icons/md';
import { toast } from 'react-hot-toast';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { Button } from '../../components/Form';
import { useNavigate } from 'react-router-dom';
import AddDoctorModal from '../../components/Modals/AddDoctorModal';
import { EmployerTable } from '../../components/Tables';
import { EmployerData } from '../../components/Datas';

function Doctor() {
  const [isOpen, setIsOpen] = useState(false);
  const [employerData, setEmployerData] = useState([]);
  const navigate = useNavigate();

  const onCloseModal = () => {
    setIsOpen(false);
  };

  const preview = (data) => {
    navigate(`/employees/preview/${data.id}`);
  };

  useEffect(() => {
    const getData = async () => {
      const data = await EmployerData();
      setEmployerData(data);
    };
    getData();
  }, []);

  return (
    <Layout>
      {isOpen && (
        <AddDoctorModal
          closeModal={onCloseModal}
          isOpen={isOpen}
          doctor={true}
          datas={null}
        />
      )}
      <button
        onClick={() => setIsOpen(true)}
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
