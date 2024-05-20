import React, { useState, useEffect } from 'react';
import { BiPlus } from 'react-icons/bi';
import Layout from '../../Layout';
import { toast } from 'react-hot-toast';
import { ProceduresTable } from '../../components/Tables'; 
import { ProceduresData } from '../../components/Datas'; 
import AddProcedureModal from '../../components/Modals/AddProcedureModal';

function Procedures() {
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [data, setData] = useState([]);
  const [selectedProcedure, setSelectedProcedure] = useState(null);

  const fetchProcedures = async () => {
    const procedures = await ProceduresData();
    setData(procedures);
  };

  const onCloseAddModal = () => {
    setIsAddModalOpen(false);
    fetchProcedures();
  };

  const onEdit = (procedure) => {
    setSelectedProcedure(procedure);
    setIsAddModalOpen(true);
  };

  const onDelete = async (id) => {
    try {
      // Lógica para eliminar el procedimiento (si está implementado)
      toast.success('Procedimiento eliminado con éxito');
      fetchProcedures();
    } catch (error) {
      console.error('Error al eliminar el procedimiento:', error);
      toast.error('Error al eliminar el procedimiento. Por favor, inténtalo de nuevo.');
    }
  };

  useEffect(() => {
    fetchProcedures();
  }, []);

  return (
    <Layout>
      {isAddModalOpen && (
        <AddProcedureModal
          closeModal={onCloseAddModal}
          isOpen={isAddModalOpen}
          procedure={selectedProcedure}
        />
      )}
      <button
        onClick={() => setIsAddModalOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      <h1 className="text-xl font-semibold">Procedimientos</h1>
      <div className="bg-white my-8 rounded-xl border-[1px] border-border p-5">
        <div className="mt-8 w-full overflow-x-scroll">
          <ProceduresTable
            data={data}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        </div>
      </div>
    </Layout>
  );
}

export default Procedures;
