import '@mantine/core/styles.css';
import { MantineProvider } from '@mantine/core';
import ColorSchemeContext from './components/ColorSchemeContext';
import { useState } from 'react';
import { Router } from './Router';
import { theme } from './theme';

export default function App() {

    return (
      <MantineProvider theme={theme} defaultColorScheme="dark">
        <Router />
      </MantineProvider>
  );
}



// return (
//   <ColorSchemeContext.Provider value={{ colorScheme, onChange: setColorScheme }}>
//     <MantineProvider theme={theme} defaultColorScheme="dark">
//       <Router />
//     </MantineProvider>
//   </ColorSchemeContext.Provider>
// );
