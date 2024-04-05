import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { logOut } from '../../features/auth/authSlice';

// Environment variable for API URL
const api = process.env.REACT_APP_API_URL;

// Base query configuration
const baseQuery = fetchBaseQuery({
    baseUrl: api,
    credentials: "include",
    prepareHeaders: (headers, { getState }) => {
        const token = getState().auth.token;
        if (token) {
            headers.set("Authorization", `Bearer ${token}`);
        }
        return headers;
    },
});

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
    try {
        return await baseQuery(args, api, extraOptions);
    } catch (error) {
        if (error.status === 401) {
            api.dispatch(logOut());
        }
        throw error;
    }
};

// Create API slice
export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: baseQueryWithReauth,
    endpoints: () => ({}),
});
