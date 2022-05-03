import React, { useEffect, useState } from 'react';
import Head from 'next/head';
import Link from 'next/link';
import { Button, Input, Modal, Page } from '@geist-ui/core';
import { useForm } from 'react-hook-form'
import { yupResolver } from '@hookform/resolvers/yup'
import * as yup from 'yup'
import { useRouter } from 'next/router';

const url = 'http://127.0.0.1:5000/'

const ipRegex = /^(((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(((\/([4-9]|[12][0-9]|3[0-2]))?)|\s?-\s?((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))))(,\s?|$))+/g

const schema = yup.object().shape({
  gateway: yup.string().matches(ipRegex, 'Ingrese una ip válida').required(),
})

const schema2 = yup.object().shape({
  broadcast: yup.string().matches(ipRegex, 'Ingrese una ip válida con máscara').required(),
})

const schema3 = yup.object().shape({
  baseIp: yup.string().matches(ipRegex, 'Ingrese una ip válida con máscara').required(),
  comparison: yup.string().matches(ipRegex, 'Ingrese una ip válida').required(),
})

function Home() {
  const { register, handleSubmit, formState: { errors } } = useForm({
    mode: 'onSubmit',
    resolver: yupResolver(schema)
  })

  const { register: register2, handleSubmit: handleSubmit2, formState: { errors: errors2 } } = useForm({
    mode: 'onSubmit',
    resolver: yupResolver(schema2)
  })

  const { register: register3, handleSubmit: handleSubmit3, formState: { errors: errors3 } } = useForm({
    mode: 'onSubmit',
    resolver: yupResolver(schema3)
  })

  const [state, setState] = useState(false)
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetch('http://127.0.0.1:5000/test')
      .then(response => response.json())
      .then(data => console.log(data));
  }, [])

  const getGateway = async (data) => {
    const response = await fetch('http://127.0.0.1:5000/gateway', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        data: data.gateway
      })
    })
    const body = await response.json()
    setMessage(body.result)
    setState(true)
  }

  const getBroadcast = async (data) => {
    const response = await fetch('http://127.0.0.1:5000/broadcast', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        data: data.broadcast
      })
    })
    const body = await response.json()
    setMessage(body.result)
    setState(true)
  }

  const getNetwork = async (data) => {
    const response = await fetch('http://127.0.0.1:5000/comparison', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        data: data.baseIp,
        data2: data.comparison
      })
    })
    const body = await response.json()
    setMessage(body.result)
    setState(true)
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
              <Input className="" {...register('gateway')} placeholder="IPv4" />
              <div className="ml-2 mb-3 mt-1 text-xs">
                {errors?.gateway?.message ?? ''}
              </div>
              <Button htmlType="submit">Obtener gateway</Button>
            </form>

            <form onSubmit={handleSubmit2(getBroadcast)} className="flex flex-col mb-4">
              <Input className="" {...register2('broadcast')} placeholder="IPv4 con máscara" />
              <div className="ml-2 mb-3 mt-1 text-xs">
                {errors2?.broadcast?.message ?? ''}
              </div>
              <Button htmlType="submit">Obtener broadcast</Button>
            </form>

            <form onSubmit={handleSubmit3(getNetwork)} className="flex flex-col">
              <Input className="" {...register3('baseIp')} placeholder="IPv4" />
              <div className="ml-2 mb-3 mt-1 text-xs">
                {errors3?.baseIp?.message ?? ''}
              </div>
              <Input className="" {...register3('comparison')} placeholder="IPv4 con máscara" />
              <div className="ml-2 mb-3 mt-1 text-xs">
                {errors3?.comparison?.message ?? ''}
              </div>
              <Button htmlType="submit">Realizar comparación</Button>
            </form>
          </div>
        </div>
        <Modal visible={state} onClose={() => setState(false)}>
          <Modal.Title>{message}</Modal.Title>
        </Modal>
      </Page>
    </>
  );
}

export default Home;
