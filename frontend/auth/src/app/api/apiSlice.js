
/**
 * Redux Toolkit API slice for managing API calls.
 * This slice includes a custom base query for handling authentication and re-authentication.
 */
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
 * Custom base query with re-authentication logic.
 * This function wraps the base query to handle re-authentication in case of an authentication error.
 * @param {Object} args - The arguments for the base query.
 * @param {Object} api - The API object from Redux Toolkit Query.
 * @param {Object} extraOptions - Additional options for the base query.
 * @returns {Promise} The result of the base query, potentially with re-authentication logic applied.
 */
const baseQueryWithReauth = async (args, api, extraOptions) => {
    let result = await baseQuery(args, api, extraOptions);

    if (result?.error) api.dispatch(logOut());
    return result;
};

/**
 * Creates the API slice with the custom base query.
 * This slice is used for making API calls throughout the application.
 */
export const apiSlice = createApi({
    baseQuery: baseQueryWithReauth,
    endpoints: builder => ({})
});
