import React, { useEffect } from 'react';
import Head from 'next/head';
import Link from 'next/link';
import { Button, Input, Page } from '@geist-ui/core';
import { useForm } from 'react-hook-form';

const url = 'http://127.0.0.1:5000/'

function Home() {
  const { register, handleSubmit, getValues } = useForm()

  useEffect(() => {
    fetch('http://127.0.0.1:5000/test')
      .then(response => response.json())
      .then(data => console.log(data));
  }, [])

  const getGateway = async () => {
    const response = await fetch(url + 'gateway', {
      method: 'POST',
      body: JSON.stringify({
        data: getValues('gateway')
      })
    })
    console.log(response)
  }

  const getBroadcast = () => {
    console.log(getValues('broadcast'))
  }

  return (
    <>
      <Head>
        <title>Inicio - Next - Electon - Tailwind</title>
      </Head>
      <Page>
        <div className='grid grid-col-1 text-2xl w-full text-center'>
          <img className='ml-auto mr-auto' src='/images/logo.png' />
        </div>
        <div className="w-full flex items-center justify-center">
          <div className='w-[40%] '>
            {/* <Link href='/next'>
              <a className='btn-blue'>Go to next page</a>
            </Link> */}
            <form onSubmit={handleSubmit(getGateway)} className="flex flex-col mb-4">
              <Input className="mb-3" {...register('gateway')} />
              <Button onClick={() => getGateway()}>Obtener gateway</Button>
            </form>

            <form onSubmit={handleSubmit(getBroadcast)} className="flex flex-col">
              <Input className="mb-3" {...register('broadcast')} />
              <Button onClick={() => getBroadcast()}>Obtener broadcast</Button>
            </form>
          </div>
        </div>
      </Page>
    </>
  );
}

export default Home;
