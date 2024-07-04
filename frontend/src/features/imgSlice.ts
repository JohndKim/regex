// features/uploadSlice.ts
import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import axios from 'axios';
import { AppDispatch } from '../store';

interface UploadState {
  error: string | null;
  extractedText: string | null;
  loading: boolean;
}

const initialState: UploadState = {
  error: null,
  extractedText: null,
  loading: false,
};

const uploadSlice = createSlice({
  name: 'upload',
  initialState,
  reducers: {
    setError(state, action: PayloadAction<string>) {
      state.error = action.payload;
      state.loading = false;
    },
    setLoading(state, action: PayloadAction<boolean>) {
      state.loading = action.payload;
    },
    setExtractedText(state, action: PayloadAction<string>) {
      state.extractedText = action.payload;
      state.loading = false;
    },
  },
});

export const { setError, setLoading, setExtractedText } = uploadSlice.actions;

export default uploadSlice.reducer;

// Action to handle file upload
export const uploadFile = (file: File) => async (dispatch: AppDispatch) => {
  dispatch(setLoading(true));

  try {
    const formData = new FormData();
    formData.append('photo', file);

    const response = await axios.post('http://127.0.0.1:8000/api/upload/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    dispatch(setExtractedText(response.data.extracted_text));
  } catch (error) {
    dispatch(setError('File upload failed'));
  }
};