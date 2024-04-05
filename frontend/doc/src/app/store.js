/**
 * Configures and exports the Redux store.
 * @constant
 * @type {Object}
 */
import { configureStore } from "@reduxjs/toolkit";
import { apiSlice } from "./api/apiSlice";
import authReducer from "../features/auth/authSlice";

/**
 * Defines the reducers used in the store.
 * @property {Object} [apiSlice.reducerPath]: The reducer for the API slice.
 * @property {Function} auth: The reducer for the authentication feature.
 */
export const store = configureStore({
    /**
     * Configures the middleware for the store.
     * @property {Function} getDefaultMiddleware: A function to get the default middleware.
     * @property {Array} apiSlice.middleware: The middleware for the API slice.
     */
    reducer: {
        [apiSlice.reducerPath]: apiSlice.reducer,
        auth: authReducer
    },
    /**
     * Enables or disables Redux DevTools based on the environment variable.
     * @property {boolean} process.env.REACT_APP_DEVTOOLS: The environment variable for enabling Redux DevTools.
     */
    middleware: getDefaultMiddleware => 
        getDefaultMiddleware().concat(apiSlice.middleware),
    devTools: process.env.REACT_APP_DEVTOOLS
});
