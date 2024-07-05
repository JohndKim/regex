import cx from 'clsx';
import { Container, createTheme, virtualColor, MantineColorsTuple } from '@mantine/core';
import classes from './styles.module.css';

const violetPanda: MantineColorsTuple = [
  '#f6ecff',
  '#e7d6fb',
  '#caabf1',
  '#ac7ce8',
  '#9354e0',
  '#833cdb',
  '#7b2eda',
  '#6921c2',
  '#5d1cae',
  '#501599'
];

export const theme = createTheme({

  colors: {
    violetPanda,
  },


  components: {
    Container: Container.extend({
      classNames: (_, { size }) => ({
        root: cx({ [classes.responsiveContainer]: size === 'responsive' }),
      }),
    }),
  },
});



