import { Button, Page, Text } from '@geist-ui/core'
import { useRouter } from 'next/router'

const Home = () => {
  const router = useRouter()
  return (
    <Page>
      <Text h1>Home Page</Text>
      <Button onClick={() => router.push('/home')} >Submit</Button>
    </Page>
  )
}

export default Home