import React, { useState, useEffect } from 'react';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { toast } from 'react-hot-toast';
import AddProcedureModal from '../../components/Modals/AddProcedureModal';
import { ProceduresTable } from '../../components/Tables'; 
import { ProceduresData } from '../../components/Datas'; 
import DeleteProcedureModal from '../../components/Modals/DelProcedureModal';

function Procedures() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [procedureData, setProcedureData] = useState([]);
  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedProcedure, setSelectedProcedure] = useState(null);

  const onCloseModal = async () => {
    setIsModalOpen(false);
    setSelectedProcedure(null);
    await getData();
  };

  const onCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setSelectedProcedure(null);
  };

  const preview = (id) => {
    const procedure = procedureData.find(pro => pro.id === id);
    setSelectedProcedure(procedure);
    setIsModalOpen(true);
  };

  const handleDelete = (procedure) => {
    setSelectedProcedure(procedure);
    setIsDeleteModalOpen(true);
  };

  const getData = async () => {
    try {
      const data = await ProceduresData();
      setProcedureData(data);
    } catch (error) {
      console.error('Error al obtener datos de procedimientos:', error);
      toast.error('Error al obtener datos de procedimientos.');
    }
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <Layout>
      {isModalOpen && (
        <AddProcedureModal
          closeModal={onCloseModal}
          isOpen={isModalOpen}
          procedure={selectedProcedure}
        />
      )}
      {isDeleteModalOpen && (
        <DeleteProcedureModal
          closeModal={onCloseDeleteModal}
          isOpen={isDeleteModalOpen}
          procedureId={selectedProcedure?.id}
          onDeleteSuccess={getData}
        />
      )}
      <button
        onClick={() => setIsModalOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      <h1 className="text-xl font-semibold">Procedimientos</h1>
      <div className="bg-white my-8 rounded-xl border-[1px] border-border p-5">
        <div className="mt-8 w-full overflow-x-scroll">
          <ProceduresTable
            data={procedureData}
            functions={{ preview, handleDelete }}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Procedures;
