import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { v4 as uuid } from "uuid";
import { message } from "antd";

export const getTrails = createAsyncThunk(
  "bookingSlice/getTrails",
  async (thunkAPI) => {
    message.loading({
      content: "Getting trails...",
      key: "TRAILS",
    });
    const response = await fetch("/trailhead/");
    return response.text();
  }
);

export const getReservations = createAsyncThunk(
  "bookingSlice/getReservations",
  async (thunkAPI) => {
    message.loading({
      content: "Getting reservations...",
      key: "RESERVATIONS",
    });
    const response = await fetch("/booking/");
    return response.json();
  }
);

export const submitReservation = createAsyncThunk(
  "bookingSlice/submitReservation",
  async (values, thunkAPI) => {
    message.loading({
      content: "Making reservation request...",
      key: "RESERVE",
    });
    const response = await fetch("/booking/", {
      method: "POST", // *GET, POST, PUT, DELETE
      body: JSON.stringify(values),
    });
    return response.json();
  }
);

const initialState = {
  reservations: [],
  trails: [],
};

export const bookingSlice = createSlice({
  name: "bookingSlice",
  initialState,
  reducers: {
    updateTrail: (state, action) => {},
  },
  extraReducers: {
    [getReservations.fulfilled]: (state, action) => {
      message.success({
        content: "Retrieved reservations.",
        key: "RESERVE",
      });
      state.reservations = action.payload || [];
    },
    [getTrails.fulfilled]: (state, action) => {
      message.success({
        content: "Retrieved trails.",
        key: "TRAILS",
      });
      state.trails = JSON.parse(action.payload);
    },
    [submitReservation.fulfilled]: (state, action) => {
      message.success({
        content: "Reservation request made. Good luck!",
        key: "RESERVE",
      });
    },
  },
});

export const { updateTrail } = bookingSlice.actions;

export const selectReservations = (state) => state.booking.reservations;
export const selectTrails = (state) => state.booking.trails;

export default bookingSlice.reducer;
