import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'; // Importing necessary functions from Redux Toolkit for creating API
import { logOut } from '../../features/auth/authSlice'; // Importing logout action creator from authSlice

// Retrieving the API URL from environment variables
const apiLink = process.env.REACT_APP_API_URL;

// Defining the baseQuery for fetching data from the API
const baseQuery = fetchBaseQuery({
    baseUrl: apiLink, // Setting the base URL for API requests
    credentials: "include", // Including credentials in the request
    prepareHeaders: (headers, { getState }) => {
        const token = getState().auth.token; // Retrieving token from auth slice state

        if (token) {
            headers.set("Authorization", `Bearer ${token}`); // Adding authorization header with token
        }
        return headers;
    },
});

// Function to handle baseQuery with reauthentication
const baseQueryWithReauth = async (args, api, extraOptions) => {
    try {
        return await baseQuery(args, api, extraOptions); // Executing baseQuery
    } catch (error) {
        if (error.status === 401) { // If status code is 401 (Unauthorized)
            api.dispatch(logOut()); // Dispatching logout action
        }
        throw error; // Throwing the error
    }
};

// Creating API slice
export const apiSlice = createApi({
    reducerPath: 'api', // Setting the reducer path
    baseQuery: baseQueryWithReauth, // Using baseQuery with reauthentication
    endpoints: () => ({}), // Defining endpoints for the API slice
});
