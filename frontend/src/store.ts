import { configureStore } from '@reduxjs/toolkit';
import grepReducer from './features/grepSlice';
import uploadReducer from './features/imgSlice';


export const store = configureStore({
  reducer: {
    grep: grepReducer,
    upload: uploadReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;