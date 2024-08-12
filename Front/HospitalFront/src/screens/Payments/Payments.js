import React, { useState,useEffect } from 'react';
import Layout from '../../Layout';
import { BiPlus } from 'react-icons/bi';
import { BillingData } from '../../components/Datas';
import { BillingTable } from '../../components/Tables';
import  AddBillingModal  from '../../components/Modals/AddBillingModal';


function Payments() {

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [billingData, setBillingData] = useState([]);
  const [selectedBilling, setSelectedBilling] = useState(null);
  const [filterDate, setFilterDate] = useState('');

  const onCloseModal = async () => {
    setIsModalOpen(false);
    setSelectedBilling(null);
    await getData();
  };

  const getData = async () => {
 
    const data = await BillingData();
 


    const normalizedData = data.map(billing => ({
      ...billing,

    }));


    const filteredData = filterDate
      ? normalizedData.filter(billing => billing.date === filterDate)
      : normalizedData;

    setBillingData(filteredData);
  };


  useEffect(() => {
    getData();
  }, [filterDate]);



  // preview
  // const previewPayment = (id) => {
  //   navigate(`/payments/preview/${id}`);
  // };

  return (
    <Layout>
      {isModalOpen && (
        <AddBillingModal
          isOpen={isModalOpen}
          onClose={onCloseModal}
          billing={selectedBilling}
        />
      )}
      <div className="flex justify-between items-center">
        <h1 className="text-3xl text-gray-700">Facturas</h1>
        <div className="flex items-center">

          <input
            type="date"
            value={filterDate}
            onChange={(e) => {
              const selectedDate = e.target.value; 
              setFilterDate(selectedDate);
            }}
            className="mr-4 px-4 py-2 border rounded-md"
          />
        <button
        onClick={() => {
          setSelectedBilling(null); 
          setIsModalOpen(true);
          }}
        className="w-16 animate-bounce h-16 border border-border z-50 bg-subMain text-white rounded-full flex-colo fixed bottom-8 right-12 button-fb"
        >
        <BiPlus className="text-2xl" />
        </button>
        </div>
      </div>
      <BillingTable
        data={billingData}
        // showPatientId={true}
        // showActions={true}
      />      
    </Layout>
  );
}

export default Payments;
