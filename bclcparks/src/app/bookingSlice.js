import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { v4 as uuid } from "uuid";
import { message } from "antd";

const initialState = {};

export const submitReservation = createAsyncThunk(
  "booking/submitReservationAPI",
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
    [submitReservation.fulfilled]: (state, action) => {
      message.success({
        content: "Reservation request made. Good luck!",
        key: "RESERVE",
      });
      message.success(JSON.stringify(action.payload));
    },
  },
});

export const {} = bookingSlice.actions;

export const selectTaskBoard = (state) => state.taskBoard.taskBoard;

export default bookingSlice.reducer;
