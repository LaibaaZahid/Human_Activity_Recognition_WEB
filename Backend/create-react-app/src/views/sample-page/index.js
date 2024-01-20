import { useState } from "react";

// material-ui
/*import { Typography } from '@mui/material';*/
import {Table} from 'ui-component/table/table.js';
import {Modal} from 'ui-component/table/Modal.jsx';

// project imports
/*import MainCard from 'ui-component/cards/MainCard';*/

// ==============================|| SAMPLE PAGE ||============================== //

const SamplePage = () => {

  const [modalOpen, setModalOpen] = useState(false);
  const [rows, setRows] = useState([
    {
      page: "User 1",
      description: "This user is using Smartphone",
      status: "activated",
    },
    {
      page: "User 2",
      description: "This user is using Smartwatch",
      status: "deactivated",
    },
    {
      page: "User 3",
      description: "This user is using Glasses",
      status: "error",
    },
  ]);
  const [rowToEdit, setRowToEdit] = useState(null);

  const handleDeleteRow = (targetIndex) => {
    setRows(rows.filter((_, idx) => idx !== targetIndex));
  };

  const handleEditRow = (idx) => {
    setRowToEdit(idx);

    setModalOpen(true);
  };

  const handleSubmit = (newRow) => {
    rowToEdit === null
      ? setRows([...rows, newRow])
      : setRows(
          rows.map((currRow, idx) => {
            if (idx !== rowToEdit) return currRow;

            return newRow;
          })
        );
  };

  return (
    <div className="App">
      <Table rows={rows} deleteRow={handleDeleteRow} editRow={handleEditRow} />
      <button onClick={() => setModalOpen(true)} className="btn addbtn">
        Add
      </button>
      {modalOpen && (
        <Modal
          closeModal={() => {
            setModalOpen(false);
            setRowToEdit(null);
          }}
          onSubmit={handleSubmit}
          defaultValue={rowToEdit !== null && rows[rowToEdit]}
        />
      )}
    </div>
  );
}

  

export default SamplePage;
