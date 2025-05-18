import React, { useEffect, useState } from 'react';
import Message from './components/Message';
import { fetchMessage } from './api';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetchMessage()
      .then(setMessage)
      .catch((err) => console.error('Error fetching message', err));
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">School Website</h1>
      <Message text={message} />
    </div>
  );
}

export default App;
