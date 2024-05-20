import React, { useState, useEffect } from 'react';
import { BiPlus } from 'react-icons/bi';
import Layout from '../Layout';
import { toast } from 'react-hot-toast';
import { SpecialistTable } from '../components/Tables';
import AddSpecialistModal from '../components/Modals/AddSpecialistModal';
import UpdateSpecialistModal from '../components/Modals/UpdSpecialistModal';
import DelSpecialistModal from '../components/Modals/DelSpecialistModal';
import { SpecialistData } from '../components/Datas';

function Receptions() {
  const [isOpen, setIsOpen] = useState(false);
  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedSpecialist, setSelectedSpecialist] = useState(null);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await SpecialistData();
        setData(result);
      } catch (error) {
        console.error('Error al obtener datos de especialistas:', error);
        toast.error('Error al obtener datos de especialistas.');
      }
    };

    fetchData();
  }, []);

  const onCloseModal = async () => {
    setIsOpen(false);
    setSelectedSpecialist(null);
    await getData();
  };

  const onCloseUpdateModal = async () => {
    setIsUpdateModalOpen(false);
    setSelectedSpecialist(null);
    await getData();
  };

  const onCloseDeleteModal = async () => {
    setIsDeleteModalOpen(false);
    setSelectedSpecialist(null);
    await getData();
  };

  const getData = async () => {
    try {
      const data = await SpecialistData();
      setData(data);
    } catch (error) {
      console.error('Error al obtener datos de especialistas:', error);
      toast.error('Error al obtener datos de especialistas.');
    }
  };

  const preview = (specialist) => {
    setSelectedSpecialist(specialist);
    setIsUpdateModalOpen(true);
  };

  const handleDelete = (specialist) => {
    setSelectedSpecialist(specialist);
    setIsDeleteModalOpen(true);
  };

  return (
    <Layout>
      {isOpen && (
        <AddSpecialistModal
          closeModal={onCloseModal}
          isOpen={isOpen}

          datas={selectedSpecialist}
        />
      )}
      {isUpdateModalOpen && (
        <UpdateSpecialistModal
          closeModal={onCloseUpdateModal}
          isOpen={isUpdateModalOpen}
          specialist={selectedSpecialist}
          onUpdateSuccess={getData}
        />
      )}
      {isDeleteModalOpen && (
        <DelSpecialistModal
          closeModal={onCloseDeleteModal}
          isOpen={isDeleteModalOpen}
          specialistId={selectedSpecialist?.id}
          onDeleteSuccess={getData}
        />
      )}
      <button
        onClick={() => setIsOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      <h1 className="text-xl font-semibold">Especialistas</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        <div className="mt-8 w-full overflow-x-scroll">
          <SpecialistTable
            data={data}
            functions={{ preview, handleDelete }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Receptions;
