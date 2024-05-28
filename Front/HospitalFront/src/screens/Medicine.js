import React, { useState, useEffect } from 'react';
import Layout from '../Layout';
import { BiPlus } from 'react-icons/bi';

import { MedicineTable } from '../components/Tables';
import { MedicineData } from '../components/Datas';
import DeleteMedicine from '../components/Modals/DelMedicineModal';
import AddMedicineModal from '../components/Modals/AddMedicineModal';

function Medicine() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [medicineData, setMedicineData] = useState([]);

  const [isDeleteModalOpen, setIsDeleteModalOpen] = useState(false);
  const [selectedMedicine, setSelectedMedicine] = useState(null);

  const onCloseModal = async () => {
    setIsModalOpen(false);
    setSelectedMedicine(null);
    await getData();
  };

  const onCloseDeleteModal = () => {
    setIsDeleteModalOpen(false);
    setSelectedMedicine(null);
  };

  const preview = (id) => {
    const medicine = medicineData.find((med) => med.id === id);
    console.log('Selected Medicine:', medicine);
    setSelectedMedicine(medicine);
    setIsModalOpen(true);
  };

  const handleDelete = async (id) => {
    setSelectedMedicine(id);
    setIsDeleteModalOpen(true);
  };

  const getData = async () => {
    const data = await MedicineData();
    setMedicineData(data);
  };

  useEffect(() => {
    getData();
  }, []);

  return (
    <Layout>
      {isModalOpen && (
        <AddMedicineModal
          closeModal={onCloseModal}
          isOpen={isModalOpen}
          medicine={selectedMedicine} // Cambiar esta línea
        />
      )}
      {isDeleteModalOpen && (
        <DeleteMedicine
          closeModal={onCloseDeleteModal}
          isOpen={isDeleteModalOpen}
          medicineId={selectedMedicine?.id}
          onDeleteSuccess={getData}
        />
      )}
      {/* add button */}
      <button
        onClick={() => setIsModalOpen(true)}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
      >
        <BiPlus className="text-2xl" />
      </button>
      <h1 className="text-xl font-semibold">Medicine</h1>
      <div
        data-aos="fade-up"
        data-aos-duration="1000"
        data-aos-delay="100"
        data-aos-offset="200"
        className="bg-white my-8 rounded-xl border-[1px] border-border p-5"
      >
        <div className="mt-8 w-full overflow-x-scroll">
          <MedicineTable
            data={medicineData}
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

export default Medicine;
