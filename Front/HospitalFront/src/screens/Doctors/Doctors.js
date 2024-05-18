import React, { useState, useEffect } from 'react';
import { MdOutlineCloudDownload } from 'react-icons/md';
import { toast } from 'react-hot-toast';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { Button } from '../../components/Form';
import { useNavigate } from 'react-router-dom';
import AddDoctorModal from '../../components/Modals/AddDoctorModal';
import axios from 'axios';
import { EmployerTable } from '../../components/Tables';

function Doctor() {
  const [isOpen, setIsOpen] = useState(false);
  const [employeesData, setEmployeesData] = useState([]);
  const navigate = useNavigate();

  const onCloseModal = () => {
    setIsOpen(false);
  };

  const preview = (data) => {
    navigate(`/employees/preview/${data.id}`);
  };

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/hospital/admin/employer')
      .then(response => {

        if (Array.isArray(response.data)) {
          setEmployeesData(response.data);
        } else if (typeof response.data === 'object' && response.data !== null) {
          setEmployeesData([response.data]);
        } else {
          console.error('La respuesta no es un arreglo ni un objeto válido:', response.data);
        }
      })
      .catch(error => {
        console.error('Error al obtener empleados:', error);
      });
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
            data={employeesData}
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
