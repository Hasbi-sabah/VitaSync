import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials, logOut } from '../../features/auth/authSlice';

// Environment variable for API URL
const api = process.env.REACT_APP_API_URL;

// Base query configuration
const baseQuery = fetchBaseQuery({
    baseUrl: api,
    credentials: "include",
    prepareHeaders: (headers, { getState }) => {
        return headers;
    },
})

/**
 * Base query function with automatic reauthentication.
 * 
 * This function extends the fetchBaseQuery to automatically log out the user
 * if an unauthorized response is received.
 * 
 * @param args - The arguments for the query.
 * @param api - The API object.
 * @param extraOptions - Additional options for the query.
 * @returns The result of the query.
 */
const baseQueryWithReauth = async (args, api, extraOptions) => {
    let result = await baseQuery(args, api, extraOptions);

    if (result?.error) api.dispatch(logOut());
    return result;
};

// Create API slice
export const apiSlice = createApi({
    baseQuery: baseQueryWithReauth,
    endpoints: builder => ({})
})
