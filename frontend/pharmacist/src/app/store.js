import { configureStore } from "@reduxjs/toolkit"; // Importing configureStore function from Redux Toolkit
import { apiSlice } from "./api/apiSlice"; // Importing the API slice
import authReducer from "../features/auth/authSlice"; // Importing the authentication reducer

// Retrieving the environment variable for Redux DevTools
const devtools = process.env.REACT_APP_DEVTOOLS;

// Configuring the Redux store
export const store = configureStore({
    reducer: {
        [apiSlice.reducerPath]: apiSlice.reducer, // Adding API slice reducer to the store
        auth: authReducer // Adding authentication reducer to the store
    },
    middleware: getDefaultMiddleware =>
        getDefaultMiddleware().concat(apiSlice.middleware), // Adding middleware for handling API requests
    devTools: devtools // Setting Redux DevTools based on environment variable
});
