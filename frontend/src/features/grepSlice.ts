import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import axios from 'axios';
import { AppDispatch } from '../store';

interface GrepResult {
  status: boolean;
  nfa: any;  // Replace with the correct type
  path: any; // Replace with the correct type
}

interface GrepState {
  loading: boolean;
  data: GrepResult | null;
  error: string | null;
}

const initialState: GrepState = {
  loading: false,
  data: null,
  error: null,
};

const grepSlice = createSlice({
  name: 'grep',
  initialState,
  reducers: {
    fetchGrepDataStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchGrepDataSuccess(state, action: PayloadAction<GrepResult>) {
      state.loading = false;
      state.data = action.payload;
    },
    fetchGrepDataFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchGrepDataStart,
  fetchGrepDataSuccess,
  fetchGrepDataFailure,
} = grepSlice.actions;

export default grepSlice.reducer;

export const fetchGrepData = ({ string, regex }: { string: string; regex: string }) => async (dispatch: AppDispatch) => {
  try {

    dispatch(fetchGrepDataStart());
    // console.log("FETCHING GREP (SENDING)")

    const response = await axios.get(`http://127.0.0.1:8000/api/grep/`, {
        params: { string, regex },
    });

    // console.log("FETCHED DATA!!!")

    dispatch(fetchGrepDataSuccess(response.data));

    // console.log("SUCCESS!!")

    // console.log(response.data)

    } catch (error) {

        if (error instanceof Error) {
            dispatch(fetchGrepDataFailure(error.message));
        } else {
            dispatch(fetchGrepDataFailure('An unknown error occurred'));
        }
  }


//     dispatch(fetchGrepDataStart());
//     const response = await axios.get('/api/grep/', {
//       string,
//       regex,
//     });


    


//     dispatch(fetchGrepDataSuccess(response.data));
//   } catch (error) {
//     // dispatch(fetchGrepDataFailure(error.message));
//   }
};
