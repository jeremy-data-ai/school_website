import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [time, setTime] = useState('');

  useEffect(() => {
    fetch('/api/message')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => console.error('Error fetching message', err));

    fetch('/api/time')
      .then((res) => res.json())
      .then((data) => setTime(data.time))
      .catch((err) => console.error('Error fetching time', err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">School Website</h1>
      <p className="text-blue-600">{message}</p>
      {time && (
        <p className="text-gray-700 mt-2" data-testid="server-time">Server time: {time}</p>
      )}
    </div>
  );
}

export default App;
