import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SamplePage = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('/api/device-users/')
      .then(response => setUsers(response.data));
  }, []);



  if (!users.length) return <p>Loading...</p>;

  return (
    <div className="App">
    <table style={{ borderCollapse: 'collapse', width: '100%' }}>
      <thead>
        <tr style={{ backgroundColor: '#f2f2f2' }}>
          <th style={{ border: '1px solid #ddd', padding: '8px' }}>ID</th>
          <th style={{ border: '1px solid #ddd', padding: '8px' }}>Device Type</th>
          <th style={{ border: '1px solid #ddd', padding: '8px' }}>Status</th>
        </tr>
      </thead>
      <tbody>
        {users.map((user, index) => (
          <tr key={user.user_id} style={{ backgroundColor: index % 2 === 0 ? '#f2f2f2' : 'white' }}>
            <td style={{ border: '1px solid #ddd', padding: '8px' }}>{user.user_id}</td>
            <td style={{ border: '1px solid #ddd', padding: '8px' }}>{user.device_type}</td>
            <td style={{ border: '1px solid #ddd', padding: '8px' }}>{user.status}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
  );
}

export default SamplePage;
