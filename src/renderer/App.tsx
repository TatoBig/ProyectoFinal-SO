/* eslint-disable react/jsx-props-no-spreading */
import { useForm } from 'react-hook-form';
import { MemoryRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

type FormValues = {
  ip: string
}

const Hello = () => {
  const { register, handleSubmit } = useForm<FormValues>();

  const onSubmit = (data: FormValues) => {
    fetch('http://127.0.0.1:5000/test')
      .then(response => response.json())
      .then(data => console.log(data));
  }

  return (
    <div>
      <form
        style={{ display: 'flex', flexDirection: 'column' }}
        onSubmit={handleSubmit(onSubmit)}
      >
        <input {...register('ip')} type="text" style={{ padding: 4 }} />
        <input type="text" style={{ padding: 4 }} />
        <button type="submit">Button</button>
      </form>
    </div>
  );
};

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Hello />} />
      </Routes>
    </Router>
  );
}
