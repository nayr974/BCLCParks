import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { v4 as uuid } from "uuid";
import { message } from "antd";

const initialState = {
  reservations: [],
};

export const getReservations = createAsyncThunk(
  "booking/getReservations",
  async (thunkAPI) => {
    message.loading({
      content: "Getting reservations...",
      key: "RESERVATIONS",
    });
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    return response.json();
  }
);

export const submitReservation = createAsyncThunk(
  "booking/submitReservation",
  async (values, thunkAPI) => {
    message.loading({
      content: "Making reservation request...",
      key: "RESERVE",
    });
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/todos/1"
    );
    return response.json();
  }
);

export const bookingSlice = createSlice({
  name: "bookingSlice",
  initialState,
  reducers: {},
  extraReducers: {
    [getReservations.fulfilled]: (state, action) => {
      message.success({
        content: "Retrieved reservations.",
        key: "RESERVE",
      });
      alert(JSON.stringify(action.payload));
      state.reservations = action.payload || {};
    },
    [submitReservation.fulfilled]: (state, action) => {
      message.success({
        content: "Reservation request made. Good luck!",
        key: "RESERVE",
      });
    },
  },
});

export const {} = bookingSlice.actions;

export const selectReservations = (state) => state.reservations;

export default bookingSlice.reducer;
