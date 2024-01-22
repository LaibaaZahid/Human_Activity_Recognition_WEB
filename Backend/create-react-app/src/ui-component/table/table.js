import React from "react";


import "./table.css";

export const Table = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('/api/device-users/')
      .then(response => setUsers(response.data));
  }, []);


  
  
  return (
    <div className="table-wrapper">
      <table className="table">
        <thead>
          <tr>
            <th>User id</th>
            <th className="expand">Device Type</th>
            <th>Status</th>
            <th>Last connected</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => {

            return (
              <tr key={user.user_id}>
                <td>{user.user_id}</td>
                <td className="expand">{user.device_type}</td>
                <td>
                  <span>
                    {user.status}
                  </span>
                </td>
                <td className="fit">
                  <span>
                   {user.last_connected}
                  </span>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};