import { configureStore } from '@reduxjs/toolkit';
import grepReducer from './features/grepSlice';

export const store = configureStore({
  reducer: {
    grep: grepReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;