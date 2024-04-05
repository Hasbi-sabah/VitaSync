import { configureStore } from "@reduxjs/toolkit";
import { apiSlice } from "./api/apiSlice";
import authReducer from "../features/auth/authSlice";

/**
 * Redux store configuration.
 * 
 * This function configures and creates the Redux store with reducers and middleware.
 * 
 * @returns The configured Redux store.
 */
const devtools = process.env.REACT_APP_DEVTOOLS;
export const store = configureStore({
    reducer: {
        [apiSlice.reducerPath]: apiSlice.reducer,
        auth: authReducer
    },
    middleware: getDefaultMiddleware => 
        getDefaultMiddleware().concat(apiSlice.middleware),
    devTools: devtools
});
