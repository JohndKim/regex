import { Container, Flex, Center } from '@mantine/core';
import Grepper from "../components/Grepper"
import Dropper from "../components/Dropper"




// home page
export function HomePage() {
    // html code
    return (
      <>
        {/* <Flex bg='teal.0' >
          <Grepper/>
        </Flex> */}

        {/* <Center bg='white.0'>
          <Grepper/>
        </Center> */}


        {/* <Grepper/> */}
        <Container size="responsive" >
          <Dropper/>
        </Container>

        
        

        {/* <Container fluid bg='red.3' h='100vh'>
          <Grepper/>
        </Container> */}


        
      </>
      
    );
  }
  